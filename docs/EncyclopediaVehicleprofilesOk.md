# EncyclopediaVehicleprofilesOk


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**meta** | [**EncyclopediaVehicleprofilesMeta**](EncyclopediaVehicleprofilesMeta.md) |  | 
**data** | **Dict[str, Optional[List[EncyclopediaVehicleprofilesDataValueInner]]]** |  | 

## Example

```python
from wot_api_client.models.encyclopedia_vehicleprofiles_ok import EncyclopediaVehicleprofilesOk

# TODO update the JSON string below
json = "{}"
# create an instance of EncyclopediaVehicleprofilesOk from a JSON string
encyclopedia_vehicleprofiles_ok_instance = EncyclopediaVehicleprofilesOk.from_json(json)
# print the JSON string representation of the object
print(EncyclopediaVehicleprofilesOk.to_json())

# convert the object into a dict
encyclopedia_vehicleprofiles_ok_dict = encyclopedia_vehicleprofiles_ok_instance.to_dict()
# create an instance of EncyclopediaVehicleprofilesOk from a dict
encyclopedia_vehicleprofiles_ok_from_dict = EncyclopediaVehicleprofilesOk.from_dict(encyclopedia_vehicleprofiles_ok_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


