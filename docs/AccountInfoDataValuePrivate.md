# AccountInfoDataValuePrivate

Player's private data

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**personal_missions** | **Dict[str, str]** | Personal Missions Progress. The key is a task id, the value is a status.  Possible statuses:   * NONE - a mission is unavailable  * UNLOCKED - a mission is available  * NEED_GET_MAIN_REWARD - the main reward has not been received  * MAIN_REWARD_GOTTEN - the main reward has been received  * NEED_GET_ADD_REWARD - additional reward has not been received  * NEED_GET_ALL_REWARDS - no rewards have been received  * ALL_REWARDS_GOTTEN - all rewards have been received . | [optional] 
**gold** | **int** | Gold | 
**battle_life_time** | **int** | Overall battle life time in seconds | 
**free_xp** | **int** | Free Experience | 
**credits** | **int** | Credits | 
**premium_expires_at** | **int** | Premium Account expiration time | 
**is_premium** | **bool** | Indicates if the account is Premium Account | 
**rented** | [**Dict[str, AccountInfoDataValuePrivateRentedValue]**](AccountInfoDataValuePrivateRentedValue.md) | Vehicle Rental. | [optional] 
**grouped_contacts** | [**AccountInfoDataValuePrivateGroupedContacts**](AccountInfoDataValuePrivateGroupedContacts.md) |  | [optional] 
**restrictions** | [**AccountInfoDataValuePrivateRestrictions**](AccountInfoDataValuePrivateRestrictions.md) |  | 
**is_bound_to_phone** | **bool** | Indicates if mobile phone number was added to the account | 
**boosters** | [**Dict[str, AccountInfoDataValuePrivateBoostersValue]**](AccountInfoDataValuePrivateBoostersValue.md) | Personal Reserves. | [optional] 
**garage** | **List[int]** | Vehicles in the Garage. | [optional] 
**ban_info** | **str** | Account ban details | 
**ban_time** | **int** | End time of account ban | 
**bonds** | **int** | Bonds | 

## Example

```python
from wot_api_client.models.account_info_data_value_private import AccountInfoDataValuePrivate

# TODO update the JSON string below
json = "{}"
# create an instance of AccountInfoDataValuePrivate from a JSON string
account_info_data_value_private_instance = AccountInfoDataValuePrivate.from_json(json)
# print the JSON string representation of the object
print(AccountInfoDataValuePrivate.to_json())

# convert the object into a dict
account_info_data_value_private_dict = account_info_data_value_private_instance.to_dict()
# create an instance of AccountInfoDataValuePrivate from a dict
account_info_data_value_private_from_dict = AccountInfoDataValuePrivate.from_dict(account_info_data_value_private_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


