# GetEncyclopediaVehicles200ResponseOneOfDataValueDefaultProfileTurret

Turret characteristics

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tier** | **int** | Tier | 
**name** | **str** | Module name | 
**weight** | **int** | Weight (kg) | 
**tag** | **str** | Module tag | 
**view_range** | **int** | View range (m) | 
**traverse_speed** | **int** | Traverse speed (deg/s) | 
**hp** | **int** | Hit points | 
**traverse_left_arc** | **int** | Traverse angle, left (deg) | 
**traverse_right_arc** | **int** | Traverse angle, right (deg) | 

## Example

```python
from wot_api_client.models.get_encyclopedia_vehicles200_response_one_of_data_value_default_profile_turret import GetEncyclopediaVehicles200ResponseOneOfDataValueDefaultProfileTurret

# TODO update the JSON string below
json = "{}"
# create an instance of GetEncyclopediaVehicles200ResponseOneOfDataValueDefaultProfileTurret from a JSON string
get_encyclopedia_vehicles200_response_one_of_data_value_default_profile_turret_instance = GetEncyclopediaVehicles200ResponseOneOfDataValueDefaultProfileTurret.from_json(json)
# print the JSON string representation of the object
print(GetEncyclopediaVehicles200ResponseOneOfDataValueDefaultProfileTurret.to_json())

# convert the object into a dict
get_encyclopedia_vehicles200_response_one_of_data_value_default_profile_turret_dict = get_encyclopedia_vehicles200_response_one_of_data_value_default_profile_turret_instance.to_dict()
# create an instance of GetEncyclopediaVehicles200ResponseOneOfDataValueDefaultProfileTurret from a dict
get_encyclopedia_vehicles200_response_one_of_data_value_default_profile_turret_from_dict = GetEncyclopediaVehicles200ResponseOneOfDataValueDefaultProfileTurret.from_dict(get_encyclopedia_vehicles200_response_one_of_data_value_default_profile_turret_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


