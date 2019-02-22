import os
import re 
import json
import time
import itertools
import requests
import argparse

'''
This module contains a management script for performing various actions on a list of Collectors.

For authentication purposes, the user must always have the following parameters when calling the script:
  -url [API endpoint URL]

Access ID and key will be prompted for if the corresponding parameters are not included.

The user provides access ID, access key, and API endpoint URL parameters in addition to one of the following three commands:
  -upgrade [version]: upgrade the list of Collectors obtained from the API to given version
  -addSource [json file path]: add source from JSON config file to the list of Collectors obtained from the API 
  -listVersions: show the versions of each Collector in the list of Collectors obtained from the API

Finally, the user can also include a command to filter and apply changes to a subset of Collectors:
  -filter [type]=[condition]

Confirmation prompts can be bypassed for automatic script running if the -y flag is used.

Sample commands:
python sumo_mgmt.py -url https://api.us2.sumologic.net/api/v1/ -accessid [ACCESS ID] -accesskey [ACCESS KEY] -listVersions
python sumo_mgmt.py -url https://api.us2.sumologic.net/api/v1/ -accessid [ACCESS ID] -accesskey [ACCESS KEY] -upgrade 19.155-13 -batchSize 50
python sumo_mgmt.py -url https://api.us2.sumologic.net/api/v1/ -accessid [ACCESS ID] -accesskey [ACCESS KEY] -addSource source.json
python sumo_mgmt.py -url https://api.us2.sumologic.net/api/v1/ -accessid [ACCESS ID] -accesskey [ACCESS KEY] -addSource source.json name=test
'''

# Constants
MAX_BATCH_SIZE = 100
MIN_BATCH_SIZE = 1
DEFAULT_BATCH_SIZE = 10

# Command line arguments
parser = argparse.ArgumentParser(description='A management script for upgrading, adding sources to, and listing available Collectors.')
parser.add_argument('-upgrade', metavar='', type=str, nargs=1, help='upgrade given set of collectors to specified version')
parser.add_argument('-batchSize', metavar='', type=int, nargs=1, help='(OPTIONAL) batch size for upgrading a given set of collectors')
parser.add_argument('-addSource', metavar='', type=str, nargs=1, help='add a source from JSON file to given set of collectors')
parser.add_argument('-accessid', metavar='', type=str, nargs=1, help='(OPTIONAL) access id for authentication')
parser.add_argument('-accesskey', metavar='', type=str, nargs=1, help='(OPTIONAL) access key for authentication')
parser.add_argument('-url', metavar='', type=str, nargs=1, help='URL for API call')
parser.add_argument('-filter', metavar='', type=str, nargs=1, help='(OPTIONAL) filter list of all collectors by given type and condition')
parser.add_argument('-listVersions', action='store_true', help='list the versions of a given set of collectors')
parser.add_argument('-getsources', action='store_true', help='gets the sources for given set of collectors')
parser.add_argument('-changesource', metavar='', type=str, nargs=1, help='chnages the sources for given set of collectors')



# Additional options
parser.add_argument('-y', '-Y', action='store_true', help='flag to automatically accept any prompts')

args = parser.parse_args()


from datetime import datetime
def log(statement):
  '''
  Prepends output with timestamp to allow for logging and then prints the output.

  Args: 
    statement (str): The output statement to be printed with a timestamp in the 
    format yyyy-MM-dd HH:mm:ss,SSS ZZZZ. 
  '''
  now = datetime.now().strftime('%Y-%m-%d %H:%M:%S,%f')[:-3]
  utc_offset = time.localtime().tm_hour - time.gmtime().tm_hour
  sign = '-' if utc_offset < 0 else '+'
  timestamp = now + ' ' + sign + str(abs(utc_offset)).zfill(2) + '00'
  
  print (timestamp + ' ' + statement)

