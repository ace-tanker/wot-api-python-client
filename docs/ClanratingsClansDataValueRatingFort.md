# ClanratingsClansDataValueRatingFort

Rating in Battles for Stronghold

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **float** | Absolute value | 
**rank** | **int** | Position | 
**rank_delta** | **int** | Change of position in rating | 

## Example

```python
from wot_api_client.models.clanratings_clans_data_value_rating_fort import ClanratingsClansDataValueRatingFort

# TODO update the JSON string below
json = "{}"
# create an instance of ClanratingsClansDataValueRatingFort from a JSON string
clanratings_clans_data_value_rating_fort_instance = ClanratingsClansDataValueRatingFort.from_json(json)
# print the JSON string representation of the object
print(ClanratingsClansDataValueRatingFort.to_json())

# convert the object into a dict
clanratings_clans_data_value_rating_fort_dict = clanratings_clans_data_value_rating_fort_instance.to_dict()
# create an instance of ClanratingsClansDataValueRatingFort from a dict
clanratings_clans_data_value_rating_fort_from_dict = ClanratingsClansDataValueRatingFort.from_dict(clanratings_clans_data_value_rating_fort_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


