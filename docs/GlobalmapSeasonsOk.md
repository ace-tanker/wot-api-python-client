# GlobalmapSeasonsOk


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**meta** | [**GlobalmapSeasonsMeta**](GlobalmapSeasonsMeta.md) |  | 
**data** | [**List[GlobalmapSeasonsDataInner]**](GlobalmapSeasonsDataInner.md) |  | 

## Example

```python
from wot_api_client.models.globalmap_seasons_ok import GlobalmapSeasonsOk

# TODO update the JSON string below
json = "{}"
# create an instance of GlobalmapSeasonsOk from a JSON string
globalmap_seasons_ok_instance = GlobalmapSeasonsOk.from_json(json)
# print the JSON string representation of the object
print(GlobalmapSeasonsOk.to_json())

# convert the object into a dict
globalmap_seasons_ok_dict = globalmap_seasons_ok_instance.to_dict()
# create an instance of GlobalmapSeasonsOk from a dict
globalmap_seasons_ok_from_dict = GlobalmapSeasonsOk.from_dict(globalmap_seasons_ok_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


