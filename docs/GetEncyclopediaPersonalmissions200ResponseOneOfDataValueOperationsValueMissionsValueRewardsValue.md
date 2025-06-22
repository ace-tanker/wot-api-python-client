# GetEncyclopediaPersonalmissions200ResponseOneOfDataValueOperationsValueMissionsValueRewardsValue


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
from wot_api_client.models.get_encyclopedia_personalmissions200_response_one_of_data_value_operations_value_missions_value_rewards_value import GetEncyclopediaPersonalmissions200ResponseOneOfDataValueOperationsValueMissionsValueRewardsValue

# TODO update the JSON string below
json = "{}"
# create an instance of GetEncyclopediaPersonalmissions200ResponseOneOfDataValueOperationsValueMissionsValueRewardsValue from a JSON string
get_encyclopedia_personalmissions200_response_one_of_data_value_operations_value_missions_value_rewards_value_instance = GetEncyclopediaPersonalmissions200ResponseOneOfDataValueOperationsValueMissionsValueRewardsValue.from_json(json)
# print the JSON string representation of the object
print(GetEncyclopediaPersonalmissions200ResponseOneOfDataValueOperationsValueMissionsValueRewardsValue.to_json())

# convert the object into a dict
get_encyclopedia_personalmissions200_response_one_of_data_value_operations_value_missions_value_rewards_value_dict = get_encyclopedia_personalmissions200_response_one_of_data_value_operations_value_missions_value_rewards_value_instance.to_dict()
# create an instance of GetEncyclopediaPersonalmissions200ResponseOneOfDataValueOperationsValueMissionsValueRewardsValue from a dict
get_encyclopedia_personalmissions200_response_one_of_data_value_operations_value_missions_value_rewards_value_from_dict = GetEncyclopediaPersonalmissions200ResponseOneOfDataValueOperationsValueMissionsValueRewardsValue.from_dict(get_encyclopedia_personalmissions200_response_one_of_data_value_operations_value_missions_value_rewards_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


