# GetClansList200ResponseOneOf


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**meta** | [**GetClansList200ResponseOneOfMeta**](GetClansList200ResponseOneOfMeta.md) |  | 
**data** | [**List[GetClansList200ResponseOneOfDataInner]**](GetClansList200ResponseOneOfDataInner.md) |  | 

## Example

```python
from wot_api_client.models.get_clans_list200_response_one_of import GetClansList200ResponseOneOf

# TODO update the JSON string below
json = "{}"
# create an instance of GetClansList200ResponseOneOf from a JSON string
get_clans_list200_response_one_of_instance = GetClansList200ResponseOneOf.from_json(json)
# print the JSON string representation of the object
print(GetClansList200ResponseOneOf.to_json())

# convert the object into a dict
get_clans_list200_response_one_of_dict = get_clans_list200_response_one_of_instance.to_dict()
# create an instance of GetClansList200ResponseOneOf from a dict
get_clans_list200_response_one_of_from_dict = GetClansList200ResponseOneOf.from_dict(get_clans_list200_response_one_of_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