import getpass
def validate():
  '''
  Validates that the arguments required for upgrading, adding a source, or listing Collector versions
  have been provided and are valid. Prints an appropriate error message otherwise. If an access key 
  and ID are not provided, they are prompted for. 

  Returns:
    bool: A boolean that is True if the arguments were valid and False otherwise.
  ''' 
  if not args.accessid:
    args.accessid = [getpass.getpass('Enter your access ID: ')]

  if not args.accesskey:
    args.accesskey = [getpass.getpass('Enter your access key: ')]

  if not args.url:
    log('[ERROR] please provide a valid URL for the API endpoint')
    parser.print_help()
    return False
  elif not args.listVersions and not args.upgrade and not args.addSource and not args.getsources and not args.changesource:
    log('[ERROR] please provide a command to list versions, upgrade, or add source')
    parser.print_help()
    return False
  else:
    if args.upgrade and args.batchSize and (args.batchSize[0] > MAX_BATCH_SIZE or args.batchSize[0] < MIN_BATCH_SIZE):
      log('[ERROR] batch size must be within range %d to %d' % (MIN_BATCH_SIZE, MAX_BATCH_SIZE))
      return False
    elif args.addSource and not is_valid_json(args.addSource[0]):
      return False
    elif args.filter and not re.match('[a-z]+=.+', args.filter[0], flags=0):
      log('[ERROR] format for filter argument is invalid')
      return False
    else:
      return True

def prompt(msg):
  '''
  Prompts the user with the given message and returns the result of the response. If
  the -y flag is on, the prompt is bypassed.

  Args:
    msg (str): The message to prompt the user with.

  Returns:
    bool: A boolean corresponding to the user's response to the prompt, where True 
    means the user chose yes and accepted the prompt and False is otherwise.
  '''
  if args.y:
    return True
  #makes this python3 compliant
  try:
    i = raw_input(msg)
  except:
    i = input(msg)
    
  while True:
    if i in ['Y', 'N', 'y', 'n']:
      return i.lower() == 'y'
    else:
      i = raw_input('Invalid option, please choose again. ' + msg)

def is_valid_json(json_file):
  '''
  Checks that the given path for the JSON source configuration file is valid.

  Args:
    json_file (str): The file path to the JSON file.

  Returns:
    bool: A boolean that is True if the file path leads to a valid JSON file and 
    False otherwise.
  '''
  if not os.path.isfile(json_file):
    log('[ERROR] invalid file path for source configuration')
    return False
  elif not json_file.lower().endswith('.json'):
    log('[ERROR] provided file path does not contain a JSON file')
    return False
  else: 
    return True

def group(n, iterable):
  '''
  Splits an iterable set into groups of size n and a group of the remaining elements 
  if needed.

  Args:
    n (int): The number of elements per group.
    iterable (list): The list whose elements are to be split into groups of size n.

  Returns:
    list: The list of groups of size n, where each group is a list of n elements.
  '''
  args = [iter(iterable)] * n
  return ([e for e in t if e != None] for t in itertools.izip_longest(*args))


def get_collectors(path, filters):
  '''
  Retrieves the list of Collectors in groups of 1000 via the API.

  Args:
    path (str): The path for the GET method that sends a request to the API. 
    filters (dict): The set of key-value pairs that the Collectors in the list must have. 

  Returns: 
    list: The list of (filtered) Collectors.

  The URL for the request is the API endpoint (e.g. 'http://api.sumologic.com/api/v1/') + 
  'collectors' for getting Collectors,
  'collectors/upgrades/collectors' for getting Collectors that can be upgraded. 

  The parameter offset is passed to indicate offset into the list of Collectors. The default 
  maximum number of Collectors to return in the request is 1000. The conditions for a
  Collector to be able for upgrade requires that it is alive, installable, in the current org,
  not in upgrading, not in the upgrade-to version, and not too old so that it cannot be upgraded.
  '''
  url = args.url[0] + path
  collector_list = []
  offset = 0

  while True:
    payload = {'offset': offset}
    r = requests.get(url, params=payload, auth=(args.accessid[0], args.accesskey[0]))
    if r.status_code != 200:
      log('[ERROR] %s' % r.json()['message'].lower()[:-1])
      break

    sublist = json.loads(r.text)['collectors']
    if not sublist:
      break

    log('[PROGRESS] fetching and sorting through the next %d to %d collectors' % (offset + 1, offset + len(sublist)))

    if filters:
      collector_list.extend(list(filter_by(sublist, filters)))
    else: 
      collector_list.extend(sublist)                           
    if len(sublist) < 1000:   # we have reached the end of the list of collectors 
      break
    offset += 1000

  return collector_list 


