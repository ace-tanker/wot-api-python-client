# ClanratingsTypesOk


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**meta** | [**ClanratingsTypesMeta**](ClanratingsTypesMeta.md) |  | 
**data** | [**Dict[str, ClanratingsTypesDataValue]**](ClanratingsTypesDataValue.md) |  | 

## Example

```python
from wot_api_client.models.clanratings_types_ok import ClanratingsTypesOk

# TODO update the JSON string below
json = "{}"
# create an instance of ClanratingsTypesOk from a JSON string
clanratings_types_ok_instance = ClanratingsTypesOk.from_json(json)
# print the JSON string representation of the object
print(ClanratingsTypesOk.to_json())

# convert the object into a dict
clanratings_types_ok_dict = clanratings_types_ok_instance.to_dict()
# create an instance of ClanratingsTypesOk from a dict
clanratings_types_ok_from_dict = ClanratingsTypesOk.from_dict(clanratings_types_ok_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


