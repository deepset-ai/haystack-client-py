# openapi_client.SearchApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**check_status**](SearchApi.md#check_status) | **GET** /initialized | Initialized
[**query**](SearchApi.md#query) | **POST** /query | Query


# **check_status**
> bool, date, datetime, dict, float, int, list, str, none_type check_status()

Initialized

This endpoint can be used during startup to understand if the  server is ready to take any requests, or is still loading.  The recommended approach is to call this endpoint with a short timeout, like 500ms, and in case of no reply, consider the server busy.

### Example


```python
import time
import openapi_client
from openapi_client.api import search_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = search_api.SearchApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Initialized
        api_response = api_instance.check_status()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling SearchApi->check_status: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**bool, date, datetime, dict, float, int, list, str, none_type**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **query**
> QueryResponse query(query_request)

Query

### Example


```python
import time
import openapi_client
from openapi_client.api import search_api
from openapi_client.model.query_request import QueryRequest
from openapi_client.model.http_validation_error import HTTPValidationError
from openapi_client.model.query_response import QueryResponse
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = search_api.SearchApi(api_client)
    query_request = QueryRequest(
        query="query_example",
        params={},
    ) # QueryRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Query
        api_response = api_instance.query(query_request)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling SearchApi->query: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query_request** | [**QueryRequest**](QueryRequest.md)|  |

### Return type

[**QueryResponse**](QueryResponse.md)

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

