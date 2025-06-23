# TanksStatsDataValueInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **int** | Player account ID | 
**tank_id** | **int** | Vehicle ID | 
**all** | [**TanksStatsDataValueInnerAll**](TanksStatsDataValueInnerAll.md) |  | 
**company** | [**TanksStatsDataValueInnerCompany**](TanksStatsDataValueInnerCompany.md) |  | 
**stronghold_defense** | [**TanksStatsDataValueInnerStrongholdDefense**](TanksStatsDataValueInnerStrongholdDefense.md) |  | 
**stronghold_skirmish** | [**TanksStatsDataValueInnerStrongholdSkirmish**](TanksStatsDataValueInnerStrongholdSkirmish.md) |  | 
**clan** | [**TanksStatsDataValueInnerClan**](TanksStatsDataValueInnerClan.md) |  | 
**random** | [**TanksStatsDataValueInnerRandom**](TanksStatsDataValueInnerRandom.md) |  | [optional] 
**fallout** | [**TanksStatsDataValueInnerFallout**](TanksStatsDataValueInnerFallout.md) |  | [optional] 
**team** | [**TanksStatsDataValueInnerTeam**](TanksStatsDataValueInnerTeam.md) |  | 
**regular_team** | [**TanksStatsDataValueInnerRegularTeam**](TanksStatsDataValueInnerRegularTeam.md) |  | 
**globalmap** | [**TanksStatsDataValueInnerGlobalmap**](TanksStatsDataValueInnerGlobalmap.md) |  | 
**epic** | [**TanksStatsDataValueInnerEpic**](TanksStatsDataValueInnerEpic.md) |  | [optional] 
**ranked_battles** | [**TanksStatsDataValueInnerRankedBattles**](TanksStatsDataValueInnerRankedBattles.md) |  | [optional] 
**max_xp** | **int** | Maximum experience per battle | 
**max_frags** | **int** | Maximum destroyed in battle | 
**frags** | **Dict[str, int]** | Details on vehicles destroyed. This data requires a valid access_token for the specified account. | 
**in_garage** | **bool** | Availability of vehicle in the Garage. This data requires a valid access_token for the specified account. | 
**mark_of_mastery** | **int** | Mastery Badges:   * 0 — None  * 1 — 3rd Class   * 2 — 2nd Class  * 3 — 1st Class  * 4 — Ace Tanker | 
**ranked_10x10** | [**TanksStatsDataValueInnerRanked10x10**](TanksStatsDataValueInnerRanked10x10.md) |  | [optional] 

## Example

```python
from wot_api_client.models.tanks_stats_data_value_inner import TanksStatsDataValueInner

# TODO update the JSON string below
json = "{}"
# create an instance of TanksStatsDataValueInner from a JSON string
tanks_stats_data_value_inner_instance = TanksStatsDataValueInner.from_json(json)
# print the JSON string representation of the object
print(TanksStatsDataValueInner.to_json())

# convert the object into a dict
tanks_stats_data_value_inner_dict = tanks_stats_data_value_inner_instance.to_dict()
# create an instance of TanksStatsDataValueInner from a dict
tanks_stats_data_value_inner_from_dict = TanksStatsDataValueInner.from_dict(tanks_stats_data_value_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


