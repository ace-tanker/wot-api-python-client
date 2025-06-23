# GlobalmapInfoError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**error** | **object** |  | 

## Example

```python
from wot_api_client.models.globalmap_info_error import GlobalmapInfoError

# TODO update the JSON string below
json = "{}"
# create an instance of GlobalmapInfoError from a JSON string
globalmap_info_error_instance = GlobalmapInfoError.from_json(json)
# print the JSON string representation of the object
print(GlobalmapInfoError.to_json())

# convert the object into a dict
globalmap_info_error_dict = globalmap_info_error_instance.to_dict()
# create an instance of GlobalmapInfoError from a dict
globalmap_info_error_from_dict = GlobalmapInfoError.from_dict(globalmap_info_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


