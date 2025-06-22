# GetEncyclopediaModules200ResponseOneOfDataValueDefaultProfileTurret

Turret characteristics

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hp** | **int** | Hit points | 
**armor_front** | **int** | Armor: front (mm) | 
**armor_sides** | **int** | Armor: sides (mm) | 
**armor_rear** | **int** | Armor: rear (mm) | 
**view_range** | **int** | View range (m) | 
**traverse_speed** | **int** | Traverse speed (deg/s) | 

## Example

```python
from wot_api_client.models.get_encyclopedia_modules200_response_one_of_data_value_default_profile_turret import GetEncyclopediaModules200ResponseOneOfDataValueDefaultProfileTurret

# TODO update the JSON string below
json = "{}"
# create an instance of GetEncyclopediaModules200ResponseOneOfDataValueDefaultProfileTurret from a JSON string
get_encyclopedia_modules200_response_one_of_data_value_default_profile_turret_instance = GetEncyclopediaModules200ResponseOneOfDataValueDefaultProfileTurret.from_json(json)
# print the JSON string representation of the object
print(GetEncyclopediaModules200ResponseOneOfDataValueDefaultProfileTurret.to_json())

# convert the object into a dict
get_encyclopedia_modules200_response_one_of_data_value_default_profile_turret_dict = get_encyclopedia_modules200_response_one_of_data_value_default_profile_turret_instance.to_dict()
# create an instance of GetEncyclopediaModules200ResponseOneOfDataValueDefaultProfileTurret from a dict
get_encyclopedia_modules200_response_one_of_data_value_default_profile_turret_from_dict = GetEncyclopediaModules200ResponseOneOfDataValueDefaultProfileTurret.from_dict(get_encyclopedia_modules200_response_one_of_data_value_default_profile_turret_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


