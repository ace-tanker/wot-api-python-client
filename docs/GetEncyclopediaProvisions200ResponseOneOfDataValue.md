# GetEncyclopediaProvisions200ResponseOneOfDataValue


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**provision_id** | **int** | Equipment or consumables ID | 
**name** | **str** | Vehicle name | 
**tag** | **str** | Technical name | 
**price_gold** | **int** | Cost in gold | 
**price_credit** | **int** | Cost in credits | 
**type** | **str** | Type: consumable or equipment | 
**description** | **str** | Achievement description | 
**weight** | **int** | Weight in kilos. Used for equipment only. | 
**image** | **str** | Image link | 

## Example

```python
from wot_api_client.models.get_encyclopedia_provisions200_response_one_of_data_value import GetEncyclopediaProvisions200ResponseOneOfDataValue

# TODO update the JSON string below
json = "{}"
# create an instance of GetEncyclopediaProvisions200ResponseOneOfDataValue from a JSON string
get_encyclopedia_provisions200_response_one_of_data_value_instance = GetEncyclopediaProvisions200ResponseOneOfDataValue.from_json(json)
# print the JSON string representation of the object
print(GetEncyclopediaProvisions200ResponseOneOfDataValue.to_json())

# convert the object into a dict
get_encyclopedia_provisions200_response_one_of_data_value_dict = get_encyclopedia_provisions200_response_one_of_data_value_instance.to_dict()
# create an instance of GetEncyclopediaProvisions200ResponseOneOfDataValue from a dict
get_encyclopedia_provisions200_response_one_of_data_value_from_dict = GetEncyclopediaProvisions200ResponseOneOfDataValue.from_dict(get_encyclopedia_provisions200_response_one_of_data_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


