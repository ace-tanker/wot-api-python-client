# GlobalmapClaninfoDataValueRatings

Clan rating on the Global Map

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**updated_at** | **int** | Ratings update time | 
**elo_6** | **int** | Clan Elo rating in Medium division | 
**elo_8** | **int** | Clan Elo rating in Champion division | 
**elo_10** | **int** | Clan Elo rating in Absolute division | 

## Example

```python
from wot_api_client.models.globalmap_claninfo_data_value_ratings import GlobalmapClaninfoDataValueRatings

# TODO update the JSON string below
json = "{}"
# create an instance of GlobalmapClaninfoDataValueRatings from a JSON string
globalmap_claninfo_data_value_ratings_instance = GlobalmapClaninfoDataValueRatings.from_json(json)
# print the JSON string representation of the object
print(GlobalmapClaninfoDataValueRatings.to_json())

# convert the object into a dict
globalmap_claninfo_data_value_ratings_dict = globalmap_claninfo_data_value_ratings_instance.to_dict()
# create an instance of GlobalmapClaninfoDataValueRatings from a dict
globalmap_claninfo_data_value_ratings_from_dict = GlobalmapClaninfoDataValueRatings.from_dict(globalmap_claninfo_data_value_ratings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


