# openapi_client.FeedbackApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**export_feedback**](FeedbackApi.md#export_feedback) | **GET** /export-feedback | Export Extractive Qa Feedback
[**get_feedback**](FeedbackApi.md#get_feedback) | **GET** /feedback | User Feedback
[**get_feedback_metrics**](FeedbackApi.md#get_feedback_metrics) | **POST** /eval-feedback | Eval Extractive Qa Feedback
[**post_feedback**](FeedbackApi.md#post_feedback) | **POST** /feedback | User Feedback


# **export_feedback**
> bool, date, datetime, dict, float, int, list, str, none_type export_feedback()

Export Extractive Qa Feedback

SQuAD format JSON export for question/answer pairs that were marked as \"relevant\".  The context_size param can be used to limit response size for large documents.

### Example


```python
import time
import openapi_client
from openapi_client.api import feedback_api
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
    api_instance = feedback_api.FeedbackApi(api_client)
    context_size = 100000 # int |  (optional) if omitted the server will use the default value of 100000
    full_document_context = True # bool |  (optional) if omitted the server will use the default value of True
    only_positive_labels = False # bool |  (optional) if omitted the server will use the default value of False

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Export Extractive Qa Feedback
        api_response = api_instance.export_feedback(context_size=context_size, full_document_context=full_document_context, only_positive_labels=only_positive_labels)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling FeedbackApi->export_feedback: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **context_size** | **int**|  | [optional] if omitted the server will use the default value of 100000
 **full_document_context** | **bool**|  | [optional] if omitted the server will use the default value of True
 **only_positive_labels** | **bool**|  | [optional] if omitted the server will use the default value of False

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
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_feedback**
> bool, date, datetime, dict, float, int, list, str, none_type get_feedback()

User Feedback

### Example


```python
import time
import openapi_client
from openapi_client.api import feedback_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = feedback_api.FeedbackApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # User Feedback
        api_response = api_instance.get_feedback()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling FeedbackApi->get_feedback: %s\n" % e)
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

# **get_feedback_metrics**
> bool, date, datetime, dict, float, int, list, str, none_type get_feedback_metrics()

Eval Extractive Qa Feedback

Return basic accuracy metrics based on the user feedback. Which ratio of answers was correct? Which ratio of documents was correct? You can supply filters in the request to only use a certain subset of labels.  **Example:**      ```         | curl --location --request POST 'http://127.0.0.1:8000/eval-doc-qa-feedback'             | --header 'Content-Type: application/json'             | --data-raw '{ \"filters\": {\"document_id\": [\"XRR3xnEBCYVTkbTystOB\"]} }'

### Example


```python
import time
import openapi_client
from openapi_client.api import feedback_api
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
    api_instance = feedback_api.FeedbackApi(api_client)
    filter_request = FilterRequest(
        filters={
            "key": None,
        },
    ) # FilterRequest |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Eval Extractive Qa Feedback
        api_response = api_instance.get_feedback_metrics(filter_request=filter_request)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling FeedbackApi->get_feedback_metrics: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_request** | [**FilterRequest**](FilterRequest.md)|  | [optional]

### Return type

**bool, date, datetime, dict, float, int, list, str, none_type**

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

# **post_feedback**
> bool, date, datetime, dict, float, int, list, str, none_type post_feedback(label_serialized)

User Feedback

### Example


```python
import time
import openapi_client
from openapi_client.api import feedback_api
from openapi_client.model.label_serialized import LabelSerialized
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
    api_instance = feedback_api.FeedbackApi(api_client)
    label_serialized = LabelSerialized(
        id="id_example",
        query="query_example",
        document=DocumentSerialized(
            content="content_example",
            content_type="text",
            id="id_example",
            meta={},
            score=3.14,
            embedding=[
                3.14,
            ],
            id_hash_keys=[
                "id_hash_keys_example",
            ],
        ),
        is_correct_answer=True,
        is_correct_document=True,
        origin="user-feedback",
        answer=AnswerSerialized(
            answer="answer_example",
            type="extractive",
            score=3.14,
            context="context_example",
            offsets_in_document=[
                Span(
                    start=1,
                    end=1,
                ),
            ],
            offsets_in_context=[
                Span(
                    start=1,
                    end=1,
                ),
            ],
            document_id="document_id_example",
            meta={},
        ),
        no_answer=True,
        pipeline_id="pipeline_id_example",
        created_at="created_at_example",
        updated_at="updated_at_example",
        meta={},
    ) # LabelSerialized | 

    # example passing only required values which don't have defaults set
    try:
        # User Feedback
        api_response = api_instance.post_feedback(label_serialized)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling FeedbackApi->post_feedback: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **label_serialized** | [**LabelSerialized**](LabelSerialized.md)|  |

### Return type

**bool, date, datetime, dict, float, int, list, str, none_type**

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

