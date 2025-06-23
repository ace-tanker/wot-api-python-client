# EncyclopediaAchievementsError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**error** | **object** |  | 

## Example

```python
from wot_api_client.models.encyclopedia_achievements_error import EncyclopediaAchievementsError

# TODO update the JSON string below
json = "{}"
# create an instance of EncyclopediaAchievementsError from a JSON string
encyclopedia_achievements_error_instance = EncyclopediaAchievementsError.from_json(json)
# print the JSON string representation of the object
print(EncyclopediaAchievementsError.to_json())

# convert the object into a dict
encyclopedia_achievements_error_dict = encyclopedia_achievements_error_instance.to_dict()
# create an instance of EncyclopediaAchievementsError from a dict
encyclopedia_achievements_error_from_dict = EncyclopediaAchievementsError.from_dict(encyclopedia_achievements_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


