# AuthLoginErrorErrorOneOf

Application authorization cancelled by user

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **float** |  | 
**message** | **str** |  | 
**var_field** | **str** |  | 
**value** | **str** |  | 

## Example

```python
from wot_api_client.models.auth_login_error_error_one_of import AuthLoginErrorErrorOneOf

# TODO update the JSON string below
json = "{}"
# create an instance of AuthLoginErrorErrorOneOf from a JSON string
auth_login_error_error_one_of_instance = AuthLoginErrorErrorOneOf.from_json(json)
# print the JSON string representation of the object
print(AuthLoginErrorErrorOneOf.to_json())

# convert the object into a dict
auth_login_error_error_one_of_dict = auth_login_error_error_one_of_instance.to_dict()
# create an instance of AuthLoginErrorErrorOneOf from a dict
auth_login_error_error_one_of_from_dict = AuthLoginErrorErrorOneOf.from_dict(auth_login_error_error_one_of_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


