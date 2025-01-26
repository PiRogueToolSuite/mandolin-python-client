# AnalysisYaraResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | [optional] [default to False]
**content** | **str** |  | [optional] 
**processors** | [**Dict[str, AnalyzerResultYaraResult]**](AnalyzerResultYaraResult.md) |  | [optional] 

## Example

```python
from mandolin_python_client.models.analysis_yara_result import AnalysisYaraResult

# TODO update the JSON string below
json = "{}"
# create an instance of AnalysisYaraResult from a JSON string
analysis_yara_result_instance = AnalysisYaraResult.from_json(json)
# print the JSON string representation of the object
print(AnalysisYaraResult.to_json())

# convert the object into a dict
analysis_yara_result_dict = analysis_yara_result_instance.to_dict()
# create an instance of AnalysisYaraResult from a dict
analysis_yara_result_from_dict = AnalysisYaraResult.from_dict(analysis_yara_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


