# GetGlobalmapInfo200ResponseOneOfData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**state** | **str** | Map status: active, frozen, turn_calculation_in_progress | 
**last_turn** | **int** | Number of last calculated turn | 
**last_turn_created_at** | **int** | Creation time of the last calculated turn in UTC | 
**last_turn_calculated_at** | **int** | Calculation time of the last turn in UTC | 

## Example

```python
from wot_api_client.models.get_globalmap_info200_response_one_of_data import GetGlobalmapInfo200ResponseOneOfData

# TODO update the JSON string below
json = "{}"
# create an instance of GetGlobalmapInfo200ResponseOneOfData from a JSON string
get_globalmap_info200_response_one_of_data_instance = GetGlobalmapInfo200ResponseOneOfData.from_json(json)
# print the JSON string representation of the object
print(GetGlobalmapInfo200ResponseOneOfData.to_json())

# convert the object into a dict
get_globalmap_info200_response_one_of_data_dict = get_globalmap_info200_response_one_of_data_instance.to_dict()
# create an instance of GetGlobalmapInfo200ResponseOneOfData from a dict
get_globalmap_info200_response_one_of_data_from_dict = GetGlobalmapInfo200ResponseOneOfData.from_dict(get_globalmap_info200_response_one_of_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


