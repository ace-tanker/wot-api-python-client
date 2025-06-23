# GlobalmapEventclaninfoOk


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**meta** | [**GlobalmapEventclaninfoMeta**](GlobalmapEventclaninfoMeta.md) |  | 
**data** | [**Dict[str, GlobalmapEventclaninfoDataValue]**](GlobalmapEventclaninfoDataValue.md) |  | 

## Example

```python
from wot_api_client.models.globalmap_eventclaninfo_ok import GlobalmapEventclaninfoOk

# TODO update the JSON string below
json = "{}"
# create an instance of GlobalmapEventclaninfoOk from a JSON string
globalmap_eventclaninfo_ok_instance = GlobalmapEventclaninfoOk.from_json(json)
# print the JSON string representation of the object
print(GlobalmapEventclaninfoOk.to_json())

# convert the object into a dict
globalmap_eventclaninfo_ok_dict = globalmap_eventclaninfo_ok_instance.to_dict()
# create an instance of GlobalmapEventclaninfoOk from a dict
globalmap_eventclaninfo_ok_from_dict = GlobalmapEventclaninfoOk.from_dict(globalmap_eventclaninfo_ok_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


