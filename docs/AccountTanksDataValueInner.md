# AccountTanksDataValueInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tank_id** | **int** | Vehicle ID | 
**mark_of_mastery** | **int** | Mastery Badges:   * 0 — None  * 1 — 3rd Class   * 2 — 2nd Class  * 3 — 1st Class  * 4 — Ace Tanker | 
**statistics** | [**AccountTanksDataValueInnerStatistics**](AccountTanksDataValueInnerStatistics.md) |  | 

## Example

```python
from wot_api_client.models.account_tanks_data_value_inner import AccountTanksDataValueInner

# TODO update the JSON string below
json = "{}"
# create an instance of AccountTanksDataValueInner from a JSON string
account_tanks_data_value_inner_instance = AccountTanksDataValueInner.from_json(json)
# print the JSON string representation of the object
print(AccountTanksDataValueInner.to_json())

# convert the object into a dict
account_tanks_data_value_inner_dict = account_tanks_data_value_inner_instance.to_dict()
# create an instance of AccountTanksDataValueInner from a dict
account_tanks_data_value_inner_from_dict = AccountTanksDataValueInner.from_dict(account_tanks_data_value_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


