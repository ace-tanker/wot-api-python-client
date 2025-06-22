# GetGlobalmapProvinces200ResponseOneOfDataInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**arena_id** | **str** | Map ID | 
**arena_name** | **str** | Localized map name | 
**daily_revenue** | **int** | Daily income | 
**front_id** | **str** | Front ID | 
**front_name** | **str** | Front name | 
**revenue_level** | **int** | Income level from 0 to 11. 0 value means that income was not raised. | 
**prime_time** | **str** | Prime Time in UTC | 
**province_id** | **str** | Province ID | 
**province_name** | **str** | Province name | 
**landing_type** | **str** | Landing type: auction, tournament or null | 
**world_redivision** | **bool** | Indicates if Repartition of the World is active | 
**current_min_bet** | **int** | Current minimum bid | 
**last_won_bet** | **int** | Last winning bid | 
**neighbours** | **List[str]** | List of adjacent provinces&#39; IDs | 
**uri** | **str** | Relative link to province | 
**round_number** | **int** | Round | 
**battles_start_at** | **str** | Battles start time in UTC | 
**status** | **str** | Tournament status: STARTED, FINISHED or null | 
**max_bets** | **int** | Maximum number of bids | 
**competitors** | **List[int]** | List of IDs of participating clans | 
**attackers** | **List[int]** | List of IDs of attacking clans | 
**active_battles** | [**List[GetGlobalmapProvinces200ResponseOneOfDataInnerActiveBattlesInner]**](GetGlobalmapProvinces200ResponseOneOfDataInnerActiveBattlesInner.md) | Current battles | 
**owner_clan_id** | **int** | Owning clan ID | 
**is_borders_disabled** | **bool** | Province borders are closed | 
**pillage_end_at** | **str** | Date when province will restore its revenue after ransack | 
**server** | **str** | Server ID | 

## Example

```python
from wot_api_client.models.get_globalmap_provinces200_response_one_of_data_inner import GetGlobalmapProvinces200ResponseOneOfDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetGlobalmapProvinces200ResponseOneOfDataInner from a JSON string
get_globalmap_provinces200_response_one_of_data_inner_instance = GetGlobalmapProvinces200ResponseOneOfDataInner.from_json(json)
# print the JSON string representation of the object
print(GetGlobalmapProvinces200ResponseOneOfDataInner.to_json())

# convert the object into a dict
get_globalmap_provinces200_response_one_of_data_inner_dict = get_globalmap_provinces200_response_one_of_data_inner_instance.to_dict()
# create an instance of GetGlobalmapProvinces200ResponseOneOfDataInner from a dict
get_globalmap_provinces200_response_one_of_data_inner_from_dict = GetGlobalmapProvinces200ResponseOneOfDataInner.from_dict(get_globalmap_provinces200_response_one_of_data_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


