# EncyclopediaCrewrolesDataValue


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**role** | **str** | Сrew qualification ID | 
**name** | **str** | Сrew qualification name | 
**skills** | **List[str]** | List of crew member qualifications | 

## Example

```python
from wot_api_client.models.encyclopedia_crewroles_data_value import EncyclopediaCrewrolesDataValue

# TODO update the JSON string below
json = "{}"
# create an instance of EncyclopediaCrewrolesDataValue from a JSON string
encyclopedia_crewroles_data_value_instance = EncyclopediaCrewrolesDataValue.from_json(json)
# print the JSON string representation of the object
print(EncyclopediaCrewrolesDataValue.to_json())

# convert the object into a dict
encyclopedia_crewroles_data_value_dict = encyclopedia_crewroles_data_value_instance.to_dict()
# create an instance of EncyclopediaCrewrolesDataValue from a dict
encyclopedia_crewroles_data_value_from_dict = EncyclopediaCrewrolesDataValue.from_dict(encyclopedia_crewroles_data_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


