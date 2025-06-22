# GetClanratingsClans200ResponseOneOf


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**meta** | [**GetAccountList200ResponseOneOfMeta**](GetAccountList200ResponseOneOfMeta.md) |  | 
**data** | [**Dict[str, GetClanratingsClans200ResponseOneOfDataValue]**](GetClanratingsClans200ResponseOneOfDataValue.md) |  | 

## Example

```python
from wot_api_client.models.get_clanratings_clans200_response_one_of import GetClanratingsClans200ResponseOneOf

# TODO update the JSON string below
json = "{}"
# create an instance of GetClanratingsClans200ResponseOneOf from a JSON string
get_clanratings_clans200_response_one_of_instance = GetClanratingsClans200ResponseOneOf.from_json(json)
# print the JSON string representation of the object
print(GetClanratingsClans200ResponseOneOf.to_json())

# convert the object into a dict
get_clanratings_clans200_response_one_of_dict = get_clanratings_clans200_response_one_of_instance.to_dict()
# create an instance of GetClanratingsClans200ResponseOneOf from a dict
get_clanratings_clans200_response_one_of_from_dict = GetClanratingsClans200ResponseOneOf.from_dict(get_clanratings_clans200_response_one_of_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


