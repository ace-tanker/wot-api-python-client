# EncyclopediaModulesError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**error** | **object** |  | 

## Example

```python
from wot_api_client.models.encyclopedia_modules_error import EncyclopediaModulesError

# TODO update the JSON string below
json = "{}"
# create an instance of EncyclopediaModulesError from a JSON string
encyclopedia_modules_error_instance = EncyclopediaModulesError.from_json(json)
# print the JSON string representation of the object
print(EncyclopediaModulesError.to_json())

# convert the object into a dict
encyclopedia_modules_error_dict = encyclopedia_modules_error_instance.to_dict()
# create an instance of EncyclopediaModulesError from a dict
encyclopedia_modules_error_from_dict = EncyclopediaModulesError.from_dict(encyclopedia_modules_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


