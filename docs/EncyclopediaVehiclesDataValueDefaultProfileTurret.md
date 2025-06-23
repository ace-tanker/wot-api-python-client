# EncyclopediaVehiclesDataValueDefaultProfileTurret

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
from wot_api_client.models.encyclopedia_vehicles_data_value_default_profile_turret import EncyclopediaVehiclesDataValueDefaultProfileTurret

# TODO update the JSON string below
json = "{}"
# create an instance of EncyclopediaVehiclesDataValueDefaultProfileTurret from a JSON string
encyclopedia_vehicles_data_value_default_profile_turret_instance = EncyclopediaVehiclesDataValueDefaultProfileTurret.from_json(json)
# print the JSON string representation of the object
print(EncyclopediaVehiclesDataValueDefaultProfileTurret.to_json())

# convert the object into a dict
encyclopedia_vehicles_data_value_default_profile_turret_dict = encyclopedia_vehicles_data_value_default_profile_turret_instance.to_dict()
# create an instance of EncyclopediaVehiclesDataValueDefaultProfileTurret from a dict
encyclopedia_vehicles_data_value_default_profile_turret_from_dict = EncyclopediaVehiclesDataValueDefaultProfileTurret.from_dict(encyclopedia_vehicles_data_value_default_profile_turret_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


