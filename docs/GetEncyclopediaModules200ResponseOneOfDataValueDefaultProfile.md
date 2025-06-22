# GetEncyclopediaModules200ResponseOneOfDataValueDefaultProfile

Basic technical characteristics of module.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gun** | [**GetEncyclopediaModules200ResponseOneOfDataValueDefaultProfileGun**](GetEncyclopediaModules200ResponseOneOfDataValueDefaultProfileGun.md) |  | 
**engine** | [**GetEncyclopediaModules200ResponseOneOfDataValueDefaultProfileEngine**](GetEncyclopediaModules200ResponseOneOfDataValueDefaultProfileEngine.md) |  | 
**turret** | [**GetEncyclopediaModules200ResponseOneOfDataValueDefaultProfileTurret**](GetEncyclopediaModules200ResponseOneOfDataValueDefaultProfileTurret.md) |  | 
**suspension** | [**GetEncyclopediaModules200ResponseOneOfDataValueDefaultProfileSuspension**](GetEncyclopediaModules200ResponseOneOfDataValueDefaultProfileSuspension.md) |  | 
**radio** | [**GetEncyclopediaModules200ResponseOneOfDataValueDefaultProfileRadio**](GetEncyclopediaModules200ResponseOneOfDataValueDefaultProfileRadio.md) |  | 

## Example

```python
from wot_api_client.models.get_encyclopedia_modules200_response_one_of_data_value_default_profile import GetEncyclopediaModules200ResponseOneOfDataValueDefaultProfile

# TODO update the JSON string below
json = "{}"
# create an instance of GetEncyclopediaModules200ResponseOneOfDataValueDefaultProfile from a JSON string
get_encyclopedia_modules200_response_one_of_data_value_default_profile_instance = GetEncyclopediaModules200ResponseOneOfDataValueDefaultProfile.from_json(json)
# print the JSON string representation of the object
print(GetEncyclopediaModules200ResponseOneOfDataValueDefaultProfile.to_json())

# convert the object into a dict
get_encyclopedia_modules200_response_one_of_data_value_default_profile_dict = get_encyclopedia_modules200_response_one_of_data_value_default_profile_instance.to_dict()
# create an instance of GetEncyclopediaModules200ResponseOneOfDataValueDefaultProfile from a dict
get_encyclopedia_modules200_response_one_of_data_value_default_profile_from_dict = GetEncyclopediaModules200ResponseOneOfDataValueDefaultProfile.from_dict(get_encyclopedia_modules200_response_one_of_data_value_default_profile_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


