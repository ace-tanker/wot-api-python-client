# GetAccountInfo200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**meta** | [**AccountInfoMeta**](AccountInfoMeta.md) |  | 
**data** | [**Dict[str, AccountInfoDataValue]**](AccountInfoDataValue.md) |  | 
**error** | [**AccountInfoErrorError**](AccountInfoErrorError.md) |  | 

## Example

```python
from wot_api_client.models.get_account_info200_response import GetAccountInfo200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetAccountInfo200Response from a JSON string
get_account_info200_response_instance = GetAccountInfo200Response.from_json(json)
# print the JSON string representation of the object
print(GetAccountInfo200Response.to_json())

# convert the object into a dict
get_account_info200_response_dict = get_account_info200_response_instance.to_dict()
# create an instance of GetAccountInfo200Response from a dict
get_account_info200_response_from_dict = GetAccountInfo200Response.from_dict(get_account_info200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


