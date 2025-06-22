# GetGlobalmapEvents200ResponseOneOf


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**meta** | [**GetGlobalmapSeasons200ResponseOneOfMeta**](GetGlobalmapSeasons200ResponseOneOfMeta.md) |  | 
**data** | [**List[GetGlobalmapEvents200ResponseOneOfDataInner]**](GetGlobalmapEvents200ResponseOneOfDataInner.md) |  | 

## Example

```python
from wot_api_client.models.get_globalmap_events200_response_one_of import GetGlobalmapEvents200ResponseOneOf

# TODO update the JSON string below
json = "{}"
# create an instance of GetGlobalmapEvents200ResponseOneOf from a JSON string
get_globalmap_events200_response_one_of_instance = GetGlobalmapEvents200ResponseOneOf.from_json(json)
# print the JSON string representation of the object
print(GetGlobalmapEvents200ResponseOneOf.to_json())

# convert the object into a dict
get_globalmap_events200_response_one_of_dict = get_globalmap_events200_response_one_of_instance.to_dict()
# create an instance of GetGlobalmapEvents200ResponseOneOf from a dict
get_globalmap_events200_response_one_of_from_dict = GetGlobalmapEvents200ResponseOneOf.from_dict(get_globalmap_events200_response_one_of_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


