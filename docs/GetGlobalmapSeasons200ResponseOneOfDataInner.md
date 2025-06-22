# GetGlobalmapSeasons200ResponseOneOfDataInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**season_id** | **str** | Season ID | 
**season_name** | **str** | Season name | 
**start** | **str** | Start time | 
**end** | **str** | Finishing time | 
**status** | **str** | Status | 
**fronts** | **List[object]** | Fronts. Only season fronts are presented in response. | 

## Example

```python
from wot_api_client.models.get_globalmap_seasons200_response_one_of_data_inner import GetGlobalmapSeasons200ResponseOneOfDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetGlobalmapSeasons200ResponseOneOfDataInner from a JSON string
get_globalmap_seasons200_response_one_of_data_inner_instance = GetGlobalmapSeasons200ResponseOneOfDataInner.from_json(json)
# print the JSON string representation of the object
print(GetGlobalmapSeasons200ResponseOneOfDataInner.to_json())

# convert the object into a dict
get_globalmap_seasons200_response_one_of_data_inner_dict = get_globalmap_seasons200_response_one_of_data_inner_instance.to_dict()
# create an instance of GetGlobalmapSeasons200ResponseOneOfDataInner from a dict
get_globalmap_seasons200_response_one_of_data_inner_from_dict = GetGlobalmapSeasons200ResponseOneOfDataInner.from_dict(get_globalmap_seasons200_response_one_of_data_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


