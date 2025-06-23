# EncyclopediaVehiclesDataValueModulesTreeValue


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**module_id** | **int** | Module ID | 
**name** | **str** | Module name | 
**type** | **str** | Module type | 
**price_credit** | **int** | Cost in credits | 
**price_xp** | **int** | Research cost | 
**next_tanks** | **List[int]** | List of vehicle IDs available after research of the module | 
**next_modules** | **List[int]** | List of module IDs available after research of the module | 
**is_default** | **bool** | Indicates if the module is basic | 

## Example

```python
from wot_api_client.models.encyclopedia_vehicles_data_value_modules_tree_value import EncyclopediaVehiclesDataValueModulesTreeValue

# TODO update the JSON string below
json = "{}"
# create an instance of EncyclopediaVehiclesDataValueModulesTreeValue from a JSON string
encyclopedia_vehicles_data_value_modules_tree_value_instance = EncyclopediaVehiclesDataValueModulesTreeValue.from_json(json)
# print the JSON string representation of the object
print(EncyclopediaVehiclesDataValueModulesTreeValue.to_json())

# convert the object into a dict
encyclopedia_vehicles_data_value_modules_tree_value_dict = encyclopedia_vehicles_data_value_modules_tree_value_instance.to_dict()
# create an instance of EncyclopediaVehiclesDataValueModulesTreeValue from a dict
encyclopedia_vehicles_data_value_modules_tree_value_from_dict = EncyclopediaVehiclesDataValueModulesTreeValue.from_dict(encyclopedia_vehicles_data_value_modules_tree_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


