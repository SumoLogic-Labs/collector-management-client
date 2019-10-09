# coding: utf-8

"""
    Sumo Logic API

    # Getting Started Welcome to the Sumo Logic API reference. You can use these APIs to interact with the Sumo Logic platform. For information on the collector and search APIs see our [API home page](https://help.sumologic.com/APIs). ## API Endpoints Sumo Logic has several deployments in different geographic locations. You'll need to use the Sumo Logic API endpoint corresponding to your geographic location. See the table below for the different API endpoints by deployment. For details determining your account's deployment see [API endpoints](https://help.sumologic.com/?cid=3011). <table>   <tr>     <td> <strong>Deployment</strong> </td>     <td> <strong>Endpoint</strong> </td>   </tr> <tr>     <td> AU </td>     <td> https://api.au.sumologic.com/api/ </td>   </tr>   <tr>     <td> CA </td>     <td> https://api.ca.sumologic.com/api/ </td>   </tr> <tr>     <td> DE </td>     <td> https://api.de.sumologic.com/api/ </td>   </tr>   <tr>     <td> EU </td>     <td> https://api.eu.sumologic.com/api/ </td>   </tr>   <tr>     <td> JP </td>     <td> https://api.jp.sumologic.com/api/ </td>   </tr>   <tr>     <td> US1 </td>     <td> https://api.sumologic.com/api/ </td>   </tr>   <tr>     <td> US2 </td>     <td> https://api.us2.sumologic.com/api/ </td>   </tr> </table> ## Authentication Sumo Logic supports the following options for API authentication: - Access ID and Access Key - Base64 encoded Access ID and Access Key  See [Access Keys](https://help.sumologic.com/Manage/Security/Access-Keys) to generate an Access Key. Make sure to copy the key you create, because it is displayed only once. When you have an Access ID and Access Key you can execute requests such as the following:   ```bash   curl -u \"<accessId>:<accessKey>\" -X GET https://api.<deployment>.sumologic.com/api/v1/users   ```  Where `deployment` is either `au`, `ca`, `de`, `eu`, `jp`, `us1`, or `us2`. See [API endpoints](#section/API-Endpoints) for details.  If you prefer to use basic access authentication, you can do a Base64 encoding of your `<accessId>:<accessKey>` to authenticate your HTTPS request. The following is an example request, replace the placeholder `<encoded>` with your encoded Access ID and Access Key string:   ```bash   curl -H \"Authorization: Basic <encoded>\" -X GET https://api.<deployment>.sumologic.com/api/v1/users   ```   Refer to [API Authentication](https://help.sumologic.com/?cid=3012) for a Base64 example.  ## Status Codes Generic status codes that apply to all our APIs. See the [HTTP status code registry](https://www.iana.org/assignments/http-status-codes/http-status-codes.xhtml) for reference. <table>   <tr>     <td> <strong>HTTP Status Code</strong> </td>     <td> <strong>Error Code</strong> </td>     <td> <strong>Description</strong> </td>   </tr>   <tr>     <td> 301 </td>     <td> moved </td>     <td> The requested resource SHOULD be accessed through returned URI in Location Header.</td>   </tr>   <tr>     <td> 401 </td>     <td> unauthorized </td>     <td> Credential could not be verified. </td>   </tr>   <tr>     <td> 403 </td>     <td> forbidden </td>     <td> This operation is not allowed for your account type or the user doesn't have the role capability to perform this action. </td>   </tr>   <tr>     <td> 404 </td>     <td> notfound </td>     <td> Requested resource could not be found. </td>   </tr>   <tr>     <td> 405 </td>     <td> method.unsupported </td>     <td> Unsupported method for URL. </td>   </tr>   <tr>     <td> 415 </td>     <td> contenttype.invalid </td>     <td> Invalid content type. </td>   </tr>   <tr>     <td> 429 </td>     <td> rate.limit.exceeded </td>     <td> The API request rate is higher than 4 request per second or inflight API requests are higher than 10 request per second. </td>   </tr>   <tr>     <td> 500 </td>     <td> internal.error </td>     <td> Internal server error. </td>   </tr>   <tr>     <td> 503 </td>     <td> service.unavailable </td>     <td> Service is currently unavailable. </td>   </tr> </table> ## Filtering Some API endpoints support filtering results on a specified set of fields. Each endpoint that supports filtering will list the fields that can be filtered. Multiple fields can be combined by using an ampersand `&` character.  For example, to get 20 users whose `firstName` is `John` and `lastName` is `Doe`:   ```bash   api.sumologic.com/v1/users?limit=20&firstName=John&lastName=Doe   ```  ## Sorting Some API endpoints support sorting fields by using the `sortBy` query parameter. The default sort order is ascending. Prefix the field with a minus sign `-` to sort in descending order.  For example, to get 20 users sorted by their `email` in descending order:   ```bash   api.sumologic.com/v1/users?limit=20&sort=-email   ```  ## Rate Limiting * A rate limit of four API requests per second (240 requests per minute) applies to all API calls from a user. * A rate limit of 10 concurrent requests to any API endpoint applies to an access key.  If a rate is exceeded, a rate limit exceeded 429 status code is returned.  ## Generating Clients You can use [OpenAPI Generator](https://openapi-generator.tech) to generate clients from the YAML file to access the API.  ### Using [NPM](https://www.npmjs.com/get-npm) 1. Install [NPM package wrapper](https://github.com/openapitools/openapi-generator-cli) globally, exposing the CLI   on the command line:   ```bash   npm install @openapitools/openapi-generator-cli -g   ```   You can see detailed instructions [here](https://openapi-generator.tech/docs/installation#npm).  2. Download the [YAML file](/docs/sumologic-api.yaml) and save it locally. Let's say the file is saved as `sumologic-api.yaml`. 3. Use the following command to generate `python` client inside the `sumo/client/python` directory:   ```bash   openapi-generator generate -i sumologic-api.yaml -g python -o sumo/client/python   ```   ### Using [Homebrew](https://brew.sh/) 1. Install OpenAPI Generator   ```bash   brew install openapi-generator   ```  2. Download the [YAML file](/docs/sumologic-api.yaml) and save it locally. Let's say the file is saved as `sumologic-api.yaml`. 3. Use the following command to generate `python` client side code inside the `sumo/client/python` directory:   ```bash   openapi-generator generate -i sumologic-api.yaml -g python -o sumo/client/python   ```   # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six
from swagger_client.models.metrics_alert_query import MetricsAlertQuery  # noqa: F401,E501
from swagger_client.models.metrics_monitor_mute_status import MetricsMonitorMuteStatus  # noqa: F401,E501
from swagger_client.models.metrics_monitor_rule import MetricsMonitorRule  # noqa: F401,E501
from swagger_client.models.resolvable_time_range import ResolvableTimeRange  # noqa: F401,E501


class MetricsMonitorDefinition(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'name': 'str',
        'description': 'str',
        'is_disabled': 'bool',
        'alert_queries': 'list[MetricsAlertQuery]',
        'queries_time_range': 'ResolvableTimeRange',
        'time_zone': 'str',
        'monitor_rules': 'list[MetricsMonitorRule]',
        'mute_status': 'MetricsMonitorMuteStatus',
        'chart_settings': 'str'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'is_disabled': 'isDisabled',
        'alert_queries': 'alertQueries',
        'queries_time_range': 'queriesTimeRange',
        'time_zone': 'timeZone',
        'monitor_rules': 'monitorRules',
        'mute_status': 'muteStatus',
        'chart_settings': 'chartSettings'
    }

    def __init__(self, name=None, description=None, is_disabled=None, alert_queries=None, queries_time_range=None, time_zone=None, monitor_rules=None, mute_status=None, chart_settings=None):  # noqa: E501
        """MetricsMonitorDefinition - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._description = None
        self._is_disabled = None
        self._alert_queries = None
        self._queries_time_range = None
        self._time_zone = None
        self._monitor_rules = None
        self._mute_status = None
        self._chart_settings = None
        self.discriminator = None
        self.name = name
        if description is not None:
            self.description = description
        self.is_disabled = is_disabled
        self.alert_queries = alert_queries
        self.queries_time_range = queries_time_range
        self.time_zone = time_zone
        self.monitor_rules = monitor_rules
        self.mute_status = mute_status
        if chart_settings is not None:
            self.chart_settings = chart_settings

    @property
    def name(self):
        """Gets the name of this MetricsMonitorDefinition.  # noqa: E501

        Name of the metrics monitor.  # noqa: E501

        :return: The name of this MetricsMonitorDefinition.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this MetricsMonitorDefinition.

        Name of the metrics monitor.  # noqa: E501

        :param name: The name of this MetricsMonitorDefinition.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def description(self):
        """Gets the description of this MetricsMonitorDefinition.  # noqa: E501

        Monitor description.  # noqa: E501

        :return: The description of this MetricsMonitorDefinition.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this MetricsMonitorDefinition.

        Monitor description.  # noqa: E501

        :param description: The description of this MetricsMonitorDefinition.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def is_disabled(self):
        """Gets the is_disabled of this MetricsMonitorDefinition.  # noqa: E501

        Is the monitor enabled.  # noqa: E501

        :return: The is_disabled of this MetricsMonitorDefinition.  # noqa: E501
        :rtype: bool
        """
        return self._is_disabled

    @is_disabled.setter
    def is_disabled(self, is_disabled):
        """Sets the is_disabled of this MetricsMonitorDefinition.

        Is the monitor enabled.  # noqa: E501

        :param is_disabled: The is_disabled of this MetricsMonitorDefinition.  # noqa: E501
        :type: bool
        """
        if is_disabled is None:
            raise ValueError("Invalid value for `is_disabled`, must not be `None`")  # noqa: E501

        self._is_disabled = is_disabled

    @property
    def alert_queries(self):
        """Gets the alert_queries of this MetricsMonitorDefinition.  # noqa: E501

        Monitor's queries.  # noqa: E501

        :return: The alert_queries of this MetricsMonitorDefinition.  # noqa: E501
        :rtype: list[MetricsAlertQuery]
        """
        return self._alert_queries

    @alert_queries.setter
    def alert_queries(self, alert_queries):
        """Sets the alert_queries of this MetricsMonitorDefinition.

        Monitor's queries.  # noqa: E501

        :param alert_queries: The alert_queries of this MetricsMonitorDefinition.  # noqa: E501
        :type: list[MetricsAlertQuery]
        """
        if alert_queries is None:
            raise ValueError("Invalid value for `alert_queries`, must not be `None`")  # noqa: E501

        self._alert_queries = alert_queries

    @property
    def queries_time_range(self):
        """Gets the queries_time_range of this MetricsMonitorDefinition.  # noqa: E501


        :return: The queries_time_range of this MetricsMonitorDefinition.  # noqa: E501
        :rtype: ResolvableTimeRange
        """
        return self._queries_time_range

    @queries_time_range.setter
    def queries_time_range(self, queries_time_range):
        """Sets the queries_time_range of this MetricsMonitorDefinition.


        :param queries_time_range: The queries_time_range of this MetricsMonitorDefinition.  # noqa: E501
        :type: ResolvableTimeRange
        """
        if queries_time_range is None:
            raise ValueError("Invalid value for `queries_time_range`, must not be `None`")  # noqa: E501

        self._queries_time_range = queries_time_range

    @property
    def time_zone(self):
        """Gets the time_zone of this MetricsMonitorDefinition.  # noqa: E501

        Time zone.  # noqa: E501

        :return: The time_zone of this MetricsMonitorDefinition.  # noqa: E501
        :rtype: str
        """
        return self._time_zone

    @time_zone.setter
    def time_zone(self, time_zone):
        """Sets the time_zone of this MetricsMonitorDefinition.

        Time zone.  # noqa: E501

        :param time_zone: The time_zone of this MetricsMonitorDefinition.  # noqa: E501
        :type: str
        """
        if time_zone is None:
            raise ValueError("Invalid value for `time_zone`, must not be `None`")  # noqa: E501

        self._time_zone = time_zone

    @property
    def monitor_rules(self):
        """Gets the monitor_rules of this MetricsMonitorDefinition.  # noqa: E501

        Monitor rules.  # noqa: E501

        :return: The monitor_rules of this MetricsMonitorDefinition.  # noqa: E501
        :rtype: list[MetricsMonitorRule]
        """
        return self._monitor_rules

    @monitor_rules.setter
    def monitor_rules(self, monitor_rules):
        """Sets the monitor_rules of this MetricsMonitorDefinition.

        Monitor rules.  # noqa: E501

        :param monitor_rules: The monitor_rules of this MetricsMonitorDefinition.  # noqa: E501
        :type: list[MetricsMonitorRule]
        """
        if monitor_rules is None:
            raise ValueError("Invalid value for `monitor_rules`, must not be `None`")  # noqa: E501

        self._monitor_rules = monitor_rules

    @property
    def mute_status(self):
        """Gets the mute_status of this MetricsMonitorDefinition.  # noqa: E501


        :return: The mute_status of this MetricsMonitorDefinition.  # noqa: E501
        :rtype: MetricsMonitorMuteStatus
        """
        return self._mute_status

    @mute_status.setter
    def mute_status(self, mute_status):
        """Sets the mute_status of this MetricsMonitorDefinition.


        :param mute_status: The mute_status of this MetricsMonitorDefinition.  # noqa: E501
        :type: MetricsMonitorMuteStatus
        """
        if mute_status is None:
            raise ValueError("Invalid value for `mute_status`, must not be `None`")  # noqa: E501

        self._mute_status = mute_status

    @property
    def chart_settings(self):
        """Gets the chart_settings of this MetricsMonitorDefinition.  # noqa: E501

        Chart settings.  # noqa: E501

        :return: The chart_settings of this MetricsMonitorDefinition.  # noqa: E501
        :rtype: str
        """
        return self._chart_settings

    @chart_settings.setter
    def chart_settings(self, chart_settings):
        """Sets the chart_settings of this MetricsMonitorDefinition.

        Chart settings.  # noqa: E501

        :param chart_settings: The chart_settings of this MetricsMonitorDefinition.  # noqa: E501
        :type: str
        """

        self._chart_settings = chart_settings

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(MetricsMonitorDefinition, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, MetricsMonitorDefinition):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
