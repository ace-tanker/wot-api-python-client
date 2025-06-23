# GlobalmapEventratingneighborsOk


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**meta** | [**GlobalmapEventratingneighborsMeta**](GlobalmapEventratingneighborsMeta.md) |  | 
**data** | [**List[GlobalmapEventratingneighborsDataInner]**](GlobalmapEventratingneighborsDataInner.md) |  | 

## Example

```python
from wot_api_client.models.globalmap_eventratingneighbors_ok import GlobalmapEventratingneighborsOk

# TODO update the JSON string below
json = "{}"
# create an instance of GlobalmapEventratingneighborsOk from a JSON string
globalmap_eventratingneighbors_ok_instance = GlobalmapEventratingneighborsOk.from_json(json)
# print the JSON string representation of the object
print(GlobalmapEventratingneighborsOk.to_json())

# convert the object into a dict
globalmap_eventratingneighbors_ok_dict = globalmap_eventratingneighbors_ok_instance.to_dict()
# create an instance of GlobalmapEventratingneighborsOk from a dict
globalmap_eventratingneighbors_ok_from_dict = GlobalmapEventratingneighborsOk.from_dict(globalmap_eventratingneighbors_ok_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


