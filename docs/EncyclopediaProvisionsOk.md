# EncyclopediaProvisionsOk


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**meta** | [**EncyclopediaProvisionsMeta**](EncyclopediaProvisionsMeta.md) |  | 
**data** | [**Dict[str, EncyclopediaProvisionsDataValue]**](EncyclopediaProvisionsDataValue.md) |  | 

## Example

```python
from wot_api_client.models.encyclopedia_provisions_ok import EncyclopediaProvisionsOk

# TODO update the JSON string below
json = "{}"
# create an instance of EncyclopediaProvisionsOk from a JSON string
encyclopedia_provisions_ok_instance = EncyclopediaProvisionsOk.from_json(json)
# print the JSON string representation of the object
print(EncyclopediaProvisionsOk.to_json())

# convert the object into a dict
encyclopedia_provisions_ok_dict = encyclopedia_provisions_ok_instance.to_dict()
# create an instance of EncyclopediaProvisionsOk from a dict
encyclopedia_provisions_ok_from_dict = EncyclopediaProvisionsOk.from_dict(encyclopedia_provisions_ok_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


