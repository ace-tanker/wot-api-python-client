# AccountInfoDataValuePrivateBoostersValue


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**state** | **str** | Status of Personal Reserves. Valid values:   * ACTIVE - Active  * INACTIVE - Inactive  * USED - Used | 
**count** | **int** | Amount of Personal Reserves | 
**expiration_time** | **int** | Expiration time | 

## Example

```python
from wot_api_client.models.account_info_data_value_private_boosters_value import AccountInfoDataValuePrivateBoostersValue

# TODO update the JSON string below
json = "{}"
# create an instance of AccountInfoDataValuePrivateBoostersValue from a JSON string
account_info_data_value_private_boosters_value_instance = AccountInfoDataValuePrivateBoostersValue.from_json(json)
# print the JSON string representation of the object
print(AccountInfoDataValuePrivateBoostersValue.to_json())

# convert the object into a dict
account_info_data_value_private_boosters_value_dict = account_info_data_value_private_boosters_value_instance.to_dict()
# create an instance of AccountInfoDataValuePrivateBoostersValue from a dict
account_info_data_value_private_boosters_value_from_dict = AccountInfoDataValuePrivateBoostersValue.from_dict(account_info_data_value_private_boosters_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


