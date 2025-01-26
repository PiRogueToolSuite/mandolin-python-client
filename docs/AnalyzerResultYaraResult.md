# AnalyzerResultYaraResult


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
**analysis** | [**YaraResult**](YaraResult.md) |  | [optional] 

## Example

```python
from mandolin_python_client.models.analyzer_result_yara_result import AnalyzerResultYaraResult

# TODO update the JSON string below
json = "{}"
# create an instance of AnalyzerResultYaraResult from a JSON string
analyzer_result_yara_result_instance = AnalyzerResultYaraResult.from_json(json)
# print the JSON string representation of the object
print(AnalyzerResultYaraResult.to_json())

# convert the object into a dict
analyzer_result_yara_result_dict = analyzer_result_yara_result_instance.to_dict()
# create an instance of AnalyzerResultYaraResult from a dict
analyzer_result_yara_result_from_dict = AnalyzerResultYaraResult.from_dict(analyzer_result_yara_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


