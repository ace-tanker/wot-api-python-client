# GetStrongholdClaninfo200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**meta** | [**GetAccountList200ResponseOneOfMeta**](GetAccountList200ResponseOneOfMeta.md) |  | 
**data** | [**Dict[str, GetStrongholdClaninfo200ResponseOneOfDataValue]**](GetStrongholdClaninfo200ResponseOneOfDataValue.md) |  | 
**error** | [**GetAccountList200ResponseOneOf1Error**](GetAccountList200ResponseOneOf1Error.md) |  | 

## Example

```python
from wot_api_client.models.get_stronghold_claninfo200_response import GetStrongholdClaninfo200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetStrongholdClaninfo200Response from a JSON string
get_stronghold_claninfo200_response_instance = GetStrongholdClaninfo200Response.from_json(json)
# print the JSON string representation of the object
print(GetStrongholdClaninfo200Response.to_json())

# convert the object into a dict
get_stronghold_claninfo200_response_dict = get_stronghold_claninfo200_response_instance.to_dict()
# create an instance of GetStrongholdClaninfo200Response from a dict
get_stronghold_claninfo200_response_from_dict = GetStrongholdClaninfo200Response.from_dict(get_stronghold_claninfo200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


