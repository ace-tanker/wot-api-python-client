# GlobalmapProvincesDataInnerActiveBattlesInnerClanB

Second challenging clan ID

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**clan_id** | **int** | Clan ID | 
**win_elo_delta** | **int** | Changes in Elo-rating due to victory | 
**loose_elo_delta** | **int** | Changes in Elo-rating due to defeat | 
**battle_reward** | **int** | Award | 

## Example

```python
from wot_api_client.models.globalmap_provinces_data_inner_active_battles_inner_clan_b import GlobalmapProvincesDataInnerActiveBattlesInnerClanB

# TODO update the JSON string below
json = "{}"
# create an instance of GlobalmapProvincesDataInnerActiveBattlesInnerClanB from a JSON string
globalmap_provinces_data_inner_active_battles_inner_clan_b_instance = GlobalmapProvincesDataInnerActiveBattlesInnerClanB.from_json(json)
# print the JSON string representation of the object
print(GlobalmapProvincesDataInnerActiveBattlesInnerClanB.to_json())

# convert the object into a dict
globalmap_provinces_data_inner_active_battles_inner_clan_b_dict = globalmap_provinces_data_inner_active_battles_inner_clan_b_instance.to_dict()
# create an instance of GlobalmapProvincesDataInnerActiveBattlesInnerClanB from a dict
globalmap_provinces_data_inner_active_battles_inner_clan_b_from_dict = GlobalmapProvincesDataInnerActiveBattlesInnerClanB.from_dict(globalmap_provinces_data_inner_active_battles_inner_clan_b_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


