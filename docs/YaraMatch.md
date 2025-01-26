# YaraMatch


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rule** | **str** |  | 
**tags** | **List[str]** |  | [optional] 
**namespace** | **str** |  | [optional] 
**meta** | **object** |  | [optional] 
**strings** | [**List[YaraString]**](YaraString.md) |  | [optional] 

## Example

```python
from mandolin_python_client.models.yara_match import YaraMatch

# TODO update the JSON string below
json = "{}"
# create an instance of YaraMatch from a JSON string
yara_match_instance = YaraMatch.from_json(json)
# print the JSON string representation of the object
print(YaraMatch.to_json())

# convert the object into a dict
yara_match_dict = yara_match_instance.to_dict()
# create an instance of YaraMatch from a dict
yara_match_from_dict = YaraMatch.from_dict(yara_match_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


