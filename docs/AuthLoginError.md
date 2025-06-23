# AuthLoginError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**error** | [**AuthLoginErrorError**](AuthLoginErrorError.md) |  | 

## Example

```python
from wot_api_client.models.auth_login_error import AuthLoginError

# TODO update the JSON string below
json = "{}"
# create an instance of AuthLoginError from a JSON string
auth_login_error_instance = AuthLoginError.from_json(json)
# print the JSON string representation of the object
print(AuthLoginError.to_json())

# convert the object into a dict
auth_login_error_dict = auth_login_error_instance.to_dict()
# create an instance of AuthLoginError from a dict
auth_login_error_from_dict = AuthLoginError.from_dict(auth_login_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


