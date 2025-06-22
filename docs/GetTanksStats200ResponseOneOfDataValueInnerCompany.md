# GetTanksStats200ResponseOneOfDataValueInnerCompany

Tank Company battles statistics

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**battles** | **int** | Battles fought | 
**wins** | **int** | Victories | 
**xp** | **int** | Total experience | 
**losses** | **int** | Defeats | 
**survived_battles** | **int** | Battles survived | 
**damage_received** | **int** | Damage received | 
**damage_dealt** | **int** | Damage caused | 
**spotted** | **int** | Enemies spotted | 
**shots** | **int** | Shots fired | 
**hits** | **int** | Hits | 
**frags** | **int** | Vehicles destroyed | 
**capture_points** | **int** | Base capture points | 
**dropped_capture_points** | **int** | Base defense points | 
**hits_percents** | **int** | Hit ratio | 
**draws** | **int** | Draws | 
**battle_avg_xp** | **int** | Average experience per battle | 
**stun_number** | **int** | Number of times an enemy was stunned by you | 
**battles_on_stunning_vehicles** | **int** | Number of battles on vehicles that cause the stun effect | 
**stun_assisted_damage** | **int** | Damage to enemy vehicles stunned by you | 
**track_assisted_damage** | **int** | Damage dealt to the target with the actor keeping-on-track assistance | 
**radio_assisted_damage** | **int** | Damage dealt to the target with the actor radio recon assistance | 

## Example

```python
from wot_api_client.models.get_tanks_stats200_response_one_of_data_value_inner_company import GetTanksStats200ResponseOneOfDataValueInnerCompany

# TODO update the JSON string below
json = "{}"
# create an instance of GetTanksStats200ResponseOneOfDataValueInnerCompany from a JSON string
get_tanks_stats200_response_one_of_data_value_inner_company_instance = GetTanksStats200ResponseOneOfDataValueInnerCompany.from_json(json)
# print the JSON string representation of the object
print(GetTanksStats200ResponseOneOfDataValueInnerCompany.to_json())

# convert the object into a dict
get_tanks_stats200_response_one_of_data_value_inner_company_dict = get_tanks_stats200_response_one_of_data_value_inner_company_instance.to_dict()
# create an instance of GetTanksStats200ResponseOneOfDataValueInnerCompany from a dict
get_tanks_stats200_response_one_of_data_value_inner_company_from_dict = GetTanksStats200ResponseOneOfDataValueInnerCompany.from_dict(get_tanks_stats200_response_one_of_data_value_inner_company_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


