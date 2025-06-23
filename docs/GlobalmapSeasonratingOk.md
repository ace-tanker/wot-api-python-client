# GlobalmapSeasonratingOk


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**meta** | [**GlobalmapSeasonratingMeta**](GlobalmapSeasonratingMeta.md) |  | 
**data** | [**List[GlobalmapSeasonratingDataInner]**](GlobalmapSeasonratingDataInner.md) |  | 

## Example

```python
from wot_api_client.models.globalmap_seasonrating_ok import GlobalmapSeasonratingOk

# TODO update the JSON string below
json = "{}"
# create an instance of GlobalmapSeasonratingOk from a JSON string
globalmap_seasonrating_ok_instance = GlobalmapSeasonratingOk.from_json(json)
# print the JSON string representation of the object
print(GlobalmapSeasonratingOk.to_json())

# convert the object into a dict
globalmap_seasonrating_ok_dict = globalmap_seasonrating_ok_instance.to_dict()
# create an instance of GlobalmapSeasonratingOk from a dict
globalmap_seasonrating_ok_from_dict = GlobalmapSeasonratingOk.from_dict(globalmap_seasonrating_ok_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


