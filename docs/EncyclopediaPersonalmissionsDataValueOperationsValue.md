# EncyclopediaPersonalmissionsDataValueOperationsValue


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
**reward** | [**EncyclopediaPersonalmissionsDataValueOperationsValueReward**](EncyclopediaPersonalmissionsDataValueOperationsValueReward.md) |  | 
**missions** | [**Dict[str, EncyclopediaPersonalmissionsDataValueOperationsValueMissionsValue]**](EncyclopediaPersonalmissionsDataValueOperationsValueMissionsValue.md) | Operation missions | 

## Example

```python
from wot_api_client.models.encyclopedia_personalmissions_data_value_operations_value import EncyclopediaPersonalmissionsDataValueOperationsValue

# TODO update the JSON string below
json = "{}"
# create an instance of EncyclopediaPersonalmissionsDataValueOperationsValue from a JSON string
encyclopedia_personalmissions_data_value_operations_value_instance = EncyclopediaPersonalmissionsDataValueOperationsValue.from_json(json)
# print the JSON string representation of the object
print(EncyclopediaPersonalmissionsDataValueOperationsValue.to_json())

# convert the object into a dict
encyclopedia_personalmissions_data_value_operations_value_dict = encyclopedia_personalmissions_data_value_operations_value_instance.to_dict()
# create an instance of EncyclopediaPersonalmissionsDataValueOperationsValue from a dict
encyclopedia_personalmissions_data_value_operations_value_from_dict = EncyclopediaPersonalmissionsDataValueOperationsValue.from_dict(encyclopedia_personalmissions_data_value_operations_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


