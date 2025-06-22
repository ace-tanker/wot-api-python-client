# GetGlobalmapEventaccountinfo200ResponseOneOf


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**meta** | [**GetAccountList200ResponseOneOfMeta**](GetAccountList200ResponseOneOfMeta.md) |  | 
**data** | [**Dict[str, GetGlobalmapEventaccountinfo200ResponseOneOfDataValue]**](GetGlobalmapEventaccountinfo200ResponseOneOfDataValue.md) |  | 

## Example

```python
from wot_api_client.models.get_globalmap_eventaccountinfo200_response_one_of import GetGlobalmapEventaccountinfo200ResponseOneOf

# TODO update the JSON string below
json = "{}"
# create an instance of GetGlobalmapEventaccountinfo200ResponseOneOf from a JSON string
get_globalmap_eventaccountinfo200_response_one_of_instance = GetGlobalmapEventaccountinfo200ResponseOneOf.from_json(json)
# print the JSON string representation of the object
print(GetGlobalmapEventaccountinfo200ResponseOneOf.to_json())

# convert the object into a dict
get_globalmap_eventaccountinfo200_response_one_of_dict = get_globalmap_eventaccountinfo200_response_one_of_instance.to_dict()
# create an instance of GetGlobalmapEventaccountinfo200ResponseOneOf from a dict
get_globalmap_eventaccountinfo200_response_one_of_from_dict = GetGlobalmapEventaccountinfo200ResponseOneOf.from_dict(get_globalmap_eventaccountinfo200_response_one_of_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


