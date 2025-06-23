# ClansInfoDataValuePrivateClanTreasury

Clan Treasury

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gold** | **int** | Amount of gold in the сlan Treasury | 
**credits** | **int** | Amount of credits in the сlan Treasury | 
**crystal** | **int** | Number of bonds in the сlan Treasury | 

## Example

```python
from wot_api_client.models.clans_info_data_value_private_clan_treasury import ClansInfoDataValuePrivateClanTreasury

# TODO update the JSON string below
json = "{}"
# create an instance of ClansInfoDataValuePrivateClanTreasury from a JSON string
clans_info_data_value_private_clan_treasury_instance = ClansInfoDataValuePrivateClanTreasury.from_json(json)
# print the JSON string representation of the object
print(ClansInfoDataValuePrivateClanTreasury.to_json())

# convert the object into a dict
clans_info_data_value_private_clan_treasury_dict = clans_info_data_value_private_clan_treasury_instance.to_dict()
# create an instance of ClansInfoDataValuePrivateClanTreasury from a dict
clans_info_data_value_private_clan_treasury_from_dict = ClansInfoDataValuePrivateClanTreasury.from_dict(clans_info_data_value_private_clan_treasury_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


