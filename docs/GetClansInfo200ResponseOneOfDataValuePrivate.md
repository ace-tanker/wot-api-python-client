# GetClansInfo200ResponseOneOfDataValuePrivate

Restricted clan information

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**treasury** | **int** | Amount of gold in the сlan Treasury | 
**clan_treasury** | [**GetClansInfo200ResponseOneOfDataValuePrivateClanTreasury**](GetClansInfo200ResponseOneOfDataValuePrivateClanTreasury.md) |  | 
**online_members** | **List[int]** | List of clan members with an active game session in World of Tanks. | [optional] 

## Example

```python
from wot_api_client.models.get_clans_info200_response_one_of_data_value_private import GetClansInfo200ResponseOneOfDataValuePrivate

# TODO update the JSON string below
json = "{}"
# create an instance of GetClansInfo200ResponseOneOfDataValuePrivate from a JSON string
get_clans_info200_response_one_of_data_value_private_instance = GetClansInfo200ResponseOneOfDataValuePrivate.from_json(json)
# print the JSON string representation of the object
print(GetClansInfo200ResponseOneOfDataValuePrivate.to_json())

# convert the object into a dict
get_clans_info200_response_one_of_data_value_private_dict = get_clans_info200_response_one_of_data_value_private_instance.to_dict()
# create an instance of GetClansInfo200ResponseOneOfDataValuePrivate from a dict
get_clans_info200_response_one_of_data_value_private_from_dict = GetClansInfo200ResponseOneOfDataValuePrivate.from_dict(get_clans_info200_response_one_of_data_value_private_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


