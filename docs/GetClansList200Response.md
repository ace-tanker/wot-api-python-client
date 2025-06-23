# GetClansList200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**meta** | [**ClansListMeta**](ClansListMeta.md) |  | 
**data** | [**List[ClansListDataInner]**](ClansListDataInner.md) |  | 
**error** | **object** |  | 

## Example

```python
from wot_api_client.models.get_clans_list200_response import GetClansList200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetClansList200Response from a JSON string
get_clans_list200_response_instance = GetClansList200Response.from_json(json)
# print the JSON string representation of the object
print(GetClansList200Response.to_json())

# convert the object into a dict
get_clans_list200_response_dict = get_clans_list200_response_instance.to_dict()
# create an instance of GetClansList200Response from a dict
get_clans_list200_response_from_dict = GetClansList200Response.from_dict(get_clans_list200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


