# AccountListErrorError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **float** |  | 
**message** | **str** |  | 
**var_field** | **str** |  | 
**value** | **str** |  | 

## Example

```python
from wot_api_client.models.account_list_error_error import AccountListErrorError

# TODO update the JSON string below
json = "{}"
# create an instance of AccountListErrorError from a JSON string
account_list_error_error_instance = AccountListErrorError.from_json(json)
# print the JSON string representation of the object
print(AccountListErrorError.to_json())

# convert the object into a dict
account_list_error_error_dict = account_list_error_error_instance.to_dict()
# create an instance of AccountListErrorError from a dict
account_list_error_error_from_dict = AccountListErrorError.from_dict(account_list_error_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


