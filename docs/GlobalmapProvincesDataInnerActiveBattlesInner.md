# GlobalmapProvincesDataInnerActiveBattlesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_at** | **str** | Battle start time in UTC | 
**round** | **int** | Round | 
**battle_reward** | **int** | Award | 
**clan_a** | [**GlobalmapProvincesDataInnerActiveBattlesInnerClanA**](GlobalmapProvincesDataInnerActiveBattlesInnerClanA.md) |  | 
**clan_b** | [**GlobalmapProvincesDataInnerActiveBattlesInnerClanB**](GlobalmapProvincesDataInnerActiveBattlesInnerClanB.md) |  | 

## Example

```python
from wot_api_client.models.globalmap_provinces_data_inner_active_battles_inner import GlobalmapProvincesDataInnerActiveBattlesInner

# TODO update the JSON string below
json = "{}"
# create an instance of GlobalmapProvincesDataInnerActiveBattlesInner from a JSON string
globalmap_provinces_data_inner_active_battles_inner_instance = GlobalmapProvincesDataInnerActiveBattlesInner.from_json(json)
# print the JSON string representation of the object
print(GlobalmapProvincesDataInnerActiveBattlesInner.to_json())

# convert the object into a dict
globalmap_provinces_data_inner_active_battles_inner_dict = globalmap_provinces_data_inner_active_battles_inner_instance.to_dict()
# create an instance of GlobalmapProvincesDataInnerActiveBattlesInner from a dict
globalmap_provinces_data_inner_active_battles_inner_from_dict = GlobalmapProvincesDataInnerActiveBattlesInner.from_dict(globalmap_provinces_data_inner_active_battles_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


