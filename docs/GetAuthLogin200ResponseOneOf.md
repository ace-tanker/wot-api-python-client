# GetAuthLogin200ResponseOneOf


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**meta** | [**GetAccountList200ResponseOneOfMeta**](GetAccountList200ResponseOneOfMeta.md) |  | 
**data** | [**GetAuthLogin200ResponseOneOfData**](GetAuthLogin200ResponseOneOfData.md) |  | 

## Example

```python
from wot_api_client.models.get_auth_login200_response_one_of import GetAuthLogin200ResponseOneOf

# TODO update the JSON string below
json = "{}"
# create an instance of GetAuthLogin200ResponseOneOf from a JSON string
get_auth_login200_response_one_of_instance = GetAuthLogin200ResponseOneOf.from_json(json)
# print the JSON string representation of the object
print(GetAuthLogin200ResponseOneOf.to_json())

# convert the object into a dict
get_auth_login200_response_one_of_dict = get_auth_login200_response_one_of_instance.to_dict()
# create an instance of GetAuthLogin200ResponseOneOf from a dict
get_auth_login200_response_one_of_from_dict = GetAuthLogin200ResponseOneOf.from_dict(get_auth_login200_response_one_of_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


