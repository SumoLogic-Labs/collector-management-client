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
from swagger_client.models.create_user_definition import CreateUserDefinition  # noqa: F401,E501
from swagger_client.models.metadata_model import MetadataModel  # noqa: F401,E501


class UserModel(CreateUserDefinition):
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
        'created_at': 'datetime',
        'created_by': 'str',
        'modified_at': 'datetime',
        'modified_by': 'str',
        'id': 'str',
        'is_active': 'bool',
        'is_locked': 'bool',
        'is_mfa_enabled': 'bool',
        'last_login_timestamp': 'datetime'
    }
    if hasattr(CreateUserDefinition, "swagger_types"):
        swagger_types.update(CreateUserDefinition.swagger_types)

    attribute_map = {
        'created_at': 'createdAt',
        'created_by': 'createdBy',
        'modified_at': 'modifiedAt',
        'modified_by': 'modifiedBy',
        'id': 'id',
        'is_active': 'isActive',
        'is_locked': 'isLocked',
        'is_mfa_enabled': 'isMfaEnabled',
        'last_login_timestamp': 'lastLoginTimestamp'
    }
    if hasattr(CreateUserDefinition, "attribute_map"):
        attribute_map.update(CreateUserDefinition.attribute_map)

    def __init__(self, created_at=None, created_by=None, modified_at=None, modified_by=None, id=None, is_active=None, is_locked=None, is_mfa_enabled=None, last_login_timestamp=None, *args, **kwargs):  # noqa: E501
        """UserModel - a model defined in Swagger"""  # noqa: E501
        self._created_at = None
        self._created_by = None
        self._modified_at = None
        self._modified_by = None
        self._id = None
        self._is_active = None
        self._is_locked = None
        self._is_mfa_enabled = None
        self._last_login_timestamp = None
        self.discriminator = None
        self.created_at = created_at
        self.created_by = created_by
        self.modified_at = modified_at
        self.modified_by = modified_by
        self.id = id
        if is_active is not None:
            self.is_active = is_active
        if is_locked is not None:
            self.is_locked = is_locked
        if is_mfa_enabled is not None:
            self.is_mfa_enabled = is_mfa_enabled
        if last_login_timestamp is not None:
            self.last_login_timestamp = last_login_timestamp
        CreateUserDefinition.__init__(self, *args, **kwargs)

    @property
    def created_at(self):
        """Gets the created_at of this UserModel.  # noqa: E501

        Creation timestamp in UTC in [RFC3339](https://tools.ietf.org/html/rfc3339) format.  # noqa: E501

        :return: The created_at of this UserModel.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this UserModel.

        Creation timestamp in UTC in [RFC3339](https://tools.ietf.org/html/rfc3339) format.  # noqa: E501

        :param created_at: The created_at of this UserModel.  # noqa: E501
        :type: datetime
        """
        if created_at is None:
            raise ValueError("Invalid value for `created_at`, must not be `None`")  # noqa: E501

        self._created_at = created_at

    @property
    def created_by(self):
        """Gets the created_by of this UserModel.  # noqa: E501

        Identifier of the user who created the resource.  # noqa: E501

        :return: The created_by of this UserModel.  # noqa: E501
        :rtype: str
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this UserModel.

        Identifier of the user who created the resource.  # noqa: E501

        :param created_by: The created_by of this UserModel.  # noqa: E501
        :type: str
        """
        if created_by is None:
            raise ValueError("Invalid value for `created_by`, must not be `None`")  # noqa: E501

        self._created_by = created_by

    @property
    def modified_at(self):
        """Gets the modified_at of this UserModel.  # noqa: E501

        Last modification timestamp in UTC.  # noqa: E501

        :return: The modified_at of this UserModel.  # noqa: E501
        :rtype: datetime
        """
        return self._modified_at

    @modified_at.setter
    def modified_at(self, modified_at):
        """Sets the modified_at of this UserModel.

        Last modification timestamp in UTC.  # noqa: E501

        :param modified_at: The modified_at of this UserModel.  # noqa: E501
        :type: datetime
        """
        if modified_at is None:
            raise ValueError("Invalid value for `modified_at`, must not be `None`")  # noqa: E501

        self._modified_at = modified_at

    @property
    def modified_by(self):
        """Gets the modified_by of this UserModel.  # noqa: E501

        Identifier of the user who last modified the resource.  # noqa: E501

        :return: The modified_by of this UserModel.  # noqa: E501
        :rtype: str
        """
        return self._modified_by

    @modified_by.setter
    def modified_by(self, modified_by):
        """Sets the modified_by of this UserModel.

        Identifier of the user who last modified the resource.  # noqa: E501

        :param modified_by: The modified_by of this UserModel.  # noqa: E501
        :type: str
        """
        if modified_by is None:
            raise ValueError("Invalid value for `modified_by`, must not be `None`")  # noqa: E501

        self._modified_by = modified_by

    @property
    def id(self):
        """Gets the id of this UserModel.  # noqa: E501

        Unique identifier for the user.  # noqa: E501

        :return: The id of this UserModel.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this UserModel.

        Unique identifier for the user.  # noqa: E501

        :param id: The id of this UserModel.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def is_active(self):
        """Gets the is_active of this UserModel.  # noqa: E501

        True if the user is active.  # noqa: E501

        :return: The is_active of this UserModel.  # noqa: E501
        :rtype: bool
        """
        return self._is_active

    @is_active.setter
    def is_active(self, is_active):
        """Sets the is_active of this UserModel.

        True if the user is active.  # noqa: E501

        :param is_active: The is_active of this UserModel.  # noqa: E501
        :type: bool
        """

        self._is_active = is_active

    @property
    def is_locked(self):
        """Gets the is_locked of this UserModel.  # noqa: E501

        This has the value `true` if the user's account has been locked. If a user tries to log into their account several times and fails, his or her account will be locked for security reasons.  # noqa: E501

        :return: The is_locked of this UserModel.  # noqa: E501
        :rtype: bool
        """
        return self._is_locked

    @is_locked.setter
    def is_locked(self, is_locked):
        """Sets the is_locked of this UserModel.

        This has the value `true` if the user's account has been locked. If a user tries to log into their account several times and fails, his or her account will be locked for security reasons.  # noqa: E501

        :param is_locked: The is_locked of this UserModel.  # noqa: E501
        :type: bool
        """

        self._is_locked = is_locked

    @property
    def is_mfa_enabled(self):
        """Gets the is_mfa_enabled of this UserModel.  # noqa: E501

        True if multi factor authentication is enabled for the user.  # noqa: E501

        :return: The is_mfa_enabled of this UserModel.  # noqa: E501
        :rtype: bool
        """
        return self._is_mfa_enabled

    @is_mfa_enabled.setter
    def is_mfa_enabled(self, is_mfa_enabled):
        """Sets the is_mfa_enabled of this UserModel.

        True if multi factor authentication is enabled for the user.  # noqa: E501

        :param is_mfa_enabled: The is_mfa_enabled of this UserModel.  # noqa: E501
        :type: bool
        """

        self._is_mfa_enabled = is_mfa_enabled

    @property
    def last_login_timestamp(self):
        """Gets the last_login_timestamp of this UserModel.  # noqa: E501

        Timestamp of the last login for the user in UTC. Will be null if the user has never logged in.  # noqa: E501

        :return: The last_login_timestamp of this UserModel.  # noqa: E501
        :rtype: datetime
        """
        return self._last_login_timestamp

    @last_login_timestamp.setter
    def last_login_timestamp(self, last_login_timestamp):
        """Sets the last_login_timestamp of this UserModel.

        Timestamp of the last login for the user in UTC. Will be null if the user has never logged in.  # noqa: E501

        :param last_login_timestamp: The last_login_timestamp of this UserModel.  # noqa: E501
        :type: datetime
        """

        self._last_login_timestamp = last_login_timestamp

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
        if issubclass(UserModel, dict):
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
        if not isinstance(other, UserModel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
