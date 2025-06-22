# GetAccountInfo200ResponseOneOfDataValuePrivateBoostersValue


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**state** | **str** | Status of Personal Reserves. Valid values:   * ACTIVE - Active  * INACTIVE - Inactive  * USED - Used | 
**count** | **int** | Amount of Personal Reserves | 
**expiration_time** | **int** | Expiration time | 

## Example

```python
from wot_api_client.models.get_account_info200_response_one_of_data_value_private_boosters_value import GetAccountInfo200ResponseOneOfDataValuePrivateBoostersValue

# TODO update the JSON string below
json = "{}"
# create an instance of GetAccountInfo200ResponseOneOfDataValuePrivateBoostersValue from a JSON string
get_account_info200_response_one_of_data_value_private_boosters_value_instance = GetAccountInfo200ResponseOneOfDataValuePrivateBoostersValue.from_json(json)
# print the JSON string representation of the object
print(GetAccountInfo200ResponseOneOfDataValuePrivateBoostersValue.to_json())

# convert the object into a dict
get_account_info200_response_one_of_data_value_private_boosters_value_dict = get_account_info200_response_one_of_data_value_private_boosters_value_instance.to_dict()
# create an instance of GetAccountInfo200ResponseOneOfDataValuePrivateBoostersValue from a dict
get_account_info200_response_one_of_data_value_private_boosters_value_from_dict = GetAccountInfo200ResponseOneOfDataValuePrivateBoostersValue.from_dict(get_account_info200_response_one_of_data_value_private_boosters_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


