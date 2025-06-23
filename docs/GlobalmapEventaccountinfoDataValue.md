# GlobalmapEventaccountinfoDataValue


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**events** | **Dict[str, Optional[List[GlobalmapEventaccountinfoDataValueEventsValueInner]]]** | Account information by events and Fronts | 

## Example

```python
from wot_api_client.models.globalmap_eventaccountinfo_data_value import GlobalmapEventaccountinfoDataValue

# TODO update the JSON string below
json = "{}"
# create an instance of GlobalmapEventaccountinfoDataValue from a JSON string
globalmap_eventaccountinfo_data_value_instance = GlobalmapEventaccountinfoDataValue.from_json(json)
# print the JSON string representation of the object
print(GlobalmapEventaccountinfoDataValue.to_json())

# convert the object into a dict
globalmap_eventaccountinfo_data_value_dict = globalmap_eventaccountinfo_data_value_instance.to_dict()
# create an instance of GlobalmapEventaccountinfoDataValue from a dict
globalmap_eventaccountinfo_data_value_from_dict = GlobalmapEventaccountinfoDataValue.from_dict(globalmap_eventaccountinfo_data_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


