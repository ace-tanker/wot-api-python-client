# GlobalmapEventsDataInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event_id** | **str** | Event ID | 
**event_name** | **str** | Event name | 
**start** | **str** | Start time | 
**end** | **str** | Finishing time | 
**status** | **str** | Status | 
**fronts** | [**List[GlobalmapEventsDataInnerFrontsInner]**](GlobalmapEventsDataInnerFrontsInner.md) | Fronts. Only event fronts are presented in response. | 

## Example

```python
from wot_api_client.models.globalmap_events_data_inner import GlobalmapEventsDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of GlobalmapEventsDataInner from a JSON string
globalmap_events_data_inner_instance = GlobalmapEventsDataInner.from_json(json)
# print the JSON string representation of the object
print(GlobalmapEventsDataInner.to_json())

# convert the object into a dict
globalmap_events_data_inner_dict = globalmap_events_data_inner_instance.to_dict()
# create an instance of GlobalmapEventsDataInner from a dict
globalmap_events_data_inner_from_dict = GlobalmapEventsDataInner.from_dict(globalmap_events_data_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


