# GetGlobalmapFronts200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**meta** | [**GlobalmapFrontsMeta**](GlobalmapFrontsMeta.md) |  | 
**data** | [**List[GlobalmapFrontsDataInner]**](GlobalmapFrontsDataInner.md) |  | 
**error** | **object** |  | 

## Example

```python
from wot_api_client.models.get_globalmap_fronts200_response import GetGlobalmapFronts200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetGlobalmapFronts200Response from a JSON string
get_globalmap_fronts200_response_instance = GetGlobalmapFronts200Response.from_json(json)
# print the JSON string representation of the object
print(GetGlobalmapFronts200Response.to_json())

# convert the object into a dict
get_globalmap_fronts200_response_dict = get_globalmap_fronts200_response_instance.to_dict()
# create an instance of GetGlobalmapFronts200Response from a dict
get_globalmap_fronts200_response_from_dict = GetGlobalmapFronts200Response.from_dict(get_globalmap_fronts200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


