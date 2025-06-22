# GetClansMemberhistory200ResponseOneOfDataValueInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **int** | Player account ID | 
**clan_id** | **int** | Clan ID | 
**joined_at** | **int** | Date when player joined clan | 
**left_at** | **int** | Date when player left clan | 
**role** | **str** | Last position in clan | 

## Example

```python
from wot_api_client.models.get_clans_memberhistory200_response_one_of_data_value_inner import GetClansMemberhistory200ResponseOneOfDataValueInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetClansMemberhistory200ResponseOneOfDataValueInner from a JSON string
get_clans_memberhistory200_response_one_of_data_value_inner_instance = GetClansMemberhistory200ResponseOneOfDataValueInner.from_json(json)
# print the JSON string representation of the object
print(GetClansMemberhistory200ResponseOneOfDataValueInner.to_json())

# convert the object into a dict
get_clans_memberhistory200_response_one_of_data_value_inner_dict = get_clans_memberhistory200_response_one_of_data_value_inner_instance.to_dict()
# create an instance of GetClansMemberhistory200ResponseOneOfDataValueInner from a dict
get_clans_memberhistory200_response_one_of_data_value_inner_from_dict = GetClansMemberhistory200ResponseOneOfDataValueInner.from_dict(get_clans_memberhistory200_response_one_of_data_value_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


