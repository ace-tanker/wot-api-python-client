# GetAuthLogin200ResponseOneOfData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**location** | **str** | URL where user is redirected for authentication. This URL is returned only if parameter **nofollow&#x3D;1** is passed in. | 

## Example

```python
from wot_api_client.models.get_auth_login200_response_one_of_data import GetAuthLogin200ResponseOneOfData

# TODO update the JSON string below
json = "{}"
# create an instance of GetAuthLogin200ResponseOneOfData from a JSON string
get_auth_login200_response_one_of_data_instance = GetAuthLogin200ResponseOneOfData.from_json(json)
# print the JSON string representation of the object
print(GetAuthLogin200ResponseOneOfData.to_json())

# convert the object into a dict
get_auth_login200_response_one_of_data_dict = get_auth_login200_response_one_of_data_instance.to_dict()
# create an instance of GetAuthLogin200ResponseOneOfData from a dict
get_auth_login200_response_one_of_data_from_dict = GetAuthLogin200ResponseOneOfData.from_dict(get_auth_login200_response_one_of_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


