# GlobalmapSeasonratingError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**error** | [**GlobalmapSeasonsErrorError**](GlobalmapSeasonsErrorError.md) |  | 

## Example

```python
from wot_api_client.models.globalmap_seasonrating_error import GlobalmapSeasonratingError

# TODO update the JSON string below
json = "{}"
# create an instance of GlobalmapSeasonratingError from a JSON string
globalmap_seasonrating_error_instance = GlobalmapSeasonratingError.from_json(json)
# print the JSON string representation of the object
print(GlobalmapSeasonratingError.to_json())

# convert the object into a dict
globalmap_seasonrating_error_dict = globalmap_seasonrating_error_instance.to_dict()
# create an instance of GlobalmapSeasonratingError from a dict
globalmap_seasonrating_error_from_dict = GlobalmapSeasonratingError.from_dict(globalmap_seasonrating_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


