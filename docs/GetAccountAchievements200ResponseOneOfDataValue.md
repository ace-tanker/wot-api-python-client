# GetAccountAchievements200ResponseOneOfDataValue


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**achievements** | **Dict[str, int]** | Achievements earned | 
**max_series** | **Dict[str, int]** | Maximum values of achievement series | 
**frags** | **Dict[str, int]** | Achievement progress | 

## Example

```python
from wot_api_client.models.get_account_achievements200_response_one_of_data_value import GetAccountAchievements200ResponseOneOfDataValue

# TODO update the JSON string below
json = "{}"
# create an instance of GetAccountAchievements200ResponseOneOfDataValue from a JSON string
get_account_achievements200_response_one_of_data_value_instance = GetAccountAchievements200ResponseOneOfDataValue.from_json(json)
# print the JSON string representation of the object
print(GetAccountAchievements200ResponseOneOfDataValue.to_json())

# convert the object into a dict
get_account_achievements200_response_one_of_data_value_dict = get_account_achievements200_response_one_of_data_value_instance.to_dict()
# create an instance of GetAccountAchievements200ResponseOneOfDataValue from a dict
get_account_achievements200_response_one_of_data_value_from_dict = GetAccountAchievements200ResponseOneOfDataValue.from_dict(get_account_achievements200_response_one_of_data_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


