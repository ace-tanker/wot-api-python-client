# GetTanksStats200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**meta** | [**GetAccountList200ResponseOneOfMeta**](GetAccountList200ResponseOneOfMeta.md) |  | 
**data** | **Dict[str, Optional[List[GetTanksStats200ResponseOneOfDataValueInner]]]** |  | 
**error** | [**GetAccountList200ResponseOneOf1Error**](GetAccountList200ResponseOneOf1Error.md) |  | 

## Example

```python
from wot_api_client.models.get_tanks_stats200_response import GetTanksStats200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetTanksStats200Response from a JSON string
get_tanks_stats200_response_instance = GetTanksStats200Response.from_json(json)
# print the JSON string representation of the object
print(GetTanksStats200Response.to_json())

# convert the object into a dict
get_tanks_stats200_response_dict = get_tanks_stats200_response_instance.to_dict()
# create an instance of GetTanksStats200Response from a dict
get_tanks_stats200_response_from_dict = GetTanksStats200Response.from_dict(get_tanks_stats200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


