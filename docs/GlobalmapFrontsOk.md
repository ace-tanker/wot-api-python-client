# GlobalmapFrontsOk


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**meta** | [**GlobalmapFrontsMeta**](GlobalmapFrontsMeta.md) |  | 
**data** | [**List[GlobalmapFrontsDataInner]**](GlobalmapFrontsDataInner.md) |  | 

## Example

```python
from wot_api_client.models.globalmap_fronts_ok import GlobalmapFrontsOk

# TODO update the JSON string below
json = "{}"
# create an instance of GlobalmapFrontsOk from a JSON string
globalmap_fronts_ok_instance = GlobalmapFrontsOk.from_json(json)
# print the JSON string representation of the object
print(GlobalmapFrontsOk.to_json())

# convert the object into a dict
globalmap_fronts_ok_dict = globalmap_fronts_ok_instance.to_dict()
# create an instance of GlobalmapFrontsOk from a dict
globalmap_fronts_ok_from_dict = GlobalmapFrontsOk.from_dict(globalmap_fronts_ok_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


