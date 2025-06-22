# Logout200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**meta** | **object** |  | 
**data** | **object** |  | 
**error** | [**GetAccountList200ResponseOneOf1Error**](GetAccountList200ResponseOneOf1Error.md) |  | 

## Example

```python
from wot_api_client.models.logout200_response import Logout200Response

# TODO update the JSON string below
json = "{}"
# create an instance of Logout200Response from a JSON string
logout200_response_instance = Logout200Response.from_json(json)
# print the JSON string representation of the object
print(Logout200Response.to_json())

# convert the object into a dict
logout200_response_dict = logout200_response_instance.to_dict()
# create an instance of Logout200Response from a dict
logout200_response_from_dict = Logout200Response.from_dict(logout200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


