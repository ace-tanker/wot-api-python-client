# EncyclopediaVehiclesOk


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**meta** | [**EncyclopediaVehiclesMeta**](EncyclopediaVehiclesMeta.md) |  | 
**data** | [**Dict[str, EncyclopediaVehiclesDataValue]**](EncyclopediaVehiclesDataValue.md) |  | 

## Example

```python
from wot_api_client.models.encyclopedia_vehicles_ok import EncyclopediaVehiclesOk

# TODO update the JSON string below
json = "{}"
# create an instance of EncyclopediaVehiclesOk from a JSON string
encyclopedia_vehicles_ok_instance = EncyclopediaVehiclesOk.from_json(json)
# print the JSON string representation of the object
print(EncyclopediaVehiclesOk.to_json())

# convert the object into a dict
encyclopedia_vehicles_ok_dict = encyclopedia_vehicles_ok_instance.to_dict()
# create an instance of EncyclopediaVehiclesOk from a dict
encyclopedia_vehicles_ok_from_dict = EncyclopediaVehiclesOk.from_dict(encyclopedia_vehicles_ok_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


