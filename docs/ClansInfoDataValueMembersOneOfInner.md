# ClansInfoDataValueMembersOneOfInner


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
from wot_api_client.models.clans_info_data_value_members_one_of_inner import ClansInfoDataValueMembersOneOfInner

# TODO update the JSON string below
json = "{}"
# create an instance of ClansInfoDataValueMembersOneOfInner from a JSON string
clans_info_data_value_members_one_of_inner_instance = ClansInfoDataValueMembersOneOfInner.from_json(json)
# print the JSON string representation of the object
print(ClansInfoDataValueMembersOneOfInner.to_json())

# convert the object into a dict
clans_info_data_value_members_one_of_inner_dict = clans_info_data_value_members_one_of_inner_instance.to_dict()
# create an instance of ClansInfoDataValueMembersOneOfInner from a dict
clans_info_data_value_members_one_of_inner_from_dict = ClansInfoDataValueMembersOneOfInner.from_dict(clans_info_data_value_members_one_of_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


