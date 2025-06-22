# GetEncyclopediaVehicles200ResponseOneOfDataValueDefaultProfile

Standard configuration characteristics

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hp** | **int** | Hit points | 
**hull_hp** | **int** | Hull HP | 
**weight** | **int** | Weight (kg) | 
**hull_weight** | **int** | Hull weight (kg) | 
**max_weight** | **int** | Load limit (kg) | 
**max_ammo** | **int** | Ammunition | 
**speed_forward** | **int** | Top speed (km/h) | 
**speed_backward** | **int** | Top reverse speed (km/h) | 
**modules** | [**GetEncyclopediaVehicles200ResponseOneOfDataValueDefaultProfileModules**](GetEncyclopediaVehicles200ResponseOneOfDataValueDefaultProfileModules.md) |  | 
**armor** | [**GetEncyclopediaVehicles200ResponseOneOfDataValueDefaultProfileArmor**](GetEncyclopediaVehicles200ResponseOneOfDataValueDefaultProfileArmor.md) |  | 
**engine** | [**GetEncyclopediaVehicles200ResponseOneOfDataValueDefaultProfileEngine**](GetEncyclopediaVehicles200ResponseOneOfDataValueDefaultProfileEngine.md) |  | 
**gun** | [**GetEncyclopediaVehicles200ResponseOneOfDataValueDefaultProfileGun**](GetEncyclopediaVehicles200ResponseOneOfDataValueDefaultProfileGun.md) |  | 
**turret** | [**GetEncyclopediaVehicles200ResponseOneOfDataValueDefaultProfileTurret**](GetEncyclopediaVehicles200ResponseOneOfDataValueDefaultProfileTurret.md) |  | 
**suspension** | [**GetEncyclopediaVehicles200ResponseOneOfDataValueDefaultProfileSuspension**](GetEncyclopediaVehicles200ResponseOneOfDataValueDefaultProfileSuspension.md) |  | 
**radio** | [**GetEncyclopediaVehicles200ResponseOneOfDataValueDefaultProfileRadio**](GetEncyclopediaVehicles200ResponseOneOfDataValueDefaultProfileRadio.md) |  | 
**ammo** | [**List[GetEncyclopediaVehicles200ResponseOneOfDataValueDefaultProfileAmmoInner]**](GetEncyclopediaVehicles200ResponseOneOfDataValueDefaultProfileAmmoInner.md) | Gun shells characteristics | 
**siege** | [**GetEncyclopediaVehicles200ResponseOneOfDataValueDefaultProfileSiege**](GetEncyclopediaVehicles200ResponseOneOfDataValueDefaultProfileSiege.md) |  | 
**rapid** | [**GetEncyclopediaVehicles200ResponseOneOfDataValueDefaultProfileRapid**](GetEncyclopediaVehicles200ResponseOneOfDataValueDefaultProfileRapid.md) |  | 

## Example

```python
from wot_api_client.models.get_encyclopedia_vehicles200_response_one_of_data_value_default_profile import GetEncyclopediaVehicles200ResponseOneOfDataValueDefaultProfile

# TODO update the JSON string below
json = "{}"
# create an instance of GetEncyclopediaVehicles200ResponseOneOfDataValueDefaultProfile from a JSON string
get_encyclopedia_vehicles200_response_one_of_data_value_default_profile_instance = GetEncyclopediaVehicles200ResponseOneOfDataValueDefaultProfile.from_json(json)
# print the JSON string representation of the object
print(GetEncyclopediaVehicles200ResponseOneOfDataValueDefaultProfile.to_json())

# convert the object into a dict
get_encyclopedia_vehicles200_response_one_of_data_value_default_profile_dict = get_encyclopedia_vehicles200_response_one_of_data_value_default_profile_instance.to_dict()
# create an instance of GetEncyclopediaVehicles200ResponseOneOfDataValueDefaultProfile from a dict
get_encyclopedia_vehicles200_response_one_of_data_value_default_profile_from_dict = GetEncyclopediaVehicles200ResponseOneOfDataValueDefaultProfile.from_dict(get_encyclopedia_vehicles200_response_one_of_data_value_default_profile_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


