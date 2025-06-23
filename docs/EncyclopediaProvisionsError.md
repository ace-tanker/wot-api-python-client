# EncyclopediaProvisionsError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**error** | **object** |  | 

## Example

```python
from wot_api_client.models.encyclopedia_provisions_error import EncyclopediaProvisionsError

# TODO update the JSON string below
json = "{}"
# create an instance of EncyclopediaProvisionsError from a JSON string
encyclopedia_provisions_error_instance = EncyclopediaProvisionsError.from_json(json)
# print the JSON string representation of the object
print(EncyclopediaProvisionsError.to_json())

# convert the object into a dict
encyclopedia_provisions_error_dict = encyclopedia_provisions_error_instance.to_dict()
# create an instance of EncyclopediaProvisionsError from a dict
encyclopedia_provisions_error_from_dict = EncyclopediaProvisionsError.from_dict(encyclopedia_provisions_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


