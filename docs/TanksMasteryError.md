# TanksMasteryError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**error** | **object** |  | 

## Example

```python
from wot_api_client.models.tanks_mastery_error import TanksMasteryError

# TODO update the JSON string below
json = "{}"
# create an instance of TanksMasteryError from a JSON string
tanks_mastery_error_instance = TanksMasteryError.from_json(json)
# print the JSON string representation of the object
print(TanksMasteryError.to_json())

# convert the object into a dict
tanks_mastery_error_dict = tanks_mastery_error_instance.to_dict()
# create an instance of TanksMasteryError from a dict
tanks_mastery_error_from_dict = TanksMasteryError.from_dict(tanks_mastery_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


