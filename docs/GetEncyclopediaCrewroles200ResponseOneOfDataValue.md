# GetEncyclopediaCrewroles200ResponseOneOfDataValue


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**role** | **str** | Сrew qualification ID | 
**name** | **str** | Сrew qualification name | 
**skills** | **List[str]** | List of crew member qualifications | 

## Example

```python
from wot_api_client.models.get_encyclopedia_crewroles200_response_one_of_data_value import GetEncyclopediaCrewroles200ResponseOneOfDataValue

# TODO update the JSON string below
json = "{}"
# create an instance of GetEncyclopediaCrewroles200ResponseOneOfDataValue from a JSON string
get_encyclopedia_crewroles200_response_one_of_data_value_instance = GetEncyclopediaCrewroles200ResponseOneOfDataValue.from_json(json)
# print the JSON string representation of the object
print(GetEncyclopediaCrewroles200ResponseOneOfDataValue.to_json())

# convert the object into a dict
get_encyclopedia_crewroles200_response_one_of_data_value_dict = get_encyclopedia_crewroles200_response_one_of_data_value_instance.to_dict()
# create an instance of GetEncyclopediaCrewroles200ResponseOneOfDataValue from a dict
get_encyclopedia_crewroles200_response_one_of_data_value_from_dict = GetEncyclopediaCrewroles200ResponseOneOfDataValue.from_dict(get_encyclopedia_crewroles200_response_one_of_data_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


