# openapi_client.FileUploadApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**file_upload_file_upload_post**](FileUploadApi.md#file_upload_file_upload_post) | **POST** /file-upload | File Upload


# **file_upload_file_upload_post**
> bool, date, datetime, dict, float, int, list, str, none_type file_upload_file_upload_post(files)

File Upload

### Example


```python
import time
import openapi_client
from openapi_client.api import file_upload_api
from openapi_client.model.http_validation_error import HTTPValidationError
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = file_upload_api.FileUploadApi(api_client)
    files = [
        open('/path/to/file', 'rb'),
    ] # [file_type] | 
    meta = "null" # str |  (optional) if omitted the server will use the default value of "null"
    remove_numeric_tables = None # bool, date, datetime, dict, float, int, list, str, none_type |  (optional)
    valid_languages = None # bool, date, datetime, dict, float, int, list, str, none_type |  (optional)
    clean_whitespace = None # bool, date, datetime, dict, float, int, list, str, none_type |  (optional)
    clean_empty_lines = None # bool, date, datetime, dict, float, int, list, str, none_type |  (optional)
    clean_header_footer = None # bool, date, datetime, dict, float, int, list, str, none_type |  (optional)
    split_by = None # bool, date, datetime, dict, float, int, list, str, none_type |  (optional)
    split_length = None # bool, date, datetime, dict, float, int, list, str, none_type |  (optional)
    split_overlap = None # bool, date, datetime, dict, float, int, list, str, none_type |  (optional)
    split_respect_sentence_boundary = None # bool, date, datetime, dict, float, int, list, str, none_type |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # File Upload
        api_response = api_instance.file_upload_file_upload_post(files)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling FileUploadApi->file_upload_file_upload_post: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # File Upload
        api_response = api_instance.file_upload_file_upload_post(files, meta=meta, remove_numeric_tables=remove_numeric_tables, valid_languages=valid_languages, clean_whitespace=clean_whitespace, clean_empty_lines=clean_empty_lines, clean_header_footer=clean_header_footer, split_by=split_by, split_length=split_length, split_overlap=split_overlap, split_respect_sentence_boundary=split_respect_sentence_boundary)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling FileUploadApi->file_upload_file_upload_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **files** | **[file_type]**|  |
 **meta** | **str**|  | [optional] if omitted the server will use the default value of "null"
 **remove_numeric_tables** | **bool, date, datetime, dict, float, int, list, str, none_type**|  | [optional]
 **valid_languages** | **bool, date, datetime, dict, float, int, list, str, none_type**|  | [optional]
 **clean_whitespace** | **bool, date, datetime, dict, float, int, list, str, none_type**|  | [optional]
 **clean_empty_lines** | **bool, date, datetime, dict, float, int, list, str, none_type**|  | [optional]
 **clean_header_footer** | **bool, date, datetime, dict, float, int, list, str, none_type**|  | [optional]
 **split_by** | **bool, date, datetime, dict, float, int, list, str, none_type**|  | [optional]
 **split_length** | **bool, date, datetime, dict, float, int, list, str, none_type**|  | [optional]
 **split_overlap** | **bool, date, datetime, dict, float, int, list, str, none_type**|  | [optional]
 **split_respect_sentence_boundary** | **bool, date, datetime, dict, float, int, list, str, none_type**|  | [optional]

### Return type

**bool, date, datetime, dict, float, int, list, str, none_type**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

