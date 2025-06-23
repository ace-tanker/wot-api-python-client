# GlobalmapEventclaninfoError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**error** | [**GlobalmapEventsErrorError**](GlobalmapEventsErrorError.md) |  | 

## Example

```python
from wot_api_client.models.globalmap_eventclaninfo_error import GlobalmapEventclaninfoError

# TODO update the JSON string below
json = "{}"
# create an instance of GlobalmapEventclaninfoError from a JSON string
globalmap_eventclaninfo_error_instance = GlobalmapEventclaninfoError.from_json(json)
# print the JSON string representation of the object
print(GlobalmapEventclaninfoError.to_json())

# convert the object into a dict
globalmap_eventclaninfo_error_dict = globalmap_eventclaninfo_error_instance.to_dict()
# create an instance of GlobalmapEventclaninfoError from a dict
globalmap_eventclaninfo_error_from_dict = GlobalmapEventclaninfoError.from_dict(globalmap_eventclaninfo_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


