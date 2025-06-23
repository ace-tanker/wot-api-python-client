# StrongholdClaninfoOk


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**meta** | [**StrongholdClaninfoMeta**](StrongholdClaninfoMeta.md) |  | 
**data** | [**Dict[str, StrongholdClaninfoDataValue]**](StrongholdClaninfoDataValue.md) |  | 

## Example

```python
from wot_api_client.models.stronghold_claninfo_ok import StrongholdClaninfoOk

# TODO update the JSON string below
json = "{}"
# create an instance of StrongholdClaninfoOk from a JSON string
stronghold_claninfo_ok_instance = StrongholdClaninfoOk.from_json(json)
# print the JSON string representation of the object
print(StrongholdClaninfoOk.to_json())

# convert the object into a dict
stronghold_claninfo_ok_dict = stronghold_claninfo_ok_instance.to_dict()
# create an instance of StrongholdClaninfoOk from a dict
stronghold_claninfo_ok_from_dict = StrongholdClaninfoOk.from_dict(stronghold_claninfo_ok_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


