# GetEncyclopediaPersonalmissions200ResponseOneOfDataValueOperationsValue


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**operation_id** | **int** | Operation ID | 
**name** | **str** | Operation name | 
**description** | **str** | Operation description | 
**image** | **str** | Link to an operation image | 
**sets_count** | **int** | Number of mission branches of the operation | 
**missions_in_set** | **int** | Number of missions in the branch | 
**next_id** | **int** | Next operation ID | 
**sets_to_next** | **int** | Number of branches until the next operation | 
**reward** | [**GetEncyclopediaPersonalmissions200ResponseOneOfDataValueOperationsValueReward**](GetEncyclopediaPersonalmissions200ResponseOneOfDataValueOperationsValueReward.md) |  | 
**missions** | [**Dict[str, GetEncyclopediaPersonalmissions200ResponseOneOfDataValueOperationsValueMissionsValue]**](GetEncyclopediaPersonalmissions200ResponseOneOfDataValueOperationsValueMissionsValue.md) | Operation missions | 

## Example

```python
from wot_api_client.models.get_encyclopedia_personalmissions200_response_one_of_data_value_operations_value import GetEncyclopediaPersonalmissions200ResponseOneOfDataValueOperationsValue

# TODO update the JSON string below
json = "{}"
# create an instance of GetEncyclopediaPersonalmissions200ResponseOneOfDataValueOperationsValue from a JSON string
get_encyclopedia_personalmissions200_response_one_of_data_value_operations_value_instance = GetEncyclopediaPersonalmissions200ResponseOneOfDataValueOperationsValue.from_json(json)
# print the JSON string representation of the object
print(GetEncyclopediaPersonalmissions200ResponseOneOfDataValueOperationsValue.to_json())

# convert the object into a dict
get_encyclopedia_personalmissions200_response_one_of_data_value_operations_value_dict = get_encyclopedia_personalmissions200_response_one_of_data_value_operations_value_instance.to_dict()
# create an instance of GetEncyclopediaPersonalmissions200ResponseOneOfDataValueOperationsValue from a dict
get_encyclopedia_personalmissions200_response_one_of_data_value_operations_value_from_dict = GetEncyclopediaPersonalmissions200ResponseOneOfDataValueOperationsValue.from_dict(get_encyclopedia_personalmissions200_response_one_of_data_value_operations_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


