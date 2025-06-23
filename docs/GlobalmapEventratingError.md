# GlobalmapEventratingError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**error** | [**GlobalmapEventsErrorError**](GlobalmapEventsErrorError.md) |  | 

## Example

```python
from wot_api_client.models.globalmap_eventrating_error import GlobalmapEventratingError

# TODO update the JSON string below
json = "{}"
# create an instance of GlobalmapEventratingError from a JSON string
globalmap_eventrating_error_instance = GlobalmapEventratingError.from_json(json)
# print the JSON string representation of the object
print(GlobalmapEventratingError.to_json())

# convert the object into a dict
globalmap_eventrating_error_dict = globalmap_eventrating_error_instance.to_dict()
# create an instance of GlobalmapEventratingError from a dict
globalmap_eventrating_error_from_dict = GlobalmapEventratingError.from_dict(globalmap_eventrating_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


