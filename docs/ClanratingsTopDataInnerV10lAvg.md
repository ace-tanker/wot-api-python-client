# ClanratingsTopDataInnerV10lAvg

Average number of vehicles of Tier 10 per clan member

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **float** | Absolute value | 
**rank** | **int** | Position | 
**rank_delta** | **int** | Change of position in rating | 

## Example

```python
from wot_api_client.models.clanratings_top_data_inner_v10l_avg import ClanratingsTopDataInnerV10lAvg

# TODO update the JSON string below
json = "{}"
# create an instance of ClanratingsTopDataInnerV10lAvg from a JSON string
clanratings_top_data_inner_v10l_avg_instance = ClanratingsTopDataInnerV10lAvg.from_json(json)
# print the JSON string representation of the object
print(ClanratingsTopDataInnerV10lAvg.to_json())

# convert the object into a dict
clanratings_top_data_inner_v10l_avg_dict = clanratings_top_data_inner_v10l_avg_instance.to_dict()
# create an instance of ClanratingsTopDataInnerV10lAvg from a dict
clanratings_top_data_inner_v10l_avg_from_dict = ClanratingsTopDataInnerV10lAvg.from_dict(clanratings_top_data_inner_v10l_avg_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


