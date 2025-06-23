# GlobalmapProvincesDataInnerActiveBattlesInnerClanA

First challenging clan ID

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**clan_id** | **int** | Clan ID | 
**win_elo_delta** | **int** | Changes in Elo-rating due to victory | 
**loose_elo_delta** | **int** | Changes in Elo-rating due to defeat | 
**battle_reward** | **int** | Award | 

## Example

```python
from wot_api_client.models.globalmap_provinces_data_inner_active_battles_inner_clan_a import GlobalmapProvincesDataInnerActiveBattlesInnerClanA

# TODO update the JSON string below
json = "{}"
# create an instance of GlobalmapProvincesDataInnerActiveBattlesInnerClanA from a JSON string
globalmap_provinces_data_inner_active_battles_inner_clan_a_instance = GlobalmapProvincesDataInnerActiveBattlesInnerClanA.from_json(json)
# print the JSON string representation of the object
print(GlobalmapProvincesDataInnerActiveBattlesInnerClanA.to_json())

# convert the object into a dict
globalmap_provinces_data_inner_active_battles_inner_clan_a_dict = globalmap_provinces_data_inner_active_battles_inner_clan_a_instance.to_dict()
# create an instance of GlobalmapProvincesDataInnerActiveBattlesInnerClanA from a dict
globalmap_provinces_data_inner_active_battles_inner_clan_a_from_dict = GlobalmapProvincesDataInnerActiveBattlesInnerClanA.from_dict(globalmap_provinces_data_inner_active_battles_inner_clan_a_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


