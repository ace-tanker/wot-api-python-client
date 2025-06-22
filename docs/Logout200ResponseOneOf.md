# Logout200ResponseOneOf


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**meta** | **object** |  | 
**data** | **object** |  | 

## Example

```python
from wot_api_client.models.logout200_response_one_of import Logout200ResponseOneOf

# TODO update the JSON string below
json = "{}"
# create an instance of Logout200ResponseOneOf from a JSON string
logout200_response_one_of_instance = Logout200ResponseOneOf.from_json(json)
# print the JSON string representation of the object
print(Logout200ResponseOneOf.to_json())

# convert the object into a dict
logout200_response_one_of_dict = logout200_response_one_of_instance.to_dict()
# create an instance of Logout200ResponseOneOf from a dict
logout200_response_one_of_from_dict = Logout200ResponseOneOf.from_dict(logout200_response_one_of_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


