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


class IngestBudgetDefinition(object):
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
        'field_value': 'str',
        'capacity_bytes': 'int',
        'timezone': 'str',
        'reset_time': 'str',
        'description': 'str',
        'action': 'str',
        'audit_threshold': 'int'
    }

    attribute_map = {
        'name': 'name',
        'field_value': 'fieldValue',
        'capacity_bytes': 'capacityBytes',
        'timezone': 'timezone',
        'reset_time': 'resetTime',
        'description': 'description',
        'action': 'action',
        'audit_threshold': 'auditThreshold'
    }

    def __init__(self, name=None, field_value=None, capacity_bytes=None, timezone=None, reset_time=None, description=None, action=None, audit_threshold=None):  # noqa: E501
        """IngestBudgetDefinition - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._field_value = None
        self._capacity_bytes = None
        self._timezone = None
        self._reset_time = None
        self._description = None
        self._action = None
        self._audit_threshold = None
        self.discriminator = None
        self.name = name
        self.field_value = field_value
        self.capacity_bytes = capacity_bytes
        self.timezone = timezone
        self.reset_time = reset_time
        if description is not None:
            self.description = description
        self.action = action
        if audit_threshold is not None:
            self.audit_threshold = audit_threshold

    @property
    def name(self):
        """Gets the name of this IngestBudgetDefinition.  # noqa: E501

        Display name of the ingest budget.  # noqa: E501

        :return: The name of this IngestBudgetDefinition.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this IngestBudgetDefinition.

        Display name of the ingest budget.  # noqa: E501

        :param name: The name of this IngestBudgetDefinition.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def field_value(self):
        """Gets the field_value of this IngestBudgetDefinition.  # noqa: E501

        Custom field value that is used to assign Collectors to the ingest budget.  # noqa: E501

        :return: The field_value of this IngestBudgetDefinition.  # noqa: E501
        :rtype: str
        """
        return self._field_value

    @field_value.setter
    def field_value(self, field_value):
        """Sets the field_value of this IngestBudgetDefinition.

        Custom field value that is used to assign Collectors to the ingest budget.  # noqa: E501

        :param field_value: The field_value of this IngestBudgetDefinition.  # noqa: E501
        :type: str
        """
        if field_value is None:
            raise ValueError("Invalid value for `field_value`, must not be `None`")  # noqa: E501

        self._field_value = field_value

    @property
    def capacity_bytes(self):
        """Gets the capacity_bytes of this IngestBudgetDefinition.  # noqa: E501

        Capacity of the ingest budget, in bytes. It takes a few minutes for Collectors to stop collecting when capacity is reached. We recommend setting a soft limit that is lower than your needed hard limit.  # noqa: E501

        :return: The capacity_bytes of this IngestBudgetDefinition.  # noqa: E501
        :rtype: int
        """
        return self._capacity_bytes

    @capacity_bytes.setter
    def capacity_bytes(self, capacity_bytes):
        """Sets the capacity_bytes of this IngestBudgetDefinition.

        Capacity of the ingest budget, in bytes. It takes a few minutes for Collectors to stop collecting when capacity is reached. We recommend setting a soft limit that is lower than your needed hard limit.  # noqa: E501

        :param capacity_bytes: The capacity_bytes of this IngestBudgetDefinition.  # noqa: E501
        :type: int
        """
        if capacity_bytes is None:
            raise ValueError("Invalid value for `capacity_bytes`, must not be `None`")  # noqa: E501

        self._capacity_bytes = capacity_bytes

    @property
    def timezone(self):
        """Gets the timezone of this IngestBudgetDefinition.  # noqa: E501

        Time zone of the reset time for the ingest budget. Follow the format in the [IANA Time Zone Database](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones#List).  # noqa: E501

        :return: The timezone of this IngestBudgetDefinition.  # noqa: E501
        :rtype: str
        """
        return self._timezone

    @timezone.setter
    def timezone(self, timezone):
        """Sets the timezone of this IngestBudgetDefinition.

        Time zone of the reset time for the ingest budget. Follow the format in the [IANA Time Zone Database](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones#List).  # noqa: E501

        :param timezone: The timezone of this IngestBudgetDefinition.  # noqa: E501
        :type: str
        """
        if timezone is None:
            raise ValueError("Invalid value for `timezone`, must not be `None`")  # noqa: E501

        self._timezone = timezone

    @property
    def reset_time(self):
        """Gets the reset_time of this IngestBudgetDefinition.  # noqa: E501

        Reset time of the ingest budget in HH:MM format.  # noqa: E501

        :return: The reset_time of this IngestBudgetDefinition.  # noqa: E501
        :rtype: str
        """
        return self._reset_time

    @reset_time.setter
    def reset_time(self, reset_time):
        """Sets the reset_time of this IngestBudgetDefinition.

        Reset time of the ingest budget in HH:MM format.  # noqa: E501

        :param reset_time: The reset_time of this IngestBudgetDefinition.  # noqa: E501
        :type: str
        """
        if reset_time is None:
            raise ValueError("Invalid value for `reset_time`, must not be `None`")  # noqa: E501

        self._reset_time = reset_time

    @property
    def description(self):
        """Gets the description of this IngestBudgetDefinition.  # noqa: E501

        Description of the ingest budget.  # noqa: E501

        :return: The description of this IngestBudgetDefinition.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this IngestBudgetDefinition.

        Description of the ingest budget.  # noqa: E501

        :param description: The description of this IngestBudgetDefinition.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def action(self):
        """Gets the action of this IngestBudgetDefinition.  # noqa: E501

        Action to take when ingest budget's capacity is reached. All actions are audited. Supported values are:   * `stopCollecting`   * `keepCollecting`  # noqa: E501

        :return: The action of this IngestBudgetDefinition.  # noqa: E501
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """Sets the action of this IngestBudgetDefinition.

        Action to take when ingest budget's capacity is reached. All actions are audited. Supported values are:   * `stopCollecting`   * `keepCollecting`  # noqa: E501

        :param action: The action of this IngestBudgetDefinition.  # noqa: E501
        :type: str
        """
        if action is None:
            raise ValueError("Invalid value for `action`, must not be `None`")  # noqa: E501

        self._action = action

    @property
    def audit_threshold(self):
        """Gets the audit_threshold of this IngestBudgetDefinition.  # noqa: E501

        The threshold as a percentage of when an ingest budget's capacity usage is logged in the Audit Index.  # noqa: E501

        :return: The audit_threshold of this IngestBudgetDefinition.  # noqa: E501
        :rtype: int
        """
        return self._audit_threshold

    @audit_threshold.setter
    def audit_threshold(self, audit_threshold):
        """Sets the audit_threshold of this IngestBudgetDefinition.

        The threshold as a percentage of when an ingest budget's capacity usage is logged in the Audit Index.  # noqa: E501

        :param audit_threshold: The audit_threshold of this IngestBudgetDefinition.  # noqa: E501
        :type: int
        """

        self._audit_threshold = audit_threshold

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
        if issubclass(IngestBudgetDefinition, dict):
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
        if not isinstance(other, IngestBudgetDefinition):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
