# EncyclopediaBadgesError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**error** | **object** |  | 

## Example

```python
from wot_api_client.models.encyclopedia_badges_error import EncyclopediaBadgesError

# TODO update the JSON string below
json = "{}"
# create an instance of EncyclopediaBadgesError from a JSON string
encyclopedia_badges_error_instance = EncyclopediaBadgesError.from_json(json)
# print the JSON string representation of the object
print(EncyclopediaBadgesError.to_json())

# convert the object into a dict
encyclopedia_badges_error_dict = encyclopedia_badges_error_instance.to_dict()
# create an instance of EncyclopediaBadgesError from a dict
encyclopedia_badges_error_from_dict = EncyclopediaBadgesError.from_dict(encyclopedia_badges_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


