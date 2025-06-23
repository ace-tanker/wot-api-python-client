# AccountInfoOk


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**meta** | [**AccountInfoMeta**](AccountInfoMeta.md) |  | 
**data** | [**Dict[str, AccountInfoDataValue]**](AccountInfoDataValue.md) |  | 

## Example

```python
from wot_api_client.models.account_info_ok import AccountInfoOk

# TODO update the JSON string below
json = "{}"
# create an instance of AccountInfoOk from a JSON string
account_info_ok_instance = AccountInfoOk.from_json(json)
# print the JSON string representation of the object
print(AccountInfoOk.to_json())

# convert the object into a dict
account_info_ok_dict = account_info_ok_instance.to_dict()
# create an instance of AccountInfoOk from a dict
account_info_ok_from_dict = AccountInfoOk.from_dict(account_info_ok_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


