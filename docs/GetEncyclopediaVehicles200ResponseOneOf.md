# GetEncyclopediaVehicles200ResponseOneOf


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**meta** | [**GetEncyclopediaVehicles200ResponseOneOfMeta**](GetEncyclopediaVehicles200ResponseOneOfMeta.md) |  | 
**data** | [**Dict[str, GetEncyclopediaVehicles200ResponseOneOfDataValue]**](GetEncyclopediaVehicles200ResponseOneOfDataValue.md) |  | 

## Example

```python
from wot_api_client.models.get_encyclopedia_vehicles200_response_one_of import GetEncyclopediaVehicles200ResponseOneOf

# TODO update the JSON string below
json = "{}"
# create an instance of GetEncyclopediaVehicles200ResponseOneOf from a JSON string
get_encyclopedia_vehicles200_response_one_of_instance = GetEncyclopediaVehicles200ResponseOneOf.from_json(json)
# print the JSON string representation of the object
print(GetEncyclopediaVehicles200ResponseOneOf.to_json())

# convert the object into a dict
get_encyclopedia_vehicles200_response_one_of_dict = get_encyclopedia_vehicles200_response_one_of_instance.to_dict()
# create an instance of GetEncyclopediaVehicles200ResponseOneOf from a dict
get_encyclopedia_vehicles200_response_one_of_from_dict = GetEncyclopediaVehicles200ResponseOneOf.from_dict(get_encyclopedia_vehicles200_response_one_of_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


