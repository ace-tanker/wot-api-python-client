# ClansListError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**error** | **object** |  | 

## Example

```python
from wot_api_client.models.clans_list_error import ClansListError

# TODO update the JSON string below
json = "{}"
# create an instance of ClansListError from a JSON string
clans_list_error_instance = ClansListError.from_json(json)
# print the JSON string representation of the object
print(ClansListError.to_json())

# convert the object into a dict
clans_list_error_dict = clans_list_error_instance.to_dict()
# create an instance of ClansListError from a dict
clans_list_error_from_dict = ClansListError.from_dict(clans_list_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


