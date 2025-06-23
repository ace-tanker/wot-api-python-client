# ClanratingsTopDataInnerGlobalRatingWeightedAvg

Weighted average of global rating value

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **float** | Absolute value | 
**rank** | **int** | Position | 
**rank_delta** | **int** | Change of position in rating | 

## Example

```python
from wot_api_client.models.clanratings_top_data_inner_global_rating_weighted_avg import ClanratingsTopDataInnerGlobalRatingWeightedAvg

# TODO update the JSON string below
json = "{}"
# create an instance of ClanratingsTopDataInnerGlobalRatingWeightedAvg from a JSON string
clanratings_top_data_inner_global_rating_weighted_avg_instance = ClanratingsTopDataInnerGlobalRatingWeightedAvg.from_json(json)
# print the JSON string representation of the object
print(ClanratingsTopDataInnerGlobalRatingWeightedAvg.to_json())

# convert the object into a dict
clanratings_top_data_inner_global_rating_weighted_avg_dict = clanratings_top_data_inner_global_rating_weighted_avg_instance.to_dict()
# create an instance of ClanratingsTopDataInnerGlobalRatingWeightedAvg from a dict
clanratings_top_data_inner_global_rating_weighted_avg_from_dict = ClanratingsTopDataInnerGlobalRatingWeightedAvg.from_dict(clanratings_top_data_inner_global_rating_weighted_avg_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


