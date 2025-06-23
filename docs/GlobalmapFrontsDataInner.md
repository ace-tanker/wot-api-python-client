# GlobalmapFrontsDataInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**front_id** | **str** | Front ID | 
**front_name** | **str** | Front name | 
**is_active** | **bool** | Indicates if a map is active | 
**is_event** | **bool** | Indicates the map type: regular map or events map | 
**vehicle_freeze** | **bool** | Indicates if vehicles blocking is active | 
**fog_of_war** | **bool** | Indicates presence of Fog of War | 
**battle_time_limit** | **int** | Maximum battle duration in minutes | 
**min_tanks_per_division** | **int** | Minimum number of vehicles in division | 
**max_tanks_per_division** | **int** | Maximum number of vehicles in division | 
**division_cost** | **int** | Division cost | 
**avg_clans_rating** | **int** | Average clans rating | 
**avg_won_bet** | **int** | Average winning bid | 
**avg_min_bet** | **int** | Average minimum bid | 
**min_vehicle_level** | **int** | Minimum vehicle Tier | 
**max_vehicle_level** | **int** | Maximum vehicle Tier | 
**available_extensions** | [**List[GlobalmapFrontsDataInnerAvailableExtensionsInner]**](GlobalmapFrontsDataInnerAvailableExtensionsInner.md) | Available modules | 
**provinces_count** | **int** | Amount of Provinces | 

## Example

```python
from wot_api_client.models.globalmap_fronts_data_inner import GlobalmapFrontsDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of GlobalmapFrontsDataInner from a JSON string
globalmap_fronts_data_inner_instance = GlobalmapFrontsDataInner.from_json(json)
# print the JSON string representation of the object
print(GlobalmapFrontsDataInner.to_json())

# convert the object into a dict
globalmap_fronts_data_inner_dict = globalmap_fronts_data_inner_instance.to_dict()
# create an instance of GlobalmapFrontsDataInner from a dict
globalmap_fronts_data_inner_from_dict = GlobalmapFrontsDataInner.from_dict(globalmap_fronts_data_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


