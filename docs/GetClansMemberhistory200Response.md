# GetClansMemberhistory200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**meta** | [**ClansMemberhistoryMeta**](ClansMemberhistoryMeta.md) |  | 
**data** | **Dict[str, Optional[List[ClansMemberhistoryDataValueInner]]]** |  | 
**error** | **object** |  | 

## Example

```python
from wot_api_client.models.get_clans_memberhistory200_response import GetClansMemberhistory200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetClansMemberhistory200Response from a JSON string
get_clans_memberhistory200_response_instance = GetClansMemberhistory200Response.from_json(json)
# print the JSON string representation of the object
print(GetClansMemberhistory200Response.to_json())

# convert the object into a dict
get_clans_memberhistory200_response_dict = get_clans_memberhistory200_response_instance.to_dict()
# create an instance of GetClansMemberhistory200Response from a dict
get_clans_memberhistory200_response_from_dict = GetClansMemberhistory200Response.from_dict(get_clans_memberhistory200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


