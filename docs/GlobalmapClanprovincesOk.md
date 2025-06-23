# GlobalmapClanprovincesOk


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**meta** | [**GlobalmapClanprovincesMeta**](GlobalmapClanprovincesMeta.md) |  | 
**data** | **Dict[str, Optional[List[GlobalmapClanprovincesDataValueInner]]]** |  | 

## Example

```python
from wot_api_client.models.globalmap_clanprovinces_ok import GlobalmapClanprovincesOk

# TODO update the JSON string below
json = "{}"
# create an instance of GlobalmapClanprovincesOk from a JSON string
globalmap_clanprovinces_ok_instance = GlobalmapClanprovincesOk.from_json(json)
# print the JSON string representation of the object
print(GlobalmapClanprovincesOk.to_json())

# convert the object into a dict
globalmap_clanprovinces_ok_dict = globalmap_clanprovinces_ok_instance.to_dict()
# create an instance of GlobalmapClanprovincesOk from a dict
globalmap_clanprovinces_ok_from_dict = GlobalmapClanprovincesOk.from_dict(globalmap_clanprovinces_ok_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


