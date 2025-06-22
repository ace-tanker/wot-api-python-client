# GetStrongholdClaninfo200ResponseOneOfDataValueBattlesSeriesForStrongholdsStatistics

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
from wot_api_client.models.get_stronghold_claninfo200_response_one_of_data_value_battles_series_for_strongholds_statistics import GetStrongholdClaninfo200ResponseOneOfDataValueBattlesSeriesForStrongholdsStatistics

# TODO update the JSON string below
json = "{}"
# create an instance of GetStrongholdClaninfo200ResponseOneOfDataValueBattlesSeriesForStrongholdsStatistics from a JSON string
get_stronghold_claninfo200_response_one_of_data_value_battles_series_for_strongholds_statistics_instance = GetStrongholdClaninfo200ResponseOneOfDataValueBattlesSeriesForStrongholdsStatistics.from_json(json)
# print the JSON string representation of the object
print(GetStrongholdClaninfo200ResponseOneOfDataValueBattlesSeriesForStrongholdsStatistics.to_json())

# convert the object into a dict
get_stronghold_claninfo200_response_one_of_data_value_battles_series_for_strongholds_statistics_dict = get_stronghold_claninfo200_response_one_of_data_value_battles_series_for_strongholds_statistics_instance.to_dict()
# create an instance of GetStrongholdClaninfo200ResponseOneOfDataValueBattlesSeriesForStrongholdsStatistics from a dict
get_stronghold_claninfo200_response_one_of_data_value_battles_series_for_strongholds_statistics_from_dict = GetStrongholdClaninfo200ResponseOneOfDataValueBattlesSeriesForStrongholdsStatistics.from_dict(get_stronghold_claninfo200_response_one_of_data_value_battles_series_for_strongholds_statistics_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


