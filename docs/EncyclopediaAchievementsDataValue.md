# EncyclopediaAchievementsDataValue


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Achievement name | 
**name_i18n** | **str** | Localized **name** field | 
**type** | **str** | Type | 
**section** | **str** | Section | 
**section_order** | **int** | Section order. Sections with a lesser value of the Section order field are displayed above sections with a greater value. | 
**image** | **str** | URL to image | 
**image_big** | **str** | 180x180px image | 
**description** | **str** | Achievement description | 
**condition** | **str** | Condition | 
**hero_info** | **str** | Historical reference | 
**order** | **int** | Achievement order in this section. Achievements with a lesser value of the Order field are displayed above achievements with a greater value. | 
**options** | [**List[EncyclopediaAchievementsDataValueOptionsInner]**](EncyclopediaAchievementsDataValueOptionsInner.md) | Service Record | 
**outdated** | **bool** | Indicates, if achievement is outdated and cannot be received anymore | 

## Example

```python
from wot_api_client.models.encyclopedia_achievements_data_value import EncyclopediaAchievementsDataValue

# TODO update the JSON string below
json = "{}"
# create an instance of EncyclopediaAchievementsDataValue from a JSON string
encyclopedia_achievements_data_value_instance = EncyclopediaAchievementsDataValue.from_json(json)
# print the JSON string representation of the object
print(EncyclopediaAchievementsDataValue.to_json())

# convert the object into a dict
encyclopedia_achievements_data_value_dict = encyclopedia_achievements_data_value_instance.to_dict()
# create an instance of EncyclopediaAchievementsDataValue from a dict
encyclopedia_achievements_data_value_from_dict = EncyclopediaAchievementsDataValue.from_dict(encyclopedia_achievements_data_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


