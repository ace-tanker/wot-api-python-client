# EncyclopediaVehiclesDataValueDefaultProfileSiege

Vehicle characteristics in Siege mode

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aim_time** | **float** | Aiming time (s) | 
**suspension_traverse_speed** | **int** | Standard suspension traverse speed | 
**move_down_arc** | **int** | Depression angle (deg) | 
**move_up_arc** | **int** | Elevation angle (deg) | 
**reload_time** | **float** | Reload time (s) | 
**dispersion** | **float** | Dispersion at 100 m (m) | 
**speed_backward** | **int** | Top reverse speed (km/h) | 
**switch_off_time** | **float** | Time needed to switch on the Siege mode | 
**switch_on_time** | **float** | Time required to switch to Siege mode | 

## Example

```python
from wot_api_client.models.encyclopedia_vehicles_data_value_default_profile_siege import EncyclopediaVehiclesDataValueDefaultProfileSiege

# TODO update the JSON string below
json = "{}"
# create an instance of EncyclopediaVehiclesDataValueDefaultProfileSiege from a JSON string
encyclopedia_vehicles_data_value_default_profile_siege_instance = EncyclopediaVehiclesDataValueDefaultProfileSiege.from_json(json)
# print the JSON string representation of the object
print(EncyclopediaVehiclesDataValueDefaultProfileSiege.to_json())

# convert the object into a dict
encyclopedia_vehicles_data_value_default_profile_siege_dict = encyclopedia_vehicles_data_value_default_profile_siege_instance.to_dict()
# create an instance of EncyclopediaVehiclesDataValueDefaultProfileSiege from a dict
encyclopedia_vehicles_data_value_default_profile_siege_from_dict = EncyclopediaVehiclesDataValueDefaultProfileSiege.from_dict(encyclopedia_vehicles_data_value_default_profile_siege_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


