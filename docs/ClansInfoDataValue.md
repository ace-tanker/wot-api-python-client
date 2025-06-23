# ClansInfoDataValue


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**clan_id** | **int** | Clan ID | 
**name** | **str** | Clan name | 
**tag** | **str** | Clan tag | 
**created_at** | **int** | Clan creation date | 
**color** | **str** | Clan color in HEX #RRGGBB | 
**members_count** | **int** | Number of clan members | 
**emblems** | [**ClansListDataInnerEmblems**](ClansListDataInnerEmblems.md) |  | 
**old_name** | **str** | Old clan name | 
**old_tag** | **str** | Old clan tag | 
**renamed_at** | **int** | Time (UTC) when clan name was changed | 
**description** | **str** | Clan description | 
**description_html** | **str** | Clan description in HTML | 
**motto** | **str** | Clan motto | 
**is_clan_disbanded** | **bool** | Clan has been deleted. The deleted clan data contains valid values for the following fields only: **clan_id**, **is_clan_disbanded**, **updated_at**. | 
**accepts_join_requests** | **bool** | Clan can invite players | 
**updated_at** | **int** | Time when clan details were updated | 
**creator_id** | **int** | Clan creator ID | 
**creator_name** | **str** | Clan creator&#39;s name | 
**leader_id** | **int** | Clan Commander ID | 
**leader_name** | **str** | Commander&#39;s name | 
**members** | [**ClansInfoDataValueMembers**](ClansInfoDataValueMembers.md) |  | 
**private** | [**ClansInfoDataValuePrivate**](ClansInfoDataValuePrivate.md) |  | 

## Example

```python
from wot_api_client.models.clans_info_data_value import ClansInfoDataValue

# TODO update the JSON string below
json = "{}"
# create an instance of ClansInfoDataValue from a JSON string
clans_info_data_value_instance = ClansInfoDataValue.from_json(json)
# print the JSON string representation of the object
print(ClansInfoDataValue.to_json())

# convert the object into a dict
clans_info_data_value_dict = clans_info_data_value_instance.to_dict()
# create an instance of ClansInfoDataValue from a dict
clans_info_data_value_from_dict = ClansInfoDataValue.from_dict(clans_info_data_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


