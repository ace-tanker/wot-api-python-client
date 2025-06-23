# EncyclopediaBoostersDataValue


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**booster_id** | **int** | Personal Reserve ID | 
**name** | **str** | Personal Reserve name | 
**description** | **str** | Personal Reserve description | 
**images** | [**EncyclopediaBoostersDataValueImages**](EncyclopediaBoostersDataValueImages.md) |  | 
**lifetime** | **int** | Personal Reserve duration in seconds | 
**resource** | **str** | Resource affected by Personal Reserve. Valid values: credits, experience, crew_experience, free_experience. | 
**is_auto** | **bool** | Personal Reserve auto activation flag | 
**expires_at** | **int** | Personal Reserve expiration time in UTC | 
**price_credit** | **int** | Cost in credits | 
**price_gold** | **int** | Price in gold | 

## Example

```python
from wot_api_client.models.encyclopedia_boosters_data_value import EncyclopediaBoostersDataValue

# TODO update the JSON string below
json = "{}"
# create an instance of EncyclopediaBoostersDataValue from a JSON string
encyclopedia_boosters_data_value_instance = EncyclopediaBoostersDataValue.from_json(json)
# print the JSON string representation of the object
print(EncyclopediaBoostersDataValue.to_json())

# convert the object into a dict
encyclopedia_boosters_data_value_dict = encyclopedia_boosters_data_value_instance.to_dict()
# create an instance of EncyclopediaBoostersDataValue from a dict
encyclopedia_boosters_data_value_from_dict = EncyclopediaBoostersDataValue.from_dict(encyclopedia_boosters_data_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


