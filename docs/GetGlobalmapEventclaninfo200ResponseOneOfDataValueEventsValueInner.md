# GetGlobalmapEventclaninfo200ResponseOneOfDataValueEventsValueInner


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
from wot_api_client.models.get_globalmap_eventclaninfo200_response_one_of_data_value_events_value_inner import GetGlobalmapEventclaninfo200ResponseOneOfDataValueEventsValueInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetGlobalmapEventclaninfo200ResponseOneOfDataValueEventsValueInner from a JSON string
get_globalmap_eventclaninfo200_response_one_of_data_value_events_value_inner_instance = GetGlobalmapEventclaninfo200ResponseOneOfDataValueEventsValueInner.from_json(json)
# print the JSON string representation of the object
print(GetGlobalmapEventclaninfo200ResponseOneOfDataValueEventsValueInner.to_json())

# convert the object into a dict
get_globalmap_eventclaninfo200_response_one_of_data_value_events_value_inner_dict = get_globalmap_eventclaninfo200_response_one_of_data_value_events_value_inner_instance.to_dict()
# create an instance of GetGlobalmapEventclaninfo200ResponseOneOfDataValueEventsValueInner from a dict
get_globalmap_eventclaninfo200_response_one_of_data_value_events_value_inner_from_dict = GetGlobalmapEventclaninfo200ResponseOneOfDataValueEventsValueInner.from_dict(get_globalmap_eventclaninfo200_response_one_of_data_value_events_value_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


