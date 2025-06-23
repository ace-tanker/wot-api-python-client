# AccountListDataInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **int** | Player ID | 
**nickname** | **str** | Player name | 

## Example

```python
from wot_api_client.models.account_list_data_inner import AccountListDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of AccountListDataInner from a JSON string
account_list_data_inner_instance = AccountListDataInner.from_json(json)
# print the JSON string representation of the object
print(AccountListDataInner.to_json())

# convert the object into a dict
account_list_data_inner_dict = account_list_data_inner_instance.to_dict()
# create an instance of AccountListDataInner from a dict
account_list_data_inner_from_dict = AccountListDataInner.from_dict(account_list_data_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


