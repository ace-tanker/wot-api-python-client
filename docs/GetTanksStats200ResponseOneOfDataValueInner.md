# GetTanksStats200ResponseOneOfDataValueInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **int** | Player account ID | 
**tank_id** | **int** | Vehicle ID | 
**all** | [**GetTanksStats200ResponseOneOfDataValueInnerAll**](GetTanksStats200ResponseOneOfDataValueInnerAll.md) |  | 
**company** | [**GetTanksStats200ResponseOneOfDataValueInnerCompany**](GetTanksStats200ResponseOneOfDataValueInnerCompany.md) |  | 
**stronghold_defense** | [**GetTanksStats200ResponseOneOfDataValueInnerStrongholdDefense**](GetTanksStats200ResponseOneOfDataValueInnerStrongholdDefense.md) |  | 
**stronghold_skirmish** | [**GetTanksStats200ResponseOneOfDataValueInnerStrongholdSkirmish**](GetTanksStats200ResponseOneOfDataValueInnerStrongholdSkirmish.md) |  | 
**clan** | [**GetTanksStats200ResponseOneOfDataValueInnerClan**](GetTanksStats200ResponseOneOfDataValueInnerClan.md) |  | 
**random** | [**GetTanksStats200ResponseOneOfDataValueInnerRandom**](GetTanksStats200ResponseOneOfDataValueInnerRandom.md) |  | [optional] 
**fallout** | [**GetTanksStats200ResponseOneOfDataValueInnerFallout**](GetTanksStats200ResponseOneOfDataValueInnerFallout.md) |  | [optional] 
**team** | [**GetTanksStats200ResponseOneOfDataValueInnerTeam**](GetTanksStats200ResponseOneOfDataValueInnerTeam.md) |  | 
**regular_team** | [**GetTanksStats200ResponseOneOfDataValueInnerRegularTeam**](GetTanksStats200ResponseOneOfDataValueInnerRegularTeam.md) |  | 
**globalmap** | [**GetTanksStats200ResponseOneOfDataValueInnerGlobalmap**](GetTanksStats200ResponseOneOfDataValueInnerGlobalmap.md) |  | 
**epic** | [**GetTanksStats200ResponseOneOfDataValueInnerEpic**](GetTanksStats200ResponseOneOfDataValueInnerEpic.md) |  | [optional] 
**ranked_battles** | [**GetTanksStats200ResponseOneOfDataValueInnerRankedBattles**](GetTanksStats200ResponseOneOfDataValueInnerRankedBattles.md) |  | [optional] 
**max_xp** | **int** | Maximum experience per battle | 
**max_frags** | **int** | Maximum destroyed in battle | 
**frags** | **Dict[str, int]** | Details on vehicles destroyed. This data requires a valid access_token for the specified account. | 
**in_garage** | **bool** | Availability of vehicle in the Garage. This data requires a valid access_token for the specified account. | 
**mark_of_mastery** | **int** | Mastery Badges:   * 0 — None  * 1 — 3rd Class   * 2 — 2nd Class  * 3 — 1st Class  * 4 — Ace Tanker | 
**ranked_10x10** | [**GetTanksStats200ResponseOneOfDataValueInnerRanked10x10**](GetTanksStats200ResponseOneOfDataValueInnerRanked10x10.md) |  | [optional] 

## Example

```python
from wot_api_client.models.get_tanks_stats200_response_one_of_data_value_inner import GetTanksStats200ResponseOneOfDataValueInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetTanksStats200ResponseOneOfDataValueInner from a JSON string
get_tanks_stats200_response_one_of_data_value_inner_instance = GetTanksStats200ResponseOneOfDataValueInner.from_json(json)
# print the JSON string representation of the object
print(GetTanksStats200ResponseOneOfDataValueInner.to_json())

# convert the object into a dict
get_tanks_stats200_response_one_of_data_value_inner_dict = get_tanks_stats200_response_one_of_data_value_inner_instance.to_dict()
# create an instance of GetTanksStats200ResponseOneOfDataValueInner from a dict
get_tanks_stats200_response_one_of_data_value_inner_from_dict = GetTanksStats200ResponseOneOfDataValueInner.from_dict(get_tanks_stats200_response_one_of_data_value_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


