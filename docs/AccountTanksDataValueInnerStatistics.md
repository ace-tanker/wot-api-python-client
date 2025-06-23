# AccountTanksDataValueInnerStatistics

Vehicle statistics

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**battles** | **int** | Battles fought | 
**wins** | **int** | Victories | 

## Example

```python
from wot_api_client.models.account_tanks_data_value_inner_statistics import AccountTanksDataValueInnerStatistics

# TODO update the JSON string below
json = "{}"
# create an instance of AccountTanksDataValueInnerStatistics from a JSON string
account_tanks_data_value_inner_statistics_instance = AccountTanksDataValueInnerStatistics.from_json(json)
# print the JSON string representation of the object
print(AccountTanksDataValueInnerStatistics.to_json())

# convert the object into a dict
account_tanks_data_value_inner_statistics_dict = account_tanks_data_value_inner_statistics_instance.to_dict()
# create an instance of AccountTanksDataValueInnerStatistics from a dict
account_tanks_data_value_inner_statistics_from_dict = AccountTanksDataValueInnerStatistics.from_dict(account_tanks_data_value_inner_statistics_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


