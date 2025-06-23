# AuthProlongateData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_token** | **str** | Access token is passed to all methods requiring authorization. | 
**expires_at** | **int** | **Access_token** expiration time | 
**account_id** | **int** | Player account ID | 

## Example

```python
from wot_api_client.models.auth_prolongate_data import AuthProlongateData

# TODO update the JSON string below
json = "{}"
# create an instance of AuthProlongateData from a JSON string
auth_prolongate_data_instance = AuthProlongateData.from_json(json)
# print the JSON string representation of the object
print(AuthProlongateData.to_json())

# convert the object into a dict
auth_prolongate_data_dict = auth_prolongate_data_instance.to_dict()
# create an instance of AuthProlongateData from a dict
auth_prolongate_data_from_dict = AuthProlongateData.from_dict(auth_prolongate_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


