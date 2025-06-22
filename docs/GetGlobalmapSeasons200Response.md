# GetGlobalmapSeasons200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**meta** | [**GetGlobalmapSeasons200ResponseOneOfMeta**](GetGlobalmapSeasons200ResponseOneOfMeta.md) |  | 
**data** | [**List[GetGlobalmapSeasons200ResponseOneOfDataInner]**](GetGlobalmapSeasons200ResponseOneOfDataInner.md) |  | 
**error** | [**GetAccountList200ResponseOneOf1Error**](GetAccountList200ResponseOneOf1Error.md) |  | 

## Example

```python
from wot_api_client.models.get_globalmap_seasons200_response import GetGlobalmapSeasons200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetGlobalmapSeasons200Response from a JSON string
get_globalmap_seasons200_response_instance = GetGlobalmapSeasons200Response.from_json(json)
# print the JSON string representation of the object
print(GetGlobalmapSeasons200Response.to_json())

# convert the object into a dict
get_globalmap_seasons200_response_dict = get_globalmap_seasons200_response_instance.to_dict()
# create an instance of GetGlobalmapSeasons200Response from a dict
get_globalmap_seasons200_response_from_dict = GetGlobalmapSeasons200Response.from_dict(get_globalmap_seasons200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


