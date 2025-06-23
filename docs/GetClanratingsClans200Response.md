# GetClanratingsClans200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**meta** | [**ClanratingsClansMeta**](ClanratingsClansMeta.md) |  | 
**data** | [**Dict[str, ClanratingsClansDataValue]**](ClanratingsClansDataValue.md) |  | 
**error** | [**ClanratingsClansErrorError**](ClanratingsClansErrorError.md) |  | 

## Example

```python
from wot_api_client.models.get_clanratings_clans200_response import GetClanratingsClans200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetClanratingsClans200Response from a JSON string
get_clanratings_clans200_response_instance = GetClanratingsClans200Response.from_json(json)
# print the JSON string representation of the object
print(GetClanratingsClans200Response.to_json())

# convert the object into a dict
get_clanratings_clans200_response_dict = get_clanratings_clans200_response_instance.to_dict()
# create an instance of GetClanratingsClans200Response from a dict
get_clanratings_clans200_response_from_dict = GetClanratingsClans200Response.from_dict(get_clanratings_clans200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


