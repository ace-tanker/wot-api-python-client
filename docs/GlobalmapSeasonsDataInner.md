# GlobalmapSeasonsDataInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**season_id** | **str** | Season ID | 
**season_name** | **str** | Season name | 
**start** | **str** | Start time | 
**end** | **str** | Finishing time | 
**status** | **str** | Status | 
**fronts** | **List[object]** | Fronts. Only season fronts are presented in response. | 

## Example

```python
from wot_api_client.models.globalmap_seasons_data_inner import GlobalmapSeasonsDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of GlobalmapSeasonsDataInner from a JSON string
globalmap_seasons_data_inner_instance = GlobalmapSeasonsDataInner.from_json(json)
# print the JSON string representation of the object
print(GlobalmapSeasonsDataInner.to_json())

# convert the object into a dict
globalmap_seasons_data_inner_dict = globalmap_seasons_data_inner_instance.to_dict()
# create an instance of GlobalmapSeasonsDataInner from a dict
globalmap_seasons_data_inner_from_dict = GlobalmapSeasonsDataInner.from_dict(globalmap_seasons_data_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


