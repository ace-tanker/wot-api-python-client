# EncyclopediaModulesMeta


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**page_total** | **int** |  | 
**total** | **int** |  | 
**limit** | **int** |  | 
**page** | **int** |  | 

## Example

```python
from wot_api_client.models.encyclopedia_modules_meta import EncyclopediaModulesMeta

# TODO update the JSON string below
json = "{}"
# create an instance of EncyclopediaModulesMeta from a JSON string
encyclopedia_modules_meta_instance = EncyclopediaModulesMeta.from_json(json)
# print the JSON string representation of the object
print(EncyclopediaModulesMeta.to_json())

# convert the object into a dict
encyclopedia_modules_meta_dict = encyclopedia_modules_meta_instance.to_dict()
# create an instance of EncyclopediaModulesMeta from a dict
encyclopedia_modules_meta_from_dict = EncyclopediaModulesMeta.from_dict(encyclopedia_modules_meta_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


