# GetAccountTanks200ResponseOneOfDataValueInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tank_id** | **int** | Vehicle ID | 
**mark_of_mastery** | **int** | Mastery Badges:   * 0 — None  * 1 — 3rd Class   * 2 — 2nd Class  * 3 — 1st Class  * 4 — Ace Tanker | 
**statistics** | [**GetAccountTanks200ResponseOneOfDataValueInnerStatistics**](GetAccountTanks200ResponseOneOfDataValueInnerStatistics.md) |  | 

## Example

```python
from wot_api_client.models.get_account_tanks200_response_one_of_data_value_inner import GetAccountTanks200ResponseOneOfDataValueInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetAccountTanks200ResponseOneOfDataValueInner from a JSON string
get_account_tanks200_response_one_of_data_value_inner_instance = GetAccountTanks200ResponseOneOfDataValueInner.from_json(json)
# print the JSON string representation of the object
print(GetAccountTanks200ResponseOneOfDataValueInner.to_json())

# convert the object into a dict
get_account_tanks200_response_one_of_data_value_inner_dict = get_account_tanks200_response_one_of_data_value_inner_instance.to_dict()
# create an instance of GetAccountTanks200ResponseOneOfDataValueInner from a dict
get_account_tanks200_response_one_of_data_value_inner_from_dict = GetAccountTanks200ResponseOneOfDataValueInner.from_dict(get_account_tanks200_response_one_of_data_value_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


