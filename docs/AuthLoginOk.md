# AuthLoginOk


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**meta** | [**AuthLoginMeta**](AuthLoginMeta.md) |  | 
**data** | [**AuthLoginData**](AuthLoginData.md) |  | 

## Example

```python
from wot_api_client.models.auth_login_ok import AuthLoginOk

# TODO update the JSON string below
json = "{}"
# create an instance of AuthLoginOk from a JSON string
auth_login_ok_instance = AuthLoginOk.from_json(json)
# print the JSON string representation of the object
print(AuthLoginOk.to_json())

# convert the object into a dict
auth_login_ok_dict = auth_login_ok_instance.to_dict()
# create an instance of AuthLoginOk from a dict
auth_login_ok_from_dict = AuthLoginOk.from_dict(auth_login_ok_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


