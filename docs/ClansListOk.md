# ClansListOk


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**meta** | [**ClansListMeta**](ClansListMeta.md) |  | 
**data** | [**List[ClansListDataInner]**](ClansListDataInner.md) |  | 

## Example

```python
from wot_api_client.models.clans_list_ok import ClansListOk

# TODO update the JSON string below
json = "{}"
# create an instance of ClansListOk from a JSON string
clans_list_ok_instance = ClansListOk.from_json(json)
# print the JSON string representation of the object
print(ClansListOk.to_json())

# convert the object into a dict
clans_list_ok_dict = clans_list_ok_instance.to_dict()
# create an instance of ClansListOk from a dict
clans_list_ok_from_dict = ClansListOk.from_dict(clans_list_ok_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


