# EncyclopediaVehiclesDataValueDefaultProfileAmmoInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Shell type | 
**damage** | **List[int]** | Damage (hp), a list of values: min, avg, max | 
**penetration** | **List[int]** | Penetration (mm), a list of values: min, avg, max | 
**stun** | [**EncyclopediaVehiclesDataValueDefaultProfileAmmoInnerStun**](EncyclopediaVehiclesDataValueDefaultProfileAmmoInnerStun.md) |  | 

## Example

```python
from wot_api_client.models.encyclopedia_vehicles_data_value_default_profile_ammo_inner import EncyclopediaVehiclesDataValueDefaultProfileAmmoInner

# TODO update the JSON string below
json = "{}"
# create an instance of EncyclopediaVehiclesDataValueDefaultProfileAmmoInner from a JSON string
encyclopedia_vehicles_data_value_default_profile_ammo_inner_instance = EncyclopediaVehiclesDataValueDefaultProfileAmmoInner.from_json(json)
# print the JSON string representation of the object
print(EncyclopediaVehiclesDataValueDefaultProfileAmmoInner.to_json())

# convert the object into a dict
encyclopedia_vehicles_data_value_default_profile_ammo_inner_dict = encyclopedia_vehicles_data_value_default_profile_ammo_inner_instance.to_dict()
# create an instance of EncyclopediaVehiclesDataValueDefaultProfileAmmoInner from a dict
encyclopedia_vehicles_data_value_default_profile_ammo_inner_from_dict = EncyclopediaVehiclesDataValueDefaultProfileAmmoInner.from_dict(encyclopedia_vehicles_data_value_default_profile_ammo_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


