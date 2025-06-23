# EncyclopediaModulesDataValueDefaultProfileTurret

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
from wot_api_client.models.encyclopedia_modules_data_value_default_profile_turret import EncyclopediaModulesDataValueDefaultProfileTurret

# TODO update the JSON string below
json = "{}"
# create an instance of EncyclopediaModulesDataValueDefaultProfileTurret from a JSON string
encyclopedia_modules_data_value_default_profile_turret_instance = EncyclopediaModulesDataValueDefaultProfileTurret.from_json(json)
# print the JSON string representation of the object
print(EncyclopediaModulesDataValueDefaultProfileTurret.to_json())

# convert the object into a dict
encyclopedia_modules_data_value_default_profile_turret_dict = encyclopedia_modules_data_value_default_profile_turret_instance.to_dict()
# create an instance of EncyclopediaModulesDataValueDefaultProfileTurret from a dict
encyclopedia_modules_data_value_default_profile_turret_from_dict = EncyclopediaModulesDataValueDefaultProfileTurret.from_dict(encyclopedia_modules_data_value_default_profile_turret_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


