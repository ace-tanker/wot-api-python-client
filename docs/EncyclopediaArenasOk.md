# EncyclopediaArenasOk


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**meta** | [**EncyclopediaArenasMeta**](EncyclopediaArenasMeta.md) |  | 
**data** | [**Dict[str, EncyclopediaArenasDataValue]**](EncyclopediaArenasDataValue.md) |  | 

## Example

```python
from wot_api_client.models.encyclopedia_arenas_ok import EncyclopediaArenasOk

# TODO update the JSON string below
json = "{}"
# create an instance of EncyclopediaArenasOk from a JSON string
encyclopedia_arenas_ok_instance = EncyclopediaArenasOk.from_json(json)
# print the JSON string representation of the object
print(EncyclopediaArenasOk.to_json())

# convert the object into a dict
encyclopedia_arenas_ok_dict = encyclopedia_arenas_ok_instance.to_dict()
# create an instance of EncyclopediaArenasOk from a dict
encyclopedia_arenas_ok_from_dict = EncyclopediaArenasOk.from_dict(encyclopedia_arenas_ok_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


