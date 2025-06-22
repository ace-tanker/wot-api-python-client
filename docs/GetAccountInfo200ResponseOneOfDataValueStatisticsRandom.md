# GetAccountInfo200ResponseOneOfDataValueStatisticsRandom

Random battles statistics.

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
**avg_damage_blocked** | **float** | Average damage blocked by armor per battle. Damage blocked by armor is damage received from shells (AP, HEAT and APCR) that hit a vehicle but caused no damage. Value is calculated starting from version 9.0. | 
**avg_damage_assisted_track** | **float** | Average damage upon your shooting the track | 
**avg_damage_assisted_radio** | **float** | Average damage upon your spotting | 
**avg_damage_assisted** | **float** | Average assisted damage without stun damage. | 
**avg_damage_assisted_stun** | **float** | Average assisted stun damage. | 

## Example

```python
from wot_api_client.models.get_account_info200_response_one_of_data_value_statistics_random import GetAccountInfo200ResponseOneOfDataValueStatisticsRandom

# TODO update the JSON string below
json = "{}"
# create an instance of GetAccountInfo200ResponseOneOfDataValueStatisticsRandom from a JSON string
get_account_info200_response_one_of_data_value_statistics_random_instance = GetAccountInfo200ResponseOneOfDataValueStatisticsRandom.from_json(json)
# print the JSON string representation of the object
print(GetAccountInfo200ResponseOneOfDataValueStatisticsRandom.to_json())

# convert the object into a dict
get_account_info200_response_one_of_data_value_statistics_random_dict = get_account_info200_response_one_of_data_value_statistics_random_instance.to_dict()
# create an instance of GetAccountInfo200ResponseOneOfDataValueStatisticsRandom from a dict
get_account_info200_response_one_of_data_value_statistics_random_from_dict = GetAccountInfo200ResponseOneOfDataValueStatisticsRandom.from_dict(get_account_info200_response_one_of_data_value_statistics_random_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


