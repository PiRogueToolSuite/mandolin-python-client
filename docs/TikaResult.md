# TikaResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content_length** | **int** |  | [optional] 
**created** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**language** | **str** |  | [optional] 
**extra** | **object** |  | [optional] 

## Example

```python
from mandolin_python_client.models.tika_result import TikaResult

# TODO update the JSON string below
json = "{}"
# create an instance of TikaResult from a JSON string
tika_result_instance = TikaResult.from_json(json)
# print the JSON string representation of the object
print(TikaResult.to_json())

# convert the object into a dict
tika_result_dict = tika_result_instance.to_dict()
# create an instance of TikaResult from a dict
tika_result_from_dict = TikaResult.from_dict(tika_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


