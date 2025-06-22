# GetGlobalmapProvinces200ResponseOneOfDataInnerActiveBattlesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_at** | **str** | Battle start time in UTC | 
**round** | **int** | Round | 
**battle_reward** | **int** | Award | 
**clan_a** | [**GetGlobalmapProvinces200ResponseOneOfDataInnerActiveBattlesInnerClanA**](GetGlobalmapProvinces200ResponseOneOfDataInnerActiveBattlesInnerClanA.md) |  | 
**clan_b** | [**GetGlobalmapProvinces200ResponseOneOfDataInnerActiveBattlesInnerClanB**](GetGlobalmapProvinces200ResponseOneOfDataInnerActiveBattlesInnerClanB.md) |  | 

## Example

```python
from wot_api_client.models.get_globalmap_provinces200_response_one_of_data_inner_active_battles_inner import GetGlobalmapProvinces200ResponseOneOfDataInnerActiveBattlesInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetGlobalmapProvinces200ResponseOneOfDataInnerActiveBattlesInner from a JSON string
get_globalmap_provinces200_response_one_of_data_inner_active_battles_inner_instance = GetGlobalmapProvinces200ResponseOneOfDataInnerActiveBattlesInner.from_json(json)
# print the JSON string representation of the object
print(GetGlobalmapProvinces200ResponseOneOfDataInnerActiveBattlesInner.to_json())

# convert the object into a dict
get_globalmap_provinces200_response_one_of_data_inner_active_battles_inner_dict = get_globalmap_provinces200_response_one_of_data_inner_active_battles_inner_instance.to_dict()
# create an instance of GetGlobalmapProvinces200ResponseOneOfDataInnerActiveBattlesInner from a dict
get_globalmap_provinces200_response_one_of_data_inner_active_battles_inner_from_dict = GetGlobalmapProvinces200ResponseOneOfDataInnerActiveBattlesInner.from_dict(get_globalmap_provinces200_response_one_of_data_inner_active_battles_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


