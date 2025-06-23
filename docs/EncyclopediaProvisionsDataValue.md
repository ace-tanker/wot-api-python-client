# EncyclopediaProvisionsDataValue


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
from wot_api_client.models.encyclopedia_provisions_data_value import EncyclopediaProvisionsDataValue

# TODO update the JSON string below
json = "{}"
# create an instance of EncyclopediaProvisionsDataValue from a JSON string
encyclopedia_provisions_data_value_instance = EncyclopediaProvisionsDataValue.from_json(json)
# print the JSON string representation of the object
print(EncyclopediaProvisionsDataValue.to_json())

# convert the object into a dict
encyclopedia_provisions_data_value_dict = encyclopedia_provisions_data_value_instance.to_dict()
# create an instance of EncyclopediaProvisionsDataValue from a dict
encyclopedia_provisions_data_value_from_dict = EncyclopediaProvisionsDataValue.from_dict(encyclopedia_provisions_data_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


