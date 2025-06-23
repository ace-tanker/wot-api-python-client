# ClanratingsClansDataValueEfficiency

Indicator of clan's performance.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **int** | Absolute value | 
**rank** | **int** | Position | 
**rank_delta** | **int** | Change of position in rating | 

## Example

```python
from wot_api_client.models.clanratings_clans_data_value_efficiency import ClanratingsClansDataValueEfficiency

# TODO update the JSON string below
json = "{}"
# create an instance of ClanratingsClansDataValueEfficiency from a JSON string
clanratings_clans_data_value_efficiency_instance = ClanratingsClansDataValueEfficiency.from_json(json)
# print the JSON string representation of the object
print(ClanratingsClansDataValueEfficiency.to_json())

# convert the object into a dict
clanratings_clans_data_value_efficiency_dict = clanratings_clans_data_value_efficiency_instance.to_dict()
# create an instance of ClanratingsClansDataValueEfficiency from a dict
clanratings_clans_data_value_efficiency_from_dict = ClanratingsClansDataValueEfficiency.from_dict(clanratings_clans_data_value_efficiency_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


