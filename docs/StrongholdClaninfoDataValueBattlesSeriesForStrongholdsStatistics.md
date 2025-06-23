# StrongholdClaninfoDataValueBattlesSeriesForStrongholdsStatistics

Statistics for skirmishes against the clan's Stronghold

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_10** | **int** | Total number of battles on Tier X vehicles | 
**win_10** | **int** | Number of victories on Tier X vehicles | 
**lose_10** | **int** | Number of defeats on Tier X vehicles | 
**total_10_in_28d** | **int** | Total number of battles on Tier X vehicles within the last 28 days | 
**win_10_in_28d** | **int** | Number of victories on Tier X vehicles within the last 28 days | 

## Example

```python
from wot_api_client.models.stronghold_claninfo_data_value_battles_series_for_strongholds_statistics import StrongholdClaninfoDataValueBattlesSeriesForStrongholdsStatistics

# TODO update the JSON string below
json = "{}"
# create an instance of StrongholdClaninfoDataValueBattlesSeriesForStrongholdsStatistics from a JSON string
stronghold_claninfo_data_value_battles_series_for_strongholds_statistics_instance = StrongholdClaninfoDataValueBattlesSeriesForStrongholdsStatistics.from_json(json)
# print the JSON string representation of the object
print(StrongholdClaninfoDataValueBattlesSeriesForStrongholdsStatistics.to_json())

# convert the object into a dict
stronghold_claninfo_data_value_battles_series_for_strongholds_statistics_dict = stronghold_claninfo_data_value_battles_series_for_strongholds_statistics_instance.to_dict()
# create an instance of StrongholdClaninfoDataValueBattlesSeriesForStrongholdsStatistics from a dict
stronghold_claninfo_data_value_battles_series_for_strongholds_statistics_from_dict = StrongholdClaninfoDataValueBattlesSeriesForStrongholdsStatistics.from_dict(stronghold_claninfo_data_value_battles_series_for_strongholds_statistics_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


