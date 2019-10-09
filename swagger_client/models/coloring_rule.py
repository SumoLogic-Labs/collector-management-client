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
from swagger_client.models.coloring_threshold import ColoringThreshold  # noqa: F401,E501


class ColoringRule(object):
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
        'scope': 'str',
        'single_series_aggregate_function': 'str',
        'multiple_series_aggregate_function': 'str',
        'color_thresholds': 'list[ColoringThreshold]'
    }

    attribute_map = {
        'scope': 'scope',
        'single_series_aggregate_function': 'singleSeriesAggregateFunction',
        'multiple_series_aggregate_function': 'multipleSeriesAggregateFunction',
        'color_thresholds': 'colorThresholds'
    }

    def __init__(self, scope=None, single_series_aggregate_function=None, multiple_series_aggregate_function=None, color_thresholds=None):  # noqa: E501
        """ColoringRule - a model defined in Swagger"""  # noqa: E501
        self._scope = None
        self._single_series_aggregate_function = None
        self._multiple_series_aggregate_function = None
        self._color_thresholds = None
        self.discriminator = None
        self.scope = scope
        self.single_series_aggregate_function = single_series_aggregate_function
        self.multiple_series_aggregate_function = multiple_series_aggregate_function
        if color_thresholds is not None:
            self.color_thresholds = color_thresholds

    @property
    def scope(self):
        """Gets the scope of this ColoringRule.  # noqa: E501

        Regex string to match queries to apply coloring to.  # noqa: E501

        :return: The scope of this ColoringRule.  # noqa: E501
        :rtype: str
        """
        return self._scope

    @scope.setter
    def scope(self, scope):
        """Sets the scope of this ColoringRule.

        Regex string to match queries to apply coloring to.  # noqa: E501

        :param scope: The scope of this ColoringRule.  # noqa: E501
        :type: str
        """
        if scope is None:
            raise ValueError("Invalid value for `scope`, must not be `None`")  # noqa: E501

        self._scope = scope

    @property
    def single_series_aggregate_function(self):
        """Gets the single_series_aggregate_function of this ColoringRule.  # noqa: E501

        Function to aggregate one series into one single value.  # noqa: E501

        :return: The single_series_aggregate_function of this ColoringRule.  # noqa: E501
        :rtype: str
        """
        return self._single_series_aggregate_function

    @single_series_aggregate_function.setter
    def single_series_aggregate_function(self, single_series_aggregate_function):
        """Sets the single_series_aggregate_function of this ColoringRule.

        Function to aggregate one series into one single value.  # noqa: E501

        :param single_series_aggregate_function: The single_series_aggregate_function of this ColoringRule.  # noqa: E501
        :type: str
        """
        if single_series_aggregate_function is None:
            raise ValueError("Invalid value for `single_series_aggregate_function`, must not be `None`")  # noqa: E501

        self._single_series_aggregate_function = single_series_aggregate_function

    @property
    def multiple_series_aggregate_function(self):
        """Gets the multiple_series_aggregate_function of this ColoringRule.  # noqa: E501

        Function to aggregate the aggregate values of multiple time series into one single value.  # noqa: E501

        :return: The multiple_series_aggregate_function of this ColoringRule.  # noqa: E501
        :rtype: str
        """
        return self._multiple_series_aggregate_function

    @multiple_series_aggregate_function.setter
    def multiple_series_aggregate_function(self, multiple_series_aggregate_function):
        """Sets the multiple_series_aggregate_function of this ColoringRule.

        Function to aggregate the aggregate values of multiple time series into one single value.  # noqa: E501

        :param multiple_series_aggregate_function: The multiple_series_aggregate_function of this ColoringRule.  # noqa: E501
        :type: str
        """
        if multiple_series_aggregate_function is None:
            raise ValueError("Invalid value for `multiple_series_aggregate_function`, must not be `None`")  # noqa: E501

        self._multiple_series_aggregate_function = multiple_series_aggregate_function

    @property
    def color_thresholds(self):
        """Gets the color_thresholds of this ColoringRule.  # noqa: E501

        Thresholds and colors to color with.  # noqa: E501

        :return: The color_thresholds of this ColoringRule.  # noqa: E501
        :rtype: list[ColoringThreshold]
        """
        return self._color_thresholds

    @color_thresholds.setter
    def color_thresholds(self, color_thresholds):
        """Sets the color_thresholds of this ColoringRule.

        Thresholds and colors to color with.  # noqa: E501

        :param color_thresholds: The color_thresholds of this ColoringRule.  # noqa: E501
        :type: list[ColoringThreshold]
        """

        self._color_thresholds = color_thresholds

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
        if issubclass(ColoringRule, dict):
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
        if not isinstance(other, ColoringRule):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
