# GetEncyclopediaAchievements200ResponseOneOfDataValueOptionsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name_i18n** | **str** | Localized **name** field | 
**image** | **str** | URL to image | 
**image_big** | **str** | 180x180px image | 
**nation_images** | [**GetEncyclopediaAchievements200ResponseOneOfDataValueOptionsInnerNationImages**](GetEncyclopediaAchievements200ResponseOneOfDataValueOptionsInnerNationImages.md) |  | 
**description** | **str** | Achievement description | 

## Example

```python
from wot_api_client.models.get_encyclopedia_achievements200_response_one_of_data_value_options_inner import GetEncyclopediaAchievements200ResponseOneOfDataValueOptionsInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetEncyclopediaAchievements200ResponseOneOfDataValueOptionsInner from a JSON string
get_encyclopedia_achievements200_response_one_of_data_value_options_inner_instance = GetEncyclopediaAchievements200ResponseOneOfDataValueOptionsInner.from_json(json)
# print the JSON string representation of the object
print(GetEncyclopediaAchievements200ResponseOneOfDataValueOptionsInner.to_json())

# convert the object into a dict
get_encyclopedia_achievements200_response_one_of_data_value_options_inner_dict = get_encyclopedia_achievements200_response_one_of_data_value_options_inner_instance.to_dict()
# create an instance of GetEncyclopediaAchievements200ResponseOneOfDataValueOptionsInner from a dict
get_encyclopedia_achievements200_response_one_of_data_value_options_inner_from_dict = GetEncyclopediaAchievements200ResponseOneOfDataValueOptionsInner.from_dict(get_encyclopedia_achievements200_response_one_of_data_value_options_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


