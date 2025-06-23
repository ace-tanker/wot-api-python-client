# EncyclopediaVehicleprofileDataValue


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hp** | **int** | Hit points | 
**hull_hp** | **int** | Hull HP | 
**weight** | **int** | Weight (kg) | 
**hull_weight** | **int** | Hull weight (kg) | 
**max_weight** | **int** | Load limit (kg) | 
**max_ammo** | **int** | Ammunition | 
**speed_forward** | **int** | Top speed (km/h) | 
**speed_backward** | **int** | Top reverse speed (km/h) | 
**modules** | [**EncyclopediaVehiclesDataValueDefaultProfileModules**](EncyclopediaVehiclesDataValueDefaultProfileModules.md) |  | 
**armor** | [**EncyclopediaVehiclesDataValueDefaultProfileArmor**](EncyclopediaVehiclesDataValueDefaultProfileArmor.md) |  | 
**engine** | [**EncyclopediaVehiclesDataValueDefaultProfileEngine**](EncyclopediaVehiclesDataValueDefaultProfileEngine.md) |  | 
**gun** | [**EncyclopediaVehiclesDataValueDefaultProfileGun**](EncyclopediaVehiclesDataValueDefaultProfileGun.md) |  | 
**turret** | [**EncyclopediaVehiclesDataValueDefaultProfileTurret**](EncyclopediaVehiclesDataValueDefaultProfileTurret.md) |  | 
**suspension** | [**EncyclopediaVehiclesDataValueDefaultProfileSuspension**](EncyclopediaVehiclesDataValueDefaultProfileSuspension.md) |  | 
**radio** | [**EncyclopediaVehiclesDataValueDefaultProfileRadio**](EncyclopediaVehiclesDataValueDefaultProfileRadio.md) |  | 
**ammo** | [**List[EncyclopediaVehiclesDataValueDefaultProfileAmmoInner]**](EncyclopediaVehiclesDataValueDefaultProfileAmmoInner.md) | Gun shells characteristics | 
**siege** | [**EncyclopediaVehiclesDataValueDefaultProfileSiege**](EncyclopediaVehiclesDataValueDefaultProfileSiege.md) |  | 
**rapid** | [**EncyclopediaVehiclesDataValueDefaultProfileRapid**](EncyclopediaVehiclesDataValueDefaultProfileRapid.md) |  | 
**tank_id** | **int** | Vehicle ID | 
**is_default** | **bool** | Standard configuration | 
**profile_id** | **str** | Vehicle Configuration ID | 

## Example

```python
from wot_api_client.models.encyclopedia_vehicleprofile_data_value import EncyclopediaVehicleprofileDataValue

# TODO update the JSON string below
json = "{}"
# create an instance of EncyclopediaVehicleprofileDataValue from a JSON string
encyclopedia_vehicleprofile_data_value_instance = EncyclopediaVehicleprofileDataValue.from_json(json)
# print the JSON string representation of the object
print(EncyclopediaVehicleprofileDataValue.to_json())

# convert the object into a dict
encyclopedia_vehicleprofile_data_value_dict = encyclopedia_vehicleprofile_data_value_instance.to_dict()
# create an instance of EncyclopediaVehicleprofileDataValue from a dict
encyclopedia_vehicleprofile_data_value_from_dict = EncyclopediaVehicleprofileDataValue.from_dict(encyclopedia_vehicleprofile_data_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


