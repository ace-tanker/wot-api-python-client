# AccountListError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**error** | [**AccountListErrorError**](AccountListErrorError.md) |  | 

## Example

```python
from wot_api_client.models.account_list_error import AccountListError

# TODO update the JSON string below
json = "{}"
# create an instance of AccountListError from a JSON string
account_list_error_instance = AccountListError.from_json(json)
# print the JSON string representation of the object
print(AccountListError.to_json())

# convert the object into a dict
account_list_error_dict = account_list_error_instance.to_dict()
# create an instance of AccountListError from a dict
account_list_error_from_dict = AccountListError.from_dict(account_list_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


