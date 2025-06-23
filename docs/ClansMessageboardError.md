# ClansMessageboardError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**error** | [**ClansMessageboardErrorError**](ClansMessageboardErrorError.md) |  | 

## Example

```python
from wot_api_client.models.clans_messageboard_error import ClansMessageboardError

# TODO update the JSON string below
json = "{}"
# create an instance of ClansMessageboardError from a JSON string
clans_messageboard_error_instance = ClansMessageboardError.from_json(json)
# print the JSON string representation of the object
print(ClansMessageboardError.to_json())

# convert the object into a dict
clans_messageboard_error_dict = clans_messageboard_error_instance.to_dict()
# create an instance of ClansMessageboardError from a dict
clans_messageboard_error_from_dict = ClansMessageboardError.from_dict(clans_messageboard_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


