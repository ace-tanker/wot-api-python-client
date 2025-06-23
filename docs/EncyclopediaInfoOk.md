# EncyclopediaInfoOk


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**meta** | [**EncyclopediaInfoMeta**](EncyclopediaInfoMeta.md) |  | 
**data** | [**EncyclopediaInfoData**](EncyclopediaInfoData.md) |  | 

## Example

```python
from wot_api_client.models.encyclopedia_info_ok import EncyclopediaInfoOk

# TODO update the JSON string below
json = "{}"
# create an instance of EncyclopediaInfoOk from a JSON string
encyclopedia_info_ok_instance = EncyclopediaInfoOk.from_json(json)
# print the JSON string representation of the object
print(EncyclopediaInfoOk.to_json())

# convert the object into a dict
encyclopedia_info_ok_dict = encyclopedia_info_ok_instance.to_dict()
# create an instance of EncyclopediaInfoOk from a dict
encyclopedia_info_ok_from_dict = EncyclopediaInfoOk.from_dict(encyclopedia_info_ok_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


