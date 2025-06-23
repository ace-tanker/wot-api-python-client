# EncyclopediaVehiclesDataValueCrewInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**member_id** | **str** | Crew member ID | 
**roles** | **Dict[str, str]** | List of crew member roles | 

## Example

```python
from wot_api_client.models.encyclopedia_vehicles_data_value_crew_inner import EncyclopediaVehiclesDataValueCrewInner

# TODO update the JSON string below
json = "{}"
# create an instance of EncyclopediaVehiclesDataValueCrewInner from a JSON string
encyclopedia_vehicles_data_value_crew_inner_instance = EncyclopediaVehiclesDataValueCrewInner.from_json(json)
# print the JSON string representation of the object
print(EncyclopediaVehiclesDataValueCrewInner.to_json())

# convert the object into a dict
encyclopedia_vehicles_data_value_crew_inner_dict = encyclopedia_vehicles_data_value_crew_inner_instance.to_dict()
# create an instance of EncyclopediaVehiclesDataValueCrewInner from a dict
encyclopedia_vehicles_data_value_crew_inner_from_dict = EncyclopediaVehiclesDataValueCrewInner.from_dict(encyclopedia_vehicles_data_value_crew_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


