# YaraResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rules** | **str** |  | 
**matches** | [**List[YaraMatch]**](YaraMatch.md) |  | [optional] 

## Example

```python
from mandolin_python_client.models.yara_result import YaraResult

# TODO update the JSON string below
json = "{}"
# create an instance of YaraResult from a JSON string
yara_result_instance = YaraResult.from_json(json)
# print the JSON string representation of the object
print(YaraResult.to_json())

# convert the object into a dict
yara_result_dict = yara_result_instance.to_dict()
# create an instance of YaraResult from a dict
yara_result_from_dict = YaraResult.from_dict(yara_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


