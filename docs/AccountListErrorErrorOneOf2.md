# AccountListErrorErrorOneOf2

Limit of specified names in **search** parameter exceeded ( >100 )

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **float** |  | 
**message** | **str** |  | 
**var_field** | **str** |  | 
**value** | **str** |  | 

## Example

```python
from wot_api_client.models.account_list_error_error_one_of2 import AccountListErrorErrorOneOf2

# TODO update the JSON string below
json = "{}"
# create an instance of AccountListErrorErrorOneOf2 from a JSON string
account_list_error_error_one_of2_instance = AccountListErrorErrorOneOf2.from_json(json)
# print the JSON string representation of the object
print(AccountListErrorErrorOneOf2.to_json())

# convert the object into a dict
account_list_error_error_one_of2_dict = account_list_error_error_one_of2_instance.to_dict()
# create an instance of AccountListErrorErrorOneOf2 from a dict
account_list_error_error_one_of2_from_dict = AccountListErrorErrorOneOf2.from_dict(account_list_error_error_one_of2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


