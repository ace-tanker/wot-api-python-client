# EncyclopediaAchievementsOk


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**meta** | [**EncyclopediaAchievementsMeta**](EncyclopediaAchievementsMeta.md) |  | 
**data** | [**Dict[str, EncyclopediaAchievementsDataValue]**](EncyclopediaAchievementsDataValue.md) |  | 

## Example

```python
from wot_api_client.models.encyclopedia_achievements_ok import EncyclopediaAchievementsOk

# TODO update the JSON string below
json = "{}"
# create an instance of EncyclopediaAchievementsOk from a JSON string
encyclopedia_achievements_ok_instance = EncyclopediaAchievementsOk.from_json(json)
# print the JSON string representation of the object
print(EncyclopediaAchievementsOk.to_json())

# convert the object into a dict
encyclopedia_achievements_ok_dict = encyclopedia_achievements_ok_instance.to_dict()
# create an instance of EncyclopediaAchievementsOk from a dict
encyclopedia_achievements_ok_from_dict = EncyclopediaAchievementsOk.from_dict(encyclopedia_achievements_ok_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


