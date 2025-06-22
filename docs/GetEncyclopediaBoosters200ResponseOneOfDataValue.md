# GetEncyclopediaBoosters200ResponseOneOfDataValue


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**booster_id** | **int** | Personal Reserve ID | 
**name** | **str** | Personal Reserve name | 
**description** | **str** | Personal Reserve description | 
**images** | [**GetEncyclopediaBoosters200ResponseOneOfDataValueImages**](GetEncyclopediaBoosters200ResponseOneOfDataValueImages.md) |  | 
**lifetime** | **int** | Personal Reserve duration in seconds | 
**resource** | **str** | Resource affected by Personal Reserve. Valid values: credits, experience, crew_experience, free_experience. | 
**is_auto** | **bool** | Personal Reserve auto activation flag | 
**expires_at** | **int** | Personal Reserve expiration time in UTC | 
**price_credit** | **int** | Cost in credits | 
**price_gold** | **int** | Price in gold | 

## Example

```python
from wot_api_client.models.get_encyclopedia_boosters200_response_one_of_data_value import GetEncyclopediaBoosters200ResponseOneOfDataValue

# TODO update the JSON string below
json = "{}"
# create an instance of GetEncyclopediaBoosters200ResponseOneOfDataValue from a JSON string
get_encyclopedia_boosters200_response_one_of_data_value_instance = GetEncyclopediaBoosters200ResponseOneOfDataValue.from_json(json)
# print the JSON string representation of the object
print(GetEncyclopediaBoosters200ResponseOneOfDataValue.to_json())

# convert the object into a dict
get_encyclopedia_boosters200_response_one_of_data_value_dict = get_encyclopedia_boosters200_response_one_of_data_value_instance.to_dict()
# create an instance of GetEncyclopediaBoosters200ResponseOneOfDataValue from a dict
get_encyclopedia_boosters200_response_one_of_data_value_from_dict = GetEncyclopediaBoosters200ResponseOneOfDataValue.from_dict(get_encyclopedia_boosters200_response_one_of_data_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


