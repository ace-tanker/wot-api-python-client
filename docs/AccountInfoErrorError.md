# AccountInfoErrorError

Limit of passed-in **account_id** IDs exceeded. Maximum: 100.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **float** |  | 
**message** | **str** |  | 
**var_field** | **str** |  | 
**value** | **str** |  | 

## Example

```python
from wot_api_client.models.account_info_error_error import AccountInfoErrorError

# TODO update the JSON string below
json = "{}"
# create an instance of AccountInfoErrorError from a JSON string
account_info_error_error_instance = AccountInfoErrorError.from_json(json)
# print the JSON string representation of the object
print(AccountInfoErrorError.to_json())

# convert the object into a dict
account_info_error_error_dict = account_info_error_error_instance.to_dict()
# create an instance of AccountInfoErrorError from a dict
account_info_error_error_from_dict = AccountInfoErrorError.from_dict(account_info_error_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


