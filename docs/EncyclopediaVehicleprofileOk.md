# EncyclopediaVehicleprofileOk


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**meta** | [**EncyclopediaVehicleprofileMeta**](EncyclopediaVehicleprofileMeta.md) |  | 
**data** | [**Dict[str, EncyclopediaVehicleprofileDataValue]**](EncyclopediaVehicleprofileDataValue.md) |  | 

## Example

```python
from wot_api_client.models.encyclopedia_vehicleprofile_ok import EncyclopediaVehicleprofileOk

# TODO update the JSON string below
json = "{}"
# create an instance of EncyclopediaVehicleprofileOk from a JSON string
encyclopedia_vehicleprofile_ok_instance = EncyclopediaVehicleprofileOk.from_json(json)
# print the JSON string representation of the object
print(EncyclopediaVehicleprofileOk.to_json())

# convert the object into a dict
encyclopedia_vehicleprofile_ok_dict = encyclopedia_vehicleprofile_ok_instance.to_dict()
# create an instance of EncyclopediaVehicleprofileOk from a dict
encyclopedia_vehicleprofile_ok_from_dict = EncyclopediaVehicleprofileOk.from_dict(encyclopedia_vehicleprofile_ok_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


