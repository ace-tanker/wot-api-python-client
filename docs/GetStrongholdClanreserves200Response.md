# GetStrongholdClanreserves200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**meta** | [**StrongholdClanreservesMeta**](StrongholdClanreservesMeta.md) |  | 
**data** | [**List[StrongholdClanreservesDataInner]**](StrongholdClanreservesDataInner.md) |  | 
**error** | [**StrongholdClanreservesErrorError**](StrongholdClanreservesErrorError.md) |  | 

## Example

```python
from wot_api_client.models.get_stronghold_clanreserves200_response import GetStrongholdClanreserves200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetStrongholdClanreserves200Response from a JSON string
get_stronghold_clanreserves200_response_instance = GetStrongholdClanreserves200Response.from_json(json)
# print the JSON string representation of the object
print(GetStrongholdClanreserves200Response.to_json())

# convert the object into a dict
get_stronghold_clanreserves200_response_dict = get_stronghold_clanreserves200_response_instance.to_dict()
# create an instance of GetStrongholdClanreserves200Response from a dict
get_stronghold_clanreserves200_response_from_dict = GetStrongholdClanreserves200Response.from_dict(get_stronghold_clanreserves200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


