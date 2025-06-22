# GetAccountList200ResponseOneOf1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**error** | [**GetAccountList200ResponseOneOf1Error**](GetAccountList200ResponseOneOf1Error.md) |  | 

## Example

```python
from wot_api_client.models.get_account_list200_response_one_of1 import GetAccountList200ResponseOneOf1

# TODO update the JSON string below
json = "{}"
# create an instance of GetAccountList200ResponseOneOf1 from a JSON string
get_account_list200_response_one_of1_instance = GetAccountList200ResponseOneOf1.from_json(json)
# print the JSON string representation of the object
print(GetAccountList200ResponseOneOf1.to_json())

# convert the object into a dict
get_account_list200_response_one_of1_dict = get_account_list200_response_one_of1_instance.to_dict()
# create an instance of GetAccountList200ResponseOneOf1 from a dict
get_account_list200_response_one_of1_from_dict = GetAccountList200ResponseOneOf1.from_dict(get_account_list200_response_one_of1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


