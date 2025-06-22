# GetGlobalmapClaninfo200ResponseOneOfDataValueRatings

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
from wot_api_client.models.get_globalmap_claninfo200_response_one_of_data_value_ratings import GetGlobalmapClaninfo200ResponseOneOfDataValueRatings

# TODO update the JSON string below
json = "{}"
# create an instance of GetGlobalmapClaninfo200ResponseOneOfDataValueRatings from a JSON string
get_globalmap_claninfo200_response_one_of_data_value_ratings_instance = GetGlobalmapClaninfo200ResponseOneOfDataValueRatings.from_json(json)
# print the JSON string representation of the object
print(GetGlobalmapClaninfo200ResponseOneOfDataValueRatings.to_json())

# convert the object into a dict
get_globalmap_claninfo200_response_one_of_data_value_ratings_dict = get_globalmap_claninfo200_response_one_of_data_value_ratings_instance.to_dict()
# create an instance of GetGlobalmapClaninfo200ResponseOneOfDataValueRatings from a dict
get_globalmap_claninfo200_response_one_of_data_value_ratings_from_dict = GetGlobalmapClaninfo200ResponseOneOfDataValueRatings.from_dict(get_globalmap_claninfo200_response_one_of_data_value_ratings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


