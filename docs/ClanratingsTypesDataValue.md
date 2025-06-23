# ClanratingsTypesDataValue


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Rating period | 
**rank_fields** | **List[str]** | Rating categories | 

## Example

```python
from wot_api_client.models.clanratings_types_data_value import ClanratingsTypesDataValue

# TODO update the JSON string below
json = "{}"
# create an instance of ClanratingsTypesDataValue from a JSON string
clanratings_types_data_value_instance = ClanratingsTypesDataValue.from_json(json)
# print the JSON string representation of the object
print(ClanratingsTypesDataValue.to_json())

# convert the object into a dict
clanratings_types_data_value_dict = clanratings_types_data_value_instance.to_dict()
# create an instance of ClanratingsTypesDataValue from a dict
clanratings_types_data_value_from_dict = ClanratingsTypesDataValue.from_dict(clanratings_types_data_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


