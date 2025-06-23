# ClanratingsClansDataValue


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**clan_id** | **int** | Clan ID | 
**clan_name** | **str** | Clan name | 
**clan_tag** | **str** | Clan tag | 
**v10l_avg** | [**ClanratingsClansDataValueV10lAvg**](ClanratingsClansDataValueV10lAvg.md) |  | 
**battles_count_avg** | [**ClanratingsClansDataValueBattlesCountAvg**](ClanratingsClansDataValueBattlesCountAvg.md) |  | 
**battles_count_avg_daily** | [**ClanratingsClansDataValueBattlesCountAvgDaily**](ClanratingsClansDataValueBattlesCountAvgDaily.md) |  | 
**global_rating_avg** | [**ClanratingsClansDataValueGlobalRatingAvg**](ClanratingsClansDataValueGlobalRatingAvg.md) |  | 
**global_rating_weighted_avg** | [**ClanratingsClansDataValueGlobalRatingWeightedAvg**](ClanratingsClansDataValueGlobalRatingWeightedAvg.md) |  | 
**efficiency** | [**ClanratingsClansDataValueEfficiency**](ClanratingsClansDataValueEfficiency.md) |  | 
**wins_ratio_avg** | [**ClanratingsClansDataValueWinsRatioAvg**](ClanratingsClansDataValueWinsRatioAvg.md) |  | 
**rating_fort** | [**ClanratingsClansDataValueRatingFort**](ClanratingsClansDataValueRatingFort.md) |  | 
**fb_elo_rating** | [**ClanratingsClansDataValueFbEloRating**](ClanratingsClansDataValueFbEloRating.md) |  | 
**fb_elo_rating_10** | [**ClanratingsClansDataValueFbEloRating10**](ClanratingsClansDataValueFbEloRating10.md) |  | 
**fb_elo_rating_8** | [**ClanratingsClansDataValueFbEloRating8**](ClanratingsClansDataValueFbEloRating8.md) |  | 
**fb_elo_rating_6** | [**ClanratingsClansDataValueFbEloRating6**](ClanratingsClansDataValueFbEloRating6.md) |  | 
**gm_elo_rating** | [**ClanratingsClansDataValueGmEloRating**](ClanratingsClansDataValueGmEloRating.md) |  | 
**gm_elo_rating_10** | [**ClanratingsClansDataValueGmEloRating10**](ClanratingsClansDataValueGmEloRating10.md) |  | 
**gm_elo_rating_8** | [**ClanratingsClansDataValueGmEloRating8**](ClanratingsClansDataValueGmEloRating8.md) |  | 
**gm_elo_rating_6** | [**ClanratingsClansDataValueGmEloRating6**](ClanratingsClansDataValueGmEloRating6.md) |  | 
**exclude_reasons** | **Dict[str, str]** | Reasons why specified rating categories were not calculated. Contains data in \&quot;key-value\&quot; format, where the key is category name and the value is reason.  Possible reasons:   * inactivity - Inactivity for 28 days  * newbies_measure - Under 10 members in the clan  * limits - Rank conditions not met  * blocked - Clan blocked  * other - Technical reasons | 

## Example

```python
from wot_api_client.models.clanratings_clans_data_value import ClanratingsClansDataValue

# TODO update the JSON string below
json = "{}"
# create an instance of ClanratingsClansDataValue from a JSON string
clanratings_clans_data_value_instance = ClanratingsClansDataValue.from_json(json)
# print the JSON string representation of the object
print(ClanratingsClansDataValue.to_json())

# convert the object into a dict
clanratings_clans_data_value_dict = clanratings_clans_data_value_instance.to_dict()
# create an instance of ClanratingsClansDataValue from a dict
clanratings_clans_data_value_from_dict = ClanratingsClansDataValue.from_dict(clanratings_clans_data_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


