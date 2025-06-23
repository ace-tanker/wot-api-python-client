# EncyclopediaPersonalmissionsOk


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**meta** | [**EncyclopediaPersonalmissionsMeta**](EncyclopediaPersonalmissionsMeta.md) |  | 
**data** | [**Dict[str, EncyclopediaPersonalmissionsDataValue]**](EncyclopediaPersonalmissionsDataValue.md) |  | 

## Example

```python
from wot_api_client.models.encyclopedia_personalmissions_ok import EncyclopediaPersonalmissionsOk

# TODO update the JSON string below
json = "{}"
# create an instance of EncyclopediaPersonalmissionsOk from a JSON string
encyclopedia_personalmissions_ok_instance = EncyclopediaPersonalmissionsOk.from_json(json)
# print the JSON string representation of the object
print(EncyclopediaPersonalmissionsOk.to_json())

# convert the object into a dict
encyclopedia_personalmissions_ok_dict = encyclopedia_personalmissions_ok_instance.to_dict()
# create an instance of EncyclopediaPersonalmissionsOk from a dict
encyclopedia_personalmissions_ok_from_dict = EncyclopediaPersonalmissionsOk.from_dict(encyclopedia_personalmissions_ok_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


