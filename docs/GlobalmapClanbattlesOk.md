# GlobalmapClanbattlesOk


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**meta** | [**GlobalmapClanbattlesMeta**](GlobalmapClanbattlesMeta.md) |  | 
**data** | [**List[GlobalmapClanbattlesDataInner]**](GlobalmapClanbattlesDataInner.md) |  | 

## Example

```python
from wot_api_client.models.globalmap_clanbattles_ok import GlobalmapClanbattlesOk

# TODO update the JSON string below
json = "{}"
# create an instance of GlobalmapClanbattlesOk from a JSON string
globalmap_clanbattles_ok_instance = GlobalmapClanbattlesOk.from_json(json)
# print the JSON string representation of the object
print(GlobalmapClanbattlesOk.to_json())

# convert the object into a dict
globalmap_clanbattles_ok_dict = globalmap_clanbattles_ok_instance.to_dict()
# create an instance of GlobalmapClanbattlesOk from a dict
globalmap_clanbattles_ok_from_dict = GlobalmapClanbattlesOk.from_dict(globalmap_clanbattles_ok_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


