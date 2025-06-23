# StrongholdClanreservesError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**error** | [**StrongholdClanreservesErrorError**](StrongholdClanreservesErrorError.md) |  | 

## Example

```python
from wot_api_client.models.stronghold_clanreserves_error import StrongholdClanreservesError

# TODO update the JSON string below
json = "{}"
# create an instance of StrongholdClanreservesError from a JSON string
stronghold_clanreserves_error_instance = StrongholdClanreservesError.from_json(json)
# print the JSON string representation of the object
print(StrongholdClanreservesError.to_json())

# convert the object into a dict
stronghold_clanreserves_error_dict = stronghold_clanreserves_error_instance.to_dict()
# create an instance of StrongholdClanreservesError from a dict
stronghold_clanreserves_error_from_dict = StrongholdClanreservesError.from_dict(stronghold_clanreserves_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


