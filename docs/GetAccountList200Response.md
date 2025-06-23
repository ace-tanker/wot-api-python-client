# GetAccountList200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**meta** | [**AccountListMeta**](AccountListMeta.md) |  | 
**data** | [**List[AccountListDataInner]**](AccountListDataInner.md) |  | 
**error** | [**AccountListErrorError**](AccountListErrorError.md) |  | 

## Example

```python
from wot_api_client.models.get_account_list200_response import GetAccountList200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetAccountList200Response from a JSON string
get_account_list200_response_instance = GetAccountList200Response.from_json(json)
# print the JSON string representation of the object
print(GetAccountList200Response.to_json())

# convert the object into a dict
get_account_list200_response_dict = get_account_list200_response_instance.to_dict()
# create an instance of GetAccountList200Response from a dict
get_account_list200_response_from_dict = GetAccountList200Response.from_dict(get_account_list200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


