# GetEncyclopediaProvisions200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**meta** | [**EncyclopediaProvisionsMeta**](EncyclopediaProvisionsMeta.md) |  | 
**data** | [**Dict[str, EncyclopediaProvisionsDataValue]**](EncyclopediaProvisionsDataValue.md) |  | 
**error** | **object** |  | 

## Example

```python
from wot_api_client.models.get_encyclopedia_provisions200_response import GetEncyclopediaProvisions200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetEncyclopediaProvisions200Response from a JSON string
get_encyclopedia_provisions200_response_instance = GetEncyclopediaProvisions200Response.from_json(json)
# print the JSON string representation of the object
print(GetEncyclopediaProvisions200Response.to_json())

# convert the object into a dict
get_encyclopedia_provisions200_response_dict = get_encyclopedia_provisions200_response_instance.to_dict()
# create an instance of GetEncyclopediaProvisions200Response from a dict
get_encyclopedia_provisions200_response_from_dict = GetEncyclopediaProvisions200Response.from_dict(get_encyclopedia_provisions200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


