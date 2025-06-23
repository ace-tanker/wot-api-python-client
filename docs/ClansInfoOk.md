# ClansInfoOk


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**meta** | [**ClansInfoMeta**](ClansInfoMeta.md) |  | 
**data** | [**Dict[str, ClansInfoDataValue]**](ClansInfoDataValue.md) |  | 

## Example

```python
from wot_api_client.models.clans_info_ok import ClansInfoOk

# TODO update the JSON string below
json = "{}"
# create an instance of ClansInfoOk from a JSON string
clans_info_ok_instance = ClansInfoOk.from_json(json)
# print the JSON string representation of the object
print(ClansInfoOk.to_json())

# convert the object into a dict
clans_info_ok_dict = clans_info_ok_instance.to_dict()
# create an instance of ClansInfoOk from a dict
clans_info_ok_from_dict = ClansInfoOk.from_dict(clans_info_ok_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


