# StrongholdClaninfoDataValueSkirmishStatistics

Clan's skirmish statistics

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_10** | **int** | Total number of battles on Tier X vehicles | 
**win_10** | **int** | Number of victories on Tier X vehicles | 
**lose_10** | **int** | Number of defeats on Tier X vehicles | 
**total_8** | **int** | Total number of battles on Tier VIII vehicles | 
**win_8** | **int** | Number of victories on Tier VIII vehicles | 
**lose_8** | **int** | Number of defeats on Tier VIII vehicles | 
**total_6** | **int** | Total number of battles on Tier VI vehicles | 
**win_6** | **int** | Number of victories on Tier VI vehicles | 
**lose_6** | **int** | Number of defeats on Tier VI vehicles | 
**total_10_in_28d** | **int** | Total number of battles on Tier X vehicles within the last 28 days | 
**win_10_in_28d** | **int** | Number of victories on Tier X vehicles within the last 28 days | 
**total_8_in_28d** | **int** | Total number of battles on Tier VIII vehicles within the last 28 days | 
**win_8_in_28d** | **int** | Number of victories on Tier VIII vehicles within the last 28 days | 
**total_6_in_28d** | **int** | Total number of battles on Tier VI vehicles within the last 28 days | 
**win_6_in_28d** | **int** | Number of victories on Tier VI vehicles within the last 28 days | 
**last_time_10** | **int** | End time of the last battle held on Tier X vehicles | 
**last_time_8** | **int** | End time of the last battle held on Tier VIII vehicles | 
**last_time_6** | **int** | End time of the last battle held on Tier VI vehicles | 

## Example

```python
from wot_api_client.models.stronghold_claninfo_data_value_skirmish_statistics import StrongholdClaninfoDataValueSkirmishStatistics

# TODO update the JSON string below
json = "{}"
# create an instance of StrongholdClaninfoDataValueSkirmishStatistics from a JSON string
stronghold_claninfo_data_value_skirmish_statistics_instance = StrongholdClaninfoDataValueSkirmishStatistics.from_json(json)
# print the JSON string representation of the object
print(StrongholdClaninfoDataValueSkirmishStatistics.to_json())

# convert the object into a dict
stronghold_claninfo_data_value_skirmish_statistics_dict = stronghold_claninfo_data_value_skirmish_statistics_instance.to_dict()
# create an instance of StrongholdClaninfoDataValueSkirmishStatistics from a dict
stronghold_claninfo_data_value_skirmish_statistics_from_dict = StrongholdClaninfoDataValueSkirmishStatistics.from_dict(stronghold_claninfo_data_value_skirmish_statistics_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


