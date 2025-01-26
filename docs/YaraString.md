# YaraString


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identifier** | **str** |  | 
**instances** | [**List[YaraStringInstance]**](YaraStringInstance.md) |  | [optional] 

## Example

```python
from mandolin_python_client.models.yara_string import YaraString

# TODO update the JSON string below
json = "{}"
# create an instance of YaraString from a JSON string
yara_string_instance = YaraString.from_json(json)
# print the JSON string representation of the object
print(YaraString.to_json())

# convert the object into a dict
yara_string_dict = yara_string_instance.to_dict()
# create an instance of YaraString from a dict
yara_string_from_dict = YaraString.from_dict(yara_string_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


