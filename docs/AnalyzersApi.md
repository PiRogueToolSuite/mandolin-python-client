# mandolin_python_client.AnalyzersApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**analyze_with_tika_analyzer_tika_post**](AnalyzersApi.md#analyze_with_tika_analyzer_tika_post) | **POST** /analyzer/tika | Analyze With Tika
[**analyze_with_yara_analyzer_yara_post**](AnalyzersApi.md#analyze_with_yara_analyzer_yara_post) | **POST** /analyzer/yara | Analyze With Yara


# **analyze_with_tika_analyzer_tika_post**
> AnalysisTikaResult analyze_with_tika_analyzer_tika_post(file)

Analyze With Tika

### Example


```python
import mandolin_python_client
from mandolin_python_client.models.analysis_tika_result import AnalysisTikaResult
from mandolin_python_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = mandolin_python_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with mandolin_python_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mandolin_python_client.AnalyzersApi(api_client)
    file = None # bytearray | 

    try:
        # Analyze With Tika
        api_response = api_instance.analyze_with_tika_analyzer_tika_post(file)
        print("The response of AnalyzersApi->analyze_with_tika_analyzer_tika_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnalyzersApi->analyze_with_tika_analyzer_tika_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file** | **bytearray**|  | 

### Return type

[**AnalysisTikaResult**](AnalysisTikaResult.md)

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

# **analyze_with_yara_analyzer_yara_post**
> AnalysisYaraResult analyze_with_yara_analyzer_yara_post(file, rules)

Analyze With Yara

### Example


```python
import mandolin_python_client
from mandolin_python_client.models.analysis_yara_result import AnalysisYaraResult
from mandolin_python_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = mandolin_python_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with mandolin_python_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mandolin_python_client.AnalyzersApi(api_client)
    file = None # bytearray | 
    rules = 'rules_example' # str | 

    try:
        # Analyze With Yara
        api_response = api_instance.analyze_with_yara_analyzer_yara_post(file, rules)
        print("The response of AnalyzersApi->analyze_with_yara_analyzer_yara_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnalyzersApi->analyze_with_yara_analyzer_yara_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file** | **bytearray**|  | 
 **rules** | **str**|  | 

### Return type

[**AnalysisYaraResult**](AnalysisYaraResult.md)

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

