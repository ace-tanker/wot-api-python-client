# ClanratingsClansOk


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**meta** | [**ClanratingsClansMeta**](ClanratingsClansMeta.md) |  | 
**data** | [**Dict[str, ClanratingsClansDataValue]**](ClanratingsClansDataValue.md) |  | 

## Example

```python
from wot_api_client.models.clanratings_clans_ok import ClanratingsClansOk

# TODO update the JSON string below
json = "{}"
# create an instance of ClanratingsClansOk from a JSON string
clanratings_clans_ok_instance = ClanratingsClansOk.from_json(json)
# print the JSON string representation of the object
print(ClanratingsClansOk.to_json())

# convert the object into a dict
clanratings_clans_ok_dict = clanratings_clans_ok_instance.to_dict()
# create an instance of ClanratingsClansOk from a dict
clanratings_clans_ok_from_dict = ClanratingsClansOk.from_dict(clanratings_clans_ok_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


