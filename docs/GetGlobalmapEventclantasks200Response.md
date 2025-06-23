# GetGlobalmapEventclantasks200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**meta** | [**GlobalmapEventclantasksMeta**](GlobalmapEventclantasksMeta.md) |  | 
**data** | **List[object]** |  | 
**error** | [**GlobalmapEventsErrorError**](GlobalmapEventsErrorError.md) |  | 

## Example

```python
from wot_api_client.models.get_globalmap_eventclantasks200_response import GetGlobalmapEventclantasks200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetGlobalmapEventclantasks200Response from a JSON string
get_globalmap_eventclantasks200_response_instance = GetGlobalmapEventclantasks200Response.from_json(json)
# print the JSON string representation of the object
print(GetGlobalmapEventclantasks200Response.to_json())

# convert the object into a dict
get_globalmap_eventclantasks200_response_dict = get_globalmap_eventclantasks200_response_instance.to_dict()
# create an instance of GetGlobalmapEventclantasks200Response from a dict
get_globalmap_eventclantasks200_response_from_dict = GetGlobalmapEventclantasks200Response.from_dict(get_globalmap_eventclantasks200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


