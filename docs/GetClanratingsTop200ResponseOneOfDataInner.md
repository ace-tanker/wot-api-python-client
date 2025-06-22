# GetClanratingsTop200ResponseOneOfDataInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**clan_id** | **int** | Clan ID | 
**clan_name** | **str** | Clan name | 
**clan_tag** | **str** | Clan tag | 
**v10l_avg** | [**GetClanratingsTop200ResponseOneOfDataInnerV10lAvg**](GetClanratingsTop200ResponseOneOfDataInnerV10lAvg.md) |  | 
**battles_count_avg** | [**GetClanratingsTop200ResponseOneOfDataInnerBattlesCountAvg**](GetClanratingsTop200ResponseOneOfDataInnerBattlesCountAvg.md) |  | 
**battles_count_avg_daily** | [**GetClanratingsTop200ResponseOneOfDataInnerBattlesCountAvgDaily**](GetClanratingsTop200ResponseOneOfDataInnerBattlesCountAvgDaily.md) |  | 
**global_rating_avg** | [**GetClanratingsTop200ResponseOneOfDataInnerGlobalRatingAvg**](GetClanratingsTop200ResponseOneOfDataInnerGlobalRatingAvg.md) |  | 
**global_rating_weighted_avg** | [**GetClanratingsTop200ResponseOneOfDataInnerGlobalRatingWeightedAvg**](GetClanratingsTop200ResponseOneOfDataInnerGlobalRatingWeightedAvg.md) |  | 
**efficiency** | [**GetClanratingsTop200ResponseOneOfDataInnerEfficiency**](GetClanratingsTop200ResponseOneOfDataInnerEfficiency.md) |  | 
**wins_ratio_avg** | [**GetClanratingsClans200ResponseOneOfDataValueWinsRatioAvg**](GetClanratingsClans200ResponseOneOfDataValueWinsRatioAvg.md) |  | 
**rating_fort** | [**GetClanratingsClans200ResponseOneOfDataValueRatingFort**](GetClanratingsClans200ResponseOneOfDataValueRatingFort.md) |  | 
**fb_elo_rating** | [**GetClanratingsClans200ResponseOneOfDataValueFbEloRating**](GetClanratingsClans200ResponseOneOfDataValueFbEloRating.md) |  | 
**fb_elo_rating_10** | [**GetClanratingsClans200ResponseOneOfDataValueFbEloRating10**](GetClanratingsClans200ResponseOneOfDataValueFbEloRating10.md) |  | 
**fb_elo_rating_8** | [**GetClanratingsClans200ResponseOneOfDataValueFbEloRating8**](GetClanratingsClans200ResponseOneOfDataValueFbEloRating8.md) |  | 
**fb_elo_rating_6** | [**GetClanratingsClans200ResponseOneOfDataValueFbEloRating6**](GetClanratingsClans200ResponseOneOfDataValueFbEloRating6.md) |  | 
**gm_elo_rating** | [**GetClanratingsClans200ResponseOneOfDataValueGmEloRating**](GetClanratingsClans200ResponseOneOfDataValueGmEloRating.md) |  | 
**gm_elo_rating_10** | [**GetClanratingsClans200ResponseOneOfDataValueGmEloRating10**](GetClanratingsClans200ResponseOneOfDataValueGmEloRating10.md) |  | 
**gm_elo_rating_8** | [**GetClanratingsClans200ResponseOneOfDataValueGmEloRating8**](GetClanratingsClans200ResponseOneOfDataValueGmEloRating8.md) |  | 
**gm_elo_rating_6** | [**GetClanratingsClans200ResponseOneOfDataValueGmEloRating6**](GetClanratingsClans200ResponseOneOfDataValueGmEloRating6.md) |  | 
**exclude_reasons** | **Dict[str, str]** | Reasons why specified rating categories were not calculated. Contains data in \&quot;key-value\&quot; format, where the key is category name and the value is reason.  Possible reasons:   * inactivity - Inactivity for 28 days  * newbies_measure - Under 10 members in the clan  * limits - Rank conditions not met  * blocked - Clan blocked  * other - Technical reasons | 

## Example

```python
from wot_api_client.models.get_clanratings_top200_response_one_of_data_inner import GetClanratingsTop200ResponseOneOfDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetClanratingsTop200ResponseOneOfDataInner from a JSON string
get_clanratings_top200_response_one_of_data_inner_instance = GetClanratingsTop200ResponseOneOfDataInner.from_json(json)
# print the JSON string representation of the object
print(GetClanratingsTop200ResponseOneOfDataInner.to_json())

# convert the object into a dict
get_clanratings_top200_response_one_of_data_inner_dict = get_clanratings_top200_response_one_of_data_inner_instance.to_dict()
# create an instance of GetClanratingsTop200ResponseOneOfDataInner from a dict
get_clanratings_top200_response_one_of_data_inner_from_dict = GetClanratingsTop200ResponseOneOfDataInner.from_dict(get_clanratings_top200_response_one_of_data_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


