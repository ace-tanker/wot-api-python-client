# EncyclopediaModulesDataValueDefaultProfileGun

Gun characteristics

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fire_rate** | **float** | Rate of fire (rounds/min) | 
**dispersion** | **float** | Dispersion at 100 m (m) | 
**aim_time** | **float** | Aiming time (s) | 
**reload_time** | **float** | Reload time (s) | 
**move_up_arc** | **int** | Elevation angle (deg) | 
**move_down_arc** | **int** | Depression angle (deg) | 
**traverse_speed** | **int** | Traverse speed (deg/s) | 
**ammo** | [**List[EncyclopediaVehiclesDataValueDefaultProfileAmmoInner]**](EncyclopediaVehiclesDataValueDefaultProfileAmmoInner.md) | Gun shells characteristics | 
**max_ammo** | **int** | Number of shells | 

## Example

```python
from wot_api_client.models.encyclopedia_modules_data_value_default_profile_gun import EncyclopediaModulesDataValueDefaultProfileGun

# TODO update the JSON string below
json = "{}"
# create an instance of EncyclopediaModulesDataValueDefaultProfileGun from a JSON string
encyclopedia_modules_data_value_default_profile_gun_instance = EncyclopediaModulesDataValueDefaultProfileGun.from_json(json)
# print the JSON string representation of the object
print(EncyclopediaModulesDataValueDefaultProfileGun.to_json())

# convert the object into a dict
encyclopedia_modules_data_value_default_profile_gun_dict = encyclopedia_modules_data_value_default_profile_gun_instance.to_dict()
# create an instance of EncyclopediaModulesDataValueDefaultProfileGun from a dict
encyclopedia_modules_data_value_default_profile_gun_from_dict = EncyclopediaModulesDataValueDefaultProfileGun.from_dict(encyclopedia_modules_data_value_default_profile_gun_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


