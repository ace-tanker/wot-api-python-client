# AccountInfoDataValue


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**statistics** | [**AccountInfoDataValueStatistics**](AccountInfoDataValueStatistics.md) |  | 
**account_id** | **int** | Player account ID | 
**created_at** | **int** | Date when player&#39;s account was created | 
**updated_at** | **int** | Date when player details were updated | 
**logout_at** | **int** | End time of last game session | 
**last_battle_time** | **int** | Last battle time | 
**nickname** | **str** | Player name | 
**global_rating** | **int** | Personal rating | 
**private** | [**AccountInfoDataValuePrivate**](AccountInfoDataValuePrivate.md) |  | 
**client_language** | **str** | Language selected in the game client | 
**clan_id** | **int** | Clan ID | 

## Example

```python
from wot_api_client.models.account_info_data_value import AccountInfoDataValue

# TODO update the JSON string below
json = "{}"
# create an instance of AccountInfoDataValue from a JSON string
account_info_data_value_instance = AccountInfoDataValue.from_json(json)
# print the JSON string representation of the object
print(AccountInfoDataValue.to_json())

# convert the object into a dict
account_info_data_value_dict = account_info_data_value_instance.to_dict()
# create an instance of AccountInfoDataValue from a dict
account_info_data_value_from_dict = AccountInfoDataValue.from_dict(account_info_data_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


