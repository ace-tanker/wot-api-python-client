# GetEncyclopediaVehicles200ResponseOneOfDataValueDefaultProfileSuspension

Suspension characteristics

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tier** | **int** | Tier | 
**name** | **str** | Module name | 
**weight** | **int** | Weight (kg) | 
**tag** | **str** | Module tag | 
**load_limit** | **int** | Load limit (kg) | 
**traverse_speed** | **int** | Traverse speed (deg/s) | 
**steering_lock_angle** | **int** | Maximum wheel turning angle (for wheeled vehicles) | 

## Example

```python
from wot_api_client.models.get_encyclopedia_vehicles200_response_one_of_data_value_default_profile_suspension import GetEncyclopediaVehicles200ResponseOneOfDataValueDefaultProfileSuspension

# TODO update the JSON string below
json = "{}"
# create an instance of GetEncyclopediaVehicles200ResponseOneOfDataValueDefaultProfileSuspension from a JSON string
get_encyclopedia_vehicles200_response_one_of_data_value_default_profile_suspension_instance = GetEncyclopediaVehicles200ResponseOneOfDataValueDefaultProfileSuspension.from_json(json)
# print the JSON string representation of the object
print(GetEncyclopediaVehicles200ResponseOneOfDataValueDefaultProfileSuspension.to_json())

# convert the object into a dict
get_encyclopedia_vehicles200_response_one_of_data_value_default_profile_suspension_dict = get_encyclopedia_vehicles200_response_one_of_data_value_default_profile_suspension_instance.to_dict()
# create an instance of GetEncyclopediaVehicles200ResponseOneOfDataValueDefaultProfileSuspension from a dict
get_encyclopedia_vehicles200_response_one_of_data_value_default_profile_suspension_from_dict = GetEncyclopediaVehicles200ResponseOneOfDataValueDefaultProfileSuspension.from_dict(get_encyclopedia_vehicles200_response_one_of_data_value_default_profile_suspension_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


