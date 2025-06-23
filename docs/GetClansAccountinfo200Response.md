# GetClansAccountinfo200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**meta** | [**ClansAccountinfoMeta**](ClansAccountinfoMeta.md) |  | 
**data** | [**Dict[str, ClansAccountinfoDataValue]**](ClansAccountinfoDataValue.md) |  | 
**error** | **object** |  | 

## Example

```python
from wot_api_client.models.get_clans_accountinfo200_response import GetClansAccountinfo200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetClansAccountinfo200Response from a JSON string
get_clans_accountinfo200_response_instance = GetClansAccountinfo200Response.from_json(json)
# print the JSON string representation of the object
print(GetClansAccountinfo200Response.to_json())

# convert the object into a dict
get_clans_accountinfo200_response_dict = get_clans_accountinfo200_response_instance.to_dict()
# create an instance of GetClansAccountinfo200Response from a dict
get_clans_accountinfo200_response_from_dict = GetClansAccountinfo200Response.from_dict(get_clans_accountinfo200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


