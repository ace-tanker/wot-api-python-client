# TanksAchievementsOk


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**meta** | [**TanksAchievementsMeta**](TanksAchievementsMeta.md) |  | 
**data** | **Dict[str, Optional[List[TanksAchievementsDataValueInner]]]** |  | 

## Example

```python
from wot_api_client.models.tanks_achievements_ok import TanksAchievementsOk

# TODO update the JSON string below
json = "{}"
# create an instance of TanksAchievementsOk from a JSON string
tanks_achievements_ok_instance = TanksAchievementsOk.from_json(json)
# print the JSON string representation of the object
print(TanksAchievementsOk.to_json())

# convert the object into a dict
tanks_achievements_ok_dict = tanks_achievements_ok_instance.to_dict()
# create an instance of TanksAchievementsOk from a dict
tanks_achievements_ok_from_dict = TanksAchievementsOk.from_dict(tanks_achievements_ok_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


