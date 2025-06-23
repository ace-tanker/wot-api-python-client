# GlobalmapEventclantasksOk


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**meta** | [**GlobalmapEventclantasksMeta**](GlobalmapEventclantasksMeta.md) |  | 
**data** | **List[object]** |  | 

## Example

```python
from wot_api_client.models.globalmap_eventclantasks_ok import GlobalmapEventclantasksOk

# TODO update the JSON string below
json = "{}"
# create an instance of GlobalmapEventclantasksOk from a JSON string
globalmap_eventclantasks_ok_instance = GlobalmapEventclantasksOk.from_json(json)
# print the JSON string representation of the object
print(GlobalmapEventclantasksOk.to_json())

# convert the object into a dict
globalmap_eventclantasks_ok_dict = globalmap_eventclantasks_ok_instance.to_dict()
# create an instance of GlobalmapEventclantasksOk from a dict
globalmap_eventclantasks_ok_from_dict = GlobalmapEventclantasksOk.from_dict(globalmap_eventclantasks_ok_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


