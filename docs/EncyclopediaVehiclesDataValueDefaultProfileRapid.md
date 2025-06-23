# EncyclopediaVehiclesDataValueDefaultProfileRapid

Vehicle characteristics in Rapid mode (for wheeled vehicles)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**speed_forward** | **int** | Top speed (km/h) | 
**speed_backward** | **int** | Top reverse speed (km/h) | 
**suspension_steering_lock_angle** | **int** | Maximum wheel turning angle | 
**switch_off_time** | **float** | Time required to switch to Cruise mode | 
**switch_on_time** | **float** | Time required to switch to Rapid mode | 

## Example

```python
from wot_api_client.models.encyclopedia_vehicles_data_value_default_profile_rapid import EncyclopediaVehiclesDataValueDefaultProfileRapid

# TODO update the JSON string below
json = "{}"
# create an instance of EncyclopediaVehiclesDataValueDefaultProfileRapid from a JSON string
encyclopedia_vehicles_data_value_default_profile_rapid_instance = EncyclopediaVehiclesDataValueDefaultProfileRapid.from_json(json)
# print the JSON string representation of the object
print(EncyclopediaVehiclesDataValueDefaultProfileRapid.to_json())

# convert the object into a dict
encyclopedia_vehicles_data_value_default_profile_rapid_dict = encyclopedia_vehicles_data_value_default_profile_rapid_instance.to_dict()
# create an instance of EncyclopediaVehiclesDataValueDefaultProfileRapid from a dict
encyclopedia_vehicles_data_value_default_profile_rapid_from_dict = EncyclopediaVehiclesDataValueDefaultProfileRapid.from_dict(encyclopedia_vehicles_data_value_default_profile_rapid_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


