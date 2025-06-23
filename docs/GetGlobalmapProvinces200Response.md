# GetGlobalmapProvinces200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**meta** | [**GlobalmapProvincesMeta**](GlobalmapProvincesMeta.md) |  | 
**data** | [**List[GlobalmapProvincesDataInner]**](GlobalmapProvincesDataInner.md) |  | 
**error** | **object** |  | 

## Example

```python
from wot_api_client.models.get_globalmap_provinces200_response import GetGlobalmapProvinces200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetGlobalmapProvinces200Response from a JSON string
get_globalmap_provinces200_response_instance = GetGlobalmapProvinces200Response.from_json(json)
# print the JSON string representation of the object
print(GetGlobalmapProvinces200Response.to_json())

# convert the object into a dict
get_globalmap_provinces200_response_dict = get_globalmap_provinces200_response_instance.to_dict()
# create an instance of GetGlobalmapProvinces200Response from a dict
get_globalmap_provinces200_response_from_dict = GetGlobalmapProvinces200Response.from_dict(get_globalmap_provinces200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


