# ClansMessageboardDataValueInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | Message text | 
**created_at** | **int** | Message creation date | 
**updated_at** | **int** | Date when message was updated | 
**author_id** | **int** | Message author ID | 
**editor_id** | **int** | ID of a player who has changed the message | 
**is_read** | **bool** | Indicates if the message has been read | 

## Example

```python
from wot_api_client.models.clans_messageboard_data_value_inner import ClansMessageboardDataValueInner

# TODO update the JSON string below
json = "{}"
# create an instance of ClansMessageboardDataValueInner from a JSON string
clans_messageboard_data_value_inner_instance = ClansMessageboardDataValueInner.from_json(json)
# print the JSON string representation of the object
print(ClansMessageboardDataValueInner.to_json())

# convert the object into a dict
clans_messageboard_data_value_inner_dict = clans_messageboard_data_value_inner_instance.to_dict()
# create an instance of ClansMessageboardDataValueInner from a dict
clans_messageboard_data_value_inner_from_dict = ClansMessageboardDataValueInner.from_dict(clans_messageboard_data_value_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


