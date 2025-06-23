# GlobalmapEventaccountratingsOk


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**meta** | [**GlobalmapEventaccountratingsMeta**](GlobalmapEventaccountratingsMeta.md) |  | 
**data** | [**List[GlobalmapEventaccountratingsDataInner]**](GlobalmapEventaccountratingsDataInner.md) |  | 

## Example

```python
from wot_api_client.models.globalmap_eventaccountratings_ok import GlobalmapEventaccountratingsOk

# TODO update the JSON string below
json = "{}"
# create an instance of GlobalmapEventaccountratingsOk from a JSON string
globalmap_eventaccountratings_ok_instance = GlobalmapEventaccountratingsOk.from_json(json)
# print the JSON string representation of the object
print(GlobalmapEventaccountratingsOk.to_json())

# convert the object into a dict
globalmap_eventaccountratings_ok_dict = globalmap_eventaccountratings_ok_instance.to_dict()
# create an instance of GlobalmapEventaccountratingsOk from a dict
globalmap_eventaccountratings_ok_from_dict = GlobalmapEventaccountratingsOk.from_dict(globalmap_eventaccountratings_ok_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


