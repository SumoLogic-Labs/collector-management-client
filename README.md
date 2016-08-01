Collector Management Script
============

This Python script allows managing a set of installed Collectors. The script currently supports:

* Listing details for a set of Collectors
* Upgrading or downgrading a set of Collectors to a desired version
* Adding a collection source to a set of Collectors

### Required Modules
The modules [requests](https://github.com/kennethreitz/requests) and [terminaltables](https://github.com/Robpol86/terminaltables) must be installed in order for the script to run properly. This can be done by simply running the commands: 
```
pip install requests
pip install terminaltables
```

### Common Parameters
The `-url`, `-accessid`, and `-accesskey` parameters are required for API authentication purposes. API endpoints can be found in the [Collector Management API](https://help.sumologic.com/APIs/Collector_Management_API/About_the_Collector_Management_API).  To generate a Sumo Logic Access Id and Access Key, see [Create Access Keys](https://help.sumologic.com/Manage/Security/Access_Keys/Create_Access_Keys).

If `-accessid` and `-accesskey` are not provided via command line arguments, the script will prompt the user to enter the access ID and key manually before proceeding.

The optional `-y` parameter can be used to bypass user prompts.

### Filtering Collectors
An optional `-filter` parameter is used to narrow the set of Collectors that will be modified for any of the three available commands. Collectors can be filtered by _name_, _category_, _version_, or _ids_ fields.

The _name_ field specifies a Collector name to filter. The wildcard character `*` may also be used.
```
-filter name=prod-collector-*
```

The _category_ field specifies a Collector category to filter. The wildcard character `*` may also be used here.
```
-filter category=test
```

The _version_ field specifies a Collector version number to filter.
```
-filter version=19.155-13
```

The _id_ field specifies a list of Collector IDs to filter, separated by commas. 
```
-filter ids=1234567,1726010,5555123
```

### Listing Versions
Relevant information about a subset of Collectors can be printed using the `-listVersions` command. An ASCII table displaying each Collector's name, id, version, category, sourceSyncMode (either "UI" or "json"), and whether the collector is "alive" (online).

Example:
```
$ python sumo_mgmt.py -url https://api.sumologic.com/api/v1/ -accessid [YOUR ACCESS ID] -accesskey [YOUR ACCESS KEY] -listVersions
```
Output:
```
2016-08-01 11:26:11,292 -0700 [PROGRESS] fetching and sorting through the next 1 to 4 collectors
2016-08-01 11:26:11,293 -0700 [INFO] 4 total collectors
+----------+-----------+-----------+----------+----------------+-------+
| name     | id        | version   | category | sourceSyncMode | alive |
+----------+-----------+-----------+----------+----------------+-------+
| ubuntu-1 | 100000077 | 19.155-13 | -        | UI             | True  |
| ubuntu-2 | 100000078 | 19.155-13 | -        | UI             | True  |
| ubuntu-3 | 100000079 | 19.155-13 | -        | UI             | True  |
| ubuntu-4 | 100000080 | 19.155-13 | -        | UI             | True  |
+----------+-----------+-----------+----------+----------------+-------+
```

### Upgrading Collectors
A given subset of Collectors can be upgraded to a desired version via the `-upgrade` command and the version number (e.g. `19.155-13`). The argument `latest` may be passed to simply upgrade to the latest production version.

A Collector is considered upgradable if it belongs to the same customer account, is installable, not currently upgrading, and not already running the upgrade-to version. See the [Upgrading Collectors help page](https://help.sumologic.com/APIs/Collector_Management_API/Upgrade_or_Downgrade_Collectors_Using_the_API).

By default, the Collectors are upgraded simultaneously in batches of 100, but an additional parameter `-batchSize` with a number between 1 and 100 may also be provided.

The progress of the upgrades are queried about once every ten seconds and is printed in a corresponding table. All print statements are prepended with a timestamp to allow for logging.

Example:
```
$ python sumo_mgmt.py -url https://api.sumologic.com/api/v1/ -accessid [YOUR ACCESS ID] -accesskey [YOUR ACCESS KEY] -upgrade latest -batchSize 20
```

Output:
```
2016-08-01 13:40:32,618 -0700 [START] upgrade for (1 to 4) of 4 collectors
...
2016-08-01 13:45:24,107 -0700 [PROGRESS] upgrade for (1 to 4) of 4 collectors
2016-08-01 13:45:24,108 -0700 [INFO] 4 total collectors
+----------+-------------+-------------+
| name     | status      | description |
+----------+-------------+-------------+
| ubuntu-1 | PENDING     |             |
| ubuntu-2 | PENDING     |             |
| ubuntu-3 | SUCCESS     |             |
| ubuntu-4 | IN PROGRESS |             |
+----------+-------------+-------------+
...
2016-08-01 13:51:49,364 -0700 [PROGRESS] upgrade for (1 to 4) of 4 collectors
2016-08-01 13:51:49,364 -0700 [INFO] 4 total collectors
+----------+---------+-------------+
| name     | status  | description |
+----------+---------+-------------+
| ubuntu-1 | SUCCESS |             |
| ubuntu-2 | SUCCESS |             |
| ubuntu-3 | SUCCESS |             |
| ubuntu-4 | SUCCESS |             |
+----------+---------+-------------+
2016-08-01 13:51:49,365 -0700 [COMPLETE] upgrade for (1 to 4) of 4 collectors
```

### Adding a Source to Collectors
A collection source can be added to a specified subset of Collectors by running the `-addSource` command along with a file path to a single JSON file containing the source definition. For more example sources types, see the help page [Use JSON to Configure Sources](https://help.sumologic.com/Send_Data/Sources/Use_JSON_to_Configure_Sources).  Note that the [Collector Management API](https://help.sumologic.com/APIs/Collector_Management_API/About_the_Collector_Management_API) only supports adding a single source at a time. The JSON file cannot contain an array of sources. Collectors must be running in cloud-managed mode (i.e., not using local JSON configuration) and must be online (`"alive": true`).

A JSON configuration file must be provided to add the source to a Collector.

Example:
```
$ python sumo_mgmt.py -url https://api.sumologic.com/api/v1/ -accessid [YOUR ACCESS ID] -accesskey [YOUR ACCESS KEY] -addSource /path/to/source.json
```

Output:
```
2016-08-01 11:30:27,502 -0700 [PROGRESS] fetching and sorting through the next 1 to 33 collectors
2016-08-01 11:30:27,503 -0700 [INFO] skipping 29 Collectors not in UI mode...
2016-08-01 11:30:27,504 -0700 [INFO] 4 total collectors
+----------+-----------+-----------+----------+----------------+-------+
| name     | id        | version   | category | sourceSyncMode | alive |
+----------+-----------+-----------+----------+----------------+-------+
| ubuntu-1 | 100000077 | 19.155-13 | -        | UI             | True  |
| ubuntu-2 | 100000078 | 19.155-13 | -        | UI             | True  |
| ubuntu-3 | 100000079 | 19.155-13 | -        | UI             | True  |
| ubuntu-4 | 100000080 | 19.155-13 | -        | UI             | True  |
+----------+-----------+-----------+----------+----------------+-------+
Add source from source.json to above Collectors? [Y/N]: Y
2016-08-01 11:30:35,898 -0700 [COMPLETE] add source to collectors
2016-08-01 11:30:35,899 -0700 [INFO] 4 total collectors
+----------+-----------+---------+-------------+
| name     | id        | status  | description |
+----------+-----------+---------+-------------+
| ubuntu-1 | 100000077 | SUCCESS |             |
| ubuntu-2 | 100000078 | SUCCESS |             |
| ubuntu-3 | 100000079 | SUCCESS |             |
| ubuntu-4 | 100000080 | SUCCESS |             |
+----------+-----------+---------+-------------+
```


Example Host Metrics source JSON file: 
```json
{
	"source": {
		"name": "Host_Metrics",
		"sourceType": "SystemStats",
		"interval": 60000,
		"metrics": ["CPU_User", "CPU_Sys", "Mem_Used"]
	}
}
```

### More Examples
Below are some additional example use cases.

***Getting help with the commands***
```
$ python sumo_mgmt.py -h
```

***Upgrading all Collectors running version A to version B***
```
$ python sumo_mgmt.py -url https://api.sumologic.com/api/v1/ -accessid [YOUR ACCESS ID] -accesskey [YOUR ACCESS KEY] -filter version=A -upgrade B
```
