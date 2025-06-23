# GlobalmapClanbattlesDataInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**front_id** | **str** | Front ID | 
**front_name** | **str** | Front name | 
**province_id** | **str** | Province ID | 
**province_name** | **str** | Province name | 
**time** | **int** | Battle date and time | 
**type** | **str** | Battle type: attack or defense | 
**competitor_id** | **int** | Enemy clan ID | 
**attack_type** | **str** | Attack Type: ground, auction, tournament | 
**vehicle_level** | **int** | Vehicle Tier | 

## Example

```python
from wot_api_client.models.globalmap_clanbattles_data_inner import GlobalmapClanbattlesDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of GlobalmapClanbattlesDataInner from a JSON string
globalmap_clanbattles_data_inner_instance = GlobalmapClanbattlesDataInner.from_json(json)
# print the JSON string representation of the object
print(GlobalmapClanbattlesDataInner.to_json())

# convert the object into a dict
globalmap_clanbattles_data_inner_dict = globalmap_clanbattles_data_inner_instance.to_dict()
# create an instance of GlobalmapClanbattlesDataInner from a dict
globalmap_clanbattles_data_inner_from_dict = GlobalmapClanbattlesDataInner.from_dict(globalmap_clanbattles_data_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


