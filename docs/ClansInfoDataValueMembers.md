# ClansInfoDataValueMembers

Information on clan members. Field format depends on members_key input parameter.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from wot_api_client.models.clans_info_data_value_members import ClansInfoDataValueMembers

# TODO update the JSON string below
json = "{}"
# create an instance of ClansInfoDataValueMembers from a JSON string
clans_info_data_value_members_instance = ClansInfoDataValueMembers.from_json(json)
# print the JSON string representation of the object
print(ClansInfoDataValueMembers.to_json())

# convert the object into a dict
clans_info_data_value_members_dict = clans_info_data_value_members_instance.to_dict()
# create an instance of ClansInfoDataValueMembers from a dict
clans_info_data_value_members_from_dict = ClansInfoDataValueMembers.from_dict(clans_info_data_value_members_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


