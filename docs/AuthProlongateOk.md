# AuthProlongateOk


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**meta** | [**AuthProlongateMeta**](AuthProlongateMeta.md) |  | 
**data** | [**AuthProlongateData**](AuthProlongateData.md) |  | 

## Example

```python
from wot_api_client.models.auth_prolongate_ok import AuthProlongateOk

# TODO update the JSON string below
json = "{}"
# create an instance of AuthProlongateOk from a JSON string
auth_prolongate_ok_instance = AuthProlongateOk.from_json(json)
# print the JSON string representation of the object
print(AuthProlongateOk.to_json())

# convert the object into a dict
auth_prolongate_ok_dict = auth_prolongate_ok_instance.to_dict()
# create an instance of AuthProlongateOk from a dict
auth_prolongate_ok_from_dict = AuthProlongateOk.from_dict(auth_prolongate_ok_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


