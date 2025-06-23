# GetEncyclopediaPersonalmissions200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**meta** | [**EncyclopediaPersonalmissionsMeta**](EncyclopediaPersonalmissionsMeta.md) |  | 
**data** | [**Dict[str, EncyclopediaPersonalmissionsDataValue]**](EncyclopediaPersonalmissionsDataValue.md) |  | 
**error** | **object** |  | 

## Example

```python
from wot_api_client.models.get_encyclopedia_personalmissions200_response import GetEncyclopediaPersonalmissions200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetEncyclopediaPersonalmissions200Response from a JSON string
get_encyclopedia_personalmissions200_response_instance = GetEncyclopediaPersonalmissions200Response.from_json(json)
# print the JSON string representation of the object
print(GetEncyclopediaPersonalmissions200Response.to_json())

# convert the object into a dict
get_encyclopedia_personalmissions200_response_dict = get_encyclopedia_personalmissions200_response_instance.to_dict()
# create an instance of GetEncyclopediaPersonalmissions200Response from a dict
get_encyclopedia_personalmissions200_response_from_dict = GetEncyclopediaPersonalmissions200Response.from_dict(get_encyclopedia_personalmissions200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


