# ClanratingsClansDataValueFbEloRating

Weighted Elo rating achieved in the Stronghold mode

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **float** | Absolute value | 
**rank** | **int** | Position | 
**rank_delta** | **int** | Change of position in rating | 

## Example

```python
from wot_api_client.models.clanratings_clans_data_value_fb_elo_rating import ClanratingsClansDataValueFbEloRating

# TODO update the JSON string below
json = "{}"
# create an instance of ClanratingsClansDataValueFbEloRating from a JSON string
clanratings_clans_data_value_fb_elo_rating_instance = ClanratingsClansDataValueFbEloRating.from_json(json)
# print the JSON string representation of the object
print(ClanratingsClansDataValueFbEloRating.to_json())

# convert the object into a dict
clanratings_clans_data_value_fb_elo_rating_dict = clanratings_clans_data_value_fb_elo_rating_instance.to_dict()
# create an instance of ClanratingsClansDataValueFbEloRating from a dict
clanratings_clans_data_value_fb_elo_rating_from_dict = ClanratingsClansDataValueFbEloRating.from_dict(clanratings_clans_data_value_fb_elo_rating_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


