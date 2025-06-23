# GlobalmapEventsOk


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**meta** | [**GlobalmapEventsMeta**](GlobalmapEventsMeta.md) |  | 
**data** | [**List[GlobalmapEventsDataInner]**](GlobalmapEventsDataInner.md) |  | 

## Example

```python
from wot_api_client.models.globalmap_events_ok import GlobalmapEventsOk

# TODO update the JSON string below
json = "{}"
# create an instance of GlobalmapEventsOk from a JSON string
globalmap_events_ok_instance = GlobalmapEventsOk.from_json(json)
# print the JSON string representation of the object
print(GlobalmapEventsOk.to_json())

# convert the object into a dict
globalmap_events_ok_dict = globalmap_events_ok_instance.to_dict()
# create an instance of GlobalmapEventsOk from a dict
globalmap_events_ok_from_dict = GlobalmapEventsOk.from_dict(globalmap_events_ok_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


