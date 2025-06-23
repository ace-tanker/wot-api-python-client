# GlobalmapEventclaninfoDataValueEventsValueInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**front_id** | **str** | Front ID | 
**event_id** | **str** | Event ID | 
**fame_points** | **int** | Total Fame Points | 
**fame_points_since_turn** | **int** | Change of Fame Points since last turn calculation | 
**url** | **str** | Link to Front | 
**rank** | **int** | Current rating | 
**rank_delta** | **int** | Rating changes during previous turn | 
**battles** | **int** | Battles fought | 
**wins** | **int** | Victories | 
**battle_fame_points** | **int** | Battle Fame Points | 
**task_fame_points** | **int** | Fame Points for completing a clan task | 

## Example

```python
from wot_api_client.models.globalmap_eventclaninfo_data_value_events_value_inner import GlobalmapEventclaninfoDataValueEventsValueInner

# TODO update the JSON string below
json = "{}"
# create an instance of GlobalmapEventclaninfoDataValueEventsValueInner from a JSON string
globalmap_eventclaninfo_data_value_events_value_inner_instance = GlobalmapEventclaninfoDataValueEventsValueInner.from_json(json)
# print the JSON string representation of the object
print(GlobalmapEventclaninfoDataValueEventsValueInner.to_json())

# convert the object into a dict
globalmap_eventclaninfo_data_value_events_value_inner_dict = globalmap_eventclaninfo_data_value_events_value_inner_instance.to_dict()
# create an instance of GlobalmapEventclaninfoDataValueEventsValueInner from a dict
globalmap_eventclaninfo_data_value_events_value_inner_from_dict = GlobalmapEventclaninfoDataValueEventsValueInner.from_dict(globalmap_eventclaninfo_data_value_events_value_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


