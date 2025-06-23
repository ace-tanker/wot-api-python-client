# GlobalmapSeasonsErrorError

Season not found

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **float** |  | 
**message** | **str** |  | 
**var_field** | **str** |  | 
**value** | **str** |  | 

## Example

```python
from wot_api_client.models.globalmap_seasons_error_error import GlobalmapSeasonsErrorError

# TODO update the JSON string below
json = "{}"
# create an instance of GlobalmapSeasonsErrorError from a JSON string
globalmap_seasons_error_error_instance = GlobalmapSeasonsErrorError.from_json(json)
# print the JSON string representation of the object
print(GlobalmapSeasonsErrorError.to_json())

# convert the object into a dict
globalmap_seasons_error_error_dict = globalmap_seasons_error_error_instance.to_dict()
# create an instance of GlobalmapSeasonsErrorError from a dict
globalmap_seasons_error_error_from_dict = GlobalmapSeasonsErrorError.from_dict(globalmap_seasons_error_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


