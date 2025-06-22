# GetTanksStats200ResponseOneOfDataValueInnerStrongholdDefense

General stats for player's battles in Stronghold defense

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
**tanking_factor** | **float** | Ratio of damage blocked by armor from AP, HEAT, and APCR shells to damage received from these types of shells. Value is calculated starting from version 9.0. | 
**direct_hits_received** | **int** | Direct hits received | 
**explosion_hits_received** | **int** | Hits received as a result of splash damage | 
**explosion_hits** | **int** | Hits on enemy as a result of splash damage | 
**piercings_received** | **int** | Penetrations received | 
**piercings** | **int** | Penetrations | 
**no_damage_direct_hits_received** | **int** | Direct hits received that caused no damage | 
**max_frags** | **int** | Maximum destroyed in battle | 
**max_xp** | **int** | Maximum experience per battle | 
**max_damage** | **int** | Maximum damage caused in a battle | 

## Example

```python
from wot_api_client.models.get_tanks_stats200_response_one_of_data_value_inner_stronghold_defense import GetTanksStats200ResponseOneOfDataValueInnerStrongholdDefense

# TODO update the JSON string below
json = "{}"
# create an instance of GetTanksStats200ResponseOneOfDataValueInnerStrongholdDefense from a JSON string
get_tanks_stats200_response_one_of_data_value_inner_stronghold_defense_instance = GetTanksStats200ResponseOneOfDataValueInnerStrongholdDefense.from_json(json)
# print the JSON string representation of the object
print(GetTanksStats200ResponseOneOfDataValueInnerStrongholdDefense.to_json())

# convert the object into a dict
get_tanks_stats200_response_one_of_data_value_inner_stronghold_defense_dict = get_tanks_stats200_response_one_of_data_value_inner_stronghold_defense_instance.to_dict()
# create an instance of GetTanksStats200ResponseOneOfDataValueInnerStrongholdDefense from a dict
get_tanks_stats200_response_one_of_data_value_inner_stronghold_defense_from_dict = GetTanksStats200ResponseOneOfDataValueInnerStrongholdDefense.from_dict(get_tanks_stats200_response_one_of_data_value_inner_stronghold_defense_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


