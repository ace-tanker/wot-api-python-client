# GetEncyclopediaVehicles200ResponseOneOfDataValueDefaultProfileRapid

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
from wot_api_client.models.get_encyclopedia_vehicles200_response_one_of_data_value_default_profile_rapid import GetEncyclopediaVehicles200ResponseOneOfDataValueDefaultProfileRapid

# TODO update the JSON string below
json = "{}"
# create an instance of GetEncyclopediaVehicles200ResponseOneOfDataValueDefaultProfileRapid from a JSON string
get_encyclopedia_vehicles200_response_one_of_data_value_default_profile_rapid_instance = GetEncyclopediaVehicles200ResponseOneOfDataValueDefaultProfileRapid.from_json(json)
# print the JSON string representation of the object
print(GetEncyclopediaVehicles200ResponseOneOfDataValueDefaultProfileRapid.to_json())

# convert the object into a dict
get_encyclopedia_vehicles200_response_one_of_data_value_default_profile_rapid_dict = get_encyclopedia_vehicles200_response_one_of_data_value_default_profile_rapid_instance.to_dict()
# create an instance of GetEncyclopediaVehicles200ResponseOneOfDataValueDefaultProfileRapid from a dict
get_encyclopedia_vehicles200_response_one_of_data_value_default_profile_rapid_from_dict = GetEncyclopediaVehicles200ResponseOneOfDataValueDefaultProfileRapid.from_dict(get_encyclopedia_vehicles200_response_one_of_data_value_default_profile_rapid_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


