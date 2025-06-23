# GetClansGlossary200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**meta** | **object** |  | 
**data** | [**ClansGlossaryData**](ClansGlossaryData.md) |  | 
**error** | **object** |  | 

## Example

```python
from wot_api_client.models.get_clans_glossary200_response import GetClansGlossary200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetClansGlossary200Response from a JSON string
get_clans_glossary200_response_instance = GetClansGlossary200Response.from_json(json)
# print the JSON string representation of the object
print(GetClansGlossary200Response.to_json())

# convert the object into a dict
get_clans_glossary200_response_dict = get_clans_glossary200_response_instance.to_dict()
# create an instance of GetClansGlossary200Response from a dict
get_clans_glossary200_response_from_dict = GetClansGlossary200Response.from_dict(get_clans_glossary200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


