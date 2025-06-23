# GlobalmapProvincesOk


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**meta** | [**GlobalmapProvincesMeta**](GlobalmapProvincesMeta.md) |  | 
**data** | [**List[GlobalmapProvincesDataInner]**](GlobalmapProvincesDataInner.md) |  | 

## Example

```python
from wot_api_client.models.globalmap_provinces_ok import GlobalmapProvincesOk

# TODO update the JSON string below
json = "{}"
# create an instance of GlobalmapProvincesOk from a JSON string
globalmap_provinces_ok_instance = GlobalmapProvincesOk.from_json(json)
# print the JSON string representation of the object
print(GlobalmapProvincesOk.to_json())

# convert the object into a dict
globalmap_provinces_ok_dict = globalmap_provinces_ok_instance.to_dict()
# create an instance of GlobalmapProvincesOk from a dict
globalmap_provinces_ok_from_dict = GlobalmapProvincesOk.from_dict(globalmap_provinces_ok_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


