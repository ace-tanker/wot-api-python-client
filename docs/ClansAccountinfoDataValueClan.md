# ClansAccountinfoDataValueClan

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
**emblems** | [**ClansListDataInnerEmblems**](ClansListDataInnerEmblems.md) |  | 

## Example

```python
from wot_api_client.models.clans_accountinfo_data_value_clan import ClansAccountinfoDataValueClan

# TODO update the JSON string below
json = "{}"
# create an instance of ClansAccountinfoDataValueClan from a JSON string
clans_accountinfo_data_value_clan_instance = ClansAccountinfoDataValueClan.from_json(json)
# print the JSON string representation of the object
print(ClansAccountinfoDataValueClan.to_json())

# convert the object into a dict
clans_accountinfo_data_value_clan_dict = clans_accountinfo_data_value_clan_instance.to_dict()
# create an instance of ClansAccountinfoDataValueClan from a dict
clans_accountinfo_data_value_clan_from_dict = ClansAccountinfoDataValueClan.from_dict(clans_accountinfo_data_value_clan_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


