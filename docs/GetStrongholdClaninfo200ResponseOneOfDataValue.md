# GetStrongholdClaninfo200ResponseOneOfDataValue


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**clan_id** | **int** | Clan ID | 
**clan_name** | **str** | Clan name | 
**clan_tag** | **str** | Clan tag | 
**stronghold_level** | **int** | Stronghold&#39;s level | 
**stronghold_buildings_level** | **int** | Total level of the Stronghold&#39;s structures | 
**command_center_arena_id** | **str** | Map ID associated with the Command Center construction site | 
**building_slots** | [**List[GetStrongholdClaninfo200ResponseOneOfDataValueBuildingSlotsInner]**](GetStrongholdClaninfo200ResponseOneOfDataValueBuildingSlotsInner.md) | Information about the Stronghold&#39;s construction sites | 
**skirmish_statistics** | [**GetStrongholdClaninfo200ResponseOneOfDataValueSkirmishStatistics**](GetStrongholdClaninfo200ResponseOneOfDataValueSkirmishStatistics.md) |  | 
**battles_for_strongholds_statistics** | [**GetStrongholdClaninfo200ResponseOneOfDataValueBattlesForStrongholdsStatistics**](GetStrongholdClaninfo200ResponseOneOfDataValueBattlesForStrongholdsStatistics.md) |  | 
**battles_series_for_strongholds_statistics** | [**GetStrongholdClaninfo200ResponseOneOfDataValueBattlesSeriesForStrongholdsStatistics**](GetStrongholdClaninfo200ResponseOneOfDataValueBattlesSeriesForStrongholdsStatistics.md) |  | 

## Example

```python
from wot_api_client.models.get_stronghold_claninfo200_response_one_of_data_value import GetStrongholdClaninfo200ResponseOneOfDataValue

# TODO update the JSON string below
json = "{}"
# create an instance of GetStrongholdClaninfo200ResponseOneOfDataValue from a JSON string
get_stronghold_claninfo200_response_one_of_data_value_instance = GetStrongholdClaninfo200ResponseOneOfDataValue.from_json(json)
# print the JSON string representation of the object
print(GetStrongholdClaninfo200ResponseOneOfDataValue.to_json())

# convert the object into a dict
get_stronghold_claninfo200_response_one_of_data_value_dict = get_stronghold_claninfo200_response_one_of_data_value_instance.to_dict()
# create an instance of GetStrongholdClaninfo200ResponseOneOfDataValue from a dict
get_stronghold_claninfo200_response_one_of_data_value_from_dict = GetStrongholdClaninfo200ResponseOneOfDataValue.from_dict(get_stronghold_claninfo200_response_one_of_data_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


