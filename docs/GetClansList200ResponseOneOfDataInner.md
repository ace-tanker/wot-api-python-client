# GetClansList200ResponseOneOfDataInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**clan_id** | **int** | Clan ID | 
**name** | **str** | Clan name | 
**tag** | **str** | Clan tag | 
**created_at** | **int** | Clan creation date | 
**color** | **str** | Clan color in HEX #RRGGBB | 
**members_count** | **int** | Number of clan members | 
**emblems** | [**GetClansList200ResponseOneOfDataInnerEmblems**](GetClansList200ResponseOneOfDataInnerEmblems.md) |  | 

## Example

```python
from wot_api_client.models.get_clans_list200_response_one_of_data_inner import GetClansList200ResponseOneOfDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetClansList200ResponseOneOfDataInner from a JSON string
get_clans_list200_response_one_of_data_inner_instance = GetClansList200ResponseOneOfDataInner.from_json(json)
# print the JSON string representation of the object
print(GetClansList200ResponseOneOfDataInner.to_json())

# convert the object into a dict
get_clans_list200_response_one_of_data_inner_dict = get_clans_list200_response_one_of_data_inner_instance.to_dict()
# create an instance of GetClansList200ResponseOneOfDataInner from a dict
get_clans_list200_response_one_of_data_inner_from_dict = GetClansList200ResponseOneOfDataInner.from_dict(get_clans_list200_response_one_of_data_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


