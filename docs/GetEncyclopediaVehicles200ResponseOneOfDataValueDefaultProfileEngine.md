# GetEncyclopediaVehicles200ResponseOneOfDataValueDefaultProfileEngine

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
from wot_api_client.models.get_encyclopedia_vehicles200_response_one_of_data_value_default_profile_engine import GetEncyclopediaVehicles200ResponseOneOfDataValueDefaultProfileEngine

# TODO update the JSON string below
json = "{}"
# create an instance of GetEncyclopediaVehicles200ResponseOneOfDataValueDefaultProfileEngine from a JSON string
get_encyclopedia_vehicles200_response_one_of_data_value_default_profile_engine_instance = GetEncyclopediaVehicles200ResponseOneOfDataValueDefaultProfileEngine.from_json(json)
# print the JSON string representation of the object
print(GetEncyclopediaVehicles200ResponseOneOfDataValueDefaultProfileEngine.to_json())

# convert the object into a dict
get_encyclopedia_vehicles200_response_one_of_data_value_default_profile_engine_dict = get_encyclopedia_vehicles200_response_one_of_data_value_default_profile_engine_instance.to_dict()
# create an instance of GetEncyclopediaVehicles200ResponseOneOfDataValueDefaultProfileEngine from a dict
get_encyclopedia_vehicles200_response_one_of_data_value_default_profile_engine_from_dict = GetEncyclopediaVehicles200ResponseOneOfDataValueDefaultProfileEngine.from_dict(get_encyclopedia_vehicles200_response_one_of_data_value_default_profile_engine_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


