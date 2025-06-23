# ClanratingsClansError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**error** | [**ClanratingsClansErrorError**](ClanratingsClansErrorError.md) |  | 

## Example

```python
from wot_api_client.models.clanratings_clans_error import ClanratingsClansError

# TODO update the JSON string below
json = "{}"
# create an instance of ClanratingsClansError from a JSON string
clanratings_clans_error_instance = ClanratingsClansError.from_json(json)
# print the JSON string representation of the object
print(ClanratingsClansError.to_json())

# convert the object into a dict
clanratings_clans_error_dict = clanratings_clans_error_instance.to_dict()
# create an instance of ClanratingsClansError from a dict
clanratings_clans_error_from_dict = ClanratingsClansError.from_dict(clanratings_clans_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


