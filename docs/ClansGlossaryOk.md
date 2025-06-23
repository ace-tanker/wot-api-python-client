# ClansGlossaryOk


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**meta** | **object** |  | 
**data** | [**ClansGlossaryData**](ClansGlossaryData.md) |  | 

## Example

```python
from wot_api_client.models.clans_glossary_ok import ClansGlossaryOk

# TODO update the JSON string below
json = "{}"
# create an instance of ClansGlossaryOk from a JSON string
clans_glossary_ok_instance = ClansGlossaryOk.from_json(json)
# print the JSON string representation of the object
print(ClansGlossaryOk.to_json())

# convert the object into a dict
clans_glossary_ok_dict = clans_glossary_ok_instance.to_dict()
# create an instance of ClansGlossaryOk from a dict
clans_glossary_ok_from_dict = ClansGlossaryOk.from_dict(clans_glossary_ok_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


