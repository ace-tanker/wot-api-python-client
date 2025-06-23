# ClansListMeta


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**total** | **int** |  | 

## Example

```python
from wot_api_client.models.clans_list_meta import ClansListMeta

# TODO update the JSON string below
json = "{}"
# create an instance of ClansListMeta from a JSON string
clans_list_meta_instance = ClansListMeta.from_json(json)
# print the JSON string representation of the object
print(ClansListMeta.to_json())

# convert the object into a dict
clans_list_meta_dict = clans_list_meta_instance.to_dict()
# create an instance of ClansListMeta from a dict
clans_list_meta_from_dict = ClansListMeta.from_dict(clans_list_meta_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


