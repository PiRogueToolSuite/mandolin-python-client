# AnalyzerResultTikaResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | [optional] [default to False]
**processor_name** | **str** |  | 
**processor_url** | **str** |  | 
**processor_description** | **str** |  | [optional] 
**error** | **str** |  | [optional] 
**error_short** | **str** |  | [optional] 
**metadata** | **object** |  | [optional] 
**analysis** | [**TikaResult**](TikaResult.md) |  | [optional] 

## Example

```python
from mandolin_python_client.models.analyzer_result_tika_result import AnalyzerResultTikaResult

# TODO update the JSON string below
json = "{}"
# create an instance of AnalyzerResultTikaResult from a JSON string
analyzer_result_tika_result_instance = AnalyzerResultTikaResult.from_json(json)
# print the JSON string representation of the object
print(AnalyzerResultTikaResult.to_json())

# convert the object into a dict
analyzer_result_tika_result_dict = analyzer_result_tika_result_instance.to_dict()
# create an instance of AnalyzerResultTikaResult from a dict
analyzer_result_tika_result_from_dict = AnalyzerResultTikaResult.from_dict(analyzer_result_tika_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


