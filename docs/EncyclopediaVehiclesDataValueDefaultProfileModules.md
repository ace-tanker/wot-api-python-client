# EncyclopediaVehiclesDataValueDefaultProfileModules

Mounted modules

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**engine_id** | **int** | Engine ID | 
**gun_id** | **int** | Gun ID | 
**turret_id** | **int** | Turret ID | 
**suspension_id** | **int** | Suspension ID | 
**radio_id** | **int** | Radio ID | 

## Example

```python
from wot_api_client.models.encyclopedia_vehicles_data_value_default_profile_modules import EncyclopediaVehiclesDataValueDefaultProfileModules

# TODO update the JSON string below
json = "{}"
# create an instance of EncyclopediaVehiclesDataValueDefaultProfileModules from a JSON string
encyclopedia_vehicles_data_value_default_profile_modules_instance = EncyclopediaVehiclesDataValueDefaultProfileModules.from_json(json)
# print the JSON string representation of the object
print(EncyclopediaVehiclesDataValueDefaultProfileModules.to_json())

# convert the object into a dict
encyclopedia_vehicles_data_value_default_profile_modules_dict = encyclopedia_vehicles_data_value_default_profile_modules_instance.to_dict()
# create an instance of EncyclopediaVehiclesDataValueDefaultProfileModules from a dict
encyclopedia_vehicles_data_value_default_profile_modules_from_dict = EncyclopediaVehiclesDataValueDefaultProfileModules.from_dict(encyclopedia_vehicles_data_value_default_profile_modules_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


