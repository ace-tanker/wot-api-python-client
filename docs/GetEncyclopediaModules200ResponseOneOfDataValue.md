# GetEncyclopediaModules200ResponseOneOfDataValue


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
**default_profile** | [**GetEncyclopediaModules200ResponseOneOfDataValueDefaultProfile**](GetEncyclopediaModules200ResponseOneOfDataValueDefaultProfile.md) |  | [optional] 

## Example

```python
from wot_api_client.models.get_encyclopedia_modules200_response_one_of_data_value import GetEncyclopediaModules200ResponseOneOfDataValue

# TODO update the JSON string below
json = "{}"
# create an instance of GetEncyclopediaModules200ResponseOneOfDataValue from a JSON string
get_encyclopedia_modules200_response_one_of_data_value_instance = GetEncyclopediaModules200ResponseOneOfDataValue.from_json(json)
# print the JSON string representation of the object
print(GetEncyclopediaModules200ResponseOneOfDataValue.to_json())

# convert the object into a dict
get_encyclopedia_modules200_response_one_of_data_value_dict = get_encyclopedia_modules200_response_one_of_data_value_instance.to_dict()
# create an instance of GetEncyclopediaModules200ResponseOneOfDataValue from a dict
get_encyclopedia_modules200_response_one_of_data_value_from_dict = GetEncyclopediaModules200ResponseOneOfDataValue.from_dict(get_encyclopedia_modules200_response_one_of_data_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


