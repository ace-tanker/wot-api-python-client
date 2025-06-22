# GetClansAccountinfo200ResponseOneOfDataValueClan

Short clan info

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

## Example

```python
from wot_api_client.models.get_clans_accountinfo200_response_one_of_data_value_clan import GetClansAccountinfo200ResponseOneOfDataValueClan

# TODO update the JSON string below
json = "{}"
# create an instance of GetClansAccountinfo200ResponseOneOfDataValueClan from a JSON string
get_clans_accountinfo200_response_one_of_data_value_clan_instance = GetClansAccountinfo200ResponseOneOfDataValueClan.from_json(json)
# print the JSON string representation of the object
print(GetClansAccountinfo200ResponseOneOfDataValueClan.to_json())

# convert the object into a dict
get_clans_accountinfo200_response_one_of_data_value_clan_dict = get_clans_accountinfo200_response_one_of_data_value_clan_instance.to_dict()
# create an instance of GetClansAccountinfo200ResponseOneOfDataValueClan from a dict
get_clans_accountinfo200_response_one_of_data_value_clan_from_dict = GetClansAccountinfo200ResponseOneOfDataValueClan.from_dict(get_clans_accountinfo200_response_one_of_data_value_clan_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


