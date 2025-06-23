# AccountAchievementsOk


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**meta** | [**AccountAchievementsMeta**](AccountAchievementsMeta.md) |  | 
**data** | [**Dict[str, AccountAchievementsDataValue]**](AccountAchievementsDataValue.md) |  | 

## Example

```python
from wot_api_client.models.account_achievements_ok import AccountAchievementsOk

# TODO update the JSON string below
json = "{}"
# create an instance of AccountAchievementsOk from a JSON string
account_achievements_ok_instance = AccountAchievementsOk.from_json(json)
# print the JSON string representation of the object
print(AccountAchievementsOk.to_json())

# convert the object into a dict
account_achievements_ok_dict = account_achievements_ok_instance.to_dict()
# create an instance of AccountAchievementsOk from a dict
account_achievements_ok_from_dict = AccountAchievementsOk.from_dict(account_achievements_ok_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


