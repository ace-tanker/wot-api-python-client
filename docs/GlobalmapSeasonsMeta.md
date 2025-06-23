# GlobalmapSeasonsMeta


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**page_total** | **int** |  | 
**page** | **int** |  | 

## Example

```python
from wot_api_client.models.globalmap_seasons_meta import GlobalmapSeasonsMeta

# TODO update the JSON string below
json = "{}"
# create an instance of GlobalmapSeasonsMeta from a JSON string
globalmap_seasons_meta_instance = GlobalmapSeasonsMeta.from_json(json)
# print the JSON string representation of the object
print(GlobalmapSeasonsMeta.to_json())

# convert the object into a dict
globalmap_seasons_meta_dict = globalmap_seasons_meta_instance.to_dict()
# create an instance of GlobalmapSeasonsMeta from a dict
globalmap_seasons_meta_from_dict = GlobalmapSeasonsMeta.from_dict(globalmap_seasons_meta_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


