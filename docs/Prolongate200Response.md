# Prolongate200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**meta** | [**AuthProlongateMeta**](AuthProlongateMeta.md) |  | 
**data** | [**AuthProlongateData**](AuthProlongateData.md) |  | 
**error** | **object** |  | 

## Example

```python
from wot_api_client.models.prolongate200_response import Prolongate200Response

# TODO update the JSON string below
json = "{}"
# create an instance of Prolongate200Response from a JSON string
prolongate200_response_instance = Prolongate200Response.from_json(json)
# print the JSON string representation of the object
print(Prolongate200Response.to_json())

# convert the object into a dict
prolongate200_response_dict = prolongate200_response_instance.to_dict()
# create an instance of Prolongate200Response from a dict
prolongate200_response_from_dict = Prolongate200Response.from_dict(prolongate200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


