# ClansInfoDataValuePrivate

Restricted clan information

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**treasury** | **int** | Amount of gold in the сlan Treasury | 
**clan_treasury** | [**ClansInfoDataValuePrivateClanTreasury**](ClansInfoDataValuePrivateClanTreasury.md) |  | 
**online_members** | **List[int]** | List of clan members with an active game session in World of Tanks. | [optional] 

## Example

```python
from wot_api_client.models.clans_info_data_value_private import ClansInfoDataValuePrivate

# TODO update the JSON string below
json = "{}"
# create an instance of ClansInfoDataValuePrivate from a JSON string
clans_info_data_value_private_instance = ClansInfoDataValuePrivate.from_json(json)
# print the JSON string representation of the object
print(ClansInfoDataValuePrivate.to_json())

# convert the object into a dict
clans_info_data_value_private_dict = clans_info_data_value_private_instance.to_dict()
# create an instance of ClansInfoDataValuePrivate from a dict
clans_info_data_value_private_from_dict = ClansInfoDataValuePrivate.from_dict(clans_info_data_value_private_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


