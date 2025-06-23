# GlobalmapSeasonratingneighborsOk


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**meta** | [**GlobalmapSeasonratingneighborsMeta**](GlobalmapSeasonratingneighborsMeta.md) |  | 
**data** | [**List[GlobalmapSeasonratingDataInner]**](GlobalmapSeasonratingDataInner.md) |  | 

## Example

```python
from wot_api_client.models.globalmap_seasonratingneighbors_ok import GlobalmapSeasonratingneighborsOk

# TODO update the JSON string below
json = "{}"
# create an instance of GlobalmapSeasonratingneighborsOk from a JSON string
globalmap_seasonratingneighbors_ok_instance = GlobalmapSeasonratingneighborsOk.from_json(json)
# print the JSON string representation of the object
print(GlobalmapSeasonratingneighborsOk.to_json())

# convert the object into a dict
globalmap_seasonratingneighbors_ok_dict = globalmap_seasonratingneighbors_ok_instance.to_dict()
# create an instance of GlobalmapSeasonratingneighborsOk from a dict
globalmap_seasonratingneighbors_ok_from_dict = GlobalmapSeasonratingneighborsOk.from_dict(globalmap_seasonratingneighbors_ok_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


