# GetEncyclopediaBadges200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**meta** | [**EncyclopediaBadgesMeta**](EncyclopediaBadgesMeta.md) |  | 
**data** | [**Dict[str, EncyclopediaBadgesDataValue]**](EncyclopediaBadgesDataValue.md) |  | 
**error** | **object** |  | 

## Example

```python
from wot_api_client.models.get_encyclopedia_badges200_response import GetEncyclopediaBadges200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetEncyclopediaBadges200Response from a JSON string
get_encyclopedia_badges200_response_instance = GetEncyclopediaBadges200Response.from_json(json)
# print the JSON string representation of the object
print(GetEncyclopediaBadges200Response.to_json())

# convert the object into a dict
get_encyclopedia_badges200_response_dict = get_encyclopedia_badges200_response_instance.to_dict()
# create an instance of GetEncyclopediaBadges200Response from a dict
get_encyclopedia_badges200_response_from_dict = GetEncyclopediaBadges200Response.from_dict(get_encyclopedia_badges200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


