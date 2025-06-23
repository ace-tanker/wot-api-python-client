# EncyclopediaBadgesOk


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**meta** | [**EncyclopediaBadgesMeta**](EncyclopediaBadgesMeta.md) |  | 
**data** | [**Dict[str, EncyclopediaBadgesDataValue]**](EncyclopediaBadgesDataValue.md) |  | 

## Example

```python
from wot_api_client.models.encyclopedia_badges_ok import EncyclopediaBadgesOk

# TODO update the JSON string below
json = "{}"
# create an instance of EncyclopediaBadgesOk from a JSON string
encyclopedia_badges_ok_instance = EncyclopediaBadgesOk.from_json(json)
# print the JSON string representation of the object
print(EncyclopediaBadgesOk.to_json())

# convert the object into a dict
encyclopedia_badges_ok_dict = encyclopedia_badges_ok_instance.to_dict()
# create an instance of EncyclopediaBadgesOk from a dict
encyclopedia_badges_ok_from_dict = EncyclopediaBadgesOk.from_dict(encyclopedia_badges_ok_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


