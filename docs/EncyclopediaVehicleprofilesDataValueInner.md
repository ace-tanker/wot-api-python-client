# EncyclopediaVehicleprofilesDataValueInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**profile_id** | **str** | Vehicle Configuration ID | 
**tank_id** | **int** | Vehicle ID | 
**is_default** | **bool** | Standard configuration | 
**price_credit** | **int** | Cost in credits | 

## Example

```python
from wot_api_client.models.encyclopedia_vehicleprofiles_data_value_inner import EncyclopediaVehicleprofilesDataValueInner

# TODO update the JSON string below
json = "{}"
# create an instance of EncyclopediaVehicleprofilesDataValueInner from a JSON string
encyclopedia_vehicleprofiles_data_value_inner_instance = EncyclopediaVehicleprofilesDataValueInner.from_json(json)
# print the JSON string representation of the object
print(EncyclopediaVehicleprofilesDataValueInner.to_json())

# convert the object into a dict
encyclopedia_vehicleprofiles_data_value_inner_dict = encyclopedia_vehicleprofiles_data_value_inner_instance.to_dict()
# create an instance of EncyclopediaVehicleprofilesDataValueInner from a dict
encyclopedia_vehicleprofiles_data_value_inner_from_dict = EncyclopediaVehicleprofilesDataValueInner.from_dict(encyclopedia_vehicleprofiles_data_value_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


