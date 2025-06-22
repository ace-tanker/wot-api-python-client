# GetEncyclopediaVehicles200ResponseOneOfDataValueDefaultProfileGun

Gun characteristics

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tier** | **int** | Tier | 
**name** | **str** | Module name | 
**weight** | **int** | Weight (kg) | 
**tag** | **str** | Module tag | 
**fire_rate** | **float** | Rate of fire (rounds/min) | 
**dispersion** | **float** | Dispersion at 100 m (m) | 
**aim_time** | **float** | Aiming time (s) | 
**reload_time** | **float** | Reload time (s) | 
**caliber** | **int** | Caliber (mm) | 
**move_up_arc** | **int** | Elevation angle (deg) | 
**move_down_arc** | **int** | Depression angle (deg) | 
**traverse_speed** | **int** | Traverse speed (deg/s) | 

## Example

```python
from wot_api_client.models.get_encyclopedia_vehicles200_response_one_of_data_value_default_profile_gun import GetEncyclopediaVehicles200ResponseOneOfDataValueDefaultProfileGun

# TODO update the JSON string below
json = "{}"
# create an instance of GetEncyclopediaVehicles200ResponseOneOfDataValueDefaultProfileGun from a JSON string
get_encyclopedia_vehicles200_response_one_of_data_value_default_profile_gun_instance = GetEncyclopediaVehicles200ResponseOneOfDataValueDefaultProfileGun.from_json(json)
# print the JSON string representation of the object
print(GetEncyclopediaVehicles200ResponseOneOfDataValueDefaultProfileGun.to_json())

# convert the object into a dict
get_encyclopedia_vehicles200_response_one_of_data_value_default_profile_gun_dict = get_encyclopedia_vehicles200_response_one_of_data_value_default_profile_gun_instance.to_dict()
# create an instance of GetEncyclopediaVehicles200ResponseOneOfDataValueDefaultProfileGun from a dict
get_encyclopedia_vehicles200_response_one_of_data_value_default_profile_gun_from_dict = GetEncyclopediaVehicles200ResponseOneOfDataValueDefaultProfileGun.from_dict(get_encyclopedia_vehicles200_response_one_of_data_value_default_profile_gun_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


