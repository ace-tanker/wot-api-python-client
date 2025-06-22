# GetGlobalmapSeasonrating200ResponseOneOf


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**meta** | [**GetGlobalmapSeasons200ResponseOneOfMeta**](GetGlobalmapSeasons200ResponseOneOfMeta.md) |  | 
**data** | [**List[GetGlobalmapSeasonrating200ResponseOneOfDataInner]**](GetGlobalmapSeasonrating200ResponseOneOfDataInner.md) |  | 

## Example

```python
from wot_api_client.models.get_globalmap_seasonrating200_response_one_of import GetGlobalmapSeasonrating200ResponseOneOf

# TODO update the JSON string below
json = "{}"
# create an instance of GetGlobalmapSeasonrating200ResponseOneOf from a JSON string
get_globalmap_seasonrating200_response_one_of_instance = GetGlobalmapSeasonrating200ResponseOneOf.from_json(json)
# print the JSON string representation of the object
print(GetGlobalmapSeasonrating200ResponseOneOf.to_json())

# convert the object into a dict
get_globalmap_seasonrating200_response_one_of_dict = get_globalmap_seasonrating200_response_one_of_instance.to_dict()
# create an instance of GetGlobalmapSeasonrating200ResponseOneOf from a dict
get_globalmap_seasonrating200_response_one_of_from_dict = GetGlobalmapSeasonrating200ResponseOneOf.from_dict(get_globalmap_seasonrating200_response_one_of_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


