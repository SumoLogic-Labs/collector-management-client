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


class RulesLibraryManagementApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_rules_full_path(self, id, **kwargs):  # noqa: E501
        """Get the path of a cloud SIEM folder or rule.  # noqa: E501

        Get the full path of folder or rule in the cloud SIEM rules library.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_rules_full_path(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Identifier of the cloud SIEM folder or rule. (required)
        :return: Path
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_rules_full_path_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_rules_full_path_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def get_rules_full_path_with_http_info(self, id, **kwargs):  # noqa: E501
        """Get the path of a cloud SIEM folder or rule.  # noqa: E501

        Get the full path of folder or rule in the cloud SIEM rules library.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_rules_full_path_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Identifier of the cloud SIEM folder or rule. (required)
        :return: Path
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_rules_full_path" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `get_rules_full_path`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

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
            '/v1/rules/{id}/path', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Path',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_rules_library_root(self, **kwargs):  # noqa: E501
        """Get the root cloud SIEM rules folder.  # noqa: E501

        Get the root folder in the cloud SIEM rules library.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_rules_library_root(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: RulesLibraryFolderResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_rules_library_root_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_rules_library_root_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_rules_library_root_with_http_info(self, **kwargs):  # noqa: E501
        """Get the root cloud SIEM rules folder.  # noqa: E501

        Get the root folder in the cloud SIEM rules library.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_rules_library_root_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: RulesLibraryFolderResponse
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
                    " to method get_rules_library_root" % key
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
            '/v1/rules/root', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='RulesLibraryFolderResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def rules_copy(self, body, id, **kwargs):  # noqa: E501
        """Copy a cloud SIEM folder or rule.  # noqa: E501

        Copy a folder or rule in the cloud SIEM rules library.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.rules_copy(body, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ContentCopyParams body: Fields include:
  1) Identifier of the parent folder to copy to.
  2) Optionally provide a new name.
  3) Optionally provide a new description.
  4) Optionally set to true if you want to copy and preserved the locked status. Requires `LockRules` capability. (required)
        :param str id: Identifier of the cloud SIEM folder or rule to copy. (required)
        :return: RulesLibraryBaseResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.rules_copy_with_http_info(body, id, **kwargs)  # noqa: E501
        else:
            (data) = self.rules_copy_with_http_info(body, id, **kwargs)  # noqa: E501
            return data

    def rules_copy_with_http_info(self, body, id, **kwargs):  # noqa: E501
        """Copy a cloud SIEM folder or rule.  # noqa: E501

        Copy a folder or rule in the cloud SIEM rules library.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.rules_copy_with_http_info(body, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ContentCopyParams body: Fields include:
  1) Identifier of the parent folder to copy to.
  2) Optionally provide a new name.
  3) Optionally provide a new description.
  4) Optionally set to true if you want to copy and preserved the locked status. Requires `LockRules` capability. (required)
        :param str id: Identifier of the cloud SIEM folder or rule to copy. (required)
        :return: RulesLibraryBaseResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method rules_copy" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `rules_copy`")  # noqa: E501
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `rules_copy`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}

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
            '/v1/rules/{id}/copy', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='RulesLibraryBaseResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def rules_create(self, body, parent_id, **kwargs):  # noqa: E501
        """Create a cloud SIEM folder or rule.   # noqa: E501

        Create a folder or rule in the cloud SIEM rules library.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.rules_create(body, parent_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param RulesLibraryBase body: The cloud SIEM folder or rule to create. (required)
        :param str parent_id: Identifier of the parent folder in which to create the cloud SIEM folder or rule. (required)
        :return: RulesLibraryBaseResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.rules_create_with_http_info(body, parent_id, **kwargs)  # noqa: E501
        else:
            (data) = self.rules_create_with_http_info(body, parent_id, **kwargs)  # noqa: E501
            return data

    def rules_create_with_http_info(self, body, parent_id, **kwargs):  # noqa: E501
        """Create a cloud SIEM folder or rule.   # noqa: E501

        Create a folder or rule in the cloud SIEM rules library.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.rules_create_with_http_info(body, parent_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param RulesLibraryBase body: The cloud SIEM folder or rule to create. (required)
        :param str parent_id: Identifier of the parent folder in which to create the cloud SIEM folder or rule. (required)
        :return: RulesLibraryBaseResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'parent_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method rules_create" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `rules_create`")  # noqa: E501
        # verify the required parameter 'parent_id' is set
        if ('parent_id' not in params or
                params['parent_id'] is None):
            raise ValueError("Missing the required parameter `parent_id` when calling `rules_create`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'parent_id' in params:
            query_params.append(('parentId', params['parent_id']))  # noqa: E501

        header_params = {}

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
            '/v1/rules', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='RulesLibraryBaseResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def rules_delete_by_id(self, id, **kwargs):  # noqa: E501
        """Delete a cloud SIEM folder or rule.   # noqa: E501

        Delete a folder or rule from the cloud SIEM rules library.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.rules_delete_by_id(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Identifier of the cloud SIEM folder or rule to delete. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.rules_delete_by_id_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.rules_delete_by_id_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def rules_delete_by_id_with_http_info(self, id, **kwargs):  # noqa: E501
        """Delete a cloud SIEM folder or rule.   # noqa: E501

        Delete a folder or rule from the cloud SIEM rules library.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.rules_delete_by_id_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Identifier of the cloud SIEM folder or rule to delete. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method rules_delete_by_id" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `rules_delete_by_id`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

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
            '/v1/rules/{id}', 'DELETE',
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

    def rules_delete_by_ids(self, ids, **kwargs):  # noqa: E501
        """Bulk delete cloud SIEM folders and rules.   # noqa: E501

        Bulk delete folders and rules by the given identifiers in the cloud SIEM rules library.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.rules_delete_by_ids(ids, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param list[str] ids: A comma-separated list of identifiers. (required)
        :return: IdToRulesLibraryBaseResponseMap
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.rules_delete_by_ids_with_http_info(ids, **kwargs)  # noqa: E501
        else:
            (data) = self.rules_delete_by_ids_with_http_info(ids, **kwargs)  # noqa: E501
            return data

    def rules_delete_by_ids_with_http_info(self, ids, **kwargs):  # noqa: E501
        """Bulk delete cloud SIEM folders and rules.   # noqa: E501

        Bulk delete folders and rules by the given identifiers in the cloud SIEM rules library.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.rules_delete_by_ids_with_http_info(ids, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param list[str] ids: A comma-separated list of identifiers. (required)
        :return: IdToRulesLibraryBaseResponseMap
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['ids']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method rules_delete_by_ids" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'ids' is set
        if ('ids' not in params or
                params['ids'] is None):
            raise ValueError("Missing the required parameter `ids` when calling `rules_delete_by_ids`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'ids' in params:
            query_params.append(('ids', params['ids']))  # noqa: E501
            collection_formats['ids'] = 'multi'  # noqa: E501

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
            '/v1/rules', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='IdToRulesLibraryBaseResponseMap',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def rules_export_item(self, id, **kwargs):  # noqa: E501
        """Export a folder or rule.  # noqa: E501

        Export a folder or rule. If the given identifier is a folder, everything under the folder is exported recursively with folder as the root.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.rules_export_item(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Identifier of the folder or rule to export. (required)
        :param bool preserve_lock: Set this to true if you want to export an object and preserve the locked status. 
        :return: RulesLibraryExportBase
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.rules_export_item_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.rules_export_item_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def rules_export_item_with_http_info(self, id, **kwargs):  # noqa: E501
        """Export a folder or rule.  # noqa: E501

        Export a folder or rule. If the given identifier is a folder, everything under the folder is exported recursively with folder as the root.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.rules_export_item_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Identifier of the folder or rule to export. (required)
        :param bool preserve_lock: Set this to true if you want to export an object and preserve the locked status. 
        :return: RulesLibraryExportBase
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'preserve_lock']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method rules_export_item" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `rules_export_item`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []
        if 'preserve_lock' in params:
            query_params.append(('preserveLock', params['preserve_lock']))  # noqa: E501

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
            '/v1/rules/{id}/export', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='RulesLibraryExportBase',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def rules_get_by_path(self, path, **kwargs):  # noqa: E501
        """Read a folder or rule by its path.  # noqa: E501

        Read a folder or rule by its path in the rules library structure.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.rules_get_by_path(path, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str path: The path of the folder or rule. (required)
        :return: RulesLibraryBaseResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.rules_get_by_path_with_http_info(path, **kwargs)  # noqa: E501
        else:
            (data) = self.rules_get_by_path_with_http_info(path, **kwargs)  # noqa: E501
            return data

    def rules_get_by_path_with_http_info(self, path, **kwargs):  # noqa: E501
        """Read a folder or rule by its path.  # noqa: E501

        Read a folder or rule by its path in the rules library structure.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.rules_get_by_path_with_http_info(path, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str path: The path of the folder or rule. (required)
        :return: RulesLibraryBaseResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['path']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method rules_get_by_path" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'path' is set
        if ('path' not in params or
                params['path'] is None):
            raise ValueError("Missing the required parameter `path` when calling `rules_get_by_path`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'path' in params:
            query_params.append(('path', params['path']))  # noqa: E501

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
            '/v1/rules/path', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='RulesLibraryBaseResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def rules_import_item(self, body, parent_id, **kwargs):  # noqa: E501
        """Import a folder or rule.  # noqa: E501

        Import a folder or rule.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.rules_import_item(body, parent_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param RulesLibraryExportBase body: The folder or rule to be imported. (required)
        :param str parent_id: Identifier of the parent folder in which to import the folder or rule. (required)
        :return: RulesLibraryBaseResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.rules_import_item_with_http_info(body, parent_id, **kwargs)  # noqa: E501
        else:
            (data) = self.rules_import_item_with_http_info(body, parent_id, **kwargs)  # noqa: E501
            return data

    def rules_import_item_with_http_info(self, body, parent_id, **kwargs):  # noqa: E501
        """Import a folder or rule.  # noqa: E501

        Import a folder or rule.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.rules_import_item_with_http_info(body, parent_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param RulesLibraryExportBase body: The folder or rule to be imported. (required)
        :param str parent_id: Identifier of the parent folder in which to import the folder or rule. (required)
        :return: RulesLibraryBaseResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'parent_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method rules_import_item" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `rules_import_item`")  # noqa: E501
        # verify the required parameter 'parent_id' is set
        if ('parent_id' not in params or
                params['parent_id'] is None):
            raise ValueError("Missing the required parameter `parent_id` when calling `rules_import_item`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'parent_id' in params:
            path_params['parentId'] = params['parent_id']  # noqa: E501

        query_params = []

        header_params = {}

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
            '/v1/rules/{parentId}/import', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='RulesLibraryBaseResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def rules_lock_by_id(self, id, **kwargs):  # noqa: E501
        """Lock a folder or rule.  # noqa: E501

        Locking requires the `LockRules` capability. When an object is locked, it can't be moved or deleted and only the local fields can be modified. Locking recursively locks all of the objects children.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.rules_lock_by_id(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: The id of the folder or rule that needs to be locked. (required)
        :return: RulesLibraryBaseResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.rules_lock_by_id_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.rules_lock_by_id_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def rules_lock_by_id_with_http_info(self, id, **kwargs):  # noqa: E501
        """Lock a folder or rule.  # noqa: E501

        Locking requires the `LockRules` capability. When an object is locked, it can't be moved or deleted and only the local fields can be modified. Locking recursively locks all of the objects children.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.rules_lock_by_id_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: The id of the folder or rule that needs to be locked. (required)
        :return: RulesLibraryBaseResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method rules_lock_by_id" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `rules_lock_by_id`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

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
            '/v1/rules/{id}/lock', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='RulesLibraryBaseResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def rules_move(self, id, parent_id, **kwargs):  # noqa: E501
        """Move a cloud SIEM folder or rule.  # noqa: E501

        Move a folder or rule to a different location in the cloud SIEM rules library.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.rules_move(id, parent_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Identifier of the folder or rule to move. (required)
        :param str parent_id: Identifier of the parent folder to move the folder or rule to. (required)
        :return: RulesLibraryBaseResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.rules_move_with_http_info(id, parent_id, **kwargs)  # noqa: E501
        else:
            (data) = self.rules_move_with_http_info(id, parent_id, **kwargs)  # noqa: E501
            return data

    def rules_move_with_http_info(self, id, parent_id, **kwargs):  # noqa: E501
        """Move a cloud SIEM folder or rule.  # noqa: E501

        Move a folder or rule to a different location in the cloud SIEM rules library.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.rules_move_with_http_info(id, parent_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Identifier of the folder or rule to move. (required)
        :param str parent_id: Identifier of the parent folder to move the folder or rule to. (required)
        :return: RulesLibraryBaseResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'parent_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method rules_move" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `rules_move`")  # noqa: E501
        # verify the required parameter 'parent_id' is set
        if ('parent_id' not in params or
                params['parent_id'] is None):
            raise ValueError("Missing the required parameter `parent_id` when calling `rules_move`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []
        if 'parent_id' in params:
            query_params.append(('parentId', params['parent_id']))  # noqa: E501

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
            '/v1/rules/{id}/move', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='RulesLibraryBaseResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def rules_read_by_id(self, id, **kwargs):  # noqa: E501
        """Get a cloud SIEM folder or rule.  # noqa: E501

        Get a folder or rule from the cloud SIEM rules library.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.rules_read_by_id(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Identifier of the cloud SIEM folder or rule to read. (required)
        :return: RulesLibraryBaseResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.rules_read_by_id_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.rules_read_by_id_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def rules_read_by_id_with_http_info(self, id, **kwargs):  # noqa: E501
        """Get a cloud SIEM folder or rule.  # noqa: E501

        Get a folder or rule from the cloud SIEM rules library.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.rules_read_by_id_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Identifier of the cloud SIEM folder or rule to read. (required)
        :return: RulesLibraryBaseResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method rules_read_by_id" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `rules_read_by_id`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

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
            '/v1/rules/{id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='RulesLibraryBaseResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def rules_read_by_ids(self, ids, **kwargs):  # noqa: E501
        """Bulk read cloud SIEM folders and rules.  # noqa: E501

        Bulk read folders and rules by the given identifiers from the cloud SIEM rules library.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.rules_read_by_ids(ids, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param list[str] ids: A comma-separated list of identifiers. (required)
        :return: IdToRulesLibraryBaseResponseMap
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.rules_read_by_ids_with_http_info(ids, **kwargs)  # noqa: E501
        else:
            (data) = self.rules_read_by_ids_with_http_info(ids, **kwargs)  # noqa: E501
            return data

    def rules_read_by_ids_with_http_info(self, ids, **kwargs):  # noqa: E501
        """Bulk read cloud SIEM folders and rules.  # noqa: E501

        Bulk read folders and rules by the given identifiers from the cloud SIEM rules library.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.rules_read_by_ids_with_http_info(ids, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param list[str] ids: A comma-separated list of identifiers. (required)
        :return: IdToRulesLibraryBaseResponseMap
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['ids']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method rules_read_by_ids" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'ids' is set
        if ('ids' not in params or
                params['ids'] is None):
            raise ValueError("Missing the required parameter `ids` when calling `rules_read_by_ids`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'ids' in params:
            query_params.append(('ids', params['ids']))  # noqa: E501
            collection_formats['ids'] = 'multi'  # noqa: E501

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
            '/v1/rules', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='IdToRulesLibraryBaseResponseMap',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def rules_read_by_path(self, path, **kwargs):  # noqa: E501
        """Get a cloud SIEM folder or rule by its path.  # noqa: E501

        Get a folder or rule by its path in the cloud SIEM rules library structure.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.rules_read_by_path(path, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str path: The path of the cloud SIEM folder or rule. (required)
        :return: RulesLibraryBaseResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.rules_read_by_path_with_http_info(path, **kwargs)  # noqa: E501
        else:
            (data) = self.rules_read_by_path_with_http_info(path, **kwargs)  # noqa: E501
            return data

    def rules_read_by_path_with_http_info(self, path, **kwargs):  # noqa: E501
        """Get a cloud SIEM folder or rule by its path.  # noqa: E501

        Get a folder or rule by its path in the cloud SIEM rules library structure.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.rules_read_by_path_with_http_info(path, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str path: The path of the cloud SIEM folder or rule. (required)
        :return: RulesLibraryBaseResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['path']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method rules_read_by_path" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'path' is set
        if ('path' not in params or
                params['path'] is None):
            raise ValueError("Missing the required parameter `path` when calling `rules_read_by_path`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'path' in params:
            query_params.append(('path', params['path']))  # noqa: E501

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
            '/v1/rules/search', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='RulesLibraryBaseResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def rules_unlock_by_id(self, id, **kwargs):  # noqa: E501
        """Unlock a folder or rule.  # noqa: E501

        Unlocking requires the `LockRules` capability. It is only possible to unlock the highest locked object in a tree of locked objects. Unlocking recursively unlocks all of the objects children.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.rules_unlock_by_id(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: The id of the folder or rule that needs to be unlocked. (required)
        :return: RulesLibraryBaseResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.rules_unlock_by_id_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.rules_unlock_by_id_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def rules_unlock_by_id_with_http_info(self, id, **kwargs):  # noqa: E501
        """Unlock a folder or rule.  # noqa: E501

        Unlocking requires the `LockRules` capability. It is only possible to unlock the highest locked object in a tree of locked objects. Unlocking recursively unlocks all of the objects children.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.rules_unlock_by_id_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: The id of the folder or rule that needs to be unlocked. (required)
        :return: RulesLibraryBaseResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method rules_unlock_by_id" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `rules_unlock_by_id`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

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
            '/v1/rules/{id}/unlock', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='RulesLibraryBaseResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def rules_update_by_id(self, body, id, **kwargs):  # noqa: E501
        """Update a cloud SIEM folder or rule.   # noqa: E501

        Update a folder or rule in the cloud SIEM rules library.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.rules_update_by_id(body, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param RulesLibraryBaseUpdate body: The folder or rule to update. The content version must match its latest version number in the cloud SIEM rules library. If the version does not match it will not be updated. (required)
        :param str id: Identifier of the cloud SIEM folder or rule to update. (required)
        :return: RulesLibraryBaseResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.rules_update_by_id_with_http_info(body, id, **kwargs)  # noqa: E501
        else:
            (data) = self.rules_update_by_id_with_http_info(body, id, **kwargs)  # noqa: E501
            return data

    def rules_update_by_id_with_http_info(self, body, id, **kwargs):  # noqa: E501
        """Update a cloud SIEM folder or rule.   # noqa: E501

        Update a folder or rule in the cloud SIEM rules library.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.rules_update_by_id_with_http_info(body, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param RulesLibraryBaseUpdate body: The folder or rule to update. The content version must match its latest version number in the cloud SIEM rules library. If the version does not match it will not be updated. (required)
        :param str id: Identifier of the cloud SIEM folder or rule to update. (required)
        :return: RulesLibraryBaseResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method rules_update_by_id" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `rules_update_by_id`")  # noqa: E501
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `rules_update_by_id`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}

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
            '/v1/rules/{id}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='RulesLibraryBaseResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
