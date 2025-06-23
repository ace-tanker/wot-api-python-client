# GlobalmapSeasonaccountinfoOk


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**meta** | [**GlobalmapSeasonaccountinfoMeta**](GlobalmapSeasonaccountinfoMeta.md) |  | 
**data** | [**Dict[str, GlobalmapSeasonaccountinfoDataValue]**](GlobalmapSeasonaccountinfoDataValue.md) |  | 

## Example

```python
from wot_api_client.models.globalmap_seasonaccountinfo_ok import GlobalmapSeasonaccountinfoOk

# TODO update the JSON string below
json = "{}"
# create an instance of GlobalmapSeasonaccountinfoOk from a JSON string
globalmap_seasonaccountinfo_ok_instance = GlobalmapSeasonaccountinfoOk.from_json(json)
# print the JSON string representation of the object
print(GlobalmapSeasonaccountinfoOk.to_json())

# convert the object into a dict
globalmap_seasonaccountinfo_ok_dict = globalmap_seasonaccountinfo_ok_instance.to_dict()
# create an instance of GlobalmapSeasonaccountinfoOk from a dict
globalmap_seasonaccountinfo_ok_from_dict = GlobalmapSeasonaccountinfoOk.from_dict(globalmap_seasonaccountinfo_ok_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


