# GlobalmapSeasonaccountinfoError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**error** | [**GlobalmapSeasonsErrorError**](GlobalmapSeasonsErrorError.md) |  | 

## Example

```python
from wot_api_client.models.globalmap_seasonaccountinfo_error import GlobalmapSeasonaccountinfoError

# TODO update the JSON string below
json = "{}"
# create an instance of GlobalmapSeasonaccountinfoError from a JSON string
globalmap_seasonaccountinfo_error_instance = GlobalmapSeasonaccountinfoError.from_json(json)
# print the JSON string representation of the object
print(GlobalmapSeasonaccountinfoError.to_json())

# convert the object into a dict
globalmap_seasonaccountinfo_error_dict = globalmap_seasonaccountinfo_error_instance.to_dict()
# create an instance of GlobalmapSeasonaccountinfoError from a dict
globalmap_seasonaccountinfo_error_from_dict = GlobalmapSeasonaccountinfoError.from_dict(globalmap_seasonaccountinfo_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


