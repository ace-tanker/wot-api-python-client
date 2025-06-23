# ClanratingsDatesOk


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**meta** | [**ClanratingsDatesMeta**](ClanratingsDatesMeta.md) |  | 
**data** | [**Dict[str, ClanratingsDatesDataValue]**](ClanratingsDatesDataValue.md) |  | 

## Example

```python
from wot_api_client.models.clanratings_dates_ok import ClanratingsDatesOk

# TODO update the JSON string below
json = "{}"
# create an instance of ClanratingsDatesOk from a JSON string
clanratings_dates_ok_instance = ClanratingsDatesOk.from_json(json)
# print the JSON string representation of the object
print(ClanratingsDatesOk.to_json())

# convert the object into a dict
clanratings_dates_ok_dict = clanratings_dates_ok_instance.to_dict()
# create an instance of ClanratingsDatesOk from a dict
clanratings_dates_ok_from_dict = ClanratingsDatesOk.from_dict(clanratings_dates_ok_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


