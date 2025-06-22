# GetEncyclopediaInfo200ResponseOneOfData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**game_version** | **str** | Game client version | 
**tanks_updated_at** | **int** | Time when vehicles details in Tankopedia were updated | 
**vehicle_types** | **Dict[str, str]** | Available vehicle types | 
**vehicle_nations** | **Dict[str, str]** | Nations available | 
**vehicle_crew_roles** | **Dict[str, str]** | Available crew qualifications | 
**languages** | **Dict[str, str]** | List of supported languages | 
**achievement_sections** | [**Dict[str, GetEncyclopediaInfo200ResponseOneOfDataAchievementSectionsValue]**](GetEncyclopediaInfo200ResponseOneOfDataAchievementSectionsValue.md) | Award sections | 

## Example

```python
from wot_api_client.models.get_encyclopedia_info200_response_one_of_data import GetEncyclopediaInfo200ResponseOneOfData

# TODO update the JSON string below
json = "{}"
# create an instance of GetEncyclopediaInfo200ResponseOneOfData from a JSON string
get_encyclopedia_info200_response_one_of_data_instance = GetEncyclopediaInfo200ResponseOneOfData.from_json(json)
# print the JSON string representation of the object
print(GetEncyclopediaInfo200ResponseOneOfData.to_json())

# convert the object into a dict
get_encyclopedia_info200_response_one_of_data_dict = get_encyclopedia_info200_response_one_of_data_instance.to_dict()
# create an instance of GetEncyclopediaInfo200ResponseOneOfData from a dict
get_encyclopedia_info200_response_one_of_data_from_dict = GetEncyclopediaInfo200ResponseOneOfData.from_dict(get_encyclopedia_info200_response_one_of_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


