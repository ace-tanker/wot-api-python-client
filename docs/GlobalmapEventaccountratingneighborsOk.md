# GlobalmapEventaccountratingneighborsOk


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**meta** | [**GlobalmapEventaccountratingneighborsMeta**](GlobalmapEventaccountratingneighborsMeta.md) |  | 
**data** | [**List[GlobalmapEventaccountratingsDataInner]**](GlobalmapEventaccountratingsDataInner.md) |  | 

## Example

```python
from wot_api_client.models.globalmap_eventaccountratingneighbors_ok import GlobalmapEventaccountratingneighborsOk

# TODO update the JSON string below
json = "{}"
# create an instance of GlobalmapEventaccountratingneighborsOk from a JSON string
globalmap_eventaccountratingneighbors_ok_instance = GlobalmapEventaccountratingneighborsOk.from_json(json)
# print the JSON string representation of the object
print(GlobalmapEventaccountratingneighborsOk.to_json())

# convert the object into a dict
globalmap_eventaccountratingneighbors_ok_dict = globalmap_eventaccountratingneighbors_ok_instance.to_dict()
# create an instance of GlobalmapEventaccountratingneighborsOk from a dict
globalmap_eventaccountratingneighbors_ok_from_dict = GlobalmapEventaccountratingneighborsOk.from_dict(globalmap_eventaccountratingneighbors_ok_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


