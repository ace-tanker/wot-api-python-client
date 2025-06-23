# StrongholdClaninfoDataValue


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**clan_id** | **int** | Clan ID | 
**clan_name** | **str** | Clan name | 
**clan_tag** | **str** | Clan tag | 
**stronghold_level** | **int** | Stronghold&#39;s level | 
**stronghold_buildings_level** | **int** | Total level of the Stronghold&#39;s structures | 
**command_center_arena_id** | **str** | Map ID associated with the Command Center construction site | 
**building_slots** | [**List[StrongholdClaninfoDataValueBuildingSlotsInner]**](StrongholdClaninfoDataValueBuildingSlotsInner.md) | Information about the Stronghold&#39;s construction sites | 
**skirmish_statistics** | [**StrongholdClaninfoDataValueSkirmishStatistics**](StrongholdClaninfoDataValueSkirmishStatistics.md) |  | 
**battles_for_strongholds_statistics** | [**StrongholdClaninfoDataValueBattlesForStrongholdsStatistics**](StrongholdClaninfoDataValueBattlesForStrongholdsStatistics.md) |  | 
**battles_series_for_strongholds_statistics** | [**StrongholdClaninfoDataValueBattlesSeriesForStrongholdsStatistics**](StrongholdClaninfoDataValueBattlesSeriesForStrongholdsStatistics.md) |  | 

## Example

```python
from wot_api_client.models.stronghold_claninfo_data_value import StrongholdClaninfoDataValue

# TODO update the JSON string below
json = "{}"
# create an instance of StrongholdClaninfoDataValue from a JSON string
stronghold_claninfo_data_value_instance = StrongholdClaninfoDataValue.from_json(json)
# print the JSON string representation of the object
print(StrongholdClaninfoDataValue.to_json())

# convert the object into a dict
stronghold_claninfo_data_value_dict = stronghold_claninfo_data_value_instance.to_dict()
# create an instance of StrongholdClaninfoDataValue from a dict
stronghold_claninfo_data_value_from_dict = StrongholdClaninfoDataValue.from_dict(stronghold_claninfo_data_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


