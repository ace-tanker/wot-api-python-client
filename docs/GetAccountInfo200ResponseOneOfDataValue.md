# GetAccountInfo200ResponseOneOfDataValue


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**statistics** | [**GetAccountInfo200ResponseOneOfDataValueStatistics**](GetAccountInfo200ResponseOneOfDataValueStatistics.md) |  | 
**account_id** | **int** | Player account ID | 
**created_at** | **int** | Date when player&#39;s account was created | 
**updated_at** | **int** | Date when player details were updated | 
**logout_at** | **int** | End time of last game session | 
**last_battle_time** | **int** | Last battle time | 
**nickname** | **str** | Player name | 
**global_rating** | **int** | Personal rating | 
**private** | [**GetAccountInfo200ResponseOneOfDataValuePrivate**](GetAccountInfo200ResponseOneOfDataValuePrivate.md) |  | 
**client_language** | **str** | Language selected in the game client | 
**clan_id** | **int** | Clan ID | 

## Example

```python
from wot_api_client.models.get_account_info200_response_one_of_data_value import GetAccountInfo200ResponseOneOfDataValue

# TODO update the JSON string below
json = "{}"
# create an instance of GetAccountInfo200ResponseOneOfDataValue from a JSON string
get_account_info200_response_one_of_data_value_instance = GetAccountInfo200ResponseOneOfDataValue.from_json(json)
# print the JSON string representation of the object
print(GetAccountInfo200ResponseOneOfDataValue.to_json())

# convert the object into a dict
get_account_info200_response_one_of_data_value_dict = get_account_info200_response_one_of_data_value_instance.to_dict()
# create an instance of GetAccountInfo200ResponseOneOfDataValue from a dict
get_account_info200_response_one_of_data_value_from_dict = GetAccountInfo200ResponseOneOfDataValue.from_dict(get_account_info200_response_one_of_data_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


