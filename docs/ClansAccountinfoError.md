# ClansAccountinfoError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**error** | **object** |  | 

## Example

```python
from wot_api_client.models.clans_accountinfo_error import ClansAccountinfoError

# TODO update the JSON string below
json = "{}"
# create an instance of ClansAccountinfoError from a JSON string
clans_accountinfo_error_instance = ClansAccountinfoError.from_json(json)
# print the JSON string representation of the object
print(ClansAccountinfoError.to_json())

# convert the object into a dict
clans_accountinfo_error_dict = clans_accountinfo_error_instance.to_dict()
# create an instance of ClansAccountinfoError from a dict
clans_accountinfo_error_from_dict = ClansAccountinfoError.from_dict(clans_accountinfo_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


