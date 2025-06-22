# GetClansMemberhistory200ResponseOneOf


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**meta** | [**GetAccountList200ResponseOneOfMeta**](GetAccountList200ResponseOneOfMeta.md) |  | 
**data** | **Dict[str, Optional[List[GetClansMemberhistory200ResponseOneOfDataValueInner]]]** |  | 

## Example

```python
from wot_api_client.models.get_clans_memberhistory200_response_one_of import GetClansMemberhistory200ResponseOneOf

# TODO update the JSON string below
json = "{}"
# create an instance of GetClansMemberhistory200ResponseOneOf from a JSON string
get_clans_memberhistory200_response_one_of_instance = GetClansMemberhistory200ResponseOneOf.from_json(json)
# print the JSON string representation of the object
print(GetClansMemberhistory200ResponseOneOf.to_json())

# convert the object into a dict
get_clans_memberhistory200_response_one_of_dict = get_clans_memberhistory200_response_one_of_instance.to_dict()
# create an instance of GetClansMemberhistory200ResponseOneOf from a dict
get_clans_memberhistory200_response_one_of_from_dict = GetClansMemberhistory200ResponseOneOf.from_dict(get_clans_memberhistory200_response_one_of_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


