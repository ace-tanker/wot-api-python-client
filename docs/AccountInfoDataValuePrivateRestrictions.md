# AccountInfoDataValuePrivateRestrictions

Account restrictions

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chat_ban_time** | **int** | End time of chat ban | 

## Example

```python
from wot_api_client.models.account_info_data_value_private_restrictions import AccountInfoDataValuePrivateRestrictions

# TODO update the JSON string below
json = "{}"
# create an instance of AccountInfoDataValuePrivateRestrictions from a JSON string
account_info_data_value_private_restrictions_instance = AccountInfoDataValuePrivateRestrictions.from_json(json)
# print the JSON string representation of the object
print(AccountInfoDataValuePrivateRestrictions.to_json())

# convert the object into a dict
account_info_data_value_private_restrictions_dict = account_info_data_value_private_restrictions_instance.to_dict()
# create an instance of AccountInfoDataValuePrivateRestrictions from a dict
account_info_data_value_private_restrictions_from_dict = AccountInfoDataValuePrivateRestrictions.from_dict(account_info_data_value_private_restrictions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


