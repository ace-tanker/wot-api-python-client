# ClansAccountinfoOk


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**meta** | [**ClansAccountinfoMeta**](ClansAccountinfoMeta.md) |  | 
**data** | [**Dict[str, ClansAccountinfoDataValue]**](ClansAccountinfoDataValue.md) |  | 

## Example

```python
from wot_api_client.models.clans_accountinfo_ok import ClansAccountinfoOk

# TODO update the JSON string below
json = "{}"
# create an instance of ClansAccountinfoOk from a JSON string
clans_accountinfo_ok_instance = ClansAccountinfoOk.from_json(json)
# print the JSON string representation of the object
print(ClansAccountinfoOk.to_json())

# convert the object into a dict
clans_accountinfo_ok_dict = clans_accountinfo_ok_instance.to_dict()
# create an instance of ClansAccountinfoOk from a dict
clans_accountinfo_ok_from_dict = ClansAccountinfoOk.from_dict(clans_accountinfo_ok_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


