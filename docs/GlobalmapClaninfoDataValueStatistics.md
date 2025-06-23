# GlobalmapClaninfoDataValueStatistics

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
from wot_api_client.models.globalmap_claninfo_data_value_statistics import GlobalmapClaninfoDataValueStatistics

# TODO update the JSON string below
json = "{}"
# create an instance of GlobalmapClaninfoDataValueStatistics from a JSON string
globalmap_claninfo_data_value_statistics_instance = GlobalmapClaninfoDataValueStatistics.from_json(json)
# print the JSON string representation of the object
print(GlobalmapClaninfoDataValueStatistics.to_json())

# convert the object into a dict
globalmap_claninfo_data_value_statistics_dict = globalmap_claninfo_data_value_statistics_instance.to_dict()
# create an instance of GlobalmapClaninfoDataValueStatistics from a dict
globalmap_claninfo_data_value_statistics_from_dict = GlobalmapClaninfoDataValueStatistics.from_dict(globalmap_claninfo_data_value_statistics_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


