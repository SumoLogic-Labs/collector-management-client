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


class FolderManagementApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_folder(self, body, **kwargs):  # noqa: E501
        """Create a new folder.  # noqa: E501

        Creates a new folder under the given parent folder.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_folder(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param FolderDefinition body: Information about the new folder. (required)
        :param str is_admin_mode: Set this to \"true\" if you want to perform the request as a Content Administrator.
        :return: Folder
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_folder_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.create_folder_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def create_folder_with_http_info(self, body, **kwargs):  # noqa: E501
        """Create a new folder.  # noqa: E501

        Creates a new folder under the given parent folder.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_folder_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param FolderDefinition body: Information about the new folder. (required)
        :param str is_admin_mode: Set this to \"true\" if you want to perform the request as a Content Administrator.
        :return: Folder
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'is_admin_mode']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_folder" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `create_folder`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

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
            '/v2/content/folders', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Folder',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_admin_recommended_folder_async(self, **kwargs):  # noqa: E501
        """Get Admin Recommended folder.  # noqa: E501

        Schedule an asynchronous job to get the top-level Admin Recommended content items.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_admin_recommended_folder_async(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str is_admin_mode: Set this to \"true\" if you want to perform the request as a Content Administrator.
        :return: BeginAsyncJobResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_admin_recommended_folder_async_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_admin_recommended_folder_async_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_admin_recommended_folder_async_with_http_info(self, **kwargs):  # noqa: E501
        """Get Admin Recommended folder.  # noqa: E501

        Schedule an asynchronous job to get the top-level Admin Recommended content items.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_admin_recommended_folder_async_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str is_admin_mode: Set this to \"true\" if you want to perform the request as a Content Administrator.
        :return: BeginAsyncJobResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['is_admin_mode']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_admin_recommended_folder_async" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

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
            '/v2/content/folders/adminRecommended', 'GET',
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

    def get_admin_recommended_folder_async_result(self, job_id, **kwargs):  # noqa: E501
        """Admin Recommended folder job result.  # noqa: E501

        Get results from Admin Recommended job for the given job identifier.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_admin_recommended_folder_async_result(job_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str job_id: The identifier of the asynchronous Admin Recommended folder job. (required)
        :return: Folder
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_admin_recommended_folder_async_result_with_http_info(job_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_admin_recommended_folder_async_result_with_http_info(job_id, **kwargs)  # noqa: E501
            return data

    def get_admin_recommended_folder_async_result_with_http_info(self, job_id, **kwargs):  # noqa: E501
        """Admin Recommended folder job result.  # noqa: E501

        Get results from Admin Recommended job for the given job identifier.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_admin_recommended_folder_async_result_with_http_info(job_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str job_id: The identifier of the asynchronous Admin Recommended folder job. (required)
        :return: Folder
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['job_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_admin_recommended_folder_async_result" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'job_id' is set
        if ('job_id' not in params or
                params['job_id'] is None):
            raise ValueError("Missing the required parameter `job_id` when calling `get_admin_recommended_folder_async_result`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'job_id' in params:
            path_params['jobId'] = params['job_id']  # noqa: E501

        query_params = []

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
            '/v2/content/folders/adminRecommended/{jobId}/result', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Folder',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_admin_recommended_folder_async_status(self, job_id, **kwargs):  # noqa: E501
        """Admin Recommended folder job status.  # noqa: E501

        Get the status of an asynchronous Admin Recommended folder job for the given job identifier.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_admin_recommended_folder_async_status(job_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str job_id: The identifier of the asynchronous Admin Recommended folder job. (required)
        :return: AsyncJobStatus
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_admin_recommended_folder_async_status_with_http_info(job_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_admin_recommended_folder_async_status_with_http_info(job_id, **kwargs)  # noqa: E501
            return data

    def get_admin_recommended_folder_async_status_with_http_info(self, job_id, **kwargs):  # noqa: E501
        """Admin Recommended folder job status.  # noqa: E501

        Get the status of an asynchronous Admin Recommended folder job for the given job identifier.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_admin_recommended_folder_async_status_with_http_info(job_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str job_id: The identifier of the asynchronous Admin Recommended folder job. (required)
        :return: AsyncJobStatus
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['job_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_admin_recommended_folder_async_status" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'job_id' is set
        if ('job_id' not in params or
                params['job_id'] is None):
            raise ValueError("Missing the required parameter `job_id` when calling `get_admin_recommended_folder_async_status`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'job_id' in params:
            path_params['jobId'] = params['job_id']  # noqa: E501

        query_params = []

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
            '/v2/content/folders/adminRecommended/{jobId}/status', 'GET',
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

    def get_folder(self, id, **kwargs):  # noqa: E501
        """Get a folder.  # noqa: E501

        Get a folder with the given identifier.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_folder(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Identifier of the folder to fetch. (required)
        :param str is_admin_mode: Set this to \"true\" if you want to perform the request as a Content Administrator.
        :return: Folder
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_folder_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_folder_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def get_folder_with_http_info(self, id, **kwargs):  # noqa: E501
        """Get a folder.  # noqa: E501

        Get a folder with the given identifier.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_folder_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Identifier of the folder to fetch. (required)
        :param str is_admin_mode: Set this to \"true\" if you want to perform the request as a Content Administrator.
        :return: Folder
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
                    " to method get_folder" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `get_folder`")  # noqa: E501

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
            '/v2/content/folders/{id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Folder',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_global_folder_async(self, **kwargs):  # noqa: E501
        """Get global folder.  # noqa: E501

        Schedule an asynchronous job to get global folder. Global folder contains all content items that a user has permissions to view in the organization.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_global_folder_async(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str is_admin_mode: Set this to \"true\" if you want to perform the request as a Content Administrator.
        :return: BeginAsyncJobResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_global_folder_async_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_global_folder_async_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_global_folder_async_with_http_info(self, **kwargs):  # noqa: E501
        """Get global folder.  # noqa: E501

        Schedule an asynchronous job to get global folder. Global folder contains all content items that a user has permissions to view in the organization.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_global_folder_async_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str is_admin_mode: Set this to \"true\" if you want to perform the request as a Content Administrator.
        :return: BeginAsyncJobResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['is_admin_mode']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_global_folder_async" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

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
            '/v2/content/folders/global', 'GET',
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

    def get_global_folder_async_result(self, job_id, **kwargs):  # noqa: E501
        """Global folder job result.  # noqa: E501

        Get results from global folder job for the given job identifier.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_global_folder_async_result(job_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str job_id: The identifier of the asynchronous global folder job. (required)
        :return: ContentList
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_global_folder_async_result_with_http_info(job_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_global_folder_async_result_with_http_info(job_id, **kwargs)  # noqa: E501
            return data

    def get_global_folder_async_result_with_http_info(self, job_id, **kwargs):  # noqa: E501
        """Global folder job result.  # noqa: E501

        Get results from global folder job for the given job identifier.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_global_folder_async_result_with_http_info(job_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str job_id: The identifier of the asynchronous global folder job. (required)
        :return: ContentList
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['job_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_global_folder_async_result" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'job_id' is set
        if ('job_id' not in params or
                params['job_id'] is None):
            raise ValueError("Missing the required parameter `job_id` when calling `get_global_folder_async_result`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'job_id' in params:
            path_params['jobId'] = params['job_id']  # noqa: E501

        query_params = []

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
            '/v2/content/folders/global/{jobId}/result', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ContentList',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_global_folder_async_status(self, job_id, **kwargs):  # noqa: E501
        """Global folder job status.  # noqa: E501

        Get the status of an asynchronous global folder job for the given job identifier.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_global_folder_async_status(job_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str job_id: The identifier of the asynchronous global folder job. (required)
        :return: AsyncJobStatus
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_global_folder_async_status_with_http_info(job_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_global_folder_async_status_with_http_info(job_id, **kwargs)  # noqa: E501
            return data

    def get_global_folder_async_status_with_http_info(self, job_id, **kwargs):  # noqa: E501
        """Global folder job status.  # noqa: E501

        Get the status of an asynchronous global folder job for the given job identifier.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_global_folder_async_status_with_http_info(job_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str job_id: The identifier of the asynchronous global folder job. (required)
        :return: AsyncJobStatus
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['job_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_global_folder_async_status" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'job_id' is set
        if ('job_id' not in params or
                params['job_id'] is None):
            raise ValueError("Missing the required parameter `job_id` when calling `get_global_folder_async_status`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'job_id' in params:
            path_params['jobId'] = params['job_id']  # noqa: E501

        query_params = []

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
            '/v2/content/folders/global/{jobId}/status', 'GET',
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

    def get_personal_folder(self, **kwargs):  # noqa: E501
        """Get personal folder.  # noqa: E501

        Get the personal folder of the current user.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_personal_folder(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: Folder
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_personal_folder_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_personal_folder_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_personal_folder_with_http_info(self, **kwargs):  # noqa: E501
        """Get personal folder.  # noqa: E501

        Get the personal folder of the current user.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_personal_folder_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: Folder
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_personal_folder" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

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
            '/v2/content/folders/personal', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Folder',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_folder(self, body, id, **kwargs):  # noqa: E501
        """Update a folder.  # noqa: E501

        Update an existing folder with the given identifier.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_folder(body, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param UpdateFolderRequest body: Information to update about the folder. (required)
        :param str id: Identifier of the folder to update. (required)
        :param str is_admin_mode: Set this to \"true\" if you want to perform the request as a Content Administrator.
        :return: Folder
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_folder_with_http_info(body, id, **kwargs)  # noqa: E501
        else:
            (data) = self.update_folder_with_http_info(body, id, **kwargs)  # noqa: E501
            return data

    def update_folder_with_http_info(self, body, id, **kwargs):  # noqa: E501
        """Update a folder.  # noqa: E501

        Update an existing folder with the given identifier.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_folder_with_http_info(body, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param UpdateFolderRequest body: Information to update about the folder. (required)
        :param str id: Identifier of the folder to update. (required)
        :param str is_admin_mode: Set this to \"true\" if you want to perform the request as a Content Administrator.
        :return: Folder
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'id', 'is_admin_mode']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_folder" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `update_folder`")  # noqa: E501
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `update_folder`")  # noqa: E501

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
            '/v2/content/folders/{id}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Folder',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
