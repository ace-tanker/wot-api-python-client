# GlobalmapEventaccountinfoError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**error** | [**GlobalmapEventaccountinfoErrorError**](GlobalmapEventaccountinfoErrorError.md) |  | 

## Example

```python
from wot_api_client.models.globalmap_eventaccountinfo_error import GlobalmapEventaccountinfoError

# TODO update the JSON string below
json = "{}"
# create an instance of GlobalmapEventaccountinfoError from a JSON string
globalmap_eventaccountinfo_error_instance = GlobalmapEventaccountinfoError.from_json(json)
# print the JSON string representation of the object
print(GlobalmapEventaccountinfoError.to_json())

# convert the object into a dict
globalmap_eventaccountinfo_error_dict = globalmap_eventaccountinfo_error_instance.to_dict()
# create an instance of GlobalmapEventaccountinfoError from a dict
globalmap_eventaccountinfo_error_from_dict = GlobalmapEventaccountinfoError.from_dict(globalmap_eventaccountinfo_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


