# GetClansInfo200ResponseOneOfDataValuePrivateClanTreasury

Clan Treasury

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gold** | **int** | Amount of gold in the сlan Treasury | 
**credits** | **int** | Amount of credits in the сlan Treasury | 
**crystal** | **int** | Number of bonds in the сlan Treasury | 

## Example

```python
from wot_api_client.models.get_clans_info200_response_one_of_data_value_private_clan_treasury import GetClansInfo200ResponseOneOfDataValuePrivateClanTreasury

# TODO update the JSON string below
json = "{}"
# create an instance of GetClansInfo200ResponseOneOfDataValuePrivateClanTreasury from a JSON string
get_clans_info200_response_one_of_data_value_private_clan_treasury_instance = GetClansInfo200ResponseOneOfDataValuePrivateClanTreasury.from_json(json)
# print the JSON string representation of the object
print(GetClansInfo200ResponseOneOfDataValuePrivateClanTreasury.to_json())

# convert the object into a dict
get_clans_info200_response_one_of_data_value_private_clan_treasury_dict = get_clans_info200_response_one_of_data_value_private_clan_treasury_instance.to_dict()
# create an instance of GetClansInfo200ResponseOneOfDataValuePrivateClanTreasury from a dict
get_clans_info200_response_one_of_data_value_private_clan_treasury_from_dict = GetClansInfo200ResponseOneOfDataValuePrivateClanTreasury.from_dict(get_clans_info200_response_one_of_data_value_private_clan_treasury_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


