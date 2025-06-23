# ClansMemberhistoryError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**error** | **object** |  | 

## Example

```python
from wot_api_client.models.clans_memberhistory_error import ClansMemberhistoryError

# TODO update the JSON string below
json = "{}"
# create an instance of ClansMemberhistoryError from a JSON string
clans_memberhistory_error_instance = ClansMemberhistoryError.from_json(json)
# print the JSON string representation of the object
print(ClansMemberhistoryError.to_json())

# convert the object into a dict
clans_memberhistory_error_dict = clans_memberhistory_error_instance.to_dict()
# create an instance of ClansMemberhistoryError from a dict
clans_memberhistory_error_from_dict = ClansMemberhistoryError.from_dict(clans_memberhistory_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


