# GetEncyclopediaVehicles200ResponseOneOfDataValueDefaultProfileAmmoInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Shell type | 
**damage** | **List[int]** | Damage (hp), a list of values: min, avg, max | 
**penetration** | **List[int]** | Penetration (mm), a list of values: min, avg, max | 
**stun** | [**GetEncyclopediaVehicles200ResponseOneOfDataValueDefaultProfileAmmoInnerStun**](GetEncyclopediaVehicles200ResponseOneOfDataValueDefaultProfileAmmoInnerStun.md) |  | 

## Example

```python
from wot_api_client.models.get_encyclopedia_vehicles200_response_one_of_data_value_default_profile_ammo_inner import GetEncyclopediaVehicles200ResponseOneOfDataValueDefaultProfileAmmoInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetEncyclopediaVehicles200ResponseOneOfDataValueDefaultProfileAmmoInner from a JSON string
get_encyclopedia_vehicles200_response_one_of_data_value_default_profile_ammo_inner_instance = GetEncyclopediaVehicles200ResponseOneOfDataValueDefaultProfileAmmoInner.from_json(json)
# print the JSON string representation of the object
print(GetEncyclopediaVehicles200ResponseOneOfDataValueDefaultProfileAmmoInner.to_json())

# convert the object into a dict
get_encyclopedia_vehicles200_response_one_of_data_value_default_profile_ammo_inner_dict = get_encyclopedia_vehicles200_response_one_of_data_value_default_profile_ammo_inner_instance.to_dict()
# create an instance of GetEncyclopediaVehicles200ResponseOneOfDataValueDefaultProfileAmmoInner from a dict
get_encyclopedia_vehicles200_response_one_of_data_value_default_profile_ammo_inner_from_dict = GetEncyclopediaVehicles200ResponseOneOfDataValueDefaultProfileAmmoInner.from_dict(get_encyclopedia_vehicles200_response_one_of_data_value_default_profile_ammo_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


