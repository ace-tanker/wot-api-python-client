# EncyclopediaBoostersOk


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**meta** | [**EncyclopediaBoostersMeta**](EncyclopediaBoostersMeta.md) |  | 
**data** | [**Dict[str, EncyclopediaBoostersDataValue]**](EncyclopediaBoostersDataValue.md) |  | 

## Example

```python
from wot_api_client.models.encyclopedia_boosters_ok import EncyclopediaBoostersOk

# TODO update the JSON string below
json = "{}"
# create an instance of EncyclopediaBoostersOk from a JSON string
encyclopedia_boosters_ok_instance = EncyclopediaBoostersOk.from_json(json)
# print the JSON string representation of the object
print(EncyclopediaBoostersOk.to_json())

# convert the object into a dict
encyclopedia_boosters_ok_dict = encyclopedia_boosters_ok_instance.to_dict()
# create an instance of EncyclopediaBoostersOk from a dict
encyclopedia_boosters_ok_from_dict = EncyclopediaBoostersOk.from_dict(encyclopedia_boosters_ok_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


