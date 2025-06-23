# StrongholdClaninfoDataValueBuildingSlotsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**position** | **str** | Position of the construction site | 
**direction** | **str** | Bridgehead&#39;s name | 
**arena_id** | **str** | Map ID associated with the current construction site | 
**building_title** | **str** | Name of the structure located on the current construction site | 
**building_level** | **int** | Level of the structure located on the current construction site | 
**reserve_title** | **str** | Name of the Reserve earned in the structure located on the current construction site | 

## Example

```python
from wot_api_client.models.stronghold_claninfo_data_value_building_slots_inner import StrongholdClaninfoDataValueBuildingSlotsInner

# TODO update the JSON string below
json = "{}"
# create an instance of StrongholdClaninfoDataValueBuildingSlotsInner from a JSON string
stronghold_claninfo_data_value_building_slots_inner_instance = StrongholdClaninfoDataValueBuildingSlotsInner.from_json(json)
# print the JSON string representation of the object
print(StrongholdClaninfoDataValueBuildingSlotsInner.to_json())

# convert the object into a dict
stronghold_claninfo_data_value_building_slots_inner_dict = stronghold_claninfo_data_value_building_slots_inner_instance.to_dict()
# create an instance of StrongholdClaninfoDataValueBuildingSlotsInner from a dict
stronghold_claninfo_data_value_building_slots_inner_from_dict = StrongholdClaninfoDataValueBuildingSlotsInner.from_dict(stronghold_claninfo_data_value_building_slots_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


