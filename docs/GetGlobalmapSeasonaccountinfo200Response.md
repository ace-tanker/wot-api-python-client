# GetGlobalmapSeasonaccountinfo200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**meta** | [**GlobalmapSeasonaccountinfoMeta**](GlobalmapSeasonaccountinfoMeta.md) |  | 
**data** | [**Dict[str, GlobalmapSeasonaccountinfoDataValue]**](GlobalmapSeasonaccountinfoDataValue.md) |  | 
**error** | [**GlobalmapSeasonsErrorError**](GlobalmapSeasonsErrorError.md) |  | 

## Example

```python
from wot_api_client.models.get_globalmap_seasonaccountinfo200_response import GetGlobalmapSeasonaccountinfo200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetGlobalmapSeasonaccountinfo200Response from a JSON string
get_globalmap_seasonaccountinfo200_response_instance = GetGlobalmapSeasonaccountinfo200Response.from_json(json)
# print the JSON string representation of the object
print(GetGlobalmapSeasonaccountinfo200Response.to_json())

# convert the object into a dict
get_globalmap_seasonaccountinfo200_response_dict = get_globalmap_seasonaccountinfo200_response_instance.to_dict()
# create an instance of GetGlobalmapSeasonaccountinfo200Response from a dict
get_globalmap_seasonaccountinfo200_response_from_dict = GetGlobalmapSeasonaccountinfo200Response.from_dict(get_globalmap_seasonaccountinfo200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


