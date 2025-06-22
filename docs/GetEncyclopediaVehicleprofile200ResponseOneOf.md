# GetEncyclopediaVehicleprofile200ResponseOneOf


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**meta** | [**GetAccountList200ResponseOneOfMeta**](GetAccountList200ResponseOneOfMeta.md) |  | 
**data** | [**Dict[str, GetEncyclopediaVehicleprofile200ResponseOneOfDataValue]**](GetEncyclopediaVehicleprofile200ResponseOneOfDataValue.md) |  | 

## Example

```python
from wot_api_client.models.get_encyclopedia_vehicleprofile200_response_one_of import GetEncyclopediaVehicleprofile200ResponseOneOf

# TODO update the JSON string below
json = "{}"
# create an instance of GetEncyclopediaVehicleprofile200ResponseOneOf from a JSON string
get_encyclopedia_vehicleprofile200_response_one_of_instance = GetEncyclopediaVehicleprofile200ResponseOneOf.from_json(json)
# print the JSON string representation of the object
print(GetEncyclopediaVehicleprofile200ResponseOneOf.to_json())

# convert the object into a dict
get_encyclopedia_vehicleprofile200_response_one_of_dict = get_encyclopedia_vehicleprofile200_response_one_of_instance.to_dict()
# create an instance of GetEncyclopediaVehicleprofile200ResponseOneOf from a dict
get_encyclopedia_vehicleprofile200_response_one_of_from_dict = GetEncyclopediaVehicleprofile200ResponseOneOf.from_dict(get_encyclopedia_vehicleprofile200_response_one_of_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


