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
from swagger_client.models.action import Action  # noqa: F401,E501
from swagger_client.models.on_time_interval_actions import OnTimeIntervalActions  # noqa: F401,E501


class RuleActions(object):
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
        'sessionize': 'bool',
        'session_key': 'str',
        'session_duration_time': 'int',
        'session_duration_time_unit': 'str',
        'on_first_trigger': 'list[Action]',
        'on_subsequent_trigger': 'list[Action]',
        'on_every_trigger': 'list[Action]',
        'on_time_interval': 'OnTimeIntervalActions',
        'on_time_expiration': 'list[Action]'
    }

    attribute_map = {
        'sessionize': 'sessionize',
        'session_key': 'sessionKey',
        'session_duration_time': 'sessionDurationTime',
        'session_duration_time_unit': 'sessionDurationTimeUnit',
        'on_first_trigger': 'onFirstTrigger',
        'on_subsequent_trigger': 'onSubsequentTrigger',
        'on_every_trigger': 'onEveryTrigger',
        'on_time_interval': 'onTimeInterval',
        'on_time_expiration': 'onTimeExpiration'
    }

    def __init__(self, sessionize=None, session_key=None, session_duration_time=None, session_duration_time_unit=None, on_first_trigger=None, on_subsequent_trigger=None, on_every_trigger=None, on_time_interval=None, on_time_expiration=None):  # noqa: E501
        """RuleActions - a model defined in Swagger"""  # noqa: E501
        self._sessionize = None
        self._session_key = None
        self._session_duration_time = None
        self._session_duration_time_unit = None
        self._on_first_trigger = None
        self._on_subsequent_trigger = None
        self._on_every_trigger = None
        self._on_time_interval = None
        self._on_time_expiration = None
        self.discriminator = None
        self.sessionize = sessionize
        if session_key is not None:
            self.session_key = session_key
        if session_duration_time is not None:
            self.session_duration_time = session_duration_time
        if session_duration_time_unit is not None:
            self.session_duration_time_unit = session_duration_time_unit
        if on_first_trigger is not None:
            self.on_first_trigger = on_first_trigger
        if on_subsequent_trigger is not None:
            self.on_subsequent_trigger = on_subsequent_trigger
        if on_every_trigger is not None:
            self.on_every_trigger = on_every_trigger
        if on_time_interval is not None:
            self.on_time_interval = on_time_interval
        if on_time_expiration is not None:
            self.on_time_expiration = on_time_expiration

    @property
    def sessionize(self):
        """Gets the sessionize of this RuleActions.  # noqa: E501

        Whether or not to sessionize the actions from this cloud SIEM rule.  # noqa: E501

        :return: The sessionize of this RuleActions.  # noqa: E501
        :rtype: bool
        """
        return self._sessionize

    @sessionize.setter
    def sessionize(self, sessionize):
        """Sets the sessionize of this RuleActions.

        Whether or not to sessionize the actions from this cloud SIEM rule.  # noqa: E501

        :param sessionize: The sessionize of this RuleActions.  # noqa: E501
        :type: bool
        """
        if sessionize is None:
            raise ValueError("Invalid value for `sessionize`, must not be `None`")  # noqa: E501

        self._sessionize = sessionize

    @property
    def session_key(self):
        """Gets the session_key of this RuleActions.  # noqa: E501

        Unique key for the session. When actions are sessionized, all events with the same sessionKey value follow the same session. Applicable only when the sessionize field is set to true.  # noqa: E501

        :return: The session_key of this RuleActions.  # noqa: E501
        :rtype: str
        """
        return self._session_key

    @session_key.setter
    def session_key(self, session_key):
        """Sets the session_key of this RuleActions.

        Unique key for the session. When actions are sessionized, all events with the same sessionKey value follow the same session. Applicable only when the sessionize field is set to true.  # noqa: E501

        :param session_key: The session_key of this RuleActions.  # noqa: E501
        :type: str
        """

        self._session_key = session_key

    @property
    def session_duration_time(self):
        """Gets the session_duration_time of this RuleActions.  # noqa: E501

        Session time duration. Applicable only when the sessionize field is set to true.  # noqa: E501

        :return: The session_duration_time of this RuleActions.  # noqa: E501
        :rtype: int
        """
        return self._session_duration_time

    @session_duration_time.setter
    def session_duration_time(self, session_duration_time):
        """Sets the session_duration_time of this RuleActions.

        Session time duration. Applicable only when the sessionize field is set to true.  # noqa: E501

        :param session_duration_time: The session_duration_time of this RuleActions.  # noqa: E501
        :type: int
        """

        self._session_duration_time = session_duration_time

    @property
    def session_duration_time_unit(self):
        """Gets the session_duration_time_unit of this RuleActions.  # noqa: E501

        Unit of time that is specified in the sessionDurationTime field. Applicable only when the sessionize field is set to true.  # noqa: E501

        :return: The session_duration_time_unit of this RuleActions.  # noqa: E501
        :rtype: str
        """
        return self._session_duration_time_unit

    @session_duration_time_unit.setter
    def session_duration_time_unit(self, session_duration_time_unit):
        """Sets the session_duration_time_unit of this RuleActions.

        Unit of time that is specified in the sessionDurationTime field. Applicable only when the sessionize field is set to true.  # noqa: E501

        :param session_duration_time_unit: The session_duration_time_unit of this RuleActions.  # noqa: E501
        :type: str
        """

        self._session_duration_time_unit = session_duration_time_unit

    @property
    def on_first_trigger(self):
        """Gets the on_first_trigger of this RuleActions.  # noqa: E501

        The list of actions to perform on the first trigger of the session.  # noqa: E501

        :return: The on_first_trigger of this RuleActions.  # noqa: E501
        :rtype: list[Action]
        """
        return self._on_first_trigger

    @on_first_trigger.setter
    def on_first_trigger(self, on_first_trigger):
        """Sets the on_first_trigger of this RuleActions.

        The list of actions to perform on the first trigger of the session.  # noqa: E501

        :param on_first_trigger: The on_first_trigger of this RuleActions.  # noqa: E501
        :type: list[Action]
        """

        self._on_first_trigger = on_first_trigger

    @property
    def on_subsequent_trigger(self):
        """Gets the on_subsequent_trigger of this RuleActions.  # noqa: E501

        The list of actions to perform on the subsequent triggers of the session.  # noqa: E501

        :return: The on_subsequent_trigger of this RuleActions.  # noqa: E501
        :rtype: list[Action]
        """
        return self._on_subsequent_trigger

    @on_subsequent_trigger.setter
    def on_subsequent_trigger(self, on_subsequent_trigger):
        """Sets the on_subsequent_trigger of this RuleActions.

        The list of actions to perform on the subsequent triggers of the session.  # noqa: E501

        :param on_subsequent_trigger: The on_subsequent_trigger of this RuleActions.  # noqa: E501
        :type: list[Action]
        """

        self._on_subsequent_trigger = on_subsequent_trigger

    @property
    def on_every_trigger(self):
        """Gets the on_every_trigger of this RuleActions.  # noqa: E501

        The list of actions to perform on every trigger of the session.  # noqa: E501

        :return: The on_every_trigger of this RuleActions.  # noqa: E501
        :rtype: list[Action]
        """
        return self._on_every_trigger

    @on_every_trigger.setter
    def on_every_trigger(self, on_every_trigger):
        """Sets the on_every_trigger of this RuleActions.

        The list of actions to perform on every trigger of the session.  # noqa: E501

        :param on_every_trigger: The on_every_trigger of this RuleActions.  # noqa: E501
        :type: list[Action]
        """

        self._on_every_trigger = on_every_trigger

    @property
    def on_time_interval(self):
        """Gets the on_time_interval of this RuleActions.  # noqa: E501


        :return: The on_time_interval of this RuleActions.  # noqa: E501
        :rtype: OnTimeIntervalActions
        """
        return self._on_time_interval

    @on_time_interval.setter
    def on_time_interval(self, on_time_interval):
        """Sets the on_time_interval of this RuleActions.


        :param on_time_interval: The on_time_interval of this RuleActions.  # noqa: E501
        :type: OnTimeIntervalActions
        """

        self._on_time_interval = on_time_interval

    @property
    def on_time_expiration(self):
        """Gets the on_time_expiration of this RuleActions.  # noqa: E501

        The list of actions to perform when the session has expired.  # noqa: E501

        :return: The on_time_expiration of this RuleActions.  # noqa: E501
        :rtype: list[Action]
        """
        return self._on_time_expiration

    @on_time_expiration.setter
    def on_time_expiration(self, on_time_expiration):
        """Sets the on_time_expiration of this RuleActions.

        The list of actions to perform when the session has expired.  # noqa: E501

        :param on_time_expiration: The on_time_expiration of this RuleActions.  # noqa: E501
        :type: list[Action]
        """

        self._on_time_expiration = on_time_expiration

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
        if issubclass(RuleActions, dict):
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
        if not isinstance(other, RuleActions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
