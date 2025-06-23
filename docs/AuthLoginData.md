# AuthLoginData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**location** | **str** | URL where user is redirected for authentication. This URL is returned only if parameter **nofollow&#x3D;1** is passed in. | 

## Example

```python
from wot_api_client.models.auth_login_data import AuthLoginData

# TODO update the JSON string below
json = "{}"
# create an instance of AuthLoginData from a JSON string
auth_login_data_instance = AuthLoginData.from_json(json)
# print the JSON string representation of the object
print(AuthLoginData.to_json())

# convert the object into a dict
auth_login_data_dict = auth_login_data_instance.to_dict()
# create an instance of AuthLoginData from a dict
auth_login_data_from_dict = AuthLoginData.from_dict(auth_login_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


