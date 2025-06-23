# EncyclopediaBadgesDataValue


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**badge_id** | **int** | Badge ID | 
**name** | **str** | Badge name | 
**description** | **str** | Badge description | 
**images** | [**EncyclopediaBadgesDataValueImages**](EncyclopediaBadgesDataValueImages.md) |  | 

## Example

```python
from wot_api_client.models.encyclopedia_badges_data_value import EncyclopediaBadgesDataValue

# TODO update the JSON string below
json = "{}"
# create an instance of EncyclopediaBadgesDataValue from a JSON string
encyclopedia_badges_data_value_instance = EncyclopediaBadgesDataValue.from_json(json)
# print the JSON string representation of the object
print(EncyclopediaBadgesDataValue.to_json())

# convert the object into a dict
encyclopedia_badges_data_value_dict = encyclopedia_badges_data_value_instance.to_dict()
# create an instance of EncyclopediaBadgesDataValue from a dict
encyclopedia_badges_data_value_from_dict = EncyclopediaBadgesDataValue.from_dict(encyclopedia_badges_data_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


