# GlobalmapSeasonratingDataInner


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
**victory_points** | **int** | Victory Points | 
**victory_points_to_next_award** | **int** | Victory Points to get the next award | 

## Example

```python
from wot_api_client.models.globalmap_seasonrating_data_inner import GlobalmapSeasonratingDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of GlobalmapSeasonratingDataInner from a JSON string
globalmap_seasonrating_data_inner_instance = GlobalmapSeasonratingDataInner.from_json(json)
# print the JSON string representation of the object
print(GlobalmapSeasonratingDataInner.to_json())

# convert the object into a dict
globalmap_seasonrating_data_inner_dict = globalmap_seasonrating_data_inner_instance.to_dict()
# create an instance of GlobalmapSeasonratingDataInner from a dict
globalmap_seasonrating_data_inner_from_dict = GlobalmapSeasonratingDataInner.from_dict(globalmap_seasonrating_data_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


