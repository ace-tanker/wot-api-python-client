# GlobalmapEventaccountinfoOk


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**meta** | [**GlobalmapEventaccountinfoMeta**](GlobalmapEventaccountinfoMeta.md) |  | 
**data** | [**Dict[str, GlobalmapEventaccountinfoDataValue]**](GlobalmapEventaccountinfoDataValue.md) |  | 

## Example

```python
from wot_api_client.models.globalmap_eventaccountinfo_ok import GlobalmapEventaccountinfoOk

# TODO update the JSON string below
json = "{}"
# create an instance of GlobalmapEventaccountinfoOk from a JSON string
globalmap_eventaccountinfo_ok_instance = GlobalmapEventaccountinfoOk.from_json(json)
# print the JSON string representation of the object
print(GlobalmapEventaccountinfoOk.to_json())

# convert the object into a dict
globalmap_eventaccountinfo_ok_dict = globalmap_eventaccountinfo_ok_instance.to_dict()
# create an instance of GlobalmapEventaccountinfoOk from a dict
globalmap_eventaccountinfo_ok_from_dict = GlobalmapEventaccountinfoOk.from_dict(globalmap_eventaccountinfo_ok_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


