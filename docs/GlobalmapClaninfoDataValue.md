# GlobalmapClaninfoDataValue


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**clan_id** | **int** | Clan ID | 
**tag** | **str** | Clan tag | 
**name** | **str** | Clan name | 
**statistics** | [**GlobalmapClaninfoDataValueStatistics**](GlobalmapClaninfoDataValueStatistics.md) |  | 
**ratings** | [**GlobalmapClaninfoDataValueRatings**](GlobalmapClaninfoDataValueRatings.md) |  | 
**private** | [**GlobalmapClaninfoDataValuePrivate**](GlobalmapClaninfoDataValuePrivate.md) |  | 

## Example

```python
from wot_api_client.models.globalmap_claninfo_data_value import GlobalmapClaninfoDataValue

# TODO update the JSON string below
json = "{}"
# create an instance of GlobalmapClaninfoDataValue from a JSON string
globalmap_claninfo_data_value_instance = GlobalmapClaninfoDataValue.from_json(json)
# print the JSON string representation of the object
print(GlobalmapClaninfoDataValue.to_json())

# convert the object into a dict
globalmap_claninfo_data_value_dict = globalmap_claninfo_data_value_instance.to_dict()
# create an instance of GlobalmapClaninfoDataValue from a dict
globalmap_claninfo_data_value_from_dict = GlobalmapClaninfoDataValue.from_dict(globalmap_claninfo_data_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


