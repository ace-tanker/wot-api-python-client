# GetAccountAchievements200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**meta** | [**GetAccountList200ResponseOneOfMeta**](GetAccountList200ResponseOneOfMeta.md) |  | 
**data** | [**Dict[str, GetAccountAchievements200ResponseOneOfDataValue]**](GetAccountAchievements200ResponseOneOfDataValue.md) |  | 
**error** | [**GetAccountList200ResponseOneOf1Error**](GetAccountList200ResponseOneOf1Error.md) |  | 

## Example

```python
from wot_api_client.models.get_account_achievements200_response import GetAccountAchievements200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetAccountAchievements200Response from a JSON string
get_account_achievements200_response_instance = GetAccountAchievements200Response.from_json(json)
# print the JSON string representation of the object
print(GetAccountAchievements200Response.to_json())

# convert the object into a dict
get_account_achievements200_response_dict = get_account_achievements200_response_instance.to_dict()
# create an instance of GetAccountAchievements200Response from a dict
get_account_achievements200_response_from_dict = GetAccountAchievements200Response.from_dict(get_account_achievements200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


