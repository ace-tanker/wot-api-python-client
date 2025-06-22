# GetGlobalmapEventaccountratings200ResponseOneOfDataInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event_id** | **str** | Event ID | 
**account_id** | **int** | Player account ID | 
**clan_id** | **int** | Clan ID | 
**clan_rank** | **int** | Clan rating | 
**battles** | **int** | Battles fought for current clan | 
**battles_to_award** | **int** | Battles to fight in a current clan to get clan award for the season | 
**award_level** | **str** | Award level | 
**updated_at** | **int** | Date when account data were updated | 
**fame_points** | **int** | Total Fame Points | 
**fame_points_to_improve_award** | **int** | Amount of Fame Points needed to improve personal award | 
**front_id** | **str** | Front ID | 
**url** | **str** | Link to Front | 
**rank** | **int** | Current rating | 
**rank_delta** | **int** | Rating changes during previous turn | 

## Example

```python
from wot_api_client.models.get_globalmap_eventaccountratings200_response_one_of_data_inner import GetGlobalmapEventaccountratings200ResponseOneOfDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetGlobalmapEventaccountratings200ResponseOneOfDataInner from a JSON string
get_globalmap_eventaccountratings200_response_one_of_data_inner_instance = GetGlobalmapEventaccountratings200ResponseOneOfDataInner.from_json(json)
# print the JSON string representation of the object
print(GetGlobalmapEventaccountratings200ResponseOneOfDataInner.to_json())

# convert the object into a dict
get_globalmap_eventaccountratings200_response_one_of_data_inner_dict = get_globalmap_eventaccountratings200_response_one_of_data_inner_instance.to_dict()
# create an instance of GetGlobalmapEventaccountratings200ResponseOneOfDataInner from a dict
get_globalmap_eventaccountratings200_response_one_of_data_inner_from_dict = GetGlobalmapEventaccountratings200ResponseOneOfDataInner.from_dict(get_globalmap_eventaccountratings200_response_one_of_data_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


