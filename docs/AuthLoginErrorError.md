# AuthLoginErrorError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **float** |  | 
**message** | **str** |  | 
**var_field** | **str** |  | 
**value** | **str** |  | 

## Example

```python
from wot_api_client.models.auth_login_error_error import AuthLoginErrorError

# TODO update the JSON string below
json = "{}"
# create an instance of AuthLoginErrorError from a JSON string
auth_login_error_error_instance = AuthLoginErrorError.from_json(json)
# print the JSON string representation of the object
print(AuthLoginErrorError.to_json())

# convert the object into a dict
auth_login_error_error_dict = auth_login_error_error_instance.to_dict()
# create an instance of AuthLoginErrorError from a dict
auth_login_error_error_from_dict = AuthLoginErrorError.from_dict(auth_login_error_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


