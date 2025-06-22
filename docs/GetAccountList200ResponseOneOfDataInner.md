# GetAccountList200ResponseOneOfDataInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **int** | Player ID | 
**nickname** | **str** | Player name | 

## Example

```python
from wot_api_client.models.get_account_list200_response_one_of_data_inner import GetAccountList200ResponseOneOfDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetAccountList200ResponseOneOfDataInner from a JSON string
get_account_list200_response_one_of_data_inner_instance = GetAccountList200ResponseOneOfDataInner.from_json(json)
# print the JSON string representation of the object
print(GetAccountList200ResponseOneOfDataInner.to_json())

# convert the object into a dict
get_account_list200_response_one_of_data_inner_dict = get_account_list200_response_one_of_data_inner_instance.to_dict()
# create an instance of GetAccountList200ResponseOneOfDataInner from a dict
get_account_list200_response_one_of_data_inner_from_dict = GetAccountList200ResponseOneOfDataInner.from_dict(get_account_list200_response_one_of_data_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


