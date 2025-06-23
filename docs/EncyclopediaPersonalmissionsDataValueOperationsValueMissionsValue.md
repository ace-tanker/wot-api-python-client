# EncyclopediaPersonalmissionsDataValueOperationsValueMissionsValue


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
**rewards** | [**Dict[str, EncyclopediaPersonalmissionsDataValueOperationsValueMissionsValueRewardsValue]**](EncyclopediaPersonalmissionsDataValueOperationsValueMissionsValueRewardsValue.md) | Rewards grouped by mission conditions | 

## Example

```python
from wot_api_client.models.encyclopedia_personalmissions_data_value_operations_value_missions_value import EncyclopediaPersonalmissionsDataValueOperationsValueMissionsValue

# TODO update the JSON string below
json = "{}"
# create an instance of EncyclopediaPersonalmissionsDataValueOperationsValueMissionsValue from a JSON string
encyclopedia_personalmissions_data_value_operations_value_missions_value_instance = EncyclopediaPersonalmissionsDataValueOperationsValueMissionsValue.from_json(json)
# print the JSON string representation of the object
print(EncyclopediaPersonalmissionsDataValueOperationsValueMissionsValue.to_json())

# convert the object into a dict
encyclopedia_personalmissions_data_value_operations_value_missions_value_dict = encyclopedia_personalmissions_data_value_operations_value_missions_value_instance.to_dict()
# create an instance of EncyclopediaPersonalmissionsDataValueOperationsValueMissionsValue from a dict
encyclopedia_personalmissions_data_value_operations_value_missions_value_from_dict = EncyclopediaPersonalmissionsDataValueOperationsValueMissionsValue.from_dict(encyclopedia_personalmissions_data_value_operations_value_missions_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


