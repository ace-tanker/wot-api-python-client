# EncyclopediaVehiclesDataValueDefaultProfileSuspension

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
from wot_api_client.models.encyclopedia_vehicles_data_value_default_profile_suspension import EncyclopediaVehiclesDataValueDefaultProfileSuspension

# TODO update the JSON string below
json = "{}"
# create an instance of EncyclopediaVehiclesDataValueDefaultProfileSuspension from a JSON string
encyclopedia_vehicles_data_value_default_profile_suspension_instance = EncyclopediaVehiclesDataValueDefaultProfileSuspension.from_json(json)
# print the JSON string representation of the object
print(EncyclopediaVehiclesDataValueDefaultProfileSuspension.to_json())

# convert the object into a dict
encyclopedia_vehicles_data_value_default_profile_suspension_dict = encyclopedia_vehicles_data_value_default_profile_suspension_instance.to_dict()
# create an instance of EncyclopediaVehiclesDataValueDefaultProfileSuspension from a dict
encyclopedia_vehicles_data_value_default_profile_suspension_from_dict = EncyclopediaVehiclesDataValueDefaultProfileSuspension.from_dict(encyclopedia_vehicles_data_value_default_profile_suspension_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


