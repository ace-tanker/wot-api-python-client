# GetClansInfo200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**meta** | [**GetAccountList200ResponseOneOfMeta**](GetAccountList200ResponseOneOfMeta.md) |  | 
**data** | [**Dict[str, GetClansInfo200ResponseOneOfDataValue]**](GetClansInfo200ResponseOneOfDataValue.md) |  | 
**error** | [**GetAccountList200ResponseOneOf1Error**](GetAccountList200ResponseOneOf1Error.md) |  | 

## Example

```python
from wot_api_client.models.get_clans_info200_response import GetClansInfo200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetClansInfo200Response from a JSON string
get_clans_info200_response_instance = GetClansInfo200Response.from_json(json)
# print the JSON string representation of the object
print(GetClansInfo200Response.to_json())

# convert the object into a dict
get_clans_info200_response_dict = get_clans_info200_response_instance.to_dict()
# create an instance of GetClansInfo200Response from a dict
get_clans_info200_response_from_dict = GetClansInfo200Response.from_dict(get_clans_info200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