def get_sources_by_collector(path, collector_list):
  '''
  Retrieves the list of Collectors in groups of 1000 via the API.

  Args:
    path (str): The path for the GET method that sends a request to the API. 
    filters (dict): The set of key-value pairs that the Collectors in the list must have. 

  Returns: 
    list: The list of (filtered) Collectors.

  The URL for the request is the API endpoint (e.g. 'http://api.sumologic.com/api/v1/') + 
  'collectors' for getting Collectors,
  'collectors/upgrades/collectors' for getting Collectors that can be upgraded. 

  The parameter offset is passed to indicate offset into the list of Collectors. The default 
  maximum number of Collectors to return in the request is 1000. The conditions for a
  Collector to be able for upgrade requires that it is alive, installable, in the current org,
  not in upgrading, not in the upgrade-to version, and not too old so that it cannot be upgraded.
  '''
  collectors_with_sources = []
  for collector in collector_list:
    source_dict = {}
    url = args.url[0] + 'collectors/' + str(collector['id']) + '/sources'
    source_list = []
    payload = {}
    r = requests.get(url, params=payload, auth=(args.accessid[0], args.accesskey[0]))
    if r.status_code != 200:
      log('[ERROR] %s' % r.json()['message'].lower()[:-1])
    

    collectors_with_sources.append(source_dict)
    source_list = json.loads(r.text)['sources']
    source_dict['id'] = str(collector['id'])
    source_dict['sourcejson'] = source_list
    log('[PROGRESS] Finished source get for collector ID: %s'%str(collector['id']))



  return collectors_with_sources 





def check_for_upgraded(collector_list):
  '''
  Adds an 'action' attribute to each Collector in the given list of Collectors. The 'action'
  attribute differentiates Collectors that need to be upgraded from the Collectors that
  are already upgraded to the upgrade-to version by comparing the version of each
  Collector with the upgrade-to version.

  Args: 
    collector_list (list): The list of Collectors to be processed.
  '''
  if args.upgrade[0] == 'latest':
    args.upgrade[0] = fetch_latest_ver()
  build = args.upgrade[0]

  for collector in collector_list:
    if collector['collectorVersion'] == build:
      collector['action'] = 'SKIPPED'
    else:
      collector['action'] = 'UPGRADE'

def fetch_latest_ver():
  latest = 'Unknown'
  url = args.url[0] + 'collectors/upgrades/targets'
  r = requests.get(url, auth=(args.accessid[0], args.accesskey[0]))
  if r.status_code != 200:
    log('[ERROR] Unable to determine latest version')
  else:
    targets = r.json()['targets']
    for target in targets:
      if target['latest'] is True:
        latest = target['version']
        break
  return latest

def upgrade_batch(batch):
  '''
  Upgrades a given batch of Collectors and returns the list of corresponding upgrade
  tasks to keep track of the progress of upgrading.

  Args:
    batch (list): The list of Collectors to be upgraded.

  Returns:
    upgrade_tasks (list): The list of upgrade tasks corresponding to the Collectors
    that were upgraded. Each upgrade task has an id, status, description, and the
    name of the Collector it is associated with.
  
  The URL for the POST request to upgrade a Collector is given by the API endpoint + 
  'collectors/upgrades/'. The parameter collectorId should give the ID of Collector to be 
  upgraded and toVersion should give the version to upgrade to. The response is a JSON
  document containing the upgrade task's id and link of the newly created task.
  '''
  build = args.upgrade[0]
  upgrade_tasks = []

  for collector in batch:
    url = args.url[0] + 'collectors/upgrades/'
    payload = {'collectorId': collector['id'], 'toVersion': build} 
    r = requests.post(url, json=payload, auth=(args.accessid[0], args.accesskey[0]))
    
    if r.status_code == 202:
      upgrade_tasks.append({'id': r.json()['id'], 'name': collector['name'], 'status': '', 'description': ''})
    else:
      upgrade_tasks.append({'id': '', 'name': collector['name'], 'status': 'FAILURE', 'description': r.json()['message']})

    time.sleep(0.2)

  return upgrade_tasks

