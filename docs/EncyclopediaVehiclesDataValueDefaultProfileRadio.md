# EncyclopediaVehiclesDataValueDefaultProfileRadio

Radio characteristics

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tier** | **int** | Tier | 
**name** | **str** | Module name | 
**weight** | **int** | Weight (kg) | 
**tag** | **str** | Module tag | 
**signal_range** | **int** | Signal range | 

## Example

```python
from wot_api_client.models.encyclopedia_vehicles_data_value_default_profile_radio import EncyclopediaVehiclesDataValueDefaultProfileRadio

# TODO update the JSON string below
json = "{}"
# create an instance of EncyclopediaVehiclesDataValueDefaultProfileRadio from a JSON string
encyclopedia_vehicles_data_value_default_profile_radio_instance = EncyclopediaVehiclesDataValueDefaultProfileRadio.from_json(json)
# print the JSON string representation of the object
print(EncyclopediaVehiclesDataValueDefaultProfileRadio.to_json())

# convert the object into a dict
encyclopedia_vehicles_data_value_default_profile_radio_dict = encyclopedia_vehicles_data_value_default_profile_radio_instance.to_dict()
# create an instance of EncyclopediaVehiclesDataValueDefaultProfileRadio from a dict
encyclopedia_vehicles_data_value_default_profile_radio_from_dict = EncyclopediaVehiclesDataValueDefaultProfileRadio.from_dict(encyclopedia_vehicles_data_value_default_profile_radio_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


