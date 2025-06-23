# GlobalmapClaninfoOk


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**meta** | [**GlobalmapClaninfoMeta**](GlobalmapClaninfoMeta.md) |  | 
**data** | [**Dict[str, GlobalmapClaninfoDataValue]**](GlobalmapClaninfoDataValue.md) |  | 

## Example

```python
from wot_api_client.models.globalmap_claninfo_ok import GlobalmapClaninfoOk

# TODO update the JSON string below
json = "{}"
# create an instance of GlobalmapClaninfoOk from a JSON string
globalmap_claninfo_ok_instance = GlobalmapClaninfoOk.from_json(json)
# print the JSON string representation of the object
print(GlobalmapClaninfoOk.to_json())

# convert the object into a dict
globalmap_claninfo_ok_dict = globalmap_claninfo_ok_instance.to_dict()
# create an instance of GlobalmapClaninfoOk from a dict
globalmap_claninfo_ok_from_dict = GlobalmapClaninfoOk.from_dict(globalmap_claninfo_ok_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


