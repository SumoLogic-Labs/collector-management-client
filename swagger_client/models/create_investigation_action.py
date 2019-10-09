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
from swagger_client.models.field_value_tuple import FieldValueTuple  # noqa: F401,E501


class CreateInvestigationAction(Action):
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
        'assignee_user_id': 'str',
        'description': 'str',
        'investigation_type': 'str',
        'status': 'str',
        'severity': 'str',
        'priority': 'str',
        'base_properties': 'list[FieldValueTuple]'
    }
    if hasattr(Action, "swagger_types"):
        swagger_types.update(Action.swagger_types)

    attribute_map = {
        'assignee_user_id': 'assigneeUserId',
        'description': 'description',
        'investigation_type': 'investigationType',
        'status': 'status',
        'severity': 'severity',
        'priority': 'priority',
        'base_properties': 'baseProperties'
    }
    if hasattr(Action, "attribute_map"):
        attribute_map.update(Action.attribute_map)

    def __init__(self, assignee_user_id=None, description=None, investigation_type=None, status=None, severity=None, priority=None, base_properties=None, *args, **kwargs):  # noqa: E501
        """CreateInvestigationAction - a model defined in Swagger"""  # noqa: E501
        self._assignee_user_id = None
        self._description = None
        self._investigation_type = None
        self._status = None
        self._severity = None
        self._priority = None
        self._base_properties = None
        self.discriminator = None
        if assignee_user_id is not None:
            self.assignee_user_id = assignee_user_id
        if description is not None:
            self.description = description
        if investigation_type is not None:
            self.investigation_type = investigation_type
        if status is not None:
            self.status = status
        if severity is not None:
            self.severity = severity
        if priority is not None:
            self.priority = priority
        if base_properties is not None:
            self.base_properties = base_properties
        Action.__init__(self, *args, **kwargs)

    @property
    def assignee_user_id(self):
        """Gets the assignee_user_id of this CreateInvestigationAction.  # noqa: E501

        The identifier of the user the investigation will be assigned to.  # noqa: E501

        :return: The assignee_user_id of this CreateInvestigationAction.  # noqa: E501
        :rtype: str
        """
        return self._assignee_user_id

    @assignee_user_id.setter
    def assignee_user_id(self, assignee_user_id):
        """Sets the assignee_user_id of this CreateInvestigationAction.

        The identifier of the user the investigation will be assigned to.  # noqa: E501

        :param assignee_user_id: The assignee_user_id of this CreateInvestigationAction.  # noqa: E501
        :type: str
        """

        self._assignee_user_id = assignee_user_id

    @property
    def description(self):
        """Gets the description of this CreateInvestigationAction.  # noqa: E501

        The description of the investigation.  # noqa: E501

        :return: The description of this CreateInvestigationAction.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CreateInvestigationAction.

        The description of the investigation.  # noqa: E501

        :param description: The description of this CreateInvestigationAction.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def investigation_type(self):
        """Gets the investigation_type of this CreateInvestigationAction.  # noqa: E501

        The type of investigation.  # noqa: E501

        :return: The investigation_type of this CreateInvestigationAction.  # noqa: E501
        :rtype: str
        """
        return self._investigation_type

    @investigation_type.setter
    def investigation_type(self, investigation_type):
        """Sets the investigation_type of this CreateInvestigationAction.

        The type of investigation.  # noqa: E501

        :param investigation_type: The investigation_type of this CreateInvestigationAction.  # noqa: E501
        :type: str
        """

        self._investigation_type = investigation_type

    @property
    def status(self):
        """Gets the status of this CreateInvestigationAction.  # noqa: E501

        The status of the investigation.  # noqa: E501

        :return: The status of this CreateInvestigationAction.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this CreateInvestigationAction.

        The status of the investigation.  # noqa: E501

        :param status: The status of this CreateInvestigationAction.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def severity(self):
        """Gets the severity of this CreateInvestigationAction.  # noqa: E501

        The severity of the investigation.  # noqa: E501

        :return: The severity of this CreateInvestigationAction.  # noqa: E501
        :rtype: str
        """
        return self._severity

    @severity.setter
    def severity(self, severity):
        """Sets the severity of this CreateInvestigationAction.

        The severity of the investigation.  # noqa: E501

        :param severity: The severity of this CreateInvestigationAction.  # noqa: E501
        :type: str
        """

        self._severity = severity

    @property
    def priority(self):
        """Gets the priority of this CreateInvestigationAction.  # noqa: E501

        The priority of the investigation.  # noqa: E501

        :return: The priority of this CreateInvestigationAction.  # noqa: E501
        :rtype: str
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        """Sets the priority of this CreateInvestigationAction.

        The priority of the investigation.  # noqa: E501

        :param priority: The priority of this CreateInvestigationAction.  # noqa: E501
        :type: str
        """

        self._priority = priority

    @property
    def base_properties(self):
        """Gets the base_properties of this CreateInvestigationAction.  # noqa: E501

        Initial properties for the investigation. An array of field names, field values, and field type tuples, where the field name is the name the field should get in the investigation, the field value is an expression that will extract a value from the events that caused the rule to fire, and the type is a link type (e.g. IP Address, USER, URL, etc).  # noqa: E501

        :return: The base_properties of this CreateInvestigationAction.  # noqa: E501
        :rtype: list[FieldValueTuple]
        """
        return self._base_properties

    @base_properties.setter
    def base_properties(self, base_properties):
        """Sets the base_properties of this CreateInvestigationAction.

        Initial properties for the investigation. An array of field names, field values, and field type tuples, where the field name is the name the field should get in the investigation, the field value is an expression that will extract a value from the events that caused the rule to fire, and the type is a link type (e.g. IP Address, USER, URL, etc).  # noqa: E501

        :param base_properties: The base_properties of this CreateInvestigationAction.  # noqa: E501
        :type: list[FieldValueTuple]
        """

        self._base_properties = base_properties

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
        if issubclass(CreateInvestigationAction, dict):
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
        if not isinstance(other, CreateInvestigationAction):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
