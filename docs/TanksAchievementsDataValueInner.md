# TanksAchievementsDataValueInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **int** | Player account ID | 
**tank_id** | **int** | Vehicle ID | 
**achievements** | **Dict[str, int]** | Achievements earned | 
**series** | **Dict[str, int]** | Current values of Achievement Series | 
**max_series** | **Dict[str, int]** | Maximum values of achievement series | 

## Example

```python
from wot_api_client.models.tanks_achievements_data_value_inner import TanksAchievementsDataValueInner

# TODO update the JSON string below
json = "{}"
# create an instance of TanksAchievementsDataValueInner from a JSON string
tanks_achievements_data_value_inner_instance = TanksAchievementsDataValueInner.from_json(json)
# print the JSON string representation of the object
print(TanksAchievementsDataValueInner.to_json())

# convert the object into a dict
tanks_achievements_data_value_inner_dict = tanks_achievements_data_value_inner_instance.to_dict()
# create an instance of TanksAchievementsDataValueInner from a dict
tanks_achievements_data_value_inner_from_dict = TanksAchievementsDataValueInner.from_dict(tanks_achievements_data_value_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


