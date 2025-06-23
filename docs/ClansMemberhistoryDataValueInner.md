# ClansMemberhistoryDataValueInner


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
from wot_api_client.models.clans_memberhistory_data_value_inner import ClansMemberhistoryDataValueInner

# TODO update the JSON string below
json = "{}"
# create an instance of ClansMemberhistoryDataValueInner from a JSON string
clans_memberhistory_data_value_inner_instance = ClansMemberhistoryDataValueInner.from_json(json)
# print the JSON string representation of the object
print(ClansMemberhistoryDataValueInner.to_json())

# convert the object into a dict
clans_memberhistory_data_value_inner_dict = clans_memberhistory_data_value_inner_instance.to_dict()
# create an instance of ClansMemberhistoryDataValueInner from a dict
clans_memberhistory_data_value_inner_from_dict = ClansMemberhistoryDataValueInner.from_dict(clans_memberhistory_data_value_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


