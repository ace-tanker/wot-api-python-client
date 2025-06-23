# AccountInfoDataValuePrivateRentedValue


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tank_id** | **int** | Rented vehicle ID | 
**compensation_credits** | **int** | Rental compensation in credits | 
**compensation_gold** | **int** | Rental compensation in gold | 
**expiration_time** | **int** | Vehicle Rental expiration time | 

## Example

```python
from wot_api_client.models.account_info_data_value_private_rented_value import AccountInfoDataValuePrivateRentedValue

# TODO update the JSON string below
json = "{}"
# create an instance of AccountInfoDataValuePrivateRentedValue from a JSON string
account_info_data_value_private_rented_value_instance = AccountInfoDataValuePrivateRentedValue.from_json(json)
# print the JSON string representation of the object
print(AccountInfoDataValuePrivateRentedValue.to_json())

# convert the object into a dict
account_info_data_value_private_rented_value_dict = account_info_data_value_private_rented_value_instance.to_dict()
# create an instance of AccountInfoDataValuePrivateRentedValue from a dict
account_info_data_value_private_rented_value_from_dict = AccountInfoDataValuePrivateRentedValue.from_dict(account_info_data_value_private_rented_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


