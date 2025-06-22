# GetGlobalmapSeasonaccountinfo200ResponseOneOfDataValueSeasonsValueInner


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
from wot_api_client.models.get_globalmap_seasonaccountinfo200_response_one_of_data_value_seasons_value_inner import GetGlobalmapSeasonaccountinfo200ResponseOneOfDataValueSeasonsValueInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetGlobalmapSeasonaccountinfo200ResponseOneOfDataValueSeasonsValueInner from a JSON string
get_globalmap_seasonaccountinfo200_response_one_of_data_value_seasons_value_inner_instance = GetGlobalmapSeasonaccountinfo200ResponseOneOfDataValueSeasonsValueInner.from_json(json)
# print the JSON string representation of the object
print(GetGlobalmapSeasonaccountinfo200ResponseOneOfDataValueSeasonsValueInner.to_json())

# convert the object into a dict
get_globalmap_seasonaccountinfo200_response_one_of_data_value_seasons_value_inner_dict = get_globalmap_seasonaccountinfo200_response_one_of_data_value_seasons_value_inner_instance.to_dict()
# create an instance of GetGlobalmapSeasonaccountinfo200ResponseOneOfDataValueSeasonsValueInner from a dict
get_globalmap_seasonaccountinfo200_response_one_of_data_value_seasons_value_inner_from_dict = GetGlobalmapSeasonaccountinfo200ResponseOneOfDataValueSeasonsValueInner.from_dict(get_globalmap_seasonaccountinfo200_response_one_of_data_value_seasons_value_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


