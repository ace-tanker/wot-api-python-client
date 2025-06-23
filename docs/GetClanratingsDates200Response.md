# GetClanratingsDates200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**meta** | [**ClanratingsDatesMeta**](ClanratingsDatesMeta.md) |  | 
**data** | [**Dict[str, ClanratingsDatesDataValue]**](ClanratingsDatesDataValue.md) |  | 
**error** | **object** |  | 

## Example

```python
from wot_api_client.models.get_clanratings_dates200_response import GetClanratingsDates200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetClanratingsDates200Response from a JSON string
get_clanratings_dates200_response_instance = GetClanratingsDates200Response.from_json(json)
# print the JSON string representation of the object
print(GetClanratingsDates200Response.to_json())

# convert the object into a dict
get_clanratings_dates200_response_dict = get_clanratings_dates200_response_instance.to_dict()
# create an instance of GetClanratingsDates200Response from a dict
get_clanratings_dates200_response_from_dict = GetClanratingsDates200Response.from_dict(get_clanratings_dates200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


