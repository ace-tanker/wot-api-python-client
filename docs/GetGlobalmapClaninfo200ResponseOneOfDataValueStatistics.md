# GetGlobalmapClaninfo200ResponseOneOfDataValueStatistics

Clan statistics on the Global Map

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**battles** | **int** | Battles fought | 
**wins** | **int** | Victories | 
**losses** | **int** | Defeats | 
**battles_10_level** | **int** | Battles fought in Absolute division | 
**battles_8_level** | **int** | Battles fought in Champion division | 
**battles_6_level** | **int** | Battles fought in Medium division | 
**wins_10_level** | **int** | Victories in Absolute division | 
**wins_8_level** | **int** | Victories in Champion division | 
**wins_6_level** | **int** | Victories in Medium division | 
**captures** | **int** | Total number by provinces captured by clan | 
**provinces_count** | **int** | Current number of captured provinces | 

## Example

```python
from wot_api_client.models.get_globalmap_claninfo200_response_one_of_data_value_statistics import GetGlobalmapClaninfo200ResponseOneOfDataValueStatistics

# TODO update the JSON string below
json = "{}"
# create an instance of GetGlobalmapClaninfo200ResponseOneOfDataValueStatistics from a JSON string
get_globalmap_claninfo200_response_one_of_data_value_statistics_instance = GetGlobalmapClaninfo200ResponseOneOfDataValueStatistics.from_json(json)
# print the JSON string representation of the object
print(GetGlobalmapClaninfo200ResponseOneOfDataValueStatistics.to_json())

# convert the object into a dict
get_globalmap_claninfo200_response_one_of_data_value_statistics_dict = get_globalmap_claninfo200_response_one_of_data_value_statistics_instance.to_dict()
# create an instance of GetGlobalmapClaninfo200ResponseOneOfDataValueStatistics from a dict
get_globalmap_claninfo200_response_one_of_data_value_statistics_from_dict = GetGlobalmapClaninfo200ResponseOneOfDataValueStatistics.from_dict(get_globalmap_claninfo200_response_one_of_data_value_statistics_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


