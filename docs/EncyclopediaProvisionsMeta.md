# EncyclopediaProvisionsMeta


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
from wot_api_client.models.encyclopedia_provisions_meta import EncyclopediaProvisionsMeta

# TODO update the JSON string below
json = "{}"
# create an instance of EncyclopediaProvisionsMeta from a JSON string
encyclopedia_provisions_meta_instance = EncyclopediaProvisionsMeta.from_json(json)
# print the JSON string representation of the object
print(EncyclopediaProvisionsMeta.to_json())

# convert the object into a dict
encyclopedia_provisions_meta_dict = encyclopedia_provisions_meta_instance.to_dict()
# create an instance of EncyclopediaProvisionsMeta from a dict
encyclopedia_provisions_meta_from_dict = EncyclopediaProvisionsMeta.from_dict(encyclopedia_provisions_meta_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