def check_batch(upgrade_tasks, batch_msg):
  '''
  Checks the status of a batch of upgrade tasks for Collectors currently going through upgrade 
  and prints the information in a table after looping through. Returns a boolean to
  indicate whether all the Collectors in the batch have finished upgrading. 

  Args:
    upgrade_tasks (list): The list of upgrade tasks for the current batch.
    batch_msg (str): The progress message to be printed with the table.

  Returns:
    bool: A boolean that is True if there are still upgrade tasks remaining and
    False otherwise. 

  The URL for the GET request to retrieve the status of an upgrade task is the API
  endpoint + 'collectors/upgrades/{upgradeID}'. The response is a JSON document 
  containing the upgrade task status, along with the associated id, collectorId, 
  toVersion, requestTime, and message. 

  The meaning of the status code is as follows: 
    0 - not started
    1 - pending, the upgrade is issued
    2 - succeed
    3 - failed
    6 - progressing, the upgrade is running on the Collector 
  '''
  tasks_remain = False

  for task in upgrade_tasks:
    if task['status'] not in ['SUCCESS', 'FAILURE', 'UNRESPONSIVE']:
      url = args.url[0] + 'collectors/upgrades/' + task['id']     
      r = requests.get(url, auth=(args.accessid[0], args.accesskey[0]), timeout=10)
      
      if r.status_code == 200:
        status = r.json()['upgrade']['status']

        if status == 0:
          tasks_remain = True
          task['status'] = 'NOT STARTED'
        elif status == 1:
          tasks_remain = True
          task['status'] = 'PENDING'
        elif status == 6:
          tasks_remain = True
          task['status'] = 'IN PROGRESS'
        elif status == 2:
          task['status'] = 'SUCCESS'
        else:
          msg = r.json()['upgrade']['message']
          task['status'] = 'FAILURE'
          task['description'] = msg
      else:
        task['status'] = 'UNRESPONSIVE'
        task['description'] = 'Failed to get status of upgrade.'

    time.sleep(0.2)

  log('[PROGRESS] %s' % batch_msg)
  print_collector_table(upgrade_tasks, ['name', 'status', 'description'])
  return tasks_remain

def wait_for_batch(upgrade_tasks, batch_msg):
  '''
  Waits until a batch of Collectors have completed upgrading by repeatedly 
  checking the set of upgrade tasks and then sleeping for 10 seconds until
  completion.

  Args:
    upgrade_tasks (list): The list of upgrade tasks for the current batch.
    batch_msg (str): The progres message to be printed when a batch is checked.
  '''
  while True: 
    tasks_remain = check_batch(upgrade_tasks, batch_msg)
    if not tasks_remain:
      break
    time.sleep(10)

def upgrade_collectors(collector_list):
  '''
  Upgrades a list of Collectors to the upgrade-to version and prints appropriate
  log messages to keep track of the progress. Collectors are upgraded in batches 
  of size DEFAULT_BATCH_SIZE by default when not specified by the user.

  Args:
    collector_list (list): The list of Collectors to be upgraded.
  '''
  batch_size = args.batchSize[0] if args.batchSize else DEFAULT_BATCH_SIZE
  total = len(collector_list)
  count = 1

  collector_batches = list(group(batch_size, collector_list))
  
  for collector_batch in collector_batches:
    batch_msg = 'upgrade for (%d to %d) of %d collectors' % (count, count + len(collector_batch) - 1, total)
    log('[START] %s' % batch_msg)
    upgrade_tasks = upgrade_batch(collector_batch)
    wait_for_batch(upgrade_tasks, batch_msg)
    log('[COMPLETE] %s' % batch_msg)
    
    count += batch_size


def add_source(collector_list):
  '''
  Adds a source specified by the JSON config file argument to the given list of
  Collectors and prints the results in a table after doing so.

  Args:
    collector_list (list): The list of Collectors to be given the new
    source.

  The URL for the POST request to create a source for a Collector is given by 
  the API endpoint + 'collectors/{collectorId}/sources'. The JSON data from the
  file is sent in the contents of the request. A status code of 201 corresponds
  to success and 400 corresponds to some failure with a message in the response.
  '''
  json_file = open(args.addSource[0], 'r+')
  json_data = json.load(json_file)

  for collector in collector_list:
    url = args.url[0] + 'collectors/' + str(collector['id']) + '/sources'
    header = {'Content-Type': 'application/json'}
    r = requests.post(url, headers=header, json=json_data, auth=(args.accessid[0], args.accesskey[0]))
    
    if r.status_code == 400:
      collector['status'] = 'FAILURE'
      collector['description'] = r.json()['message']
    elif r.status_code == 201:
      collector['status'] = 'SUCCESS'
      collector['description'] = 'Added source %d.' % r.json()['source']['id'] 
  
  log('[COMPLETE] add source to collectors')
  print_collector_table(collector_list, ['name', 'status', 'description'])  


