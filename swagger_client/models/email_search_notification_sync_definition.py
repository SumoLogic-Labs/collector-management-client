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
from swagger_client.models.schedule_notification_sync_definition import ScheduleNotificationSyncDefinition  # noqa: F401,E501


class EmailSearchNotificationSyncDefinition(ScheduleNotificationSyncDefinition):
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
        'to_list': 'list[str]',
        'subject_template': 'str',
        'include_query': 'bool',
        'include_result_set': 'bool',
        'include_histogram': 'bool',
        'include_csv_attachment': 'bool'
    }
    if hasattr(ScheduleNotificationSyncDefinition, "swagger_types"):
        swagger_types.update(ScheduleNotificationSyncDefinition.swagger_types)

    attribute_map = {
        'to_list': 'toList',
        'subject_template': 'subjectTemplate',
        'include_query': 'includeQuery',
        'include_result_set': 'includeResultSet',
        'include_histogram': 'includeHistogram',
        'include_csv_attachment': 'includeCsvAttachment'
    }
    if hasattr(ScheduleNotificationSyncDefinition, "attribute_map"):
        attribute_map.update(ScheduleNotificationSyncDefinition.attribute_map)

    def __init__(self, to_list=None, subject_template=None, include_query=True, include_result_set=True, include_histogram=True, include_csv_attachment=False, *args, **kwargs):  # noqa: E501
        """EmailSearchNotificationSyncDefinition - a model defined in Swagger"""  # noqa: E501
        self._to_list = None
        self._subject_template = None
        self._include_query = None
        self._include_result_set = None
        self._include_histogram = None
        self._include_csv_attachment = None
        self.discriminator = None
        self.to_list = to_list
        if subject_template is not None:
            self.subject_template = subject_template
        if include_query is not None:
            self.include_query = include_query
        if include_result_set is not None:
            self.include_result_set = include_result_set
        if include_histogram is not None:
            self.include_histogram = include_histogram
        if include_csv_attachment is not None:
            self.include_csv_attachment = include_csv_attachment
        ScheduleNotificationSyncDefinition.__init__(self, *args, **kwargs)

    @property
    def to_list(self):
        """Gets the to_list of this EmailSearchNotificationSyncDefinition.  # noqa: E501

        A list of email recipients.  # noqa: E501

        :return: The to_list of this EmailSearchNotificationSyncDefinition.  # noqa: E501
        :rtype: list[str]
        """
        return self._to_list

    @to_list.setter
    def to_list(self, to_list):
        """Sets the to_list of this EmailSearchNotificationSyncDefinition.

        A list of email recipients.  # noqa: E501

        :param to_list: The to_list of this EmailSearchNotificationSyncDefinition.  # noqa: E501
        :type: list[str]
        """
        if to_list is None:
            raise ValueError("Invalid value for `to_list`, must not be `None`")  # noqa: E501

        self._to_list = to_list

    @property
    def subject_template(self):
        """Gets the subject_template of this EmailSearchNotificationSyncDefinition.  # noqa: E501

        If the notification is scheduled with a threshold, the default subject template will be \"Search Alert: $AlertCondition results found for $SearchName\". For email notifications without a threshold, the default subject template is \"Search Results: $SearchName\".  # noqa: E501

        :return: The subject_template of this EmailSearchNotificationSyncDefinition.  # noqa: E501
        :rtype: str
        """
        return self._subject_template

    @subject_template.setter
    def subject_template(self, subject_template):
        """Sets the subject_template of this EmailSearchNotificationSyncDefinition.

        If the notification is scheduled with a threshold, the default subject template will be \"Search Alert: $AlertCondition results found for $SearchName\". For email notifications without a threshold, the default subject template is \"Search Results: $SearchName\".  # noqa: E501

        :param subject_template: The subject_template of this EmailSearchNotificationSyncDefinition.  # noqa: E501
        :type: str
        """

        self._subject_template = subject_template

    @property
    def include_query(self):
        """Gets the include_query of this EmailSearchNotificationSyncDefinition.  # noqa: E501

        A boolean value to indicate if the search query should be included in the notification email.  # noqa: E501

        :return: The include_query of this EmailSearchNotificationSyncDefinition.  # noqa: E501
        :rtype: bool
        """
        return self._include_query

    @include_query.setter
    def include_query(self, include_query):
        """Sets the include_query of this EmailSearchNotificationSyncDefinition.

        A boolean value to indicate if the search query should be included in the notification email.  # noqa: E501

        :param include_query: The include_query of this EmailSearchNotificationSyncDefinition.  # noqa: E501
        :type: bool
        """

        self._include_query = include_query

    @property
    def include_result_set(self):
        """Gets the include_result_set of this EmailSearchNotificationSyncDefinition.  # noqa: E501

        A boolean value to indicate if the search result set should be included in the notification email.  # noqa: E501

        :return: The include_result_set of this EmailSearchNotificationSyncDefinition.  # noqa: E501
        :rtype: bool
        """
        return self._include_result_set

    @include_result_set.setter
    def include_result_set(self, include_result_set):
        """Sets the include_result_set of this EmailSearchNotificationSyncDefinition.

        A boolean value to indicate if the search result set should be included in the notification email.  # noqa: E501

        :param include_result_set: The include_result_set of this EmailSearchNotificationSyncDefinition.  # noqa: E501
        :type: bool
        """

        self._include_result_set = include_result_set

    @property
    def include_histogram(self):
        """Gets the include_histogram of this EmailSearchNotificationSyncDefinition.  # noqa: E501

        A boolean value to indicate if the search result histogram should be included in the notification email.  # noqa: E501

        :return: The include_histogram of this EmailSearchNotificationSyncDefinition.  # noqa: E501
        :rtype: bool
        """
        return self._include_histogram

    @include_histogram.setter
    def include_histogram(self, include_histogram):
        """Sets the include_histogram of this EmailSearchNotificationSyncDefinition.

        A boolean value to indicate if the search result histogram should be included in the notification email.  # noqa: E501

        :param include_histogram: The include_histogram of this EmailSearchNotificationSyncDefinition.  # noqa: E501
        :type: bool
        """

        self._include_histogram = include_histogram

    @property
    def include_csv_attachment(self):
        """Gets the include_csv_attachment of this EmailSearchNotificationSyncDefinition.  # noqa: E501

        A boolean value to indicate if the search results should be included in the notification email as a CSV attachment.  # noqa: E501

        :return: The include_csv_attachment of this EmailSearchNotificationSyncDefinition.  # noqa: E501
        :rtype: bool
        """
        return self._include_csv_attachment

    @include_csv_attachment.setter
    def include_csv_attachment(self, include_csv_attachment):
        """Sets the include_csv_attachment of this EmailSearchNotificationSyncDefinition.

        A boolean value to indicate if the search results should be included in the notification email as a CSV attachment.  # noqa: E501

        :param include_csv_attachment: The include_csv_attachment of this EmailSearchNotificationSyncDefinition.  # noqa: E501
        :type: bool
        """

        self._include_csv_attachment = include_csv_attachment

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
        if issubclass(EmailSearchNotificationSyncDefinition, dict):
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
        if not isinstance(other, EmailSearchNotificationSyncDefinition):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
