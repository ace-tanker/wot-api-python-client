# GetGlobalmapClaninfo200ResponseOneOfDataValue


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**clan_id** | **int** | Clan ID | 
**tag** | **str** | Clan tag | 
**name** | **str** | Clan name | 
**statistics** | [**GetGlobalmapClaninfo200ResponseOneOfDataValueStatistics**](GetGlobalmapClaninfo200ResponseOneOfDataValueStatistics.md) |  | 
**ratings** | [**GetGlobalmapClaninfo200ResponseOneOfDataValueRatings**](GetGlobalmapClaninfo200ResponseOneOfDataValueRatings.md) |  | 
**private** | [**GetGlobalmapClaninfo200ResponseOneOfDataValuePrivate**](GetGlobalmapClaninfo200ResponseOneOfDataValuePrivate.md) |  | 

## Example

```python
from wot_api_client.models.get_globalmap_claninfo200_response_one_of_data_value import GetGlobalmapClaninfo200ResponseOneOfDataValue

# TODO update the JSON string below
json = "{}"
# create an instance of GetGlobalmapClaninfo200ResponseOneOfDataValue from a JSON string
get_globalmap_claninfo200_response_one_of_data_value_instance = GetGlobalmapClaninfo200ResponseOneOfDataValue.from_json(json)
# print the JSON string representation of the object
print(GetGlobalmapClaninfo200ResponseOneOfDataValue.to_json())

# convert the object into a dict
get_globalmap_claninfo200_response_one_of_data_value_dict = get_globalmap_claninfo200_response_one_of_data_value_instance.to_dict()
# create an instance of GetGlobalmapClaninfo200ResponseOneOfDataValue from a dict
get_globalmap_claninfo200_response_one_of_data_value_from_dict = GetGlobalmapClaninfo200ResponseOneOfDataValue.from_dict(get_globalmap_claninfo200_response_one_of_data_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


