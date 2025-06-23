# ClansMemberhistoryOk


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**meta** | [**ClansMemberhistoryMeta**](ClansMemberhistoryMeta.md) |  | 
**data** | **Dict[str, Optional[List[ClansMemberhistoryDataValueInner]]]** |  | 

## Example

```python
from wot_api_client.models.clans_memberhistory_ok import ClansMemberhistoryOk

# TODO update the JSON string below
json = "{}"
# create an instance of ClansMemberhistoryOk from a JSON string
clans_memberhistory_ok_instance = ClansMemberhistoryOk.from_json(json)
# print the JSON string representation of the object
print(ClansMemberhistoryOk.to_json())

# convert the object into a dict
clans_memberhistory_ok_dict = clans_memberhistory_ok_instance.to_dict()
# create an instance of ClansMemberhistoryOk from a dict
clans_memberhistory_ok_from_dict = ClansMemberhistoryOk.from_dict(clans_memberhistory_ok_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


