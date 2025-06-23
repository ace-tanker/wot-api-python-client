# AccountAchievementsDataValue


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**achievements** | **Dict[str, int]** | Achievements earned | 
**max_series** | **Dict[str, int]** | Maximum values of achievement series | 
**frags** | **Dict[str, int]** | Achievement progress | 

## Example

```python
from wot_api_client.models.account_achievements_data_value import AccountAchievementsDataValue

# TODO update the JSON string below
json = "{}"
# create an instance of AccountAchievementsDataValue from a JSON string
account_achievements_data_value_instance = AccountAchievementsDataValue.from_json(json)
# print the JSON string representation of the object
print(AccountAchievementsDataValue.to_json())

# convert the object into a dict
account_achievements_data_value_dict = account_achievements_data_value_instance.to_dict()
# create an instance of AccountAchievementsDataValue from a dict
account_achievements_data_value_from_dict = AccountAchievementsDataValue.from_dict(account_achievements_data_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


