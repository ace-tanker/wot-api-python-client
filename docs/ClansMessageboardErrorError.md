# ClansMessageboardErrorError

Player is not a clan member

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **float** |  | 
**message** | **str** |  | 
**var_field** | **str** |  | 
**value** | **str** |  | 

## Example

```python
from wot_api_client.models.clans_messageboard_error_error import ClansMessageboardErrorError

# TODO update the JSON string below
json = "{}"
# create an instance of ClansMessageboardErrorError from a JSON string
clans_messageboard_error_error_instance = ClansMessageboardErrorError.from_json(json)
# print the JSON string representation of the object
print(ClansMessageboardErrorError.to_json())

# convert the object into a dict
clans_messageboard_error_error_dict = clans_messageboard_error_error_instance.to_dict()
# create an instance of ClansMessageboardErrorError from a dict
clans_messageboard_error_error_from_dict = ClansMessageboardErrorError.from_dict(clans_messageboard_error_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


