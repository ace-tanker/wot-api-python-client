# GetAccountInfo200ResponseOneOfDataValuePrivateRentedValue


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tank_id** | **int** | Rented vehicle ID | 
**compensation_credits** | **int** | Rental compensation in credits | 
**compensation_gold** | **int** | Rental compensation in gold | 
**expiration_time** | **int** | Vehicle Rental expiration time | 

## Example

```python
from wot_api_client.models.get_account_info200_response_one_of_data_value_private_rented_value import GetAccountInfo200ResponseOneOfDataValuePrivateRentedValue

# TODO update the JSON string below
json = "{}"
# create an instance of GetAccountInfo200ResponseOneOfDataValuePrivateRentedValue from a JSON string
get_account_info200_response_one_of_data_value_private_rented_value_instance = GetAccountInfo200ResponseOneOfDataValuePrivateRentedValue.from_json(json)
# print the JSON string representation of the object
print(GetAccountInfo200ResponseOneOfDataValuePrivateRentedValue.to_json())

# convert the object into a dict
get_account_info200_response_one_of_data_value_private_rented_value_dict = get_account_info200_response_one_of_data_value_private_rented_value_instance.to_dict()
# create an instance of GetAccountInfo200ResponseOneOfDataValuePrivateRentedValue from a dict
get_account_info200_response_one_of_data_value_private_rented_value_from_dict = GetAccountInfo200ResponseOneOfDataValuePrivateRentedValue.from_dict(get_account_info200_response_one_of_data_value_private_rented_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


