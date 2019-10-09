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
from swagger_client.models.container_panel import ContainerPanel  # noqa: F401,E501
from swagger_client.models.content_sync_definition import ContentSyncDefinition  # noqa: F401,E501
from swagger_client.models.resolvable_time_range import ResolvableTimeRange  # noqa: F401,E501
from swagger_client.models.topology_label_map import TopologyLabelMap  # noqa: F401,E501


class MewboardSyncDefinition(ContentSyncDefinition):
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
        'description': 'str',
        'title': 'str',
        'root_panel': 'ContainerPanel',
        'theme': 'str',
        'topology_label_map': 'TopologyLabelMap',
        'refresh_interval': 'float',
        'time_range': 'ResolvableTimeRange'
    }
    if hasattr(ContentSyncDefinition, "swagger_types"):
        swagger_types.update(ContentSyncDefinition.swagger_types)

    attribute_map = {
        'description': 'description',
        'title': 'title',
        'root_panel': 'rootPanel',
        'theme': 'theme',
        'topology_label_map': 'topologyLabelMap',
        'refresh_interval': 'refreshInterval',
        'time_range': 'timeRange'
    }
    if hasattr(ContentSyncDefinition, "attribute_map"):
        attribute_map.update(ContentSyncDefinition.attribute_map)

    def __init__(self, description=None, title=None, root_panel=None, theme=None, topology_label_map=None, refresh_interval=None, time_range=None, *args, **kwargs):  # noqa: E501
        """MewboardSyncDefinition - a model defined in Swagger"""  # noqa: E501
        self._description = None
        self._title = None
        self._root_panel = None
        self._theme = None
        self._topology_label_map = None
        self._refresh_interval = None
        self._time_range = None
        self.discriminator = None
        self.description = description
        self.title = title
        self.root_panel = root_panel
        if theme is not None:
            self.theme = theme
        self.topology_label_map = topology_label_map
        if refresh_interval is not None:
            self.refresh_interval = refresh_interval
        if time_range is not None:
            self.time_range = time_range
        ContentSyncDefinition.__init__(self, *args, **kwargs)

    @property
    def description(self):
        """Gets the description of this MewboardSyncDefinition.  # noqa: E501

        A description of the dashboard.  # noqa: E501

        :return: The description of this MewboardSyncDefinition.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this MewboardSyncDefinition.

        A description of the dashboard.  # noqa: E501

        :param description: The description of this MewboardSyncDefinition.  # noqa: E501
        :type: str
        """
        if description is None:
            raise ValueError("Invalid value for `description`, must not be `None`")  # noqa: E501

        self._description = description

    @property
    def title(self):
        """Gets the title of this MewboardSyncDefinition.  # noqa: E501

        The title of the dashboard.  # noqa: E501

        :return: The title of this MewboardSyncDefinition.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this MewboardSyncDefinition.

        The title of the dashboard.  # noqa: E501

        :param title: The title of this MewboardSyncDefinition.  # noqa: E501
        :type: str
        """
        if title is None:
            raise ValueError("Invalid value for `title`, must not be `None`")  # noqa: E501

        self._title = title

    @property
    def root_panel(self):
        """Gets the root_panel of this MewboardSyncDefinition.  # noqa: E501


        :return: The root_panel of this MewboardSyncDefinition.  # noqa: E501
        :rtype: ContainerPanel
        """
        return self._root_panel

    @root_panel.setter
    def root_panel(self, root_panel):
        """Sets the root_panel of this MewboardSyncDefinition.


        :param root_panel: The root_panel of this MewboardSyncDefinition.  # noqa: E501
        :type: ContainerPanel
        """
        if root_panel is None:
            raise ValueError("Invalid value for `root_panel`, must not be `None`")  # noqa: E501

        self._root_panel = root_panel

    @property
    def theme(self):
        """Gets the theme of this MewboardSyncDefinition.  # noqa: E501

        Theme for the dashboard, can be light or dark.  # noqa: E501

        :return: The theme of this MewboardSyncDefinition.  # noqa: E501
        :rtype: str
        """
        return self._theme

    @theme.setter
    def theme(self, theme):
        """Sets the theme of this MewboardSyncDefinition.

        Theme for the dashboard, can be light or dark.  # noqa: E501

        :param theme: The theme of this MewboardSyncDefinition.  # noqa: E501
        :type: str
        """

        self._theme = theme

    @property
    def topology_label_map(self):
        """Gets the topology_label_map of this MewboardSyncDefinition.  # noqa: E501


        :return: The topology_label_map of this MewboardSyncDefinition.  # noqa: E501
        :rtype: TopologyLabelMap
        """
        return self._topology_label_map

    @topology_label_map.setter
    def topology_label_map(self, topology_label_map):
        """Sets the topology_label_map of this MewboardSyncDefinition.


        :param topology_label_map: The topology_label_map of this MewboardSyncDefinition.  # noqa: E501
        :type: TopologyLabelMap
        """
        if topology_label_map is None:
            raise ValueError("Invalid value for `topology_label_map`, must not be `None`")  # noqa: E501

        self._topology_label_map = topology_label_map

    @property
    def refresh_interval(self):
        """Gets the refresh_interval of this MewboardSyncDefinition.  # noqa: E501

        Interval of time (in seconds) to automatically refresh the dashboard. A value of 0 means we never automatically refresh the dashboard.  # noqa: E501

        :return: The refresh_interval of this MewboardSyncDefinition.  # noqa: E501
        :rtype: float
        """
        return self._refresh_interval

    @refresh_interval.setter
    def refresh_interval(self, refresh_interval):
        """Sets the refresh_interval of this MewboardSyncDefinition.

        Interval of time (in seconds) to automatically refresh the dashboard. A value of 0 means we never automatically refresh the dashboard.  # noqa: E501

        :param refresh_interval: The refresh_interval of this MewboardSyncDefinition.  # noqa: E501
        :type: float
        """

        self._refresh_interval = refresh_interval

    @property
    def time_range(self):
        """Gets the time_range of this MewboardSyncDefinition.  # noqa: E501


        :return: The time_range of this MewboardSyncDefinition.  # noqa: E501
        :rtype: ResolvableTimeRange
        """
        return self._time_range

    @time_range.setter
    def time_range(self, time_range):
        """Sets the time_range of this MewboardSyncDefinition.


        :param time_range: The time_range of this MewboardSyncDefinition.  # noqa: E501
        :type: ResolvableTimeRange
        """

        self._time_range = time_range

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
        if issubclass(MewboardSyncDefinition, dict):
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
        if not isinstance(other, MewboardSyncDefinition):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
