# EncyclopediaModulesDataValueDefaultProfile

Basic technical characteristics of module.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gun** | [**EncyclopediaModulesDataValueDefaultProfileGun**](EncyclopediaModulesDataValueDefaultProfileGun.md) |  | 
**engine** | [**EncyclopediaModulesDataValueDefaultProfileEngine**](EncyclopediaModulesDataValueDefaultProfileEngine.md) |  | 
**turret** | [**EncyclopediaModulesDataValueDefaultProfileTurret**](EncyclopediaModulesDataValueDefaultProfileTurret.md) |  | 
**suspension** | [**EncyclopediaModulesDataValueDefaultProfileSuspension**](EncyclopediaModulesDataValueDefaultProfileSuspension.md) |  | 
**radio** | [**EncyclopediaModulesDataValueDefaultProfileRadio**](EncyclopediaModulesDataValueDefaultProfileRadio.md) |  | 

## Example

```python
from wot_api_client.models.encyclopedia_modules_data_value_default_profile import EncyclopediaModulesDataValueDefaultProfile

# TODO update the JSON string below
json = "{}"
# create an instance of EncyclopediaModulesDataValueDefaultProfile from a JSON string
encyclopedia_modules_data_value_default_profile_instance = EncyclopediaModulesDataValueDefaultProfile.from_json(json)
# print the JSON string representation of the object
print(EncyclopediaModulesDataValueDefaultProfile.to_json())

# convert the object into a dict
encyclopedia_modules_data_value_default_profile_dict = encyclopedia_modules_data_value_default_profile_instance.to_dict()
# create an instance of EncyclopediaModulesDataValueDefaultProfile from a dict
encyclopedia_modules_data_value_default_profile_from_dict = EncyclopediaModulesDataValueDefaultProfile.from_dict(encyclopedia_modules_data_value_default_profile_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


