# GetClansGlossary200ResponseOneOf


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**meta** | **object** |  | 
**data** | [**GetClansGlossary200ResponseOneOfData**](GetClansGlossary200ResponseOneOfData.md) |  | 

## Example

```python
from wot_api_client.models.get_clans_glossary200_response_one_of import GetClansGlossary200ResponseOneOf

# TODO update the JSON string below
json = "{}"
# create an instance of GetClansGlossary200ResponseOneOf from a JSON string
get_clans_glossary200_response_one_of_instance = GetClansGlossary200ResponseOneOf.from_json(json)
# print the JSON string representation of the object
print(GetClansGlossary200ResponseOneOf.to_json())

# convert the object into a dict
get_clans_glossary200_response_one_of_dict = get_clans_glossary200_response_one_of_instance.to_dict()
# create an instance of GetClansGlossary200ResponseOneOf from a dict
get_clans_glossary200_response_one_of_from_dict = GetClansGlossary200ResponseOneOf.from_dict(get_clans_glossary200_response_one_of_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


