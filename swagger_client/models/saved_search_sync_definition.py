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
from swagger_client.models.query_parameter_sync_definition import QueryParameterSyncDefinition  # noqa: F401,E501


class SavedSearchSyncDefinition(object):
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
        'query_text': 'str',
        'default_time_range': 'str',
        'by_receipt_time': 'bool',
        'view_name': 'str',
        'view_start_time': 'datetime',
        'query_parameters': 'list[QueryParameterSyncDefinition]'
    }

    attribute_map = {
        'query_text': 'queryText',
        'default_time_range': 'defaultTimeRange',
        'by_receipt_time': 'byReceiptTime',
        'view_name': 'viewName',
        'view_start_time': 'viewStartTime',
        'query_parameters': 'queryParameters'
    }

    def __init__(self, query_text=None, default_time_range=None, by_receipt_time=False, view_name=None, view_start_time=None, query_parameters=None):  # noqa: E501
        """SavedSearchSyncDefinition - a model defined in Swagger"""  # noqa: E501
        self._query_text = None
        self._default_time_range = None
        self._by_receipt_time = None
        self._view_name = None
        self._view_start_time = None
        self._query_parameters = None
        self.discriminator = None
        self.query_text = query_text
        self.default_time_range = default_time_range
        self.by_receipt_time = by_receipt_time
        if view_name is not None:
            self.view_name = view_name
        if view_start_time is not None:
            self.view_start_time = view_start_time
        self.query_parameters = query_parameters

    @property
    def query_text(self):
        """Gets the query_text of this SavedSearchSyncDefinition.  # noqa: E501

        The text of a Sumo Logic query.  # noqa: E501

        :return: The query_text of this SavedSearchSyncDefinition.  # noqa: E501
        :rtype: str
        """
        return self._query_text

    @query_text.setter
    def query_text(self, query_text):
        """Sets the query_text of this SavedSearchSyncDefinition.

        The text of a Sumo Logic query.  # noqa: E501

        :param query_text: The query_text of this SavedSearchSyncDefinition.  # noqa: E501
        :type: str
        """
        if query_text is None:
            raise ValueError("Invalid value for `query_text`, must not be `None`")  # noqa: E501

        self._query_text = query_text

    @property
    def default_time_range(self):
        """Gets the default_time_range of this SavedSearchSyncDefinition.  # noqa: E501

        Default time range for the search. Possible types of time ranges are:   - relative time range: e.g. \"-1d -12h\" represents a time range from one day ago to 12 hours ago.   - absolute time range: e.g. \"01-04-2017 20:32:00 to 01-04-2017 20:35:00\" represents a time range     from April 1st, 2017 at 8:32 PM until April 1st, 2017 at 8:35 PM.  # noqa: E501

        :return: The default_time_range of this SavedSearchSyncDefinition.  # noqa: E501
        :rtype: str
        """
        return self._default_time_range

    @default_time_range.setter
    def default_time_range(self, default_time_range):
        """Sets the default_time_range of this SavedSearchSyncDefinition.

        Default time range for the search. Possible types of time ranges are:   - relative time range: e.g. \"-1d -12h\" represents a time range from one day ago to 12 hours ago.   - absolute time range: e.g. \"01-04-2017 20:32:00 to 01-04-2017 20:35:00\" represents a time range     from April 1st, 2017 at 8:32 PM until April 1st, 2017 at 8:35 PM.  # noqa: E501

        :param default_time_range: The default_time_range of this SavedSearchSyncDefinition.  # noqa: E501
        :type: str
        """
        if default_time_range is None:
            raise ValueError("Invalid value for `default_time_range`, must not be `None`")  # noqa: E501

        self._default_time_range = default_time_range

    @property
    def by_receipt_time(self):
        """Gets the by_receipt_time of this SavedSearchSyncDefinition.  # noqa: E501

        Set it to true to run the search using receipt time. By default, searches do not run by receipt time.  # noqa: E501

        :return: The by_receipt_time of this SavedSearchSyncDefinition.  # noqa: E501
        :rtype: bool
        """
        return self._by_receipt_time

    @by_receipt_time.setter
    def by_receipt_time(self, by_receipt_time):
        """Sets the by_receipt_time of this SavedSearchSyncDefinition.

        Set it to true to run the search using receipt time. By default, searches do not run by receipt time.  # noqa: E501

        :param by_receipt_time: The by_receipt_time of this SavedSearchSyncDefinition.  # noqa: E501
        :type: bool
        """
        if by_receipt_time is None:
            raise ValueError("Invalid value for `by_receipt_time`, must not be `None`")  # noqa: E501

        self._by_receipt_time = by_receipt_time

    @property
    def view_name(self):
        """Gets the view_name of this SavedSearchSyncDefinition.  # noqa: E501

        The name of the Scheduled View that has indexed the data you want to search.  # noqa: E501

        :return: The view_name of this SavedSearchSyncDefinition.  # noqa: E501
        :rtype: str
        """
        return self._view_name

    @view_name.setter
    def view_name(self, view_name):
        """Sets the view_name of this SavedSearchSyncDefinition.

        The name of the Scheduled View that has indexed the data you want to search.  # noqa: E501

        :param view_name: The view_name of this SavedSearchSyncDefinition.  # noqa: E501
        :type: str
        """

        self._view_name = view_name

    @property
    def view_start_time(self):
        """Gets the view_start_time of this SavedSearchSyncDefinition.  # noqa: E501

        Start timestamp of the Scheduled View in UTC format.  # noqa: E501

        :return: The view_start_time of this SavedSearchSyncDefinition.  # noqa: E501
        :rtype: datetime
        """
        return self._view_start_time

    @view_start_time.setter
    def view_start_time(self, view_start_time):
        """Sets the view_start_time of this SavedSearchSyncDefinition.

        Start timestamp of the Scheduled View in UTC format.  # noqa: E501

        :param view_start_time: The view_start_time of this SavedSearchSyncDefinition.  # noqa: E501
        :type: datetime
        """

        self._view_start_time = view_start_time

    @property
    def query_parameters(self):
        """Gets the query_parameters of this SavedSearchSyncDefinition.  # noqa: E501

        An array of search query parameter objects.  # noqa: E501

        :return: The query_parameters of this SavedSearchSyncDefinition.  # noqa: E501
        :rtype: list[QueryParameterSyncDefinition]
        """
        return self._query_parameters

    @query_parameters.setter
    def query_parameters(self, query_parameters):
        """Sets the query_parameters of this SavedSearchSyncDefinition.

        An array of search query parameter objects.  # noqa: E501

        :param query_parameters: The query_parameters of this SavedSearchSyncDefinition.  # noqa: E501
        :type: list[QueryParameterSyncDefinition]
        """
        if query_parameters is None:
            raise ValueError("Invalid value for `query_parameters`, must not be `None`")  # noqa: E501

        self._query_parameters = query_parameters

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
        if issubclass(SavedSearchSyncDefinition, dict):
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
        if not isinstance(other, SavedSearchSyncDefinition):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
