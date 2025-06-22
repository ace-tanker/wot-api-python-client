# GetClansInfo200ResponseOneOfDataValueMembersOneOfInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **int** | Player account ID | 
**account_name** | **str** | Player name | 
**joined_at** | **int** | Date when player joined clan | 
**role** | **str** | Technical position name | 
**role_i18n** | **str** | Position | 

## Example

```python
from wot_api_client.models.get_clans_info200_response_one_of_data_value_members_one_of_inner import GetClansInfo200ResponseOneOfDataValueMembersOneOfInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetClansInfo200ResponseOneOfDataValueMembersOneOfInner from a JSON string
get_clans_info200_response_one_of_data_value_members_one_of_inner_instance = GetClansInfo200ResponseOneOfDataValueMembersOneOfInner.from_json(json)
# print the JSON string representation of the object
print(GetClansInfo200ResponseOneOfDataValueMembersOneOfInner.to_json())

# convert the object into a dict
get_clans_info200_response_one_of_data_value_members_one_of_inner_dict = get_clans_info200_response_one_of_data_value_members_one_of_inner_instance.to_dict()
# create an instance of GetClansInfo200ResponseOneOfDataValueMembersOneOfInner from a dict
get_clans_info200_response_one_of_data_value_members_one_of_inner_from_dict = GetClansInfo200ResponseOneOfDataValueMembersOneOfInner.from_dict(get_clans_info200_response_one_of_data_value_members_one_of_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


