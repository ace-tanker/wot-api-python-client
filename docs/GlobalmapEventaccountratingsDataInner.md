# GlobalmapEventaccountratingsDataInner


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
from wot_api_client.models.globalmap_eventaccountratings_data_inner import GlobalmapEventaccountratingsDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of GlobalmapEventaccountratingsDataInner from a JSON string
globalmap_eventaccountratings_data_inner_instance = GlobalmapEventaccountratingsDataInner.from_json(json)
# print the JSON string representation of the object
print(GlobalmapEventaccountratingsDataInner.to_json())

# convert the object into a dict
globalmap_eventaccountratings_data_inner_dict = globalmap_eventaccountratings_data_inner_instance.to_dict()
# create an instance of GlobalmapEventaccountratingsDataInner from a dict
globalmap_eventaccountratings_data_inner_from_dict = GlobalmapEventaccountratingsDataInner.from_dict(globalmap_eventaccountratings_data_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


