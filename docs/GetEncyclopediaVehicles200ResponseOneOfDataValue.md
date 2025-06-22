# GetEncyclopediaVehicles200ResponseOneOfDataValue


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tank_id** | **int** | Vehicle ID | 
**type** | **str** | Vehicle type | 
**tag** | **str** | Vehicle tag | 
**name** | **str** | Vehicle name | 
**short_name** | **str** | Vehicle short name | 
**description** | **str** | Vehicle description | 
**nation** | **str** | Nation | 
**tier** | **int** | Tier | 
**is_premium** | **bool** | Indicates if the vehicle is Premium vehicle | 
**is_gift** | **bool** | Indicates if the vehicle is a gift vehicle | 
**is_wheeled** | **bool** | Indicates if the vehicle is a wheeled vehicle | 
**is_premium_igr** | **bool** | Indicates the IGR vehicle. Active only for Korea realm | 
**images** | [**GetEncyclopediaVehicles200ResponseOneOfDataValueImages**](GetEncyclopediaVehicles200ResponseOneOfDataValueImages.md) |  | 
**price_credit** | **int** | Cost in credits | 
**price_gold** | **int** | Cost in gold | 
**prices_xp** | **Dict[str, int]** | List of research costs in form of pairs:  * parent vehicle ID * cost of research in XP | 
**next_tanks** | **Dict[str, int]** | List of vehicles available for research in form of pairs:  * researched vehicle ID * cost of research in XP | 
**default_profile** | [**GetEncyclopediaVehicles200ResponseOneOfDataValueDefaultProfile**](GetEncyclopediaVehicles200ResponseOneOfDataValueDefaultProfile.md) |  | 
**guns** | **List[int]** | List of compatible gun IDs | 
**turrets** | **List[int]** | List of compatible turret IDs | 
**engines** | **List[int]** | List of compatible engine IDs | 
**suspensions** | **List[int]** | List of compatible suspension IDs | 
**radios** | **List[int]** | List of compatible radio IDs | 
**provisions** | **List[int]** | List of IDs of compatible equipment and consumables | 
**modules_tree** | [**Dict[str, GetEncyclopediaVehicles200ResponseOneOfDataValueModulesTreeValue]**](GetEncyclopediaVehicles200ResponseOneOfDataValueModulesTreeValue.md) | Module research information | 
**crew** | [**List[GetEncyclopediaVehicles200ResponseOneOfDataValueCrewInner]**](GetEncyclopediaVehicles200ResponseOneOfDataValueCrewInner.md) | Crew | 
**multination** | [**Dict[str, GetEncyclopediaVehicles200ResponseOneOfDataValueMultinationValue]**](GetEncyclopediaVehicles200ResponseOneOfDataValueMultinationValue.md) | Информация об мультинации | 

## Example

```python
from wot_api_client.models.get_encyclopedia_vehicles200_response_one_of_data_value import GetEncyclopediaVehicles200ResponseOneOfDataValue

# TODO update the JSON string below
json = "{}"
# create an instance of GetEncyclopediaVehicles200ResponseOneOfDataValue from a JSON string
get_encyclopedia_vehicles200_response_one_of_data_value_instance = GetEncyclopediaVehicles200ResponseOneOfDataValue.from_json(json)
# print the JSON string representation of the object
print(GetEncyclopediaVehicles200ResponseOneOfDataValue.to_json())

# convert the object into a dict
get_encyclopedia_vehicles200_response_one_of_data_value_dict = get_encyclopedia_vehicles200_response_one_of_data_value_instance.to_dict()
# create an instance of GetEncyclopediaVehicles200ResponseOneOfDataValue from a dict
get_encyclopedia_vehicles200_response_one_of_data_value_from_dict = GetEncyclopediaVehicles200ResponseOneOfDataValue.from_dict(get_encyclopedia_vehicles200_response_one_of_data_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


