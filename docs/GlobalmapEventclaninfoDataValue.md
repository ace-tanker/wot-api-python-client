# GlobalmapEventclaninfoDataValue


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**events** | **Dict[str, Optional[List[GlobalmapEventclaninfoDataValueEventsValueInner]]]** | Clan info by events and Fronts | 

## Example

```python
from wot_api_client.models.globalmap_eventclaninfo_data_value import GlobalmapEventclaninfoDataValue

# TODO update the JSON string below
json = "{}"
# create an instance of GlobalmapEventclaninfoDataValue from a JSON string
globalmap_eventclaninfo_data_value_instance = GlobalmapEventclaninfoDataValue.from_json(json)
# print the JSON string representation of the object
print(GlobalmapEventclaninfoDataValue.to_json())

# convert the object into a dict
globalmap_eventclaninfo_data_value_dict = globalmap_eventclaninfo_data_value_instance.to_dict()
# create an instance of GlobalmapEventclaninfoDataValue from a dict
globalmap_eventclaninfo_data_value_from_dict = GlobalmapEventclaninfoDataValue.from_dict(globalmap_eventclaninfo_data_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


