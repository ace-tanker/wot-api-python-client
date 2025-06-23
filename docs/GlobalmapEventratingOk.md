# GlobalmapEventratingOk


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**meta** | [**GlobalmapEventratingMeta**](GlobalmapEventratingMeta.md) |  | 
**data** | [**List[GlobalmapEventratingDataInner]**](GlobalmapEventratingDataInner.md) |  | 

## Example

```python
from wot_api_client.models.globalmap_eventrating_ok import GlobalmapEventratingOk

# TODO update the JSON string below
json = "{}"
# create an instance of GlobalmapEventratingOk from a JSON string
globalmap_eventrating_ok_instance = GlobalmapEventratingOk.from_json(json)
# print the JSON string representation of the object
print(GlobalmapEventratingOk.to_json())

# convert the object into a dict
globalmap_eventrating_ok_dict = globalmap_eventrating_ok_instance.to_dict()
# create an instance of GlobalmapEventratingOk from a dict
globalmap_eventrating_ok_from_dict = GlobalmapEventratingOk.from_dict(globalmap_eventrating_ok_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


