# YaraStringInstance


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**matched_length** | **int** |  | 
**offset** | **int** |  | 
**plaintext** | **str** |  | [optional] 

## Example

```python
from mandolin_python_client.models.yara_string_instance import YaraStringInstance

# TODO update the JSON string below
json = "{}"
# create an instance of YaraStringInstance from a JSON string
yara_string_instance_instance = YaraStringInstance.from_json(json)
# print the JSON string representation of the object
print(YaraStringInstance.to_json())

# convert the object into a dict
yara_string_instance_dict = yara_string_instance_instance.to_dict()
# create an instance of YaraStringInstance from a dict
yara_string_instance_from_dict = YaraStringInstance.from_dict(yara_string_instance_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