def change_source(collector_list, name = 'ProdWebServices'):
  '''
  Adds a source specified by the JSON config file argument to the given list of
  Collectors and prints the results in a table after doing so.

  Args:
    collector_list (list): The list of Collectors to be given the new
    source.

  The URL for the POST request to create a source for a Collector is given by 
  the API endpoint + 'collectors/{collectorId}/sources'. The JSON data from the
  file is sent in the contents of the request. A status code of 201 corresponds
  to success and 400 corresponds to some failure with a message in the response.
  '''
  json_file = open(args.changesource[0], 'r+')
  json_data = json.load(json_file)
  
  for collector in collector_list:
    for source in collector['sourcejson']:
      log( source['name'])
      if source['name'] == name:
        url = args.url[0] + 'collectors/' + str(collector['id']) + '/sources/' + str(source['id'])
        log(url)
        header = {'Content-Type': 'application/json'}
        #first get the source
        r = requests.get(url, headers=header, json=json_data, auth=(args.accessid[0], args.accesskey[0]))
        etag = r.headers['ETag']
        header = {'Content-Type': 'application/json', 'If-Match':etag}
        r = requests.post(url, headers=header, json=json_data, auth=(args.accessid[0], args.accesskey[0]))

        if r.status_code == 400 or r.status_code == 405:
          collector['status'] = 'FAILURE'
          collector['description'] = r.json()['message']
        elif r.status_code == 201:
          collector['status'] = 'SUCCESS'
          collector['description'] = 'Chnaged source %d.' % r.json()['source']['id'] 
  
    log('[COMPLETE] changed source in collectors')
    #print_collector_table(collector_list, ['name', 'status', 'description'])  


def filter_by(list, pairs):
  '''
  Uses a generator to filter the elements in the list by the specified pairs.
  Wildcard characters are allowed for the values of the key-value pairs.

  Args:
    list (list): The list of elements to be filtered.
    pairs (dict): The key-value pairs that the elements must have in order
    to be included.

  Yields:
    elem (object): The next element in the list that fulfills the conditions of
    the filter.
  '''
  for elem in list:
    is_valid = True
    for key in pairs:
      if (not key in elem) or (not re.match('^' + str(pairs[key]) + '$', str(elem[key]), flags=0)): 
        is_valid = False
        break
    if is_valid:
      yield elem

def filter_by_ids(list, ids):
  '''
  Uses a generator to filter the elements in the list by ID. The element
  need only have an ID contained in the given list of possible IDs.

  Args:
    list (list): The list of elements to be filtered.
    ids (list): The list of IDs that an element must have one of in order
    to be included.

  Yields:
    elem (object): The next element in the list that fulfills the
    stated condition.
  '''
  for elem in list:
    if str(elem['id']) in ids:
      yield elem

def filter_collectors(collector_list):
  '''
  Filters the given list of Collectors using the key-value pairs passed
  in the -filter command and returns this list.

  Args:
    collector_list (list): The list of Collectors to be filtered.

  Returns:
    list: The list of Collectors now filtered.

  A filter parameter can be of the form 'name=my-name', 'category=my-category',
  'version=19.155-13', or 'ids=1723253,1093253,232354'. IDs must be separated 
  in a list by commas.
  '''
  filter_pair = args.filter[0].replace('*', '.*').split('=', 1)
  filter_type = filter_pair[0]
  condition = filter_pair[1]

  if filter_type == 'name' or filter_type == 'category':
    return list(filter_by(collector_list, {filter_type: condition}))
  elif filter_type == 'version':
    return list(filter_by(collector_list, {'collectorVersion': condition}))
  elif filter_type == 'ids':
    id_list = condition.split(',')
    return list(filter_by_ids(collector_list, id_list))
  else:
    log('[ERROR] filter type does not exist, collectors will not be filtered')
    return collector_list 

