# GlobalmapSeasonaccountinfoDataValueSeasonsValueInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **int** | Account ID | 
**award_level** | **str** | Award level | 
**battles** | **int** | Battles fought for current clan | 
**battles_to_award** | **int** | Battles to fight in a current clan to get clan award for the season | 
**clan_id** | **int** | Clan ID | 
**clan_rank** | **int** | Clan rating | 
**season_id** | **str** | Season ID | 
**vehicle_level** | **int** | Vehicle Tier | 
**updated_at** | **int** | Date when account data were updated | 

## Example

```python
from wot_api_client.models.globalmap_seasonaccountinfo_data_value_seasons_value_inner import GlobalmapSeasonaccountinfoDataValueSeasonsValueInner

# TODO update the JSON string below
json = "{}"
# create an instance of GlobalmapSeasonaccountinfoDataValueSeasonsValueInner from a JSON string
globalmap_seasonaccountinfo_data_value_seasons_value_inner_instance = GlobalmapSeasonaccountinfoDataValueSeasonsValueInner.from_json(json)
# print the JSON string representation of the object
print(GlobalmapSeasonaccountinfoDataValueSeasonsValueInner.to_json())

# convert the object into a dict
globalmap_seasonaccountinfo_data_value_seasons_value_inner_dict = globalmap_seasonaccountinfo_data_value_seasons_value_inner_instance.to_dict()
# create an instance of GlobalmapSeasonaccountinfoDataValueSeasonsValueInner from a dict
globalmap_seasonaccountinfo_data_value_seasons_value_inner_from_dict = GlobalmapSeasonaccountinfoDataValueSeasonsValueInner.from_dict(globalmap_seasonaccountinfo_data_value_seasons_value_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


