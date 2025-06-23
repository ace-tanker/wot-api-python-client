# GlobalmapEventsMeta


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**page_total** | **int** |  | 
**page** | **int** |  | 

## Example

```python
from wot_api_client.models.globalmap_events_meta import GlobalmapEventsMeta

# TODO update the JSON string below
json = "{}"
# create an instance of GlobalmapEventsMeta from a JSON string
globalmap_events_meta_instance = GlobalmapEventsMeta.from_json(json)
# print the JSON string representation of the object
print(GlobalmapEventsMeta.to_json())

# convert the object into a dict
globalmap_events_meta_dict = globalmap_events_meta_instance.to_dict()
# create an instance of GlobalmapEventsMeta from a dict
globalmap_events_meta_from_dict = GlobalmapEventsMeta.from_dict(globalmap_events_meta_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


