# GetEncyclopediaBadges200ResponseOneOfDataValue


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**badge_id** | **int** | Badge ID | 
**name** | **str** | Badge name | 
**description** | **str** | Badge description | 
**images** | [**GetEncyclopediaBadges200ResponseOneOfDataValueImages**](GetEncyclopediaBadges200ResponseOneOfDataValueImages.md) |  | 

## Example

```python
from wot_api_client.models.get_encyclopedia_badges200_response_one_of_data_value import GetEncyclopediaBadges200ResponseOneOfDataValue

# TODO update the JSON string below
json = "{}"
# create an instance of GetEncyclopediaBadges200ResponseOneOfDataValue from a JSON string
get_encyclopedia_badges200_response_one_of_data_value_instance = GetEncyclopediaBadges200ResponseOneOfDataValue.from_json(json)
# print the JSON string representation of the object
print(GetEncyclopediaBadges200ResponseOneOfDataValue.to_json())

# convert the object into a dict
get_encyclopedia_badges200_response_one_of_data_value_dict = get_encyclopedia_badges200_response_one_of_data_value_instance.to_dict()
# create an instance of GetEncyclopediaBadges200ResponseOneOfDataValue from a dict
get_encyclopedia_badges200_response_one_of_data_value_from_dict = GetEncyclopediaBadges200ResponseOneOfDataValue.from_dict(get_encyclopedia_badges200_response_one_of_data_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


