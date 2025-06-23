# ClanratingsNeighborsOk


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**meta** | [**ClanratingsNeighborsMeta**](ClanratingsNeighborsMeta.md) |  | 
**data** | [**List[ClanratingsClansDataValue]**](ClanratingsClansDataValue.md) |  | 

## Example

```python
from wot_api_client.models.clanratings_neighbors_ok import ClanratingsNeighborsOk

# TODO update the JSON string below
json = "{}"
# create an instance of ClanratingsNeighborsOk from a JSON string
clanratings_neighbors_ok_instance = ClanratingsNeighborsOk.from_json(json)
# print the JSON string representation of the object
print(ClanratingsNeighborsOk.to_json())

# convert the object into a dict
clanratings_neighbors_ok_dict = clanratings_neighbors_ok_instance.to_dict()
# create an instance of ClanratingsNeighborsOk from a dict
clanratings_neighbors_ok_from_dict = ClanratingsNeighborsOk.from_dict(clanratings_neighbors_ok_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


