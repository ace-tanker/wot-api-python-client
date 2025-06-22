# GetEncyclopediaVehicleprofiles200ResponseOneOfDataValueInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**profile_id** | **str** | Vehicle Configuration ID | 
**tank_id** | **int** | Vehicle ID | 
**is_default** | **bool** | Standard configuration | 
**price_credit** | **int** | Cost in credits | 

## Example

```python
from wot_api_client.models.get_encyclopedia_vehicleprofiles200_response_one_of_data_value_inner import GetEncyclopediaVehicleprofiles200ResponseOneOfDataValueInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetEncyclopediaVehicleprofiles200ResponseOneOfDataValueInner from a JSON string
get_encyclopedia_vehicleprofiles200_response_one_of_data_value_inner_instance = GetEncyclopediaVehicleprofiles200ResponseOneOfDataValueInner.from_json(json)
# print the JSON string representation of the object
print(GetEncyclopediaVehicleprofiles200ResponseOneOfDataValueInner.to_json())

# convert the object into a dict
get_encyclopedia_vehicleprofiles200_response_one_of_data_value_inner_dict = get_encyclopedia_vehicleprofiles200_response_one_of_data_value_inner_instance.to_dict()
# create an instance of GetEncyclopediaVehicleprofiles200ResponseOneOfDataValueInner from a dict
get_encyclopedia_vehicleprofiles200_response_one_of_data_value_inner_from_dict = GetEncyclopediaVehicleprofiles200ResponseOneOfDataValueInner.from_dict(get_encyclopedia_vehicleprofiles200_response_one_of_data_value_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


