# AccountListErrorErrorOneOf

**Search** parameter not specified with no account_id

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **float** |  | 
**message** | **str** |  | 
**var_field** | **str** |  | 
**value** | **str** |  | 

## Example

```python
from wot_api_client.models.account_list_error_error_one_of import AccountListErrorErrorOneOf

# TODO update the JSON string below
json = "{}"
# create an instance of AccountListErrorErrorOneOf from a JSON string
account_list_error_error_one_of_instance = AccountListErrorErrorOneOf.from_json(json)
# print the JSON string representation of the object
print(AccountListErrorErrorOneOf.to_json())

# convert the object into a dict
account_list_error_error_one_of_dict = account_list_error_error_one_of_instance.to_dict()
# create an instance of AccountListErrorErrorOneOf from a dict
account_list_error_error_one_of_from_dict = AccountListErrorErrorOneOf.from_dict(account_list_error_error_one_of_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


