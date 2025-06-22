# GetEncyclopediaPersonalmissions200ResponseOneOfDataValueOperationsValueMissionsValue


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mission_id** | **int** | Mission ID | 
**set_id** | **int** | Mission branch ID | 
**name** | **str** | Mission name | 
**description** | **str** | Mission description | 
**hint** | **str** | Hints | 
**min_level** | **int** | Minimum vehicle Tier | 
**max_level** | **int** | Maximum vehicle Tier | 
**tags** | **List[str]** | Mission tags | 
**rewards** | [**Dict[str, GetEncyclopediaPersonalmissions200ResponseOneOfDataValueOperationsValueMissionsValueRewardsValue]**](GetEncyclopediaPersonalmissions200ResponseOneOfDataValueOperationsValueMissionsValueRewardsValue.md) | Rewards grouped by mission conditions | 

## Example

```python
from wot_api_client.models.get_encyclopedia_personalmissions200_response_one_of_data_value_operations_value_missions_value import GetEncyclopediaPersonalmissions200ResponseOneOfDataValueOperationsValueMissionsValue

# TODO update the JSON string below
json = "{}"
# create an instance of GetEncyclopediaPersonalmissions200ResponseOneOfDataValueOperationsValueMissionsValue from a JSON string
get_encyclopedia_personalmissions200_response_one_of_data_value_operations_value_missions_value_instance = GetEncyclopediaPersonalmissions200ResponseOneOfDataValueOperationsValueMissionsValue.from_json(json)
# print the JSON string representation of the object
print(GetEncyclopediaPersonalmissions200ResponseOneOfDataValueOperationsValueMissionsValue.to_json())

# convert the object into a dict
get_encyclopedia_personalmissions200_response_one_of_data_value_operations_value_missions_value_dict = get_encyclopedia_personalmissions200_response_one_of_data_value_operations_value_missions_value_instance.to_dict()
# create an instance of GetEncyclopediaPersonalmissions200ResponseOneOfDataValueOperationsValueMissionsValue from a dict
get_encyclopedia_personalmissions200_response_one_of_data_value_operations_value_missions_value_from_dict = GetEncyclopediaPersonalmissions200ResponseOneOfDataValueOperationsValueMissionsValue.from_dict(get_encyclopedia_personalmissions200_response_one_of_data_value_operations_value_missions_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


