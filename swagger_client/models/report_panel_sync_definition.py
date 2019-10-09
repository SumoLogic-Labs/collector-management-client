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
from swagger_client.models.metrics_query_sync_definition import MetricsQuerySyncDefinition  # noqa: F401,E501
from swagger_client.models.query_parameter_sync_definition import QueryParameterSyncDefinition  # noqa: F401,E501
from swagger_client.models.resolvable_time_range import ResolvableTimeRange  # noqa: F401,E501


class ReportPanelSyncDefinition(object):
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
        'viewer_type': 'str',
        'detail_level': 'int',
        'query_string': 'str',
        'metrics_queries': 'list[MetricsQuerySyncDefinition]',
        'time_range': 'ResolvableTimeRange',
        'x': 'int',
        'y': 'int',
        'width': 'int',
        'height': 'int',
        'properties': 'str',
        'id': 'str',
        'desired_quantization_in_secs': 'int',
        'query_parameters': 'list[QueryParameterSyncDefinition]'
    }

    attribute_map = {
        'name': 'name',
        'viewer_type': 'viewerType',
        'detail_level': 'detailLevel',
        'query_string': 'queryString',
        'metrics_queries': 'metricsQueries',
        'time_range': 'timeRange',
        'x': 'x',
        'y': 'y',
        'width': 'width',
        'height': 'height',
        'properties': 'properties',
        'id': 'id',
        'desired_quantization_in_secs': 'desiredQuantizationInSecs',
        'query_parameters': 'queryParameters'
    }

    def __init__(self, name=None, viewer_type=None, detail_level=None, query_string=None, metrics_queries=None, time_range=None, x=None, y=None, width=None, height=None, properties=None, id=None, desired_quantization_in_secs=None, query_parameters=None):  # noqa: E501
        """ReportPanelSyncDefinition - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._viewer_type = None
        self._detail_level = None
        self._query_string = None
        self._metrics_queries = None
        self._time_range = None
        self._x = None
        self._y = None
        self._width = None
        self._height = None
        self._properties = None
        self._id = None
        self._desired_quantization_in_secs = None
        self._query_parameters = None
        self.discriminator = None
        self.name = name
        self.viewer_type = viewer_type
        self.detail_level = detail_level
        self.query_string = query_string
        self.metrics_queries = metrics_queries
        self.time_range = time_range
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.properties = properties
        self.id = id
        if desired_quantization_in_secs is not None:
            self.desired_quantization_in_secs = desired_quantization_in_secs
        self.query_parameters = query_parameters

    @property
    def name(self):
        """Gets the name of this ReportPanelSyncDefinition.  # noqa: E501

        The title of the panel.  # noqa: E501

        :return: The name of this ReportPanelSyncDefinition.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ReportPanelSyncDefinition.

        The title of the panel.  # noqa: E501

        :param name: The name of this ReportPanelSyncDefinition.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def viewer_type(self):
        """Gets the viewer_type of this ReportPanelSyncDefinition.  # noqa: E501

        Type of [area chart](https://help.sumologic.com/Dashboards-and-Alerts/Dashboards/Chart-Panel-Types). Supported values are:   1. `table` for Table   2. `bar` for Bar Chart   3. `column` for Column Chart   4. `line` for Line Chart   5. `area` for Area Chart   6. `pie` for Pie Chart   7. `svv` for Single Value Viewer   8. `title` for Title Panel   9. `text` for Text Panel  Values 1-7 are used for Data Panels.  # noqa: E501

        :return: The viewer_type of this ReportPanelSyncDefinition.  # noqa: E501
        :rtype: str
        """
        return self._viewer_type

    @viewer_type.setter
    def viewer_type(self, viewer_type):
        """Sets the viewer_type of this ReportPanelSyncDefinition.

        Type of [area chart](https://help.sumologic.com/Dashboards-and-Alerts/Dashboards/Chart-Panel-Types). Supported values are:   1. `table` for Table   2. `bar` for Bar Chart   3. `column` for Column Chart   4. `line` for Line Chart   5. `area` for Area Chart   6. `pie` for Pie Chart   7. `svv` for Single Value Viewer   8. `title` for Title Panel   9. `text` for Text Panel  Values 1-7 are used for Data Panels.  # noqa: E501

        :param viewer_type: The viewer_type of this ReportPanelSyncDefinition.  # noqa: E501
        :type: str
        """
        if viewer_type is None:
            raise ValueError("Invalid value for `viewer_type`, must not be `None`")  # noqa: E501

        self._viewer_type = viewer_type

    @property
    def detail_level(self):
        """Gets the detail_level of this ReportPanelSyncDefinition.  # noqa: E501

        Supported values are:   - `1` for small   - `2` for medium   - `3` for large  # noqa: E501

        :return: The detail_level of this ReportPanelSyncDefinition.  # noqa: E501
        :rtype: int
        """
        return self._detail_level

    @detail_level.setter
    def detail_level(self, detail_level):
        """Sets the detail_level of this ReportPanelSyncDefinition.

        Supported values are:   - `1` for small   - `2` for medium   - `3` for large  # noqa: E501

        :param detail_level: The detail_level of this ReportPanelSyncDefinition.  # noqa: E501
        :type: int
        """
        if detail_level is None:
            raise ValueError("Invalid value for `detail_level`, must not be `None`")  # noqa: E501

        self._detail_level = detail_level

    @property
    def query_string(self):
        """Gets the query_string of this ReportPanelSyncDefinition.  # noqa: E501

        The query to run, for panels associated to log searches.  # noqa: E501

        :return: The query_string of this ReportPanelSyncDefinition.  # noqa: E501
        :rtype: str
        """
        return self._query_string

    @query_string.setter
    def query_string(self, query_string):
        """Sets the query_string of this ReportPanelSyncDefinition.

        The query to run, for panels associated to log searches.  # noqa: E501

        :param query_string: The query_string of this ReportPanelSyncDefinition.  # noqa: E501
        :type: str
        """
        if query_string is None:
            raise ValueError("Invalid value for `query_string`, must not be `None`")  # noqa: E501

        self._query_string = query_string

    @property
    def metrics_queries(self):
        """Gets the metrics_queries of this ReportPanelSyncDefinition.  # noqa: E501

        The query or queries to run, for panels associated to metrics searches.  # noqa: E501

        :return: The metrics_queries of this ReportPanelSyncDefinition.  # noqa: E501
        :rtype: list[MetricsQuerySyncDefinition]
        """
        return self._metrics_queries

    @metrics_queries.setter
    def metrics_queries(self, metrics_queries):
        """Sets the metrics_queries of this ReportPanelSyncDefinition.

        The query or queries to run, for panels associated to metrics searches.  # noqa: E501

        :param metrics_queries: The metrics_queries of this ReportPanelSyncDefinition.  # noqa: E501
        :type: list[MetricsQuerySyncDefinition]
        """
        if metrics_queries is None:
            raise ValueError("Invalid value for `metrics_queries`, must not be `None`")  # noqa: E501

        self._metrics_queries = metrics_queries

    @property
    def time_range(self):
        """Gets the time_range of this ReportPanelSyncDefinition.  # noqa: E501


        :return: The time_range of this ReportPanelSyncDefinition.  # noqa: E501
        :rtype: ResolvableTimeRange
        """
        return self._time_range

    @time_range.setter
    def time_range(self, time_range):
        """Sets the time_range of this ReportPanelSyncDefinition.


        :param time_range: The time_range of this ReportPanelSyncDefinition.  # noqa: E501
        :type: ResolvableTimeRange
        """
        if time_range is None:
            raise ValueError("Invalid value for `time_range`, must not be `None`")  # noqa: E501

        self._time_range = time_range

    @property
    def x(self):
        """Gets the x of this ReportPanelSyncDefinition.  # noqa: E501

        The horizontal position of the panel. A sumo screen is divided into 24 columns. The value for x can be any integer from 0 to 24.  # noqa: E501

        :return: The x of this ReportPanelSyncDefinition.  # noqa: E501
        :rtype: int
        """
        return self._x

    @x.setter
    def x(self, x):
        """Sets the x of this ReportPanelSyncDefinition.

        The horizontal position of the panel. A sumo screen is divided into 24 columns. The value for x can be any integer from 0 to 24.  # noqa: E501

        :param x: The x of this ReportPanelSyncDefinition.  # noqa: E501
        :type: int
        """
        if x is None:
            raise ValueError("Invalid value for `x`, must not be `None`")  # noqa: E501

        self._x = x

    @property
    def y(self):
        """Gets the y of this ReportPanelSyncDefinition.  # noqa: E501

        The vertical position of the panel. A sumo screen is divided into 24 rows. The value for y can be any integer from 0 to 24.  # noqa: E501

        :return: The y of this ReportPanelSyncDefinition.  # noqa: E501
        :rtype: int
        """
        return self._y

    @y.setter
    def y(self, y):
        """Sets the y of this ReportPanelSyncDefinition.

        The vertical position of the panel. A sumo screen is divided into 24 rows. The value for y can be any integer from 0 to 24.  # noqa: E501

        :param y: The y of this ReportPanelSyncDefinition.  # noqa: E501
        :type: int
        """
        if y is None:
            raise ValueError("Invalid value for `y`, must not be `None`")  # noqa: E501

        self._y = y

    @property
    def width(self):
        """Gets the width of this ReportPanelSyncDefinition.  # noqa: E501

        The width of the panel.  # noqa: E501

        :return: The width of this ReportPanelSyncDefinition.  # noqa: E501
        :rtype: int
        """
        return self._width

    @width.setter
    def width(self, width):
        """Sets the width of this ReportPanelSyncDefinition.

        The width of the panel.  # noqa: E501

        :param width: The width of this ReportPanelSyncDefinition.  # noqa: E501
        :type: int
        """
        if width is None:
            raise ValueError("Invalid value for `width`, must not be `None`")  # noqa: E501

        self._width = width

    @property
    def height(self):
        """Gets the height of this ReportPanelSyncDefinition.  # noqa: E501

        The height of the panel.  # noqa: E501

        :return: The height of this ReportPanelSyncDefinition.  # noqa: E501
        :rtype: int
        """
        return self._height

    @height.setter
    def height(self, height):
        """Sets the height of this ReportPanelSyncDefinition.

        The height of the panel.  # noqa: E501

        :param height: The height of this ReportPanelSyncDefinition.  # noqa: E501
        :type: int
        """
        if height is None:
            raise ValueError("Invalid value for `height`, must not be `None`")  # noqa: E501

        self._height = height

    @property
    def properties(self):
        """Gets the properties of this ReportPanelSyncDefinition.  # noqa: E501

        Visual settings for the panel.  # noqa: E501

        :return: The properties of this ReportPanelSyncDefinition.  # noqa: E501
        :rtype: str
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """Sets the properties of this ReportPanelSyncDefinition.

        Visual settings for the panel.  # noqa: E501

        :param properties: The properties of this ReportPanelSyncDefinition.  # noqa: E501
        :type: str
        """
        if properties is None:
            raise ValueError("Invalid value for `properties`, must not be `None`")  # noqa: E501

        self._properties = properties

    @property
    def id(self):
        """Gets the id of this ReportPanelSyncDefinition.  # noqa: E501

        A string identifier that you can use to refer to the panel in filters.panelIds.  # noqa: E501

        :return: The id of this ReportPanelSyncDefinition.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ReportPanelSyncDefinition.

        A string identifier that you can use to refer to the panel in filters.panelIds.  # noqa: E501

        :param id: The id of this ReportPanelSyncDefinition.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def desired_quantization_in_secs(self):
        """Gets the desired_quantization_in_secs of this ReportPanelSyncDefinition.  # noqa: E501

        The quantization interval aligns your time series data to common intervals on the time axis (for example every one minute) to optimize the visualization and performance.  # noqa: E501

        :return: The desired_quantization_in_secs of this ReportPanelSyncDefinition.  # noqa: E501
        :rtype: int
        """
        return self._desired_quantization_in_secs

    @desired_quantization_in_secs.setter
    def desired_quantization_in_secs(self, desired_quantization_in_secs):
        """Sets the desired_quantization_in_secs of this ReportPanelSyncDefinition.

        The quantization interval aligns your time series data to common intervals on the time axis (for example every one minute) to optimize the visualization and performance.  # noqa: E501

        :param desired_quantization_in_secs: The desired_quantization_in_secs of this ReportPanelSyncDefinition.  # noqa: E501
        :type: int
        """

        self._desired_quantization_in_secs = desired_quantization_in_secs

    @property
    def query_parameters(self):
        """Gets the query_parameters of this ReportPanelSyncDefinition.  # noqa: E501

        The parameters for parameterized searches.  # noqa: E501

        :return: The query_parameters of this ReportPanelSyncDefinition.  # noqa: E501
        :rtype: list[QueryParameterSyncDefinition]
        """
        return self._query_parameters

    @query_parameters.setter
    def query_parameters(self, query_parameters):
        """Sets the query_parameters of this ReportPanelSyncDefinition.

        The parameters for parameterized searches.  # noqa: E501

        :param query_parameters: The query_parameters of this ReportPanelSyncDefinition.  # noqa: E501
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
        if issubclass(ReportPanelSyncDefinition, dict):
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
        if not isinstance(other, ReportPanelSyncDefinition):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
