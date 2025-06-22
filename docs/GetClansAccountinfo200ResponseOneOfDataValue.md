# GetClansAccountinfo200ResponseOneOfDataValue


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **int** | Player account ID | 
**account_name** | **str** | Player name | 
**joined_at** | **int** | Date when player joined clan | 
**role** | **str** | Technical position name | 
**role_i18n** | **str** | Position | 
**clan** | [**GetClansAccountinfo200ResponseOneOfDataValueClan**](GetClansAccountinfo200ResponseOneOfDataValueClan.md) |  | 

## Example

```python
from wot_api_client.models.get_clans_accountinfo200_response_one_of_data_value import GetClansAccountinfo200ResponseOneOfDataValue

# TODO update the JSON string below
json = "{}"
# create an instance of GetClansAccountinfo200ResponseOneOfDataValue from a JSON string
get_clans_accountinfo200_response_one_of_data_value_instance = GetClansAccountinfo200ResponseOneOfDataValue.from_json(json)
# print the JSON string representation of the object
print(GetClansAccountinfo200ResponseOneOfDataValue.to_json())

# convert the object into a dict
get_clans_accountinfo200_response_one_of_data_value_dict = get_clans_accountinfo200_response_one_of_data_value_instance.to_dict()
# create an instance of GetClansAccountinfo200ResponseOneOfDataValue from a dict
get_clans_accountinfo200_response_one_of_data_value_from_dict = GetClansAccountinfo200ResponseOneOfDataValue.from_dict(get_clans_accountinfo200_response_one_of_data_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


