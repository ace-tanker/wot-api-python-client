# GetAccountInfo200ResponseOneOfDataValueStatistics

Player statistics

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**trees_cut** | **int** | Trees knocked down | 
**all** | [**GetAccountInfo200ResponseOneOfDataValueStatisticsAll**](GetAccountInfo200ResponseOneOfDataValueStatisticsAll.md) |  | 
**company** | [**GetAccountInfo200ResponseOneOfDataValueStatisticsCompany**](GetAccountInfo200ResponseOneOfDataValueStatisticsCompany.md) |  | 
**clan** | [**GetAccountInfo200ResponseOneOfDataValueStatisticsClan**](GetAccountInfo200ResponseOneOfDataValueStatisticsClan.md) |  | 
**fallout** | [**GetAccountInfo200ResponseOneOfDataValueStatisticsFallout**](GetAccountInfo200ResponseOneOfDataValueStatisticsFallout.md) |  | [optional] 
**random** | [**GetAccountInfo200ResponseOneOfDataValueStatisticsRandom**](GetAccountInfo200ResponseOneOfDataValueStatisticsRandom.md) |  | [optional] 
**stronghold_defense** | [**GetAccountInfo200ResponseOneOfDataValueStatisticsStrongholdDefense**](GetAccountInfo200ResponseOneOfDataValueStatisticsStrongholdDefense.md) |  | 
**stronghold_skirmish** | [**GetAccountInfo200ResponseOneOfDataValueStatisticsStrongholdSkirmish**](GetAccountInfo200ResponseOneOfDataValueStatisticsStrongholdSkirmish.md) |  | 
**historical** | [**GetAccountInfo200ResponseOneOfDataValueStatisticsHistorical**](GetAccountInfo200ResponseOneOfDataValueStatisticsHistorical.md) |  | 
**frags** | **Dict[str, int]** | Number and models of vehicles destroyed by a player. Player&#39;s private data. | 
**team** | [**GetAccountInfo200ResponseOneOfDataValueStatisticsTeam**](GetAccountInfo200ResponseOneOfDataValueStatisticsTeam.md) |  | 
**epic** | [**GetAccountInfo200ResponseOneOfDataValueStatisticsEpic**](GetAccountInfo200ResponseOneOfDataValueStatisticsEpic.md) |  | [optional] 
**regular_team** | [**GetAccountInfo200ResponseOneOfDataValueStatisticsRegularTeam**](GetAccountInfo200ResponseOneOfDataValueStatisticsRegularTeam.md) |  | 
**globalmap_middle** | [**GetAccountInfo200ResponseOneOfDataValueStatisticsGlobalmapMiddle**](GetAccountInfo200ResponseOneOfDataValueStatisticsGlobalmapMiddle.md) |  | [optional] 
**globalmap_champion** | [**GetAccountInfo200ResponseOneOfDataValueStatisticsGlobalmapChampion**](GetAccountInfo200ResponseOneOfDataValueStatisticsGlobalmapChampion.md) |  | [optional] 
**globalmap_absolute** | [**GetAccountInfo200ResponseOneOfDataValueStatisticsGlobalmapAbsolute**](GetAccountInfo200ResponseOneOfDataValueStatisticsGlobalmapAbsolute.md) |  | [optional] 
**ranked_battles** | [**GetAccountInfo200ResponseOneOfDataValueStatisticsRankedBattles**](GetAccountInfo200ResponseOneOfDataValueStatisticsRankedBattles.md) |  | [optional] 
**ranked_battles_current** | [**GetAccountInfo200ResponseOneOfDataValueStatisticsRankedBattlesCurrent**](GetAccountInfo200ResponseOneOfDataValueStatisticsRankedBattlesCurrent.md) |  | [optional] 
**ranked_battles_previous** | [**GetAccountInfo200ResponseOneOfDataValueStatisticsRankedBattlesPrevious**](GetAccountInfo200ResponseOneOfDataValueStatisticsRankedBattlesPrevious.md) |  | [optional] 
**ranked_10x10** | [**GetAccountInfo200ResponseOneOfDataValueStatisticsRanked10x10**](GetAccountInfo200ResponseOneOfDataValueStatisticsRanked10x10.md) |  | [optional] 
**ranked_15x15** | [**GetAccountInfo200ResponseOneOfDataValueStatisticsRanked15x15**](GetAccountInfo200ResponseOneOfDataValueStatisticsRanked15x15.md) |  | [optional] 
**ranked_season_1** | [**GetAccountInfo200ResponseOneOfDataValueStatisticsRankedSeason1**](GetAccountInfo200ResponseOneOfDataValueStatisticsRankedSeason1.md) |  | [optional] 
**ranked_season_2** | [**GetAccountInfo200ResponseOneOfDataValueStatisticsRankedSeason2**](GetAccountInfo200ResponseOneOfDataValueStatisticsRankedSeason2.md) |  | [optional] 
**ranked_season_3** | [**GetAccountInfo200ResponseOneOfDataValueStatisticsRankedSeason3**](GetAccountInfo200ResponseOneOfDataValueStatisticsRankedSeason3.md) |  | [optional] 

## Example

```python
from wot_api_client.models.get_account_info200_response_one_of_data_value_statistics import GetAccountInfo200ResponseOneOfDataValueStatistics

# TODO update the JSON string below
json = "{}"
# create an instance of GetAccountInfo200ResponseOneOfDataValueStatistics from a JSON string
get_account_info200_response_one_of_data_value_statistics_instance = GetAccountInfo200ResponseOneOfDataValueStatistics.from_json(json)
# print the JSON string representation of the object
print(GetAccountInfo200ResponseOneOfDataValueStatistics.to_json())

# convert the object into a dict
get_account_info200_response_one_of_data_value_statistics_dict = get_account_info200_response_one_of_data_value_statistics_instance.to_dict()
# create an instance of GetAccountInfo200ResponseOneOfDataValueStatistics from a dict
get_account_info200_response_one_of_data_value_statistics_from_dict = GetAccountInfo200ResponseOneOfDataValueStatistics.from_dict(get_account_info200_response_one_of_data_value_statistics_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


