# ClanratingsClansDataValueGmEloRating

Elo rating on the Global Map

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **float** | Absolute value | 
**rank** | **int** | Position | 
**rank_delta** | **int** | Change of position in rating | 

## Example

```python
from wot_api_client.models.clanratings_clans_data_value_gm_elo_rating import ClanratingsClansDataValueGmEloRating

# TODO update the JSON string below
json = "{}"
# create an instance of ClanratingsClansDataValueGmEloRating from a JSON string
clanratings_clans_data_value_gm_elo_rating_instance = ClanratingsClansDataValueGmEloRating.from_json(json)
# print the JSON string representation of the object
print(ClanratingsClansDataValueGmEloRating.to_json())

# convert the object into a dict
clanratings_clans_data_value_gm_elo_rating_dict = clanratings_clans_data_value_gm_elo_rating_instance.to_dict()
# create an instance of ClanratingsClansDataValueGmEloRating from a dict
clanratings_clans_data_value_gm_elo_rating_from_dict = ClanratingsClansDataValueGmEloRating.from_dict(clanratings_clans_data_value_gm_elo_rating_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


