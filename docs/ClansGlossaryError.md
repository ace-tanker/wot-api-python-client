# ClansGlossaryError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**error** | **object** |  | 

## Example

```python
from wot_api_client.models.clans_glossary_error import ClansGlossaryError

# TODO update the JSON string below
json = "{}"
# create an instance of ClansGlossaryError from a JSON string
clans_glossary_error_instance = ClansGlossaryError.from_json(json)
# print the JSON string representation of the object
print(ClansGlossaryError.to_json())

# convert the object into a dict
clans_glossary_error_dict = clans_glossary_error_instance.to_dict()
# create an instance of ClansGlossaryError from a dict
clans_glossary_error_from_dict = ClansGlossaryError.from_dict(clans_glossary_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


