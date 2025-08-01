# GlobalmapClanprovincesDataValueInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**arena_id** | **str** | Map ID | 
**arena_name** | **str** | Localized map name | 
**daily_revenue** | **int** | Daily income | 
**front_id** | **str** | Front ID | 
**front_name** | **str** | Front name | 
**revenue_level** | **int** | Income level from 0 to 11. 0 value means that income was not raised. | 
**prime_time** | **str** | Prime Time in UTC | 
**province_id** | **str** | Province ID | 
**province_name** | **str** | Province name | 
**clan_id** | **int** | Clan ID | 
**landing_type** | **str** | Indicates the landing type of a province | 
**turns_owned** | **int** | Province owned (number of turns) | 
**max_vehicle_level** | **int** | Maximum vehicle Tier in a Front | 
**private** | **object** | Restricted province information | 
**pillage_end_at** | **str** | Date when province will restore its revenue after ransack | 

## Example

```python
from wot_api_client.models.globalmap_clanprovinces_data_value_inner import GlobalmapClanprovincesDataValueInner

# TODO update the JSON string below
json = "{}"
# create an instance of GlobalmapClanprovincesDataValueInner from a JSON string
globalmap_clanprovinces_data_value_inner_instance = GlobalmapClanprovincesDataValueInner.from_json(json)
# print the JSON string representation of the object
print(GlobalmapClanprovincesDataValueInner.to_json())

# convert the object into a dict
globalmap_clanprovinces_data_value_inner_dict = globalmap_clanprovinces_data_value_inner_instance.to_dict()
# create an instance of GlobalmapClanprovincesDataValueInner from a dict
globalmap_clanprovinces_data_value_inner_from_dict = GlobalmapClanprovincesDataValueInner.from_dict(globalmap_clanprovinces_data_value_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


