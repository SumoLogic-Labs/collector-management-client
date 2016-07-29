Collector Management Script
============

Managing a specified subset of installed Collectors can be done by running this script written in Python. The script allows for the ability to upgrade or downgrade Collectors to the desired version, add a source to the Collectors, and list relevant information, namely version number, for the Collectors.

### Installation
The modules [requests](https://github.com/kennethreitz/requests) and [terminaltables](https://github.com/Robpol86/terminaltables) must be installed in order for the script to run properly. This can be done by simply running the commands: 
```
pip install requests
pip install terminaltables
```

### Requirements
**Upgrading**

* A Collector is considered upgradable if it is in the current org, is installable, not currently upgrading, and not on the upgrade-to version. See the [Upgrading Collectors help page](https://help.sumologic.com/APIs/Collector_Management_API/Upgrade_or_Downgrade_Collectors_Using_the_API).

**Adding Sources**

* A Collector may add a source if the following fields are of the given values: `"sourceSyncMode": "UI"`, `"collectorType": "Installable"`, `"alive": true`.
* For a source like Host Metrics, the Collector must also be a version that is able to support it.

The '-url', '-accessid', and '-accesskey' parameters should be passed with their respective arguments in order for API authentication purposes. For example, the API endpoint for US1 is `https://api.sumologic.com/api/v1/`. API endpoints can be found in the [Collector Management API](https://help.sumologic.com/APIs/Collector_Management_API/About_the_Collector_Management_API). Be sure to use the exact URL provided.

As an alternative, if an access ID and access key are not provided, the user will simply be prompted to enter the access ID and key manually before proceeding.

### Filtering Collectors
An optional '-filter' parameter with arguments can be passed to narrow the set of Collectors that will be modified for any of the three available commands. The list of Collectors can be filtered by _name_, _category_, _version_, or _ids_ fields as shown

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
Relevant information about a subset of Collectors can be printed using the '-listVersions' command. An ASCII table displaying each Collector's `name`, `id`, `collectorVersion`, `category`, `sourceSyncMode`, and `alive` attributes will be output. 

Sample call:
```
$ python sumo_mgmt.py -url https://api.sumologic.com/api/v1/ -accessid [YOUR ACCESS ID] -accesskey [YOUR ACCESS KEY] -listVersions
```

### Upgrading Collectors
A given subset of Collectors can be upgraded to a desired version via the '-upgrade' command and the version number (e.g. `19.155-13`). The argument `latest` may be passed to simply upgrade to the latest production version.

By default, the Collectors are upgraded simultaneously in batches of 100, but an additional parameter '-batchSize' with a number between 1 and 100 may also be given.

The progress of the upgrades are queried about once every ten seconds and is printed in a corresponding table. All print statements are prepended with a timestamp to allow for logging.

Sample call:
```
$ python sumo_mgmt.py -url https://api.sumologic.com/api/v1/ -accessid [YOUR ACCESS ID] -accesskey [YOUR ACCESS KEY] -upgrade latest -batchSize 20
```

To bypass the confirmation prompts before this command, pass the '-y' flag. This also applies to the '-addSource' command.

### Adding (Host Metrics) Source to Collectors
The Host Metrics Source can be quickly added to a specified subset of Collectors by running the '-addSource' command along with a file path. This procedure can be generalized for other types of sources as well. For more information on formatting the JSON file, see the [Collector Management API](https://help.sumologic.com/APIs/Collector_Management_API/About_the_Collector_Management_API).

A JSON configuration file must be provided to add the source to a Collector.

Sample call:
```
$ python sumo_mgmt.py -url https://api.sumologic.com/api/v1/ -accessid [YOUR ACCESS ID] -accesskey [YOUR ACCESS KEY] -addSource [YOUR JSON FILE]
```

Provided sample file for Host Metrics: 
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

Attributes may be modified and include:

  * **name**: Name of the source (String)
  * **sourceType**: Type of source (String)
  * **interval**: Interval in milliseconds between each metrics ingest (Int)
  * **metrics**: List of metrics datapoints to be collected (Array)

See the [Host Metrics help page](https://docs.google.com/document/d/1akczEaoJkXCxvOZZzF_W-3X97KBKRYhwA4RCvW6kStY/edit#heading=h.hv8q5bn0byvm) for a list of metrics available.

### More Examples
Below are some additional example use cases.

***Getting help with the commands***
```
$ python sumo_mgmt.py -h
```

***Bypassing prompts***
```
$ python sumo_mgmt.py -url https://api.sumologic.com/api/v1/ -accessid [YOUR ACCESS ID] -accesskey [YOUR ACCESS KEY] -addSource source.json -y
```

***Upgrading all Collectors running version A to version B***
```
$ python sumo_mgmt.py -url https://api.sumologic.com/api/v1/ -accessid [YOUR ACCESS ID] -accesskey [YOUR ACCESS KEY] -upgrade B -filter version=A
```
