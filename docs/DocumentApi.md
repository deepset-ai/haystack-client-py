# openapi_client.DocumentApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_documents**](DocumentApi.md#delete_documents) | **POST** /documents/delete_by_filters | Delete Documents By Filter
[**get_documents**](DocumentApi.md#get_documents) | **POST** /documents/get_by_filters | Get Documents By Filter


# **delete_documents**
> bool delete_documents(filter_request)

Delete Documents By Filter

Can be used to delete documents from a document store.  :param filters: Filters to narrow down the documents to delete.                 Example: '{\"filters\": {{\"name\": [\"some\", \"more\"], \"category\": [\"only_one\"]}}'                 To delete all documents you should provide an empty dict, like:                 '{\"filters\": {}}'

### Example


```python
import time
import openapi_client
from openapi_client.api import document_api
from openapi_client.model.filter_request import FilterRequest
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
    api_instance = document_api.DocumentApi(api_client)
    filter_request = FilterRequest(
        filters={
            "key": None,
        },
    ) # FilterRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Delete Documents By Filter
        api_response = api_instance.delete_documents(filter_request)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DocumentApi->delete_documents: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_request** | [**FilterRequest**](FilterRequest.md)|  |

### Return type

**bool**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_documents**
> [DocumentSerialized] get_documents(filter_request)

Get Documents By Filter

Can be used to get documents from a document store.  :param filters: Filters to narrow down the documents to delete.                 Example: '{\"filters\": {{\"name\": [\"some\", \"more\"], \"category\": [\"only_one\"]}}'                 To get all documents you should provide an empty dict, like:                 '{\"filters\": {}}'

### Example


```python
import time
import openapi_client
from openapi_client.api import document_api
from openapi_client.model.document_serialized import DocumentSerialized
from openapi_client.model.filter_request import FilterRequest
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
    api_instance = document_api.DocumentApi(api_client)
    filter_request = FilterRequest(
        filters={
            "key": None,
        },
    ) # FilterRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Get Documents By Filter
        api_response = api_instance.get_documents(filter_request)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DocumentApi->get_documents: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_request** | [**FilterRequest**](FilterRequest.md)|  |

### Return type

[**[DocumentSerialized]**](DocumentSerialized.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

