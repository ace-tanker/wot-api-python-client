# TanksStatsDataValueInnerRandom

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
**max_frags** | **int** | Maximum destroyed in battle | 
**max_xp** | **int** | Maximum experience per battle | 
**max_damage** | **int** | Maximum damage caused in a battle | 

## Example

```python
from wot_api_client.models.tanks_stats_data_value_inner_random import TanksStatsDataValueInnerRandom

# TODO update the JSON string below
json = "{}"
# create an instance of TanksStatsDataValueInnerRandom from a JSON string
tanks_stats_data_value_inner_random_instance = TanksStatsDataValueInnerRandom.from_json(json)
# print the JSON string representation of the object
print(TanksStatsDataValueInnerRandom.to_json())

# convert the object into a dict
tanks_stats_data_value_inner_random_dict = tanks_stats_data_value_inner_random_instance.to_dict()
# create an instance of TanksStatsDataValueInnerRandom from a dict
tanks_stats_data_value_inner_random_from_dict = TanksStatsDataValueInnerRandom.from_dict(tanks_stats_data_value_inner_random_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


