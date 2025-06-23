# StrongholdClaninfoDataValueBattlesForStrongholdsStatistics

Statistics for the clan's battles in the Stronghold mode

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_10** | **int** | Total number of battles on Tier X vehicles | 
**win_10** | **int** | Number of victories on Tier X vehicles | 
**lose_10** | **int** | Number of defeats on Tier X vehicles | 
**total_10_in_28d** | **int** | Total number of battles on Tier X vehicles within the last 28 days | 
**win_10_in_28d** | **int** | Number of victories on Tier X vehicles within the last 28 days | 
**last_time_10** | **int** | End time of the last battle held on Tier X vehicles | 

## Example

```python
from wot_api_client.models.stronghold_claninfo_data_value_battles_for_strongholds_statistics import StrongholdClaninfoDataValueBattlesForStrongholdsStatistics

# TODO update the JSON string below
json = "{}"
# create an instance of StrongholdClaninfoDataValueBattlesForStrongholdsStatistics from a JSON string
stronghold_claninfo_data_value_battles_for_strongholds_statistics_instance = StrongholdClaninfoDataValueBattlesForStrongholdsStatistics.from_json(json)
# print the JSON string representation of the object
print(StrongholdClaninfoDataValueBattlesForStrongholdsStatistics.to_json())

# convert the object into a dict
stronghold_claninfo_data_value_battles_for_strongholds_statistics_dict = stronghold_claninfo_data_value_battles_for_strongholds_statistics_instance.to_dict()
# create an instance of StrongholdClaninfoDataValueBattlesForStrongholdsStatistics from a dict
stronghold_claninfo_data_value_battles_for_strongholds_statistics_from_dict = StrongholdClaninfoDataValueBattlesForStrongholdsStatistics.from_dict(stronghold_claninfo_data_value_battles_for_strongholds_statistics_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


