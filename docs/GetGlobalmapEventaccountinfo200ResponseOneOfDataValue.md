# GetGlobalmapEventaccountinfo200ResponseOneOfDataValue


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**events** | **Dict[str, Optional[List[GetGlobalmapEventaccountinfo200ResponseOneOfDataValueEventsValueInner]]]** | Account information by events and Fronts | 

## Example

```python
from wot_api_client.models.get_globalmap_eventaccountinfo200_response_one_of_data_value import GetGlobalmapEventaccountinfo200ResponseOneOfDataValue

# TODO update the JSON string below
json = "{}"
# create an instance of GetGlobalmapEventaccountinfo200ResponseOneOfDataValue from a JSON string
get_globalmap_eventaccountinfo200_response_one_of_data_value_instance = GetGlobalmapEventaccountinfo200ResponseOneOfDataValue.from_json(json)
# print the JSON string representation of the object
print(GetGlobalmapEventaccountinfo200ResponseOneOfDataValue.to_json())

# convert the object into a dict
get_globalmap_eventaccountinfo200_response_one_of_data_value_dict = get_globalmap_eventaccountinfo200_response_one_of_data_value_instance.to_dict()
# create an instance of GetGlobalmapEventaccountinfo200ResponseOneOfDataValue from a dict
get_globalmap_eventaccountinfo200_response_one_of_data_value_from_dict = GetGlobalmapEventaccountinfo200ResponseOneOfDataValue.from_dict(get_globalmap_eventaccountinfo200_response_one_of_data_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


