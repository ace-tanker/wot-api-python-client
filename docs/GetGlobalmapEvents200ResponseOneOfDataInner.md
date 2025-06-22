# GetGlobalmapEvents200ResponseOneOfDataInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event_id** | **str** | Event ID | 
**event_name** | **str** | Event name | 
**start** | **str** | Start time | 
**end** | **str** | Finishing time | 
**status** | **str** | Status | 
**fronts** | [**List[GetGlobalmapEvents200ResponseOneOfDataInnerFrontsInner]**](GetGlobalmapEvents200ResponseOneOfDataInnerFrontsInner.md) | Fronts. Only event fronts are presented in response. | 

## Example

```python
from wot_api_client.models.get_globalmap_events200_response_one_of_data_inner import GetGlobalmapEvents200ResponseOneOfDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetGlobalmapEvents200ResponseOneOfDataInner from a JSON string
get_globalmap_events200_response_one_of_data_inner_instance = GetGlobalmapEvents200ResponseOneOfDataInner.from_json(json)
# print the JSON string representation of the object
print(GetGlobalmapEvents200ResponseOneOfDataInner.to_json())

# convert the object into a dict
get_globalmap_events200_response_one_of_data_inner_dict = get_globalmap_events200_response_one_of_data_inner_instance.to_dict()
# create an instance of GetGlobalmapEvents200ResponseOneOfDataInner from a dict
get_globalmap_events200_response_one_of_data_inner_from_dict = GetGlobalmapEvents200ResponseOneOfDataInner.from_dict(get_globalmap_events200_response_one_of_data_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


