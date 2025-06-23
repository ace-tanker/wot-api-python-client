# AuthLogoutError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**error** | **object** |  | 

## Example

```python
from wot_api_client.models.auth_logout_error import AuthLogoutError

# TODO update the JSON string below
json = "{}"
# create an instance of AuthLogoutError from a JSON string
auth_logout_error_instance = AuthLogoutError.from_json(json)
# print the JSON string representation of the object
print(AuthLogoutError.to_json())

# convert the object into a dict
auth_logout_error_dict = auth_logout_error_instance.to_dict()
# create an instance of AuthLogoutError from a dict
auth_logout_error_from_dict = AuthLogoutError.from_dict(auth_logout_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


