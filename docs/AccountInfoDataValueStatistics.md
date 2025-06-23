# AccountInfoDataValueStatistics

Player statistics

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**trees_cut** | **int** | Trees knocked down | 
**all** | [**AccountInfoDataValueStatisticsAll**](AccountInfoDataValueStatisticsAll.md) |  | 
**company** | [**AccountInfoDataValueStatisticsCompany**](AccountInfoDataValueStatisticsCompany.md) |  | 
**clan** | [**AccountInfoDataValueStatisticsClan**](AccountInfoDataValueStatisticsClan.md) |  | 
**fallout** | [**AccountInfoDataValueStatisticsFallout**](AccountInfoDataValueStatisticsFallout.md) |  | [optional] 
**random** | [**AccountInfoDataValueStatisticsRandom**](AccountInfoDataValueStatisticsRandom.md) |  | [optional] 
**stronghold_defense** | [**AccountInfoDataValueStatisticsStrongholdDefense**](AccountInfoDataValueStatisticsStrongholdDefense.md) |  | 
**stronghold_skirmish** | [**AccountInfoDataValueStatisticsStrongholdSkirmish**](AccountInfoDataValueStatisticsStrongholdSkirmish.md) |  | 
**historical** | [**AccountInfoDataValueStatisticsHistorical**](AccountInfoDataValueStatisticsHistorical.md) |  | 
**frags** | **Dict[str, int]** | Number and models of vehicles destroyed by a player. Player&#39;s private data. | 
**team** | [**AccountInfoDataValueStatisticsTeam**](AccountInfoDataValueStatisticsTeam.md) |  | 
**epic** | [**AccountInfoDataValueStatisticsEpic**](AccountInfoDataValueStatisticsEpic.md) |  | [optional] 
**regular_team** | [**AccountInfoDataValueStatisticsRegularTeam**](AccountInfoDataValueStatisticsRegularTeam.md) |  | 
**globalmap_middle** | [**AccountInfoDataValueStatisticsGlobalmapMiddle**](AccountInfoDataValueStatisticsGlobalmapMiddle.md) |  | [optional] 
**globalmap_champion** | [**AccountInfoDataValueStatisticsGlobalmapChampion**](AccountInfoDataValueStatisticsGlobalmapChampion.md) |  | [optional] 
**globalmap_absolute** | [**AccountInfoDataValueStatisticsGlobalmapAbsolute**](AccountInfoDataValueStatisticsGlobalmapAbsolute.md) |  | [optional] 
**ranked_battles** | [**AccountInfoDataValueStatisticsRankedBattles**](AccountInfoDataValueStatisticsRankedBattles.md) |  | [optional] 
**ranked_battles_current** | [**AccountInfoDataValueStatisticsRankedBattlesCurrent**](AccountInfoDataValueStatisticsRankedBattlesCurrent.md) |  | [optional] 
**ranked_battles_previous** | [**AccountInfoDataValueStatisticsRankedBattlesPrevious**](AccountInfoDataValueStatisticsRankedBattlesPrevious.md) |  | [optional] 
**ranked_10x10** | [**AccountInfoDataValueStatisticsRanked10x10**](AccountInfoDataValueStatisticsRanked10x10.md) |  | [optional] 
**ranked_15x15** | [**AccountInfoDataValueStatisticsRanked15x15**](AccountInfoDataValueStatisticsRanked15x15.md) |  | [optional] 
**ranked_season_1** | [**AccountInfoDataValueStatisticsRankedSeason1**](AccountInfoDataValueStatisticsRankedSeason1.md) |  | [optional] 
**ranked_season_2** | [**AccountInfoDataValueStatisticsRankedSeason2**](AccountInfoDataValueStatisticsRankedSeason2.md) |  | [optional] 
**ranked_season_3** | [**AccountInfoDataValueStatisticsRankedSeason3**](AccountInfoDataValueStatisticsRankedSeason3.md) |  | [optional] 

## Example

```python
from wot_api_client.models.account_info_data_value_statistics import AccountInfoDataValueStatistics

# TODO update the JSON string below
json = "{}"
# create an instance of AccountInfoDataValueStatistics from a JSON string
account_info_data_value_statistics_instance = AccountInfoDataValueStatistics.from_json(json)
# print the JSON string representation of the object
print(AccountInfoDataValueStatistics.to_json())

# convert the object into a dict
account_info_data_value_statistics_dict = account_info_data_value_statistics_instance.to_dict()
# create an instance of AccountInfoDataValueStatistics from a dict
account_info_data_value_statistics_from_dict = AccountInfoDataValueStatistics.from_dict(account_info_data_value_statistics_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


