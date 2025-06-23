# ClansAccountinfoDataValue


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **int** | Player account ID | 
**account_name** | **str** | Player name | 
**joined_at** | **int** | Date when player joined clan | 
**role** | **str** | Technical position name | 
**role_i18n** | **str** | Position | 
**clan** | [**ClansAccountinfoDataValueClan**](ClansAccountinfoDataValueClan.md) |  | 

## Example

```python
from wot_api_client.models.clans_accountinfo_data_value import ClansAccountinfoDataValue

# TODO update the JSON string below
json = "{}"
# create an instance of ClansAccountinfoDataValue from a JSON string
clans_accountinfo_data_value_instance = ClansAccountinfoDataValue.from_json(json)
# print the JSON string representation of the object
print(ClansAccountinfoDataValue.to_json())

# convert the object into a dict
clans_accountinfo_data_value_dict = clans_accountinfo_data_value_instance.to_dict()
# create an instance of ClansAccountinfoDataValue from a dict
clans_accountinfo_data_value_from_dict = ClansAccountinfoDataValue.from_dict(clans_accountinfo_data_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


