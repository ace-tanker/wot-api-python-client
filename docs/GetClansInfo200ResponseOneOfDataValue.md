# GetClansInfo200ResponseOneOfDataValue


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**clan_id** | **int** | Clan ID | 
**name** | **str** | Clan name | 
**tag** | **str** | Clan tag | 
**created_at** | **int** | Clan creation date | 
**color** | **str** | Clan color in HEX #RRGGBB | 
**members_count** | **int** | Number of clan members | 
**emblems** | [**GetClansList200ResponseOneOfDataInnerEmblems**](GetClansList200ResponseOneOfDataInnerEmblems.md) |  | 
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
**members** | [**GetClansInfo200ResponseOneOfDataValueMembers**](GetClansInfo200ResponseOneOfDataValueMembers.md) |  | 
**private** | [**GetClansInfo200ResponseOneOfDataValuePrivate**](GetClansInfo200ResponseOneOfDataValuePrivate.md) |  | 

## Example

```python
from wot_api_client.models.get_clans_info200_response_one_of_data_value import GetClansInfo200ResponseOneOfDataValue

# TODO update the JSON string below
json = "{}"
# create an instance of GetClansInfo200ResponseOneOfDataValue from a JSON string
get_clans_info200_response_one_of_data_value_instance = GetClansInfo200ResponseOneOfDataValue.from_json(json)
# print the JSON string representation of the object
print(GetClansInfo200ResponseOneOfDataValue.to_json())

# convert the object into a dict
get_clans_info200_response_one_of_data_value_dict = get_clans_info200_response_one_of_data_value_instance.to_dict()
# create an instance of GetClansInfo200ResponseOneOfDataValue from a dict
get_clans_info200_response_one_of_data_value_from_dict = GetClansInfo200ResponseOneOfDataValue.from_dict(get_clans_info200_response_one_of_data_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


