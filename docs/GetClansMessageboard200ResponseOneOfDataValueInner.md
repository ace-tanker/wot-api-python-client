# GetClansMessageboard200ResponseOneOfDataValueInner


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
from wot_api_client.models.get_clans_messageboard200_response_one_of_data_value_inner import GetClansMessageboard200ResponseOneOfDataValueInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetClansMessageboard200ResponseOneOfDataValueInner from a JSON string
get_clans_messageboard200_response_one_of_data_value_inner_instance = GetClansMessageboard200ResponseOneOfDataValueInner.from_json(json)
# print the JSON string representation of the object
print(GetClansMessageboard200ResponseOneOfDataValueInner.to_json())

# convert the object into a dict
get_clans_messageboard200_response_one_of_data_value_inner_dict = get_clans_messageboard200_response_one_of_data_value_inner_instance.to_dict()
# create an instance of GetClansMessageboard200ResponseOneOfDataValueInner from a dict
get_clans_messageboard200_response_one_of_data_value_inner_from_dict = GetClansMessageboard200ResponseOneOfDataValueInner.from_dict(get_clans_messageboard200_response_one_of_data_value_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


