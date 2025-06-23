# AccountListOk


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**meta** | [**AccountListMeta**](AccountListMeta.md) |  | 
**data** | [**List[AccountListDataInner]**](AccountListDataInner.md) |  | 

## Example

```python
from wot_api_client.models.account_list_ok import AccountListOk

# TODO update the JSON string below
json = "{}"
# create an instance of AccountListOk from a JSON string
account_list_ok_instance = AccountListOk.from_json(json)
# print the JSON string representation of the object
print(AccountListOk.to_json())

# convert the object into a dict
account_list_ok_dict = account_list_ok_instance.to_dict()
# create an instance of AccountListOk from a dict
account_list_ok_from_dict = AccountListOk.from_dict(account_list_ok_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


