# ClanratingsTopDataInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**clan_id** | **int** | Clan ID | 
**clan_name** | **str** | Clan name | 
**clan_tag** | **str** | Clan tag | 
**v10l_avg** | [**ClanratingsTopDataInnerV10lAvg**](ClanratingsTopDataInnerV10lAvg.md) |  | 
**battles_count_avg** | [**ClanratingsTopDataInnerBattlesCountAvg**](ClanratingsTopDataInnerBattlesCountAvg.md) |  | 
**battles_count_avg_daily** | [**ClanratingsTopDataInnerBattlesCountAvgDaily**](ClanratingsTopDataInnerBattlesCountAvgDaily.md) |  | 
**global_rating_avg** | [**ClanratingsTopDataInnerGlobalRatingAvg**](ClanratingsTopDataInnerGlobalRatingAvg.md) |  | 
**global_rating_weighted_avg** | [**ClanratingsTopDataInnerGlobalRatingWeightedAvg**](ClanratingsTopDataInnerGlobalRatingWeightedAvg.md) |  | 
**efficiency** | [**ClanratingsTopDataInnerEfficiency**](ClanratingsTopDataInnerEfficiency.md) |  | 
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
from wot_api_client.models.clanratings_top_data_inner import ClanratingsTopDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of ClanratingsTopDataInner from a JSON string
clanratings_top_data_inner_instance = ClanratingsTopDataInner.from_json(json)
# print the JSON string representation of the object
print(ClanratingsTopDataInner.to_json())

# convert the object into a dict
clanratings_top_data_inner_dict = clanratings_top_data_inner_instance.to_dict()
# create an instance of ClanratingsTopDataInner from a dict
clanratings_top_data_inner_from_dict = ClanratingsTopDataInner.from_dict(clanratings_top_data_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


