# ClansGlossaryData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**clans_roles** | **Dict[str, str]** | Available clan positions | 

## Example

```python
from wot_api_client.models.clans_glossary_data import ClansGlossaryData

# TODO update the JSON string below
json = "{}"
# create an instance of ClansGlossaryData from a JSON string
clans_glossary_data_instance = ClansGlossaryData.from_json(json)
# print the JSON string representation of the object
print(ClansGlossaryData.to_json())

# convert the object into a dict
clans_glossary_data_dict = clans_glossary_data_instance.to_dict()
# create an instance of ClansGlossaryData from a dict
clans_glossary_data_from_dict = ClansGlossaryData.from_dict(clans_glossary_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


