# GlobalmapInfoOk


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**meta** | [**GlobalmapInfoMeta**](GlobalmapInfoMeta.md) |  | 
**data** | [**GlobalmapInfoData**](GlobalmapInfoData.md) |  | 

## Example

```python
from wot_api_client.models.globalmap_info_ok import GlobalmapInfoOk

# TODO update the JSON string below
json = "{}"
# create an instance of GlobalmapInfoOk from a JSON string
globalmap_info_ok_instance = GlobalmapInfoOk.from_json(json)
# print the JSON string representation of the object
print(GlobalmapInfoOk.to_json())

# convert the object into a dict
globalmap_info_ok_dict = globalmap_info_ok_instance.to_dict()
# create an instance of GlobalmapInfoOk from a dict
globalmap_info_ok_from_dict = GlobalmapInfoOk.from_dict(globalmap_info_ok_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


