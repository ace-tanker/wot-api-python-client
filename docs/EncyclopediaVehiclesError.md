# EncyclopediaVehiclesError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**error** | **object** |  | 

## Example

```python
from wot_api_client.models.encyclopedia_vehicles_error import EncyclopediaVehiclesError

# TODO update the JSON string below
json = "{}"
# create an instance of EncyclopediaVehiclesError from a JSON string
encyclopedia_vehicles_error_instance = EncyclopediaVehiclesError.from_json(json)
# print the JSON string representation of the object
print(EncyclopediaVehiclesError.to_json())

# convert the object into a dict
encyclopedia_vehicles_error_dict = encyclopedia_vehicles_error_instance.to_dict()
# create an instance of EncyclopediaVehiclesError from a dict
encyclopedia_vehicles_error_from_dict = EncyclopediaVehiclesError.from_dict(encyclopedia_vehicles_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


