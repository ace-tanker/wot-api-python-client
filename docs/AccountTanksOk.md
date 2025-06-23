# AccountTanksOk


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**meta** | [**AccountTanksMeta**](AccountTanksMeta.md) |  | 
**data** | **Dict[str, Optional[List[AccountTanksDataValueInner]]]** |  | 

## Example

```python
from wot_api_client.models.account_tanks_ok import AccountTanksOk

# TODO update the JSON string below
json = "{}"
# create an instance of AccountTanksOk from a JSON string
account_tanks_ok_instance = AccountTanksOk.from_json(json)
# print the JSON string representation of the object
print(AccountTanksOk.to_json())

# convert the object into a dict
account_tanks_ok_dict = account_tanks_ok_instance.to_dict()
# create an instance of AccountTanksOk from a dict
account_tanks_ok_from_dict = AccountTanksOk.from_dict(account_tanks_ok_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


