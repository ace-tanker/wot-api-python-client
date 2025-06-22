# GetGlobalmapEventrating200ResponseOneOfDataInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**clan_id** | **int** | Clan ID | 
**name** | **str** | Clan name | 
**tag** | **str** | Clan tag | 
**color** | **str** | Clan color | 
**award_level** | **str** | Award level | 
**rank** | **int** | Current rating | 
**rank_delta** | **int** | Rating changes during previous turn | 
**updated_at** | **int** | Date of rating calculation | 
**battle_fame_points** | **int** | Battle Fame Points | 
**total_fame_points** | **int** | Total Fame Points | 
**task_fame_points** | **int** | Fame Points for completing a clan task | 
**fame_points_to_improve_award** | **int** | Amount of Fame Points needed to improve personal award | 

## Example

```python
from wot_api_client.models.get_globalmap_eventrating200_response_one_of_data_inner import GetGlobalmapEventrating200ResponseOneOfDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetGlobalmapEventrating200ResponseOneOfDataInner from a JSON string
get_globalmap_eventrating200_response_one_of_data_inner_instance = GetGlobalmapEventrating200ResponseOneOfDataInner.from_json(json)
# print the JSON string representation of the object
print(GetGlobalmapEventrating200ResponseOneOfDataInner.to_json())

# convert the object into a dict
get_globalmap_eventrating200_response_one_of_data_inner_dict = get_globalmap_eventrating200_response_one_of_data_inner_instance.to_dict()
# create an instance of GetGlobalmapEventrating200ResponseOneOfDataInner from a dict
get_globalmap_eventrating200_response_one_of_data_inner_from_dict = GetGlobalmapEventrating200ResponseOneOfDataInner.from_dict(get_globalmap_eventrating200_response_one_of_data_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


