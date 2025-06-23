# AccountInfoError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**error** | [**AccountInfoErrorError**](AccountInfoErrorError.md) |  | 

## Example

```python
from wot_api_client.models.account_info_error import AccountInfoError

# TODO update the JSON string below
json = "{}"
# create an instance of AccountInfoError from a JSON string
account_info_error_instance = AccountInfoError.from_json(json)
# print the JSON string representation of the object
print(AccountInfoError.to_json())

# convert the object into a dict
account_info_error_dict = account_info_error_instance.to_dict()
# create an instance of AccountInfoError from a dict
account_info_error_from_dict = AccountInfoError.from_dict(account_info_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


