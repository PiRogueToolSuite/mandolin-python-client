# AnalysisTikaResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | [optional] [default to False]
**content** | **str** |  | [optional] 
**processors** | [**Dict[str, AnalyzerResultTikaResult]**](AnalyzerResultTikaResult.md) |  | [optional] 

## Example

```python
from mandolin_python_client.models.analysis_tika_result import AnalysisTikaResult

# TODO update the JSON string below
json = "{}"
# create an instance of AnalysisTikaResult from a JSON string
analysis_tika_result_instance = AnalysisTikaResult.from_json(json)
# print the JSON string representation of the object
print(AnalysisTikaResult.to_json())

# convert the object into a dict
analysis_tika_result_dict = analysis_tika_result_instance.to_dict()
# create an instance of AnalysisTikaResult from a dict
analysis_tika_result_from_dict = AnalysisTikaResult.from_dict(analysis_tika_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


