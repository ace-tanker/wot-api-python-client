# EncyclopediaVehiclesDataValueDefaultProfileEngine

Engine characteristics

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tier** | **int** | Tier | 
**name** | **str** | Module name | 
**weight** | **int** | Weight (kg) | 
**tag** | **str** | Module tag | 
**power** | **int** | Engine Power (hp) | 
**fire_chance** | **float** | Chance of engine fire | 

## Example

```python
from wot_api_client.models.encyclopedia_vehicles_data_value_default_profile_engine import EncyclopediaVehiclesDataValueDefaultProfileEngine

# TODO update the JSON string below
json = "{}"
# create an instance of EncyclopediaVehiclesDataValueDefaultProfileEngine from a JSON string
encyclopedia_vehicles_data_value_default_profile_engine_instance = EncyclopediaVehiclesDataValueDefaultProfileEngine.from_json(json)
# print the JSON string representation of the object
print(EncyclopediaVehiclesDataValueDefaultProfileEngine.to_json())

# convert the object into a dict
encyclopedia_vehicles_data_value_default_profile_engine_dict = encyclopedia_vehicles_data_value_default_profile_engine_instance.to_dict()
# create an instance of EncyclopediaVehiclesDataValueDefaultProfileEngine from a dict
encyclopedia_vehicles_data_value_default_profile_engine_from_dict = EncyclopediaVehiclesDataValueDefaultProfileEngine.from_dict(encyclopedia_vehicles_data_value_default_profile_engine_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


