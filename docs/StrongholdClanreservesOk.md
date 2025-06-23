# StrongholdClanreservesOk


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**meta** | [**StrongholdClanreservesMeta**](StrongholdClanreservesMeta.md) |  | 
**data** | [**List[StrongholdClanreservesDataInner]**](StrongholdClanreservesDataInner.md) |  | 

## Example

```python
from wot_api_client.models.stronghold_clanreserves_ok import StrongholdClanreservesOk

# TODO update the JSON string below
json = "{}"
# create an instance of StrongholdClanreservesOk from a JSON string
stronghold_clanreserves_ok_instance = StrongholdClanreservesOk.from_json(json)
# print the JSON string representation of the object
print(StrongholdClanreservesOk.to_json())

# convert the object into a dict
stronghold_clanreserves_ok_dict = stronghold_clanreserves_ok_instance.to_dict()
# create an instance of StrongholdClanreservesOk from a dict
stronghold_clanreserves_ok_from_dict = StrongholdClanreservesOk.from_dict(stronghold_clanreserves_ok_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


