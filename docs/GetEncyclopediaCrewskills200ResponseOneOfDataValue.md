# GetEncyclopediaCrewskills200ResponseOneOfDataValue


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**skill** | **str** | Skill ID | 
**name** | **str** | Skill name | 
**description** | **str** | Skill description | 
**image_url** | [**GetEncyclopediaCrewskills200ResponseOneOfDataValueImageUrl**](GetEncyclopediaCrewskills200ResponseOneOfDataValueImageUrl.md) |  | 
**is_perk** | **bool** | Indicates if it is a perk | 

## Example

```python
from wot_api_client.models.get_encyclopedia_crewskills200_response_one_of_data_value import GetEncyclopediaCrewskills200ResponseOneOfDataValue

# TODO update the JSON string below
json = "{}"
# create an instance of GetEncyclopediaCrewskills200ResponseOneOfDataValue from a JSON string
get_encyclopedia_crewskills200_response_one_of_data_value_instance = GetEncyclopediaCrewskills200ResponseOneOfDataValue.from_json(json)
# print the JSON string representation of the object
print(GetEncyclopediaCrewskills200ResponseOneOfDataValue.to_json())

# convert the object into a dict
get_encyclopedia_crewskills200_response_one_of_data_value_dict = get_encyclopedia_crewskills200_response_one_of_data_value_instance.to_dict()
# create an instance of GetEncyclopediaCrewskills200ResponseOneOfDataValue from a dict
get_encyclopedia_crewskills200_response_one_of_data_value_from_dict = GetEncyclopediaCrewskills200ResponseOneOfDataValue.from_dict(get_encyclopedia_crewskills200_response_one_of_data_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


