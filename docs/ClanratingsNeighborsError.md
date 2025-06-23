# ClanratingsNeighborsError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**error** | [**ClanratingsClansErrorError**](ClanratingsClansErrorError.md) |  | 

## Example

```python
from wot_api_client.models.clanratings_neighbors_error import ClanratingsNeighborsError

# TODO update the JSON string below
json = "{}"
# create an instance of ClanratingsNeighborsError from a JSON string
clanratings_neighbors_error_instance = ClanratingsNeighborsError.from_json(json)
# print the JSON string representation of the object
print(ClanratingsNeighborsError.to_json())

# convert the object into a dict
clanratings_neighbors_error_dict = clanratings_neighbors_error_instance.to_dict()
# create an instance of ClanratingsNeighborsError from a dict
clanratings_neighbors_error_from_dict = ClanratingsNeighborsError.from_dict(clanratings_neighbors_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


