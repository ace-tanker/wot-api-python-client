# EncyclopediaInfoData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**game_version** | **str** | Game client version | 
**tanks_updated_at** | **int** | Time when vehicles details in Tankopedia were updated | 
**vehicle_types** | **Dict[str, str]** | Available vehicle types | 
**vehicle_nations** | **Dict[str, str]** | Nations available | 
**vehicle_crew_roles** | **Dict[str, str]** | Available crew qualifications | 
**languages** | **Dict[str, str]** | List of supported languages | 
**achievement_sections** | [**Dict[str, EncyclopediaInfoDataAchievementSectionsValue]**](EncyclopediaInfoDataAchievementSectionsValue.md) | Award sections | 

## Example

```python
from wot_api_client.models.encyclopedia_info_data import EncyclopediaInfoData

# TODO update the JSON string below
json = "{}"
# create an instance of EncyclopediaInfoData from a JSON string
encyclopedia_info_data_instance = EncyclopediaInfoData.from_json(json)
# print the JSON string representation of the object
print(EncyclopediaInfoData.to_json())

# convert the object into a dict
encyclopedia_info_data_dict = encyclopedia_info_data_instance.to_dict()
# create an instance of EncyclopediaInfoData from a dict
encyclopedia_info_data_from_dict = EncyclopediaInfoData.from_dict(encyclopedia_info_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


