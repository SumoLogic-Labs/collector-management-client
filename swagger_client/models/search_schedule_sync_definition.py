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
from swagger_client.models.notification_threshold_sync_definition import NotificationThresholdSyncDefinition  # noqa: F401,E501
from swagger_client.models.resolvable_time_range import ResolvableTimeRange  # noqa: F401,E501
from swagger_client.models.schedule_notification_sync_definition import ScheduleNotificationSyncDefinition  # noqa: F401,E501
from swagger_client.models.schedule_search_parameter_sync_definition import ScheduleSearchParameterSyncDefinition  # noqa: F401,E501


class SearchScheduleSyncDefinition(object):
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
        'cron_expression': 'str',
        'displayable_time_range': 'str',
        'parseable_time_range': 'ResolvableTimeRange',
        'time_zone': 'str',
        'threshold': 'NotificationThresholdSyncDefinition',
        'notification': 'ScheduleNotificationSyncDefinition',
        'schedule_type': 'str',
        'mute_error_emails': 'bool',
        'parameters': 'list[ScheduleSearchParameterSyncDefinition]'
    }

    attribute_map = {
        'cron_expression': 'cronExpression',
        'displayable_time_range': 'displayableTimeRange',
        'parseable_time_range': 'parseableTimeRange',
        'time_zone': 'timeZone',
        'threshold': 'threshold',
        'notification': 'notification',
        'schedule_type': 'scheduleType',
        'mute_error_emails': 'muteErrorEmails',
        'parameters': 'parameters'
    }

    def __init__(self, cron_expression=None, displayable_time_range=None, parseable_time_range=None, time_zone=None, threshold=None, notification=None, schedule_type=None, mute_error_emails=None, parameters=None):  # noqa: E501
        """SearchScheduleSyncDefinition - a model defined in Swagger"""  # noqa: E501
        self._cron_expression = None
        self._displayable_time_range = None
        self._parseable_time_range = None
        self._time_zone = None
        self._threshold = None
        self._notification = None
        self._schedule_type = None
        self._mute_error_emails = None
        self._parameters = None
        self.discriminator = None
        if cron_expression is not None:
            self.cron_expression = cron_expression
        if displayable_time_range is not None:
            self.displayable_time_range = displayable_time_range
        self.parseable_time_range = parseable_time_range
        self.time_zone = time_zone
        if threshold is not None:
            self.threshold = threshold
        self.notification = notification
        self.schedule_type = schedule_type
        if mute_error_emails is not None:
            self.mute_error_emails = mute_error_emails
        self.parameters = parameters

    @property
    def cron_expression(self):
        """Gets the cron_expression of this SearchScheduleSyncDefinition.  # noqa: E501

        Cron-like expression specifying the search's schedule. Field scheduleType must be set to \"Custom\", otherwise, scheduleType takes precedence over cronExpression.  # noqa: E501

        :return: The cron_expression of this SearchScheduleSyncDefinition.  # noqa: E501
        :rtype: str
        """
        return self._cron_expression

    @cron_expression.setter
    def cron_expression(self, cron_expression):
        """Sets the cron_expression of this SearchScheduleSyncDefinition.

        Cron-like expression specifying the search's schedule. Field scheduleType must be set to \"Custom\", otherwise, scheduleType takes precedence over cronExpression.  # noqa: E501

        :param cron_expression: The cron_expression of this SearchScheduleSyncDefinition.  # noqa: E501
        :type: str
        """

        self._cron_expression = cron_expression

    @property
    def displayable_time_range(self):
        """Gets the displayable_time_range of this SearchScheduleSyncDefinition.  # noqa: E501

        A human-friendly text describing the query time range. For e.g. \"-2h\", \"last three days\", \"team default time\"  # noqa: E501

        :return: The displayable_time_range of this SearchScheduleSyncDefinition.  # noqa: E501
        :rtype: str
        """
        return self._displayable_time_range

    @displayable_time_range.setter
    def displayable_time_range(self, displayable_time_range):
        """Sets the displayable_time_range of this SearchScheduleSyncDefinition.

        A human-friendly text describing the query time range. For e.g. \"-2h\", \"last three days\", \"team default time\"  # noqa: E501

        :param displayable_time_range: The displayable_time_range of this SearchScheduleSyncDefinition.  # noqa: E501
        :type: str
        """

        self._displayable_time_range = displayable_time_range

    @property
    def parseable_time_range(self):
        """Gets the parseable_time_range of this SearchScheduleSyncDefinition.  # noqa: E501


        :return: The parseable_time_range of this SearchScheduleSyncDefinition.  # noqa: E501
        :rtype: ResolvableTimeRange
        """
        return self._parseable_time_range

    @parseable_time_range.setter
    def parseable_time_range(self, parseable_time_range):
        """Sets the parseable_time_range of this SearchScheduleSyncDefinition.


        :param parseable_time_range: The parseable_time_range of this SearchScheduleSyncDefinition.  # noqa: E501
        :type: ResolvableTimeRange
        """
        if parseable_time_range is None:
            raise ValueError("Invalid value for `parseable_time_range`, must not be `None`")  # noqa: E501

        self._parseable_time_range = parseable_time_range

    @property
    def time_zone(self):
        """Gets the time_zone of this SearchScheduleSyncDefinition.  # noqa: E501

        Time zone identifier for time specification. Either an abbreviation such as \"PST\", a full name such as \"America/Los_Angeles\", or a custom ID such as \"GMT-8:00\". Note that the support of abbreviations is for JDK 1.1.x compatibility only and full names should be used.  # noqa: E501

        :return: The time_zone of this SearchScheduleSyncDefinition.  # noqa: E501
        :rtype: str
        """
        return self._time_zone

    @time_zone.setter
    def time_zone(self, time_zone):
        """Sets the time_zone of this SearchScheduleSyncDefinition.

        Time zone identifier for time specification. Either an abbreviation such as \"PST\", a full name such as \"America/Los_Angeles\", or a custom ID such as \"GMT-8:00\". Note that the support of abbreviations is for JDK 1.1.x compatibility only and full names should be used.  # noqa: E501

        :param time_zone: The time_zone of this SearchScheduleSyncDefinition.  # noqa: E501
        :type: str
        """
        if time_zone is None:
            raise ValueError("Invalid value for `time_zone`, must not be `None`")  # noqa: E501

        self._time_zone = time_zone

    @property
    def threshold(self):
        """Gets the threshold of this SearchScheduleSyncDefinition.  # noqa: E501


        :return: The threshold of this SearchScheduleSyncDefinition.  # noqa: E501
        :rtype: NotificationThresholdSyncDefinition
        """
        return self._threshold

    @threshold.setter
    def threshold(self, threshold):
        """Sets the threshold of this SearchScheduleSyncDefinition.


        :param threshold: The threshold of this SearchScheduleSyncDefinition.  # noqa: E501
        :type: NotificationThresholdSyncDefinition
        """

        self._threshold = threshold

    @property
    def notification(self):
        """Gets the notification of this SearchScheduleSyncDefinition.  # noqa: E501


        :return: The notification of this SearchScheduleSyncDefinition.  # noqa: E501
        :rtype: ScheduleNotificationSyncDefinition
        """
        return self._notification

    @notification.setter
    def notification(self, notification):
        """Sets the notification of this SearchScheduleSyncDefinition.


        :param notification: The notification of this SearchScheduleSyncDefinition.  # noqa: E501
        :type: ScheduleNotificationSyncDefinition
        """
        if notification is None:
            raise ValueError("Invalid value for `notification`, must not be `None`")  # noqa: E501

        self._notification = notification

    @property
    def schedule_type(self):
        """Gets the schedule_type of this SearchScheduleSyncDefinition.  # noqa: E501

        Run schedule of the scheduled search. Set to \"Custom\" to specify the schedule with a CRON expression. Possible schedule types are:   - `RealTime`   - `15Minutes`   - `1Hour`   - `2Hours`   - `4Hours`   - `6Hours`   - `8Hours`   - `12Hours`   - `1Day`   - `1Week`   - `Custom`  # noqa: E501

        :return: The schedule_type of this SearchScheduleSyncDefinition.  # noqa: E501
        :rtype: str
        """
        return self._schedule_type

    @schedule_type.setter
    def schedule_type(self, schedule_type):
        """Sets the schedule_type of this SearchScheduleSyncDefinition.

        Run schedule of the scheduled search. Set to \"Custom\" to specify the schedule with a CRON expression. Possible schedule types are:   - `RealTime`   - `15Minutes`   - `1Hour`   - `2Hours`   - `4Hours`   - `6Hours`   - `8Hours`   - `12Hours`   - `1Day`   - `1Week`   - `Custom`  # noqa: E501

        :param schedule_type: The schedule_type of this SearchScheduleSyncDefinition.  # noqa: E501
        :type: str
        """
        if schedule_type is None:
            raise ValueError("Invalid value for `schedule_type`, must not be `None`")  # noqa: E501

        self._schedule_type = schedule_type

    @property
    def mute_error_emails(self):
        """Gets the mute_error_emails of this SearchScheduleSyncDefinition.  # noqa: E501

        If enabled, emails are not sent out in case of errors with the search.  # noqa: E501

        :return: The mute_error_emails of this SearchScheduleSyncDefinition.  # noqa: E501
        :rtype: bool
        """
        return self._mute_error_emails

    @mute_error_emails.setter
    def mute_error_emails(self, mute_error_emails):
        """Sets the mute_error_emails of this SearchScheduleSyncDefinition.

        If enabled, emails are not sent out in case of errors with the search.  # noqa: E501

        :param mute_error_emails: The mute_error_emails of this SearchScheduleSyncDefinition.  # noqa: E501
        :type: bool
        """

        self._mute_error_emails = mute_error_emails

    @property
    def parameters(self):
        """Gets the parameters of this SearchScheduleSyncDefinition.  # noqa: E501

        A list of scheduled search parameters.  # noqa: E501

        :return: The parameters of this SearchScheduleSyncDefinition.  # noqa: E501
        :rtype: list[ScheduleSearchParameterSyncDefinition]
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters):
        """Sets the parameters of this SearchScheduleSyncDefinition.

        A list of scheduled search parameters.  # noqa: E501

        :param parameters: The parameters of this SearchScheduleSyncDefinition.  # noqa: E501
        :type: list[ScheduleSearchParameterSyncDefinition]
        """
        if parameters is None:
            raise ValueError("Invalid value for `parameters`, must not be `None`")  # noqa: E501

        self._parameters = parameters

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
        if issubclass(SearchScheduleSyncDefinition, dict):
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
        if not isinstance(other, SearchScheduleSyncDefinition):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
