# EncyclopediaAchievementsDataValueOptionsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name_i18n** | **str** | Localized **name** field | 
**image** | **str** | URL to image | 
**image_big** | **str** | 180x180px image | 
**nation_images** | [**EncyclopediaAchievementsDataValueOptionsInnerNationImages**](EncyclopediaAchievementsDataValueOptionsInnerNationImages.md) |  | 
**description** | **str** | Achievement description | 

## Example

```python
from wot_api_client.models.encyclopedia_achievements_data_value_options_inner import EncyclopediaAchievementsDataValueOptionsInner

# TODO update the JSON string below
json = "{}"
# create an instance of EncyclopediaAchievementsDataValueOptionsInner from a JSON string
encyclopedia_achievements_data_value_options_inner_instance = EncyclopediaAchievementsDataValueOptionsInner.from_json(json)
# print the JSON string representation of the object
print(EncyclopediaAchievementsDataValueOptionsInner.to_json())

# convert the object into a dict
encyclopedia_achievements_data_value_options_inner_dict = encyclopedia_achievements_data_value_options_inner_instance.to_dict()
# create an instance of EncyclopediaAchievementsDataValueOptionsInner from a dict
encyclopedia_achievements_data_value_options_inner_from_dict = EncyclopediaAchievementsDataValueOptionsInner.from_dict(encyclopedia_achievements_data_value_options_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


