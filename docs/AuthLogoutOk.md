# AuthLogoutOk


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**meta** | **object** |  | 
**data** | **object** |  | 

## Example

```python
from wot_api_client.models.auth_logout_ok import AuthLogoutOk

# TODO update the JSON string below
json = "{}"
# create an instance of AuthLogoutOk from a JSON string
auth_logout_ok_instance = AuthLogoutOk.from_json(json)
# print the JSON string representation of the object
print(AuthLogoutOk.to_json())

# convert the object into a dict
auth_logout_ok_dict = auth_logout_ok_instance.to_dict()
# create an instance of AuthLogoutOk from a dict
auth_logout_ok_from_dict = AuthLogoutOk.from_dict(auth_logout_ok_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


