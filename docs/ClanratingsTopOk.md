# ClanratingsTopOk


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**meta** | [**ClanratingsTopMeta**](ClanratingsTopMeta.md) |  | 
**data** | [**List[ClanratingsTopDataInner]**](ClanratingsTopDataInner.md) |  | 

## Example

```python
from wot_api_client.models.clanratings_top_ok import ClanratingsTopOk

# TODO update the JSON string below
json = "{}"
# create an instance of ClanratingsTopOk from a JSON string
clanratings_top_ok_instance = ClanratingsTopOk.from_json(json)
# print the JSON string representation of the object
print(ClanratingsTopOk.to_json())

# convert the object into a dict
clanratings_top_ok_dict = clanratings_top_ok_instance.to_dict()
# create an instance of ClanratingsTopOk from a dict
clanratings_top_ok_from_dict = ClanratingsTopOk.from_dict(clanratings_top_ok_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


