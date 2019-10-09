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


class EmailAction(Action):
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
        'recipients': 'list[str]',
        'cc_recipients': 'list[str]',
        'bcc_recipients': 'list[str]',
        'subject': 'str',
        'message_body': 'str',
        'body_format': 'str',
        'time_zone': 'str'
    }
    if hasattr(Action, "swagger_types"):
        swagger_types.update(Action.swagger_types)

    attribute_map = {
        'recipients': 'recipients',
        'cc_recipients': 'ccRecipients',
        'bcc_recipients': 'bccRecipients',
        'subject': 'subject',
        'message_body': 'messageBody',
        'body_format': 'bodyFormat',
        'time_zone': 'timeZone'
    }
    if hasattr(Action, "attribute_map"):
        attribute_map.update(Action.attribute_map)

    def __init__(self, recipients=None, cc_recipients=None, bcc_recipients=None, subject=None, message_body=None, body_format='text/html', time_zone=None, *args, **kwargs):  # noqa: E501
        """EmailAction - a model defined in Swagger"""  # noqa: E501
        self._recipients = None
        self._cc_recipients = None
        self._bcc_recipients = None
        self._subject = None
        self._message_body = None
        self._body_format = None
        self._time_zone = None
        self.discriminator = None
        self.recipients = recipients
        if cc_recipients is not None:
            self.cc_recipients = cc_recipients
        if bcc_recipients is not None:
            self.bcc_recipients = bcc_recipients
        self.subject = subject
        self.message_body = message_body
        if body_format is not None:
            self.body_format = body_format
        if time_zone is not None:
            self.time_zone = time_zone
        Action.__init__(self, *args, **kwargs)

    @property
    def recipients(self):
        """Gets the recipients of this EmailAction.  # noqa: E501

        A list of email addresses to send to when the rule fires.  # noqa: E501

        :return: The recipients of this EmailAction.  # noqa: E501
        :rtype: list[str]
        """
        return self._recipients

    @recipients.setter
    def recipients(self, recipients):
        """Sets the recipients of this EmailAction.

        A list of email addresses to send to when the rule fires.  # noqa: E501

        :param recipients: The recipients of this EmailAction.  # noqa: E501
        :type: list[str]
        """
        if recipients is None:
            raise ValueError("Invalid value for `recipients`, must not be `None`")  # noqa: E501

        self._recipients = recipients

    @property
    def cc_recipients(self):
        """Gets the cc_recipients of this EmailAction.  # noqa: E501

        A list of email addresses to copy to when the rule fires.  # noqa: E501

        :return: The cc_recipients of this EmailAction.  # noqa: E501
        :rtype: list[str]
        """
        return self._cc_recipients

    @cc_recipients.setter
    def cc_recipients(self, cc_recipients):
        """Sets the cc_recipients of this EmailAction.

        A list of email addresses to copy to when the rule fires.  # noqa: E501

        :param cc_recipients: The cc_recipients of this EmailAction.  # noqa: E501
        :type: list[str]
        """

        self._cc_recipients = cc_recipients

    @property
    def bcc_recipients(self):
        """Gets the bcc_recipients of this EmailAction.  # noqa: E501

        A list of email addresses to blind copy to when the rule fires.  # noqa: E501

        :return: The bcc_recipients of this EmailAction.  # noqa: E501
        :rtype: list[str]
        """
        return self._bcc_recipients

    @bcc_recipients.setter
    def bcc_recipients(self, bcc_recipients):
        """Sets the bcc_recipients of this EmailAction.

        A list of email addresses to blind copy to when the rule fires.  # noqa: E501

        :param bcc_recipients: The bcc_recipients of this EmailAction.  # noqa: E501
        :type: list[str]
        """

        self._bcc_recipients = bcc_recipients

    @property
    def subject(self):
        """Gets the subject of this EmailAction.  # noqa: E501

        The subject line of the email.  # noqa: E501

        :return: The subject of this EmailAction.  # noqa: E501
        :rtype: str
        """
        return self._subject

    @subject.setter
    def subject(self, subject):
        """Sets the subject of this EmailAction.

        The subject line of the email.  # noqa: E501

        :param subject: The subject of this EmailAction.  # noqa: E501
        :type: str
        """
        if subject is None:
            raise ValueError("Invalid value for `subject`, must not be `None`")  # noqa: E501

        self._subject = subject

    @property
    def message_body(self):
        """Gets the message_body of this EmailAction.  # noqa: E501

        The message body of the email to send.  # noqa: E501

        :return: The message_body of this EmailAction.  # noqa: E501
        :rtype: str
        """
        return self._message_body

    @message_body.setter
    def message_body(self, message_body):
        """Sets the message_body of this EmailAction.

        The message body of the email to send.  # noqa: E501

        :param message_body: The message_body of this EmailAction.  # noqa: E501
        :type: str
        """
        if message_body is None:
            raise ValueError("Invalid value for `message_body`, must not be `None`")  # noqa: E501

        self._message_body = message_body

    @property
    def body_format(self):
        """Gets the body_format of this EmailAction.  # noqa: E501

        The format of the message body.  # noqa: E501

        :return: The body_format of this EmailAction.  # noqa: E501
        :rtype: str
        """
        return self._body_format

    @body_format.setter
    def body_format(self, body_format):
        """Sets the body_format of this EmailAction.

        The format of the message body.  # noqa: E501

        :param body_format: The body_format of this EmailAction.  # noqa: E501
        :type: str
        """

        self._body_format = body_format

    @property
    def time_zone(self):
        """Gets the time_zone of this EmailAction.  # noqa: E501

        Time zone.  # noqa: E501

        :return: The time_zone of this EmailAction.  # noqa: E501
        :rtype: str
        """
        return self._time_zone

    @time_zone.setter
    def time_zone(self, time_zone):
        """Sets the time_zone of this EmailAction.

        Time zone.  # noqa: E501

        :param time_zone: The time_zone of this EmailAction.  # noqa: E501
        :type: str
        """

        self._time_zone = time_zone

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
        if issubclass(EmailAction, dict):
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
        if not isinstance(other, EmailAction):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
