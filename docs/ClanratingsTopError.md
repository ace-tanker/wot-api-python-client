# ClanratingsTopError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**error** | [**ClanratingsClansErrorError**](ClanratingsClansErrorError.md) |  | 

## Example

```python
from wot_api_client.models.clanratings_top_error import ClanratingsTopError

# TODO update the JSON string below
json = "{}"
# create an instance of ClanratingsTopError from a JSON string
clanratings_top_error_instance = ClanratingsTopError.from_json(json)
# print the JSON string representation of the object
print(ClanratingsTopError.to_json())

# convert the object into a dict
clanratings_top_error_dict = clanratings_top_error_instance.to_dict()
# create an instance of ClanratingsTopError from a dict
clanratings_top_error_from_dict = ClanratingsTopError.from_dict(clanratings_top_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


