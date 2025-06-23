# AccountListErrorErrorOneOf1

**Search** parameter is not long enough. Allowed value depends on **type** parameter.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **float** |  | 
**message** | **str** |  | 
**var_field** | **str** |  | 
**value** | **str** |  | 

## Example

```python
from wot_api_client.models.account_list_error_error_one_of1 import AccountListErrorErrorOneOf1

# TODO update the JSON string below
json = "{}"
# create an instance of AccountListErrorErrorOneOf1 from a JSON string
account_list_error_error_one_of1_instance = AccountListErrorErrorOneOf1.from_json(json)
# print the JSON string representation of the object
print(AccountListErrorErrorOneOf1.to_json())

# convert the object into a dict
account_list_error_error_one_of1_dict = account_list_error_error_one_of1_instance.to_dict()
# create an instance of AccountListErrorErrorOneOf1 from a dict
account_list_error_error_one_of1_from_dict = AccountListErrorErrorOneOf1.from_dict(account_list_error_error_one_of1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


