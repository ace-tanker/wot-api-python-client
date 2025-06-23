# AccountTanksError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**error** | **object** |  | 

## Example

```python
from wot_api_client.models.account_tanks_error import AccountTanksError

# TODO update the JSON string below
json = "{}"
# create an instance of AccountTanksError from a JSON string
account_tanks_error_instance = AccountTanksError.from_json(json)
# print the JSON string representation of the object
print(AccountTanksError.to_json())

# convert the object into a dict
account_tanks_error_dict = account_tanks_error_instance.to_dict()
# create an instance of AccountTanksError from a dict
account_tanks_error_from_dict = AccountTanksError.from_dict(account_tanks_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


