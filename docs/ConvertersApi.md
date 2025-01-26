# mandolin_python_client.ConvertersApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**generate_thumbnail_converter_thumbnail_post**](ConvertersApi.md#generate_thumbnail_converter_thumbnail_post) | **POST** /converter/thumbnail | Generate Thumbnail


# **generate_thumbnail_converter_thumbnail_post**
> generate_thumbnail_converter_thumbnail_post(file, width=width, height=height, color=color, strategy=strategy)

Generate Thumbnail

### Example


```python
import mandolin_python_client
from mandolin_python_client.models.thumbnail_strategy import ThumbnailStrategy
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
    api_instance = mandolin_python_client.ConvertersApi(api_client)
    file = None # bytearray | 
    width = 300 # int |  (optional) (default to 300)
    height = 200 # int |  (optional) (default to 200)
    color = 'color_example' # str |  (optional)
    strategy = mandolin_python_client.ThumbnailStrategy() # ThumbnailStrategy |  (optional)

    try:
        # Generate Thumbnail
        api_instance.generate_thumbnail_converter_thumbnail_post(file, width=width, height=height, color=color, strategy=strategy)
    except Exception as e:
        print("Exception when calling ConvertersApi->generate_thumbnail_converter_thumbnail_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file** | **bytearray**|  | 
 **width** | **int**|  | [optional] [default to 300]
 **height** | **int**|  | [optional] [default to 200]
 **color** | **str**|  | [optional] 
 **strategy** | [**ThumbnailStrategy**](.md)|  | [optional] 

### Return type

void (empty response body)

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

