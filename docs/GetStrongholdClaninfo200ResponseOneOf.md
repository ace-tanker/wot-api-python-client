# GetStrongholdClaninfo200ResponseOneOf


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**meta** | [**GetAccountList200ResponseOneOfMeta**](GetAccountList200ResponseOneOfMeta.md) |  | 
**data** | [**Dict[str, GetStrongholdClaninfo200ResponseOneOfDataValue]**](GetStrongholdClaninfo200ResponseOneOfDataValue.md) |  | 

## Example

```python
from wot_api_client.models.get_stronghold_claninfo200_response_one_of import GetStrongholdClaninfo200ResponseOneOf

# TODO update the JSON string below
json = "{}"
# create an instance of GetStrongholdClaninfo200ResponseOneOf from a JSON string
get_stronghold_claninfo200_response_one_of_instance = GetStrongholdClaninfo200ResponseOneOf.from_json(json)
# print the JSON string representation of the object
print(GetStrongholdClaninfo200ResponseOneOf.to_json())

# convert the object into a dict
get_stronghold_claninfo200_response_one_of_dict = get_stronghold_claninfo200_response_one_of_instance.to_dict()
# create an instance of GetStrongholdClaninfo200ResponseOneOf from a dict
get_stronghold_claninfo200_response_one_of_from_dict = GetStrongholdClaninfo200ResponseOneOf.from_dict(get_stronghold_claninfo200_response_one_of_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


