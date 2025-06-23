# GetGlobalmapClanprovinces200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**meta** | [**GlobalmapClanprovincesMeta**](GlobalmapClanprovincesMeta.md) |  | 
**data** | **Dict[str, Optional[List[GlobalmapClanprovincesDataValueInner]]]** |  | 
**error** | **object** |  | 

## Example

```python
from wot_api_client.models.get_globalmap_clanprovinces200_response import GetGlobalmapClanprovinces200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetGlobalmapClanprovinces200Response from a JSON string
get_globalmap_clanprovinces200_response_instance = GetGlobalmapClanprovinces200Response.from_json(json)
# print the JSON string representation of the object
print(GetGlobalmapClanprovinces200Response.to_json())

# convert the object into a dict
get_globalmap_clanprovinces200_response_dict = get_globalmap_clanprovinces200_response_instance.to_dict()
# create an instance of GetGlobalmapClanprovinces200Response from a dict
get_globalmap_clanprovinces200_response_from_dict = GetGlobalmapClanprovinces200Response.from_dict(get_globalmap_clanprovinces200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


