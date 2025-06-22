# GetGlobalmapEventaccountinfo200ResponseOneOfDataValueEventsValueInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **int** | Account ID | 
**award_level** | **str** | Award level | 
**battles** | **int** | Battles fought for current clan | 
**battles_to_award** | **int** | Battles to fight in a current clan to get clan award for the season | 
**clan_id** | **int** | Clan ID | 
**clan_rank** | **int** | Clan rating | 
**event_id** | **str** | Event ID | 
**fame_points** | **int** | Total Fame Points | 
**fame_points_since_turn** | **int** | Change of Fame Points since last turn calculation | 
**fame_points_to_improve_award** | **int** | Amount of Fame Points needed to improve personal award | 
**front_id** | **str** | Front ID | 
**rank** | **int** | Current rating | 
**rank_delta** | **int** | Rating changes during previous turn | 
**updated_at** | **int** | Date when account data were updated | 
**url** | **str** | Link to Front | 

## Example

```python
from wot_api_client.models.get_globalmap_eventaccountinfo200_response_one_of_data_value_events_value_inner import GetGlobalmapEventaccountinfo200ResponseOneOfDataValueEventsValueInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetGlobalmapEventaccountinfo200ResponseOneOfDataValueEventsValueInner from a JSON string
get_globalmap_eventaccountinfo200_response_one_of_data_value_events_value_inner_instance = GetGlobalmapEventaccountinfo200ResponseOneOfDataValueEventsValueInner.from_json(json)
# print the JSON string representation of the object
print(GetGlobalmapEventaccountinfo200ResponseOneOfDataValueEventsValueInner.to_json())

# convert the object into a dict
get_globalmap_eventaccountinfo200_response_one_of_data_value_events_value_inner_dict = get_globalmap_eventaccountinfo200_response_one_of_data_value_events_value_inner_instance.to_dict()
# create an instance of GetGlobalmapEventaccountinfo200ResponseOneOfDataValueEventsValueInner from a dict
get_globalmap_eventaccountinfo200_response_one_of_data_value_events_value_inner_from_dict = GetGlobalmapEventaccountinfo200ResponseOneOfDataValueEventsValueInner.from_dict(get_globalmap_eventaccountinfo200_response_one_of_data_value_events_value_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


