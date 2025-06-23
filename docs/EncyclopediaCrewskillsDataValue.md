# EncyclopediaCrewskillsDataValue


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**skill** | **str** | Skill ID | 
**name** | **str** | Skill name | 
**description** | **str** | Skill description | 
**image_url** | [**EncyclopediaCrewskillsDataValueImageUrl**](EncyclopediaCrewskillsDataValueImageUrl.md) |  | 
**is_perk** | **bool** | Indicates if it is a perk | 

## Example

```python
from wot_api_client.models.encyclopedia_crewskills_data_value import EncyclopediaCrewskillsDataValue

# TODO update the JSON string below
json = "{}"
# create an instance of EncyclopediaCrewskillsDataValue from a JSON string
encyclopedia_crewskills_data_value_instance = EncyclopediaCrewskillsDataValue.from_json(json)
# print the JSON string representation of the object
print(EncyclopediaCrewskillsDataValue.to_json())

# convert the object into a dict
encyclopedia_crewskills_data_value_dict = encyclopedia_crewskills_data_value_instance.to_dict()
# create an instance of EncyclopediaCrewskillsDataValue from a dict
encyclopedia_crewskills_data_value_from_dict = EncyclopediaCrewskillsDataValue.from_dict(encyclopedia_crewskills_data_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


