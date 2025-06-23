# EncyclopediaArenasDataValue


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**arena_id** | **str** | Map ID | 
**camouflage_type** | **str** | Map type | 
**name_i18n** | **str** | Localized map name | 
**description** | **str** | Short map description | 

## Example

```python
from wot_api_client.models.encyclopedia_arenas_data_value import EncyclopediaArenasDataValue

# TODO update the JSON string below
json = "{}"
# create an instance of EncyclopediaArenasDataValue from a JSON string
encyclopedia_arenas_data_value_instance = EncyclopediaArenasDataValue.from_json(json)
# print the JSON string representation of the object
print(EncyclopediaArenasDataValue.to_json())

# convert the object into a dict
encyclopedia_arenas_data_value_dict = encyclopedia_arenas_data_value_instance.to_dict()
# create an instance of EncyclopediaArenasDataValue from a dict
encyclopedia_arenas_data_value_from_dict = EncyclopediaArenasDataValue.from_dict(encyclopedia_arenas_data_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


