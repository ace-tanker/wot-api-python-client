# TanksMasteryOk


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**meta** | [**TanksMasteryMeta**](TanksMasteryMeta.md) |  | 
**data** | [**TanksMasteryData**](TanksMasteryData.md) |  | 

## Example

```python
from wot_api_client.models.tanks_mastery_ok import TanksMasteryOk

# TODO update the JSON string below
json = "{}"
# create an instance of TanksMasteryOk from a JSON string
tanks_mastery_ok_instance = TanksMasteryOk.from_json(json)
# print the JSON string representation of the object
print(TanksMasteryOk.to_json())

# convert the object into a dict
tanks_mastery_ok_dict = tanks_mastery_ok_instance.to_dict()
# create an instance of TanksMasteryOk from a dict
tanks_mastery_ok_from_dict = TanksMasteryOk.from_dict(tanks_mastery_ok_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


