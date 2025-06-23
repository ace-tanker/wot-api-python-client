# GlobalmapSeasonsError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**error** | [**GlobalmapSeasonsErrorError**](GlobalmapSeasonsErrorError.md) |  | 

## Example

```python
from wot_api_client.models.globalmap_seasons_error import GlobalmapSeasonsError

# TODO update the JSON string below
json = "{}"
# create an instance of GlobalmapSeasonsError from a JSON string
globalmap_seasons_error_instance = GlobalmapSeasonsError.from_json(json)
# print the JSON string representation of the object
print(GlobalmapSeasonsError.to_json())

# convert the object into a dict
globalmap_seasons_error_dict = globalmap_seasons_error_instance.to_dict()
# create an instance of GlobalmapSeasonsError from a dict
globalmap_seasons_error_from_dict = GlobalmapSeasonsError.from_dict(globalmap_seasons_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


