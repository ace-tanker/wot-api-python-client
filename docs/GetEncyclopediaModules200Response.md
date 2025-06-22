# GetEncyclopediaModules200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**meta** | [**GetEncyclopediaProvisions200ResponseOneOfMeta**](GetEncyclopediaProvisions200ResponseOneOfMeta.md) |  | 
**data** | [**Dict[str, GetEncyclopediaModules200ResponseOneOfDataValue]**](GetEncyclopediaModules200ResponseOneOfDataValue.md) |  | 
**error** | [**GetAccountList200ResponseOneOf1Error**](GetAccountList200ResponseOneOf1Error.md) |  | 

## Example

```python
from wot_api_client.models.get_encyclopedia_modules200_response import GetEncyclopediaModules200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetEncyclopediaModules200Response from a JSON string
get_encyclopedia_modules200_response_instance = GetEncyclopediaModules200Response.from_json(json)
# print the JSON string representation of the object
print(GetEncyclopediaModules200Response.to_json())

# convert the object into a dict
get_encyclopedia_modules200_response_dict = get_encyclopedia_modules200_response_instance.to_dict()
# create an instance of GetEncyclopediaModules200Response from a dict
get_encyclopedia_modules200_response_from_dict = GetEncyclopediaModules200Response.from_dict(get_encyclopedia_modules200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


