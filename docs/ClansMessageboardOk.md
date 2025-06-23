# ClansMessageboardOk


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**meta** | [**ClansMessageboardMeta**](ClansMessageboardMeta.md) |  | 
**data** | **Dict[str, Optional[List[ClansMessageboardDataValueInner]]]** |  | 

## Example

```python
from wot_api_client.models.clans_messageboard_ok import ClansMessageboardOk

# TODO update the JSON string below
json = "{}"
# create an instance of ClansMessageboardOk from a JSON string
clans_messageboard_ok_instance = ClansMessageboardOk.from_json(json)
# print the JSON string representation of the object
print(ClansMessageboardOk.to_json())

# convert the object into a dict
clans_messageboard_ok_dict = clans_messageboard_ok_instance.to_dict()
# create an instance of ClansMessageboardOk from a dict
clans_messageboard_ok_from_dict = ClansMessageboardOk.from_dict(clans_messageboard_ok_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


