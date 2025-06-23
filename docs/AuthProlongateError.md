# AuthProlongateError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**error** | **object** |  | 

## Example

```python
from wot_api_client.models.auth_prolongate_error import AuthProlongateError

# TODO update the JSON string below
json = "{}"
# create an instance of AuthProlongateError from a JSON string
auth_prolongate_error_instance = AuthProlongateError.from_json(json)
# print the JSON string representation of the object
print(AuthProlongateError.to_json())

# convert the object into a dict
auth_prolongate_error_dict = auth_prolongate_error_instance.to_dict()
# create an instance of AuthProlongateError from a dict
auth_prolongate_error_from_dict = AuthProlongateError.from_dict(auth_prolongate_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