from terminaltables import AsciiTable
def print_collector_table(collectors, headings):
  '''
  Given a set of headings and a list of Collectors, prints the attributes
  of each Collector (one per row) specified in the headings in a nice
  ASCII table. If an attribute is empty, a dash is printed in the column 
  instead.

  Args:
    collectors (list): The list of Collectors to be printed.
    headings (list): The list of headings for the table.
  '''
  table_data = []
  table_data.append(headings)
  table_rows = 0

  if collectors:
    for collector in collectors:
      row = []
      for col in headings:
        if col == 'category' and 'category' not in collector:
          row.append('-')
        elif col == 'version':
          row.append(collector['collectorVersion'])
        else:
          row.append(collector[col])
      table_data.append(row)  
    table_rows = len(table_data) - 1  
  else:
    table_data.append(['-'] * len(headings))   # prints blanks if table has no entries
  
  table = AsciiTable(table_data)
  log('[INFO] %d total collectors\n%s' % (table_rows, table.table))

def print_sources_table(collectors, headings):
  '''
  Given a set of headings and a list of Collectors, prints the attributes
  of each Collector (one per row) specified in the headings in a nice
  ASCII table. If an attribute is empty, a dash is printed in the column 
  instead.

  Args:
    collectors (list): The list of Collectors to be printed.
    headings (list): The list of headings for the table.
  '''
  table_data = []
  table_data.append(headings)
  table_rows = 0

  if collectors:
    for collector in collectors:
      for source in collector['sourcejson']:
        row = []
        row.append(collector['id'])
        for col in headings[1:]:
          row.append(source[col])
        table_data.append(row)  
    table_rows = len(table_data) - 1  
  else:
    table_data.append(['-'] * len(headings))   # prints blanks if table has no entries
  
  table = AsciiTable(table_data)
  log('[INFO] %d total sources\n%s' % (table_rows, table.table))
  

if __name__ == "__main__":
  if validate():
    table_headings = ['name', 'id', 'version', 'category', 'sourceSyncMode', 'alive']
    source_table_headings = ['collectorid','name', 'id', 'description', 'category']
    
    if args.listVersions:
      collectors = get_collectors('collectors', {'collectorType': 'Installable'})
    elif args.upgrade: 
      collectors = get_collectors('collectors/upgrades/collectors', None)
      check_for_upgraded(collectors)
      table_headings.append('action')
      msg = 'Perform upgrade to version ' + str(args.upgrade[0]) + ' with above Collectors? [Y/N]: '
    elif args.addSource: 
      any_source_collectors = get_collectors('collectors', {'collectorType': 'Installable', 'alive': True})
      collectors = list(filter_by(any_source_collectors, {'sourceSyncMode': 'UI'}))   # filters further 
      log('[INFO] skipping %d collectors not in UI mode...' % (len(any_source_collectors) - len(collectors)))
      msg = 'Add source from ' + str(args.addSource[0]) + ' to above Collectors? [Y/N]: '
    elif args.getsources:
      any_source_collectors = get_collectors('collectors', {'collectorType': 'Installable', 'alive': True})
      collectors = list(filter_by(any_source_collectors, {'sourceSyncMode': 'UI'}))   # filters further         
    elif args.changesource:
      any_source_collectors = get_collectors('collectors', {'collectorType': 'Installable', 'alive': True})
      collectors = list(filter_by(any_source_collectors, {'sourceSyncMode': 'UI'}))   # filters further          
      msg = 'Change source from ' + str(args.changesource[0]) + ' to above Collectors? [Y/N]: '
       
    if args.filter:
      log("Filtering")
      collectors = filter_collectors(collectors)
    else:
      collectors = list(filter_by(collectors, {'name': '.*'}))   # quick fix for invalid names

    print_collector_table(collectors, table_headings)

    if collectors and args.upgrade and prompt(msg):
      upgrade_collectors(list(filter_by(collectors, {'action': 'UPGRADE'})))
    elif collectors and args.addSource and prompt(msg):
      add_source(collectors)
    elif args.getsources:
      collectors_with_sources = get_sources_by_collector('collectors', collectors)
      print_sources_table(collectors_with_sources, source_table_headings)
    elif args.changesource  and prompt(msg):
      collectors_with_sources = get_sources_by_collector('collectors', collectors)
      print_sources_table(collectors_with_sources, source_table_headings)
      change_source(collectors_with_sources)
