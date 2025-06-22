# GetGlobalmapEventaccountinfo200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**meta** | [**GetAccountList200ResponseOneOfMeta**](GetAccountList200ResponseOneOfMeta.md) |  | 
**data** | [**Dict[str, GetGlobalmapEventaccountinfo200ResponseOneOfDataValue]**](GetGlobalmapEventaccountinfo200ResponseOneOfDataValue.md) |  | 
**error** | [**GetAccountList200ResponseOneOf1Error**](GetAccountList200ResponseOneOf1Error.md) |  | 

## Example

```python
from wot_api_client.models.get_globalmap_eventaccountinfo200_response import GetGlobalmapEventaccountinfo200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetGlobalmapEventaccountinfo200Response from a JSON string
get_globalmap_eventaccountinfo200_response_instance = GetGlobalmapEventaccountinfo200Response.from_json(json)
# print the JSON string representation of the object
print(GetGlobalmapEventaccountinfo200Response.to_json())

# convert the object into a dict
get_globalmap_eventaccountinfo200_response_dict = get_globalmap_eventaccountinfo200_response_instance.to_dict()
# create an instance of GetGlobalmapEventaccountinfo200Response from a dict
get_globalmap_eventaccountinfo200_response_from_dict = GetGlobalmapEventaccountinfo200Response.from_dict(get_globalmap_eventaccountinfo200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


