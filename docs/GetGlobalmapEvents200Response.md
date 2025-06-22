# GetGlobalmapEvents200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**meta** | [**GetGlobalmapSeasons200ResponseOneOfMeta**](GetGlobalmapSeasons200ResponseOneOfMeta.md) |  | 
**data** | [**List[GetGlobalmapEvents200ResponseOneOfDataInner]**](GetGlobalmapEvents200ResponseOneOfDataInner.md) |  | 
**error** | [**GetAccountList200ResponseOneOf1Error**](GetAccountList200ResponseOneOf1Error.md) |  | 

## Example

```python
from wot_api_client.models.get_globalmap_events200_response import GetGlobalmapEvents200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetGlobalmapEvents200Response from a JSON string
get_globalmap_events200_response_instance = GetGlobalmapEvents200Response.from_json(json)
# print the JSON string representation of the object
print(GetGlobalmapEvents200Response.to_json())

# convert the object into a dict
get_globalmap_events200_response_dict = get_globalmap_events200_response_instance.to_dict()
# create an instance of GetGlobalmapEvents200Response from a dict
get_globalmap_events200_response_from_dict = GetGlobalmapEvents200Response.from_dict(get_globalmap_events200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


