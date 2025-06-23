# EncyclopediaModulesDataValue


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**module_id** | **int** | Module ID | 
**type** | **str** | Module type | 
**name** | **str** | Module name | 
**price_credit** | **int** | Cost in credits | 
**image** | **str** | Image link | 
**weight** | **int** | Weight (kg) | 
**tier** | **int** | Tier | 
**nation** | **str** | Nation | 
**tanks** | **List[int]** | Vehicles compatible with module | 
**default_profile** | [**EncyclopediaModulesDataValueDefaultProfile**](EncyclopediaModulesDataValueDefaultProfile.md) |  | [optional] 

## Example

```python
from wot_api_client.models.encyclopedia_modules_data_value import EncyclopediaModulesDataValue

# TODO update the JSON string below
json = "{}"
# create an instance of EncyclopediaModulesDataValue from a JSON string
encyclopedia_modules_data_value_instance = EncyclopediaModulesDataValue.from_json(json)
# print the JSON string representation of the object
print(EncyclopediaModulesDataValue.to_json())

# convert the object into a dict
encyclopedia_modules_data_value_dict = encyclopedia_modules_data_value_instance.to_dict()
# create an instance of EncyclopediaModulesDataValue from a dict
encyclopedia_modules_data_value_from_dict = EncyclopediaModulesDataValue.from_dict(encyclopedia_modules_data_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


