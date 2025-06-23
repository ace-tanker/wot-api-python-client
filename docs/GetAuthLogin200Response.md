# GetAuthLogin200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**meta** | [**AuthLoginMeta**](AuthLoginMeta.md) |  | 
**data** | [**AuthLoginData**](AuthLoginData.md) |  | 
**error** | [**AuthLoginErrorError**](AuthLoginErrorError.md) |  | 

## Example

```python
from wot_api_client.models.get_auth_login200_response import GetAuthLogin200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetAuthLogin200Response from a JSON string
get_auth_login200_response_instance = GetAuthLogin200Response.from_json(json)
# print the JSON string representation of the object
print(GetAuthLogin200Response.to_json())

# convert the object into a dict
get_auth_login200_response_dict = get_auth_login200_response_instance.to_dict()
# create an instance of GetAuthLogin200Response from a dict
get_auth_login200_response_from_dict = GetAuthLogin200Response.from_dict(get_auth_login200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


