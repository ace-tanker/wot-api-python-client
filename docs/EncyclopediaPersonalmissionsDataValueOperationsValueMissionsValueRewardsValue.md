# EncyclopediaPersonalmissionsDataValueOperationsValueMissionsValueRewardsValue


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**conditions** | **str** | Mission conditions | 
**credits** | **int** | Credits | 
**items** | **Dict[str, int]** | List of equipment or consumables in the following format: Id–number of items | 
**premium** | **int** | Days of Premium Account | 
**free_xp** | **int** | Free Experience | 
**tokens** | **int** | Tokens | 
**slots** | **int** | Slots | 
**berths** | **int** | Bunks in Barracks | 

## Example

```python
from wot_api_client.models.encyclopedia_personalmissions_data_value_operations_value_missions_value_rewards_value import EncyclopediaPersonalmissionsDataValueOperationsValueMissionsValueRewardsValue

# TODO update the JSON string below
json = "{}"
# create an instance of EncyclopediaPersonalmissionsDataValueOperationsValueMissionsValueRewardsValue from a JSON string
encyclopedia_personalmissions_data_value_operations_value_missions_value_rewards_value_instance = EncyclopediaPersonalmissionsDataValueOperationsValueMissionsValueRewardsValue.from_json(json)
# print the JSON string representation of the object
print(EncyclopediaPersonalmissionsDataValueOperationsValueMissionsValueRewardsValue.to_json())

# convert the object into a dict
encyclopedia_personalmissions_data_value_operations_value_missions_value_rewards_value_dict = encyclopedia_personalmissions_data_value_operations_value_missions_value_rewards_value_instance.to_dict()
# create an instance of EncyclopediaPersonalmissionsDataValueOperationsValueMissionsValueRewardsValue from a dict
encyclopedia_personalmissions_data_value_operations_value_missions_value_rewards_value_from_dict = EncyclopediaPersonalmissionsDataValueOperationsValueMissionsValueRewardsValue.from_dict(encyclopedia_personalmissions_data_value_operations_value_missions_value_rewards_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


