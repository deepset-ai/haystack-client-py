"""
    Haystack-API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 0.1
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from openapi_client.api_client import ApiClient, Endpoint as _Endpoint
from openapi_client.model_utils import (  # noqa: F401
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types
)
from openapi_client.model.http_validation_error import HTTPValidationError


class FileUploadApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.upload_file_endpoint = _Endpoint(
            settings={
                'response_type': (bool, date, datetime, dict, float, int, list, str, none_type,),
                'auth': [],
                'endpoint_path': '/file-upload',
                'operation_id': 'upload_file',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'files',
                    'meta',
                    'remove_numeric_tables',
                    'valid_languages',
                    'clean_whitespace',
                    'clean_empty_lines',
                    'clean_header_footer',
                    'split_by',
                    'split_length',
                    'split_overlap',
                    'split_respect_sentence_boundary',
                ],
                'required': [
                    'files',
                ],
                'nullable': [
                    'remove_numeric_tables',
                    'valid_languages',
                    'clean_whitespace',
                    'clean_empty_lines',
                    'clean_header_footer',
                    'split_by',
                    'split_length',
                    'split_overlap',
                    'split_respect_sentence_boundary',
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'files':
                        ([file_type],),
                    'meta':
                        (str,),
                    'remove_numeric_tables':
                        (bool, date, datetime, dict, float, int, list, str, none_type,),
                    'valid_languages':
                        (bool, date, datetime, dict, float, int, list, str, none_type,),
                    'clean_whitespace':
                        (bool, date, datetime, dict, float, int, list, str, none_type,),
                    'clean_empty_lines':
                        (bool, date, datetime, dict, float, int, list, str, none_type,),
                    'clean_header_footer':
                        (bool, date, datetime, dict, float, int, list, str, none_type,),
                    'split_by':
                        (bool, date, datetime, dict, float, int, list, str, none_type,),
                    'split_length':
                        (bool, date, datetime, dict, float, int, list, str, none_type,),
                    'split_overlap':
                        (bool, date, datetime, dict, float, int, list, str, none_type,),
                    'split_respect_sentence_boundary':
                        (bool, date, datetime, dict, float, int, list, str, none_type,),
                },
                'attribute_map': {
                    'files': 'files',
                    'meta': 'meta',
                    'remove_numeric_tables': 'remove_numeric_tables',
                    'valid_languages': 'valid_languages',
                    'clean_whitespace': 'clean_whitespace',
                    'clean_empty_lines': 'clean_empty_lines',
                    'clean_header_footer': 'clean_header_footer',
                    'split_by': 'split_by',
                    'split_length': 'split_length',
                    'split_overlap': 'split_overlap',
                    'split_respect_sentence_boundary': 'split_respect_sentence_boundary',
                },
                'location_map': {
                    'files': 'form',
                    'meta': 'form',
                    'remove_numeric_tables': 'form',
                    'valid_languages': 'form',
                    'clean_whitespace': 'form',
                    'clean_empty_lines': 'form',
                    'clean_header_footer': 'form',
                    'split_by': 'form',
                    'split_length': 'form',
                    'split_overlap': 'form',
                    'split_respect_sentence_boundary': 'form',
                },
                'collection_format_map': {
                    'files': 'csv',
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'multipart/form-data'
                ]
            },
            api_client=api_client
        )

    def upload_file(
        self,
        files,
        **kwargs
    ):
        """File Upload  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.upload_file(files, async_req=True)
        >>> result = thread.get()

        Args:
            files ([file_type]):

        Keyword Args:
            meta (str): [optional] if omitted the server will use the default value of "null"
            remove_numeric_tables (bool, date, datetime, dict, float, int, list, str, none_type): [optional]
            valid_languages (bool, date, datetime, dict, float, int, list, str, none_type): [optional]
            clean_whitespace (bool, date, datetime, dict, float, int, list, str, none_type): [optional]
            clean_empty_lines (bool, date, datetime, dict, float, int, list, str, none_type): [optional]
            clean_header_footer (bool, date, datetime, dict, float, int, list, str, none_type): [optional]
            split_by (bool, date, datetime, dict, float, int, list, str, none_type): [optional]
            split_length (bool, date, datetime, dict, float, int, list, str, none_type): [optional]
            split_overlap (bool, date, datetime, dict, float, int, list, str, none_type): [optional]
            split_respect_sentence_boundary (bool, date, datetime, dict, float, int, list, str, none_type): [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            bool, date, datetime, dict, float, int, list, str, none_type
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['files'] = \
            files
        return self.upload_file_endpoint.call_with_http_info(**kwargs)

