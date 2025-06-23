# GlobalmapEventsErrorError

Event not found

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **float** |  | 
**message** | **str** |  | 
**var_field** | **str** |  | 
**value** | **str** |  | 

## Example

```python
from wot_api_client.models.globalmap_events_error_error import GlobalmapEventsErrorError

# TODO update the JSON string below
json = "{}"
# create an instance of GlobalmapEventsErrorError from a JSON string
globalmap_events_error_error_instance = GlobalmapEventsErrorError.from_json(json)
# print the JSON string representation of the object
print(GlobalmapEventsErrorError.to_json())

# convert the object into a dict
globalmap_events_error_error_dict = globalmap_events_error_error_instance.to_dict()
# create an instance of GlobalmapEventsErrorError from a dict
globalmap_events_error_error_from_dict = GlobalmapEventsErrorError.from_dict(globalmap_events_error_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


