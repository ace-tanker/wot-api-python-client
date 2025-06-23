# AccountAchievementsError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**error** | **object** |  | 

## Example

```python
from wot_api_client.models.account_achievements_error import AccountAchievementsError

# TODO update the JSON string below
json = "{}"
# create an instance of AccountAchievementsError from a JSON string
account_achievements_error_instance = AccountAchievementsError.from_json(json)
# print the JSON string representation of the object
print(AccountAchievementsError.to_json())

# convert the object into a dict
account_achievements_error_dict = account_achievements_error_instance.to_dict()
# create an instance of AccountAchievementsError from a dict
account_achievements_error_from_dict = AccountAchievementsError.from_dict(account_achievements_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


