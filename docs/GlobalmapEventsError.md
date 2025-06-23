# GlobalmapEventsError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**error** | [**GlobalmapEventsErrorError**](GlobalmapEventsErrorError.md) |  | 

## Example

```python
from wot_api_client.models.globalmap_events_error import GlobalmapEventsError

# TODO update the JSON string below
json = "{}"
# create an instance of GlobalmapEventsError from a JSON string
globalmap_events_error_instance = GlobalmapEventsError.from_json(json)
# print the JSON string representation of the object
print(GlobalmapEventsError.to_json())

# convert the object into a dict
globalmap_events_error_dict = globalmap_events_error_instance.to_dict()
# create an instance of GlobalmapEventsError from a dict
globalmap_events_error_from_dict = GlobalmapEventsError.from_dict(globalmap_events_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


