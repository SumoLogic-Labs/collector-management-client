# coding: utf-8

"""
    Sumo Logic API

    # Getting Started Welcome to the Sumo Logic API reference. You can use these APIs to interact with the Sumo Logic platform. For information on the collector and search APIs see our [API home page](https://help.sumologic.com/APIs). ## API Endpoints Sumo Logic has several deployments in different geographic locations. You'll need to use the Sumo Logic API endpoint corresponding to your geographic location. See the table below for the different API endpoints by deployment. For details determining your account's deployment see [API endpoints](https://help.sumologic.com/?cid=3011). <table>   <tr>     <td> <strong>Deployment</strong> </td>     <td> <strong>Endpoint</strong> </td>   </tr> <tr>     <td> AU </td>     <td> https://api.au.sumologic.com/api/ </td>   </tr>   <tr>     <td> CA </td>     <td> https://api.ca.sumologic.com/api/ </td>   </tr> <tr>     <td> DE </td>     <td> https://api.de.sumologic.com/api/ </td>   </tr>   <tr>     <td> EU </td>     <td> https://api.eu.sumologic.com/api/ </td>   </tr>   <tr>     <td> JP </td>     <td> https://api.jp.sumologic.com/api/ </td>   </tr>   <tr>     <td> US1 </td>     <td> https://api.sumologic.com/api/ </td>   </tr>   <tr>     <td> US2 </td>     <td> https://api.us2.sumologic.com/api/ </td>   </tr> </table> ## Authentication Sumo Logic supports the following options for API authentication: - Access ID and Access Key - Base64 encoded Access ID and Access Key  See [Access Keys](https://help.sumologic.com/Manage/Security/Access-Keys) to generate an Access Key. Make sure to copy the key you create, because it is displayed only once. When you have an Access ID and Access Key you can execute requests such as the following:   ```bash   curl -u \"<accessId>:<accessKey>\" -X GET https://api.<deployment>.sumologic.com/api/v1/users   ```  Where `deployment` is either `au`, `ca`, `de`, `eu`, `jp`, `us1`, or `us2`. See [API endpoints](#section/API-Endpoints) for details.  If you prefer to use basic access authentication, you can do a Base64 encoding of your `<accessId>:<accessKey>` to authenticate your HTTPS request. The following is an example request, replace the placeholder `<encoded>` with your encoded Access ID and Access Key string:   ```bash   curl -H \"Authorization: Basic <encoded>\" -X GET https://api.<deployment>.sumologic.com/api/v1/users   ```   Refer to [API Authentication](https://help.sumologic.com/?cid=3012) for a Base64 example.  ## Status Codes Generic status codes that apply to all our APIs. See the [HTTP status code registry](https://www.iana.org/assignments/http-status-codes/http-status-codes.xhtml) for reference. <table>   <tr>     <td> <strong>HTTP Status Code</strong> </td>     <td> <strong>Error Code</strong> </td>     <td> <strong>Description</strong> </td>   </tr>   <tr>     <td> 301 </td>     <td> moved </td>     <td> The requested resource SHOULD be accessed through returned URI in Location Header.</td>   </tr>   <tr>     <td> 401 </td>     <td> unauthorized </td>     <td> Credential could not be verified. </td>   </tr>   <tr>     <td> 403 </td>     <td> forbidden </td>     <td> This operation is not allowed for your account type or the user doesn't have the role capability to perform this action. </td>   </tr>   <tr>     <td> 404 </td>     <td> notfound </td>     <td> Requested resource could not be found. </td>   </tr>   <tr>     <td> 405 </td>     <td> method.unsupported </td>     <td> Unsupported method for URL. </td>   </tr>   <tr>     <td> 415 </td>     <td> contenttype.invalid </td>     <td> Invalid content type. </td>   </tr>   <tr>     <td> 429 </td>     <td> rate.limit.exceeded </td>     <td> The API request rate is higher than 4 request per second or inflight API requests are higher than 10 request per second. </td>   </tr>   <tr>     <td> 500 </td>     <td> internal.error </td>     <td> Internal server error. </td>   </tr>   <tr>     <td> 503 </td>     <td> service.unavailable </td>     <td> Service is currently unavailable. </td>   </tr> </table> ## Filtering Some API endpoints support filtering results on a specified set of fields. Each endpoint that supports filtering will list the fields that can be filtered. Multiple fields can be combined by using an ampersand `&` character.  For example, to get 20 users whose `firstName` is `John` and `lastName` is `Doe`:   ```bash   api.sumologic.com/v1/users?limit=20&firstName=John&lastName=Doe   ```  ## Sorting Some API endpoints support sorting fields by using the `sortBy` query parameter. The default sort order is ascending. Prefix the field with a minus sign `-` to sort in descending order.  For example, to get 20 users sorted by their `email` in descending order:   ```bash   api.sumologic.com/v1/users?limit=20&sort=-email   ```  ## Rate Limiting * A rate limit of four API requests per second (240 requests per minute) applies to all API calls from a user. * A rate limit of 10 concurrent requests to any API endpoint applies to an access key.  If a rate is exceeded, a rate limit exceeded 429 status code is returned.  ## Generating Clients You can use [OpenAPI Generator](https://openapi-generator.tech) to generate clients from the YAML file to access the API.  ### Using [NPM](https://www.npmjs.com/get-npm) 1. Install [NPM package wrapper](https://github.com/openapitools/openapi-generator-cli) globally, exposing the CLI   on the command line:   ```bash   npm install @openapitools/openapi-generator-cli -g   ```   You can see detailed instructions [here](https://openapi-generator.tech/docs/installation#npm).  2. Download the [YAML file](/docs/sumologic-api.yaml) and save it locally. Let's say the file is saved as `sumologic-api.yaml`. 3. Use the following command to generate `python` client inside the `sumo/client/python` directory:   ```bash   openapi-generator generate -i sumologic-api.yaml -g python -o sumo/client/python   ```   ### Using [Homebrew](https://brew.sh/) 1. Install OpenAPI Generator   ```bash   brew install openapi-generator   ```  2. Download the [YAML file](/docs/sumologic-api.yaml) and save it locally. Let's say the file is saved as `sumologic-api.yaml`. 3. Use the following command to generate `python` client side code inside the `sumo/client/python` directory:   ```bash   openapi-generator generate -i sumologic-api.yaml -g python -o sumo/client/python   ```   # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class ContentManagementApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def async_copy_status(self, id, job_id, **kwargs):  # noqa: E501
        """Content copy job status.  # noqa: E501

        Get the status of the copy request with the given job identifier. On success, field `statusMessage` will contain identifier of the newly copied content in format: `id: {hexIdentifier}`.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.async_copy_status(id, job_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: The identifier of the content which was copied. (required)
        :param str job_id: The identifier of the asynchronous copy request job. (required)
        :param str is_admin_mode: Set this to \"true\" if you want to perform the request as a Content Administrator.
        :return: AsyncJobStatus
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.async_copy_status_with_http_info(id, job_id, **kwargs)  # noqa: E501
        else:
            (data) = self.async_copy_status_with_http_info(id, job_id, **kwargs)  # noqa: E501
            return data

    def async_copy_status_with_http_info(self, id, job_id, **kwargs):  # noqa: E501
        """Content copy job status.  # noqa: E501

        Get the status of the copy request with the given job identifier. On success, field `statusMessage` will contain identifier of the newly copied content in format: `id: {hexIdentifier}`.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.async_copy_status_with_http_info(id, job_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: The identifier of the content which was copied. (required)
        :param str job_id: The identifier of the asynchronous copy request job. (required)
        :param str is_admin_mode: Set this to \"true\" if you want to perform the request as a Content Administrator.
        :return: AsyncJobStatus
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'job_id', 'is_admin_mode']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method async_copy_status" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `async_copy_status`")  # noqa: E501
        # verify the required parameter 'job_id' is set
        if ('job_id' not in params or
                params['job_id'] is None):
            raise ValueError("Missing the required parameter `job_id` when calling `async_copy_status`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501
        if 'job_id' in params:
            path_params['jobId'] = params['job_id']  # noqa: E501

        query_params = []

        header_params = {}
        if 'is_admin_mode' in params:
            header_params['isAdminMode'] = params['is_admin_mode']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/v2/content/{id}/copy/{jobId}/status', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AsyncJobStatus',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def begin_async_copy(self, id, destination_folder, **kwargs):  # noqa: E501
        """Start a content copy job.  # noqa: E501

        Start an asynchronous content copy job with the given identifier to the destination folder. If the content item is a folder, everything under the folder is copied recursively.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.begin_async_copy(id, destination_folder, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: The identifier of the content item to copy. Identifiers from the Library in the Sumo user interface are provided in decimal format which is incompatible with this API. The identifier needs to be in hexadecimal format. (required)
        :param str destination_folder: The identifier of the destination folder. (required)
        :param str is_admin_mode: Set this to \"true\" if you want to perform the request as a Content Administrator.
        :return: BeginAsyncJobResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.begin_async_copy_with_http_info(id, destination_folder, **kwargs)  # noqa: E501
        else:
            (data) = self.begin_async_copy_with_http_info(id, destination_folder, **kwargs)  # noqa: E501
            return data

    def begin_async_copy_with_http_info(self, id, destination_folder, **kwargs):  # noqa: E501
        """Start a content copy job.  # noqa: E501

        Start an asynchronous content copy job with the given identifier to the destination folder. If the content item is a folder, everything under the folder is copied recursively.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.begin_async_copy_with_http_info(id, destination_folder, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: The identifier of the content item to copy. Identifiers from the Library in the Sumo user interface are provided in decimal format which is incompatible with this API. The identifier needs to be in hexadecimal format. (required)
        :param str destination_folder: The identifier of the destination folder. (required)
        :param str is_admin_mode: Set this to \"true\" if you want to perform the request as a Content Administrator.
        :return: BeginAsyncJobResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'destination_folder', 'is_admin_mode']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method begin_async_copy" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `begin_async_copy`")  # noqa: E501
        # verify the required parameter 'destination_folder' is set
        if ('destination_folder' not in params or
                params['destination_folder'] is None):
            raise ValueError("Missing the required parameter `destination_folder` when calling `begin_async_copy`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []
        if 'destination_folder' in params:
            query_params.append(('destinationFolder', params['destination_folder']))  # noqa: E501

        header_params = {}
        if 'is_admin_mode' in params:
            header_params['isAdminMode'] = params['is_admin_mode']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/v2/content/{id}/copy', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='BeginAsyncJobResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def begin_async_delete(self, id, **kwargs):  # noqa: E501
        """Start a content deletion job.  # noqa: E501

        Start an asynchronous content deletion job with the given identifier.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.begin_async_delete(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Identifier of the content to delete. Identifiers from the Library in the Sumo user interface are provided in decimal format which is incompatible with this API. The identifier needs to be in hexadecimal format. (required)
        :param str is_admin_mode: Set this to \"true\" if you want to perform the request as a Content Administrator.
        :return: BeginAsyncJobResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.begin_async_delete_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.begin_async_delete_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def begin_async_delete_with_http_info(self, id, **kwargs):  # noqa: E501
        """Start a content deletion job.  # noqa: E501

        Start an asynchronous content deletion job with the given identifier.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.begin_async_delete_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Identifier of the content to delete. Identifiers from the Library in the Sumo user interface are provided in decimal format which is incompatible with this API. The identifier needs to be in hexadecimal format. (required)
        :param str is_admin_mode: Set this to \"true\" if you want to perform the request as a Content Administrator.
        :return: BeginAsyncJobResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'is_admin_mode']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method begin_async_delete" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `begin_async_delete`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}
        if 'is_admin_mode' in params:
            header_params['isAdminMode'] = params['is_admin_mode']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/v2/content/{id}/delete', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='BeginAsyncJobResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def begin_async_export(self, id, **kwargs):  # noqa: E501
        """Start a content export job.  # noqa: E501

        Schedule an asynchronous export of content with the given identifier. If the content item is a folder, everything under the folder is exported recursively with folder as the root. The results from this export are incompatible with the Library import feature in the Sumo user interface.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.begin_async_export(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: The identifier of the content item to export. Identifiers from the Library in the Sumo user interface are provided in decimal format which is incompatible with this API. The identifier needs to be in hexadecimal format. (required)
        :param str is_admin_mode: Set this to \"true\" if you want to perform the request as a Content Administrator.
        :return: BeginAsyncJobResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.begin_async_export_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.begin_async_export_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def begin_async_export_with_http_info(self, id, **kwargs):  # noqa: E501
        """Start a content export job.  # noqa: E501

        Schedule an asynchronous export of content with the given identifier. If the content item is a folder, everything under the folder is exported recursively with folder as the root. The results from this export are incompatible with the Library import feature in the Sumo user interface.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.begin_async_export_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: The identifier of the content item to export. Identifiers from the Library in the Sumo user interface are provided in decimal format which is incompatible with this API. The identifier needs to be in hexadecimal format. (required)
        :param str is_admin_mode: Set this to \"true\" if you want to perform the request as a Content Administrator.
        :return: BeginAsyncJobResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'is_admin_mode']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method begin_async_export" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `begin_async_export`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}
        if 'is_admin_mode' in params:
            header_params['isAdminMode'] = params['is_admin_mode']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/v2/content/{id}/export', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='BeginAsyncJobResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def begin_async_import(self, body, folder_id, **kwargs):  # noqa: E501
        """Start a content import job.  # noqa: E501

        Schedule an asynchronous import of content inside an existing folder with the given identifier. Import requests can be used to create or update content within a folder. Content items need to have a unique name within their folder. If there is already a content item with the same name in the folder, you can set the `overwrite` parameter to `true` to overwrite existing content items. By default, the `overwrite` parameter is set to `false`, where the import will fail if a content item with the same name already exist.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.begin_async_import(body, folder_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ContentSyncDefinition body: The content to import. (required)
        :param str folder_id: The identifier of the folder to import into. Identifiers from the Library in the Sumo user interface are provided in decimal format which is incompatible with this API. The identifier needs to be in hexadecimal format. (required)
        :param str is_admin_mode: Set this to \"true\" if you want to perform the request as a Content Administrator.
        :param bool overwrite: Set this to \"true\" to overwrite a content item if the name already exists.
        :return: BeginAsyncJobResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.begin_async_import_with_http_info(body, folder_id, **kwargs)  # noqa: E501
        else:
            (data) = self.begin_async_import_with_http_info(body, folder_id, **kwargs)  # noqa: E501
            return data

    def begin_async_import_with_http_info(self, body, folder_id, **kwargs):  # noqa: E501
        """Start a content import job.  # noqa: E501

        Schedule an asynchronous import of content inside an existing folder with the given identifier. Import requests can be used to create or update content within a folder. Content items need to have a unique name within their folder. If there is already a content item with the same name in the folder, you can set the `overwrite` parameter to `true` to overwrite existing content items. By default, the `overwrite` parameter is set to `false`, where the import will fail if a content item with the same name already exist.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.begin_async_import_with_http_info(body, folder_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ContentSyncDefinition body: The content to import. (required)
        :param str folder_id: The identifier of the folder to import into. Identifiers from the Library in the Sumo user interface are provided in decimal format which is incompatible with this API. The identifier needs to be in hexadecimal format. (required)
        :param str is_admin_mode: Set this to \"true\" if you want to perform the request as a Content Administrator.
        :param bool overwrite: Set this to \"true\" to overwrite a content item if the name already exists.
        :return: BeginAsyncJobResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'folder_id', 'is_admin_mode', 'overwrite']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method begin_async_import" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `begin_async_import`")  # noqa: E501
        # verify the required parameter 'folder_id' is set
        if ('folder_id' not in params or
                params['folder_id'] is None):
            raise ValueError("Missing the required parameter `folder_id` when calling `begin_async_import`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'folder_id' in params:
            path_params['folderId'] = params['folder_id']  # noqa: E501

        query_params = []
        if 'overwrite' in params:
            query_params.append(('overwrite', params['overwrite']))  # noqa: E501

        header_params = {}
        if 'is_admin_mode' in params:
            header_params['isAdminMode'] = params['is_admin_mode']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/v2/content/folders/{folderId}/import', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='BeginAsyncJobResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_async_delete_status(self, id, job_id, **kwargs):  # noqa: E501
        """Content deletion job status.  # noqa: E501

        Get the status of an asynchronous content deletion job request for the given job identifier.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_async_delete_status(id, job_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Identifier of the content to delete. (required)
        :param str job_id: The identifier of the asynchronous job. (required)
        :param str is_admin_mode: Set this to \"true\" if you want to perform the request as a Content Administrator.
        :return: AsyncJobStatus
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_async_delete_status_with_http_info(id, job_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_async_delete_status_with_http_info(id, job_id, **kwargs)  # noqa: E501
            return data

    def get_async_delete_status_with_http_info(self, id, job_id, **kwargs):  # noqa: E501
        """Content deletion job status.  # noqa: E501

        Get the status of an asynchronous content deletion job request for the given job identifier.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_async_delete_status_with_http_info(id, job_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Identifier of the content to delete. (required)
        :param str job_id: The identifier of the asynchronous job. (required)
        :param str is_admin_mode: Set this to \"true\" if you want to perform the request as a Content Administrator.
        :return: AsyncJobStatus
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'job_id', 'is_admin_mode']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_async_delete_status" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `get_async_delete_status`")  # noqa: E501
        # verify the required parameter 'job_id' is set
        if ('job_id' not in params or
                params['job_id'] is None):
            raise ValueError("Missing the required parameter `job_id` when calling `get_async_delete_status`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501
        if 'job_id' in params:
            path_params['jobId'] = params['job_id']  # noqa: E501

        query_params = []

        header_params = {}
        if 'is_admin_mode' in params:
            header_params['isAdminMode'] = params['is_admin_mode']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/v2/content/{id}/delete/{jobId}/status', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AsyncJobStatus',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_async_export_result(self, content_id, job_id, **kwargs):  # noqa: E501
        """Content export job result.  # noqa: E501

        Get results from content export job for the given job identifier. The results from this export are incompatible with the Library import feature in the Sumo user interface.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_async_export_result(content_id, job_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str content_id: The identifier of the exported content item. (required)
        :param str job_id: The identifier of the asynchronous job. (required)
        :param str is_admin_mode: Set this to \"true\" if you want to perform the request as a Content Administrator.
        :return: ContentSyncDefinition
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_async_export_result_with_http_info(content_id, job_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_async_export_result_with_http_info(content_id, job_id, **kwargs)  # noqa: E501
            return data

    def get_async_export_result_with_http_info(self, content_id, job_id, **kwargs):  # noqa: E501
        """Content export job result.  # noqa: E501

        Get results from content export job for the given job identifier. The results from this export are incompatible with the Library import feature in the Sumo user interface.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_async_export_result_with_http_info(content_id, job_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str content_id: The identifier of the exported content item. (required)
        :param str job_id: The identifier of the asynchronous job. (required)
        :param str is_admin_mode: Set this to \"true\" if you want to perform the request as a Content Administrator.
        :return: ContentSyncDefinition
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['content_id', 'job_id', 'is_admin_mode']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_async_export_result" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'content_id' is set
        if ('content_id' not in params or
                params['content_id'] is None):
            raise ValueError("Missing the required parameter `content_id` when calling `get_async_export_result`")  # noqa: E501
        # verify the required parameter 'job_id' is set
        if ('job_id' not in params or
                params['job_id'] is None):
            raise ValueError("Missing the required parameter `job_id` when calling `get_async_export_result`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'content_id' in params:
            path_params['contentId'] = params['content_id']  # noqa: E501
        if 'job_id' in params:
            path_params['jobId'] = params['job_id']  # noqa: E501

        query_params = []

        header_params = {}
        if 'is_admin_mode' in params:
            header_params['isAdminMode'] = params['is_admin_mode']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/v2/content/{contentId}/export/{jobId}/result', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ContentSyncDefinition',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_async_export_status(self, content_id, job_id, **kwargs):  # noqa: E501
        """Content export job status.  # noqa: E501

        Get the status of an asynchronous content export request for the given job identifier. On success, use the [getExportResult](#operation/getAsyncExportResult) endpoint to get the result of the export job.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_async_export_status(content_id, job_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str content_id: The identifier of the exported content item. (required)
        :param str job_id: The identifier of the asynchronous export job. (required)
        :param str is_admin_mode: Set this to \"true\" if you want to perform the request as a Content Administrator.
        :return: AsyncJobStatus
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_async_export_status_with_http_info(content_id, job_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_async_export_status_with_http_info(content_id, job_id, **kwargs)  # noqa: E501
            return data

    def get_async_export_status_with_http_info(self, content_id, job_id, **kwargs):  # noqa: E501
        """Content export job status.  # noqa: E501

        Get the status of an asynchronous content export request for the given job identifier. On success, use the [getExportResult](#operation/getAsyncExportResult) endpoint to get the result of the export job.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_async_export_status_with_http_info(content_id, job_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str content_id: The identifier of the exported content item. (required)
        :param str job_id: The identifier of the asynchronous export job. (required)
        :param str is_admin_mode: Set this to \"true\" if you want to perform the request as a Content Administrator.
        :return: AsyncJobStatus
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['content_id', 'job_id', 'is_admin_mode']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_async_export_status" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'content_id' is set
        if ('content_id' not in params or
                params['content_id'] is None):
            raise ValueError("Missing the required parameter `content_id` when calling `get_async_export_status`")  # noqa: E501
        # verify the required parameter 'job_id' is set
        if ('job_id' not in params or
                params['job_id'] is None):
            raise ValueError("Missing the required parameter `job_id` when calling `get_async_export_status`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'content_id' in params:
            path_params['contentId'] = params['content_id']  # noqa: E501
        if 'job_id' in params:
            path_params['jobId'] = params['job_id']  # noqa: E501

        query_params = []

        header_params = {}
        if 'is_admin_mode' in params:
            header_params['isAdminMode'] = params['is_admin_mode']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/v2/content/{contentId}/export/{jobId}/status', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AsyncJobStatus',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_async_import_status(self, folder_id, job_id, **kwargs):  # noqa: E501
        """Content import job status.  # noqa: E501

        Get the status of a content import job for the given job identifier.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_async_import_status(folder_id, job_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str folder_id: The identifier of the folder to import into. (required)
        :param str job_id: The identifier of the import request. (required)
        :param str is_admin_mode: Set this to \"true\" if you want to perform the request as a Content Administrator.
        :return: AsyncJobStatus
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_async_import_status_with_http_info(folder_id, job_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_async_import_status_with_http_info(folder_id, job_id, **kwargs)  # noqa: E501
            return data

    def get_async_import_status_with_http_info(self, folder_id, job_id, **kwargs):  # noqa: E501
        """Content import job status.  # noqa: E501

        Get the status of a content import job for the given job identifier.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_async_import_status_with_http_info(folder_id, job_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str folder_id: The identifier of the folder to import into. (required)
        :param str job_id: The identifier of the import request. (required)
        :param str is_admin_mode: Set this to \"true\" if you want to perform the request as a Content Administrator.
        :return: AsyncJobStatus
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['folder_id', 'job_id', 'is_admin_mode']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_async_import_status" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'folder_id' is set
        if ('folder_id' not in params or
                params['folder_id'] is None):
            raise ValueError("Missing the required parameter `folder_id` when calling `get_async_import_status`")  # noqa: E501
        # verify the required parameter 'job_id' is set
        if ('job_id' not in params or
                params['job_id'] is None):
            raise ValueError("Missing the required parameter `job_id` when calling `get_async_import_status`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'folder_id' in params:
            path_params['folderId'] = params['folder_id']  # noqa: E501
        if 'job_id' in params:
            path_params['jobId'] = params['job_id']  # noqa: E501

        query_params = []

        header_params = {}
        if 'is_admin_mode' in params:
            header_params['isAdminMode'] = params['is_admin_mode']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/v2/content/folders/{folderId}/import/{jobId}/status', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AsyncJobStatus',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def move_item(self, destination_folder_id, id, **kwargs):  # noqa: E501
        """Move an item.  # noqa: E501

        Moves an item from its current location to another folder.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.move_item(destination_folder_id, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str destination_folder_id: Identifier of the destination folder. (required)
        :param str id: Identifier of the item the user wants to move. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.move_item_with_http_info(destination_folder_id, id, **kwargs)  # noqa: E501
        else:
            (data) = self.move_item_with_http_info(destination_folder_id, id, **kwargs)  # noqa: E501
            return data

    def move_item_with_http_info(self, destination_folder_id, id, **kwargs):  # noqa: E501
        """Move an item.  # noqa: E501

        Moves an item from its current location to another folder.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.move_item_with_http_info(destination_folder_id, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str destination_folder_id: Identifier of the destination folder. (required)
        :param str id: Identifier of the item the user wants to move. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['destination_folder_id', 'id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method move_item" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'destination_folder_id' is set
        if ('destination_folder_id' not in params or
                params['destination_folder_id'] is None):
            raise ValueError("Missing the required parameter `destination_folder_id` when calling `move_item`")  # noqa: E501
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `move_item`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []
        if 'destination_folder_id' in params:
            query_params.append(('destinationFolderId', params['destination_folder_id']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/v2/content/{id}/move', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
