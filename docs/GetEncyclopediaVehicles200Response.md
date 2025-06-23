# GetEncyclopediaVehicles200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**meta** | [**EncyclopediaVehiclesMeta**](EncyclopediaVehiclesMeta.md) |  | 
**data** | [**Dict[str, EncyclopediaVehiclesDataValue]**](EncyclopediaVehiclesDataValue.md) |  | 
**error** | **object** |  | 

## Example

```python
from wot_api_client.models.get_encyclopedia_vehicles200_response import GetEncyclopediaVehicles200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetEncyclopediaVehicles200Response from a JSON string
get_encyclopedia_vehicles200_response_instance = GetEncyclopediaVehicles200Response.from_json(json)
# print the JSON string representation of the object
print(GetEncyclopediaVehicles200Response.to_json())

# convert the object into a dict
get_encyclopedia_vehicles200_response_dict = get_encyclopedia_vehicles200_response_instance.to_dict()
# create an instance of GetEncyclopediaVehicles200Response from a dict
get_encyclopedia_vehicles200_response_from_dict = GetEncyclopediaVehicles200Response.from_dict(get_encyclopedia_vehicles200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


