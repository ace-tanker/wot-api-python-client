# GlobalmapProvincesError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**error** | **object** |  | 

## Example

```python
from wot_api_client.models.globalmap_provinces_error import GlobalmapProvincesError

# TODO update the JSON string below
json = "{}"
# create an instance of GlobalmapProvincesError from a JSON string
globalmap_provinces_error_instance = GlobalmapProvincesError.from_json(json)
# print the JSON string representation of the object
print(GlobalmapProvincesError.to_json())

# convert the object into a dict
globalmap_provinces_error_dict = globalmap_provinces_error_instance.to_dict()
# create an instance of GlobalmapProvincesError from a dict
globalmap_provinces_error_from_dict = GlobalmapProvincesError.from_dict(globalmap_provinces_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


