# ClansListDataInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**clan_id** | **int** | Clan ID | 
**name** | **str** | Clan name | 
**tag** | **str** | Clan tag | 
**created_at** | **int** | Clan creation date | 
**color** | **str** | Clan color in HEX #RRGGBB | 
**members_count** | **int** | Number of clan members | 
**emblems** | [**ClansListDataInnerEmblems**](ClansListDataInnerEmblems.md) |  | 

## Example

```python
from wot_api_client.models.clans_list_data_inner import ClansListDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of ClansListDataInner from a JSON string
clans_list_data_inner_instance = ClansListDataInner.from_json(json)
# print the JSON string representation of the object
print(ClansListDataInner.to_json())

# convert the object into a dict
clans_list_data_inner_dict = clans_list_data_inner_instance.to_dict()
# create an instance of ClansListDataInner from a dict
clans_list_data_inner_from_dict = ClansListDataInner.from_dict(clans_list_data_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


