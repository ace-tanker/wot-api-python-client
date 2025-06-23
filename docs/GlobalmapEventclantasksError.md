# GlobalmapEventclantasksError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**error** | [**GlobalmapEventsErrorError**](GlobalmapEventsErrorError.md) |  | 

## Example

```python
from wot_api_client.models.globalmap_eventclantasks_error import GlobalmapEventclantasksError

# TODO update the JSON string below
json = "{}"
# create an instance of GlobalmapEventclantasksError from a JSON string
globalmap_eventclantasks_error_instance = GlobalmapEventclantasksError.from_json(json)
# print the JSON string representation of the object
print(GlobalmapEventclantasksError.to_json())

# convert the object into a dict
globalmap_eventclantasks_error_dict = globalmap_eventclantasks_error_instance.to_dict()
# create an instance of GlobalmapEventclantasksError from a dict
globalmap_eventclantasks_error_from_dict = GlobalmapEventclantasksError.from_dict(globalmap_eventclantasks_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


