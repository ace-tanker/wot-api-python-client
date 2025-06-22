# GetTanksMastery200ResponseOneOfData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**distribution** | **Dict[str, Dict[str, int]]** | Values of these percentiles for each piece of equipment | 
**updated_at** | **int** | Date of data update | 

## Example

```python
from wot_api_client.models.get_tanks_mastery200_response_one_of_data import GetTanksMastery200ResponseOneOfData

# TODO update the JSON string below
json = "{}"
# create an instance of GetTanksMastery200ResponseOneOfData from a JSON string
get_tanks_mastery200_response_one_of_data_instance = GetTanksMastery200ResponseOneOfData.from_json(json)
# print the JSON string representation of the object
print(GetTanksMastery200ResponseOneOfData.to_json())

# convert the object into a dict
get_tanks_mastery200_response_one_of_data_dict = get_tanks_mastery200_response_one_of_data_instance.to_dict()
# create an instance of GetTanksMastery200ResponseOneOfData from a dict
get_tanks_mastery200_response_one_of_data_from_dict = GetTanksMastery200ResponseOneOfData.from_dict(get_tanks_mastery200_response_one_of_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


