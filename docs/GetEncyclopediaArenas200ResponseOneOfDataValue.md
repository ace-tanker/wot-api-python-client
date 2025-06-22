# GetEncyclopediaArenas200ResponseOneOfDataValue


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**arena_id** | **str** | Map ID | 
**camouflage_type** | **str** | Map type | 
**name_i18n** | **str** | Localized map name | 
**description** | **str** | Short map description | 

## Example

```python
from wot_api_client.models.get_encyclopedia_arenas200_response_one_of_data_value import GetEncyclopediaArenas200ResponseOneOfDataValue

# TODO update the JSON string below
json = "{}"
# create an instance of GetEncyclopediaArenas200ResponseOneOfDataValue from a JSON string
get_encyclopedia_arenas200_response_one_of_data_value_instance = GetEncyclopediaArenas200ResponseOneOfDataValue.from_json(json)
# print the JSON string representation of the object
print(GetEncyclopediaArenas200ResponseOneOfDataValue.to_json())

# convert the object into a dict
get_encyclopedia_arenas200_response_one_of_data_value_dict = get_encyclopedia_arenas200_response_one_of_data_value_instance.to_dict()
# create an instance of GetEncyclopediaArenas200ResponseOneOfDataValue from a dict
get_encyclopedia_arenas200_response_one_of_data_value_from_dict = GetEncyclopediaArenas200ResponseOneOfDataValue.from_dict(get_encyclopedia_arenas200_response_one_of_data_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


