# EncyclopediaModulesOk


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**meta** | [**EncyclopediaModulesMeta**](EncyclopediaModulesMeta.md) |  | 
**data** | [**Dict[str, EncyclopediaModulesDataValue]**](EncyclopediaModulesDataValue.md) |  | 

## Example

```python
from wot_api_client.models.encyclopedia_modules_ok import EncyclopediaModulesOk

# TODO update the JSON string below
json = "{}"
# create an instance of EncyclopediaModulesOk from a JSON string
encyclopedia_modules_ok_instance = EncyclopediaModulesOk.from_json(json)
# print the JSON string representation of the object
print(EncyclopediaModulesOk.to_json())

# convert the object into a dict
encyclopedia_modules_ok_dict = encyclopedia_modules_ok_instance.to_dict()
# create an instance of EncyclopediaModulesOk from a dict
encyclopedia_modules_ok_from_dict = EncyclopediaModulesOk.from_dict(encyclopedia_modules_ok_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


