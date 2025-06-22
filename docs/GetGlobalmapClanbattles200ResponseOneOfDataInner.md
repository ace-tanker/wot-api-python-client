# GetGlobalmapClanbattles200ResponseOneOfDataInner


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
from wot_api_client.models.get_globalmap_clanbattles200_response_one_of_data_inner import GetGlobalmapClanbattles200ResponseOneOfDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetGlobalmapClanbattles200ResponseOneOfDataInner from a JSON string
get_globalmap_clanbattles200_response_one_of_data_inner_instance = GetGlobalmapClanbattles200ResponseOneOfDataInner.from_json(json)
# print the JSON string representation of the object
print(GetGlobalmapClanbattles200ResponseOneOfDataInner.to_json())

# convert the object into a dict
get_globalmap_clanbattles200_response_one_of_data_inner_dict = get_globalmap_clanbattles200_response_one_of_data_inner_instance.to_dict()
# create an instance of GetGlobalmapClanbattles200ResponseOneOfDataInner from a dict
get_globalmap_clanbattles200_response_one_of_data_inner_from_dict = GetGlobalmapClanbattles200ResponseOneOfDataInner.from_dict(get_globalmap_clanbattles200_response_one_of_data_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


