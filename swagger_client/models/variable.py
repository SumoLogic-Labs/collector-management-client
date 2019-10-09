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
from swagger_client.models.variable_source_definition import VariableSourceDefinition  # noqa: F401,E501


class Variable(object):
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
        'id': 'str',
        'name': 'str',
        'display_name': 'str',
        'default_value': 'str',
        'source_definition': 'VariableSourceDefinition',
        'allow_multi_select': 'bool',
        'include_all_option': 'bool',
        'hide_from_ui': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'display_name': 'displayName',
        'default_value': 'defaultValue',
        'source_definition': 'sourceDefinition',
        'allow_multi_select': 'allowMultiSelect',
        'include_all_option': 'includeAllOption',
        'hide_from_ui': 'hideFromUI'
    }

    def __init__(self, id=None, name=None, display_name=None, default_value=None, source_definition=None, allow_multi_select=None, include_all_option=None, hide_from_ui=None):  # noqa: E501
        """Variable - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._name = None
        self._display_name = None
        self._default_value = None
        self._source_definition = None
        self._allow_multi_select = None
        self._include_all_option = None
        self._hide_from_ui = None
        self.discriminator = None
        if id is not None:
            self.id = id
        self.name = name
        if display_name is not None:
            self.display_name = display_name
        if default_value is not None:
            self.default_value = default_value
        self.source_definition = source_definition
        self.allow_multi_select = allow_multi_select
        self.include_all_option = include_all_option
        self.hide_from_ui = hide_from_ui

    @property
    def id(self):
        """Gets the id of this Variable.  # noqa: E501

        Unique identifier for the variable.  # noqa: E501

        :return: The id of this Variable.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Variable.

        Unique identifier for the variable.  # noqa: E501

        :param id: The id of this Variable.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this Variable.  # noqa: E501

        Name of the variable. The variable name is case-insensitive. Only numbers, spaces, and underscores are allowed in the variable name.   # noqa: E501

        :return: The name of this Variable.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Variable.

        Name of the variable. The variable name is case-insensitive. Only numbers, spaces, and underscores are allowed in the variable name.   # noqa: E501

        :param name: The name of this Variable.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def display_name(self):
        """Gets the display_name of this Variable.  # noqa: E501

        Display name of the variable shown in the UI. If this field is empty, the name field will be used. The display name is case-insensitive. Only numbers, spaces, and underscores are allowed in the variable name.   # noqa: E501

        :return: The display_name of this Variable.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this Variable.

        Display name of the variable shown in the UI. If this field is empty, the name field will be used. The display name is case-insensitive. Only numbers, spaces, and underscores are allowed in the variable name.   # noqa: E501

        :param display_name: The display_name of this Variable.  # noqa: E501
        :type: str
        """

        self._display_name = display_name

    @property
    def default_value(self):
        """Gets the default_value of this Variable.  # noqa: E501

        Default value of the variable.  # noqa: E501

        :return: The default_value of this Variable.  # noqa: E501
        :rtype: str
        """
        return self._default_value

    @default_value.setter
    def default_value(self, default_value):
        """Sets the default_value of this Variable.

        Default value of the variable.  # noqa: E501

        :param default_value: The default_value of this Variable.  # noqa: E501
        :type: str
        """

        self._default_value = default_value

    @property
    def source_definition(self):
        """Gets the source_definition of this Variable.  # noqa: E501


        :return: The source_definition of this Variable.  # noqa: E501
        :rtype: VariableSourceDefinition
        """
        return self._source_definition

    @source_definition.setter
    def source_definition(self, source_definition):
        """Sets the source_definition of this Variable.


        :param source_definition: The source_definition of this Variable.  # noqa: E501
        :type: VariableSourceDefinition
        """
        if source_definition is None:
            raise ValueError("Invalid value for `source_definition`, must not be `None`")  # noqa: E501

        self._source_definition = source_definition

    @property
    def allow_multi_select(self):
        """Gets the allow_multi_select of this Variable.  # noqa: E501

        Allow multiple selections in the values dropdown.  # noqa: E501

        :return: The allow_multi_select of this Variable.  # noqa: E501
        :rtype: bool
        """
        return self._allow_multi_select

    @allow_multi_select.setter
    def allow_multi_select(self, allow_multi_select):
        """Sets the allow_multi_select of this Variable.

        Allow multiple selections in the values dropdown.  # noqa: E501

        :param allow_multi_select: The allow_multi_select of this Variable.  # noqa: E501
        :type: bool
        """
        if allow_multi_select is None:
            raise ValueError("Invalid value for `allow_multi_select`, must not be `None`")  # noqa: E501

        self._allow_multi_select = allow_multi_select

    @property
    def include_all_option(self):
        """Gets the include_all_option of this Variable.  # noqa: E501

        Include an \"All\" option at the top of the variable's values dropdown.  # noqa: E501

        :return: The include_all_option of this Variable.  # noqa: E501
        :rtype: bool
        """
        return self._include_all_option

    @include_all_option.setter
    def include_all_option(self, include_all_option):
        """Sets the include_all_option of this Variable.

        Include an \"All\" option at the top of the variable's values dropdown.  # noqa: E501

        :param include_all_option: The include_all_option of this Variable.  # noqa: E501
        :type: bool
        """
        if include_all_option is None:
            raise ValueError("Invalid value for `include_all_option`, must not be `None`")  # noqa: E501

        self._include_all_option = include_all_option

    @property
    def hide_from_ui(self):
        """Gets the hide_from_ui of this Variable.  # noqa: E501

        Hide the variable in the dashboard UI.  # noqa: E501

        :return: The hide_from_ui of this Variable.  # noqa: E501
        :rtype: bool
        """
        return self._hide_from_ui

    @hide_from_ui.setter
    def hide_from_ui(self, hide_from_ui):
        """Sets the hide_from_ui of this Variable.

        Hide the variable in the dashboard UI.  # noqa: E501

        :param hide_from_ui: The hide_from_ui of this Variable.  # noqa: E501
        :type: bool
        """
        if hide_from_ui is None:
            raise ValueError("Invalid value for `hide_from_ui`, must not be `None`")  # noqa: E501

        self._hide_from_ui = hide_from_ui

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
        if issubclass(Variable, dict):
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
        if not isinstance(other, Variable):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
