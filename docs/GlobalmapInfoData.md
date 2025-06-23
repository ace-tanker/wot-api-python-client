# GlobalmapInfoData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**state** | **str** | Map status: active, frozen, turn_calculation_in_progress | 
**last_turn** | **int** | Number of last calculated turn | 
**last_turn_created_at** | **int** | Creation time of the last calculated turn in UTC | 
**last_turn_calculated_at** | **int** | Calculation time of the last turn in UTC | 

## Example

```python
from wot_api_client.models.globalmap_info_data import GlobalmapInfoData

# TODO update the JSON string below
json = "{}"
# create an instance of GlobalmapInfoData from a JSON string
globalmap_info_data_instance = GlobalmapInfoData.from_json(json)
# print the JSON string representation of the object
print(GlobalmapInfoData.to_json())

# convert the object into a dict
globalmap_info_data_dict = globalmap_info_data_instance.to_dict()
# create an instance of GlobalmapInfoData from a dict
globalmap_info_data_from_dict = GlobalmapInfoData.from_dict(globalmap_info_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


