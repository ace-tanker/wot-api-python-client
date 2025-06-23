# GlobalmapEventaccountratingsError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**error** | [**GlobalmapEventsErrorError**](GlobalmapEventsErrorError.md) |  | 

## Example

```python
from wot_api_client.models.globalmap_eventaccountratings_error import GlobalmapEventaccountratingsError

# TODO update the JSON string below
json = "{}"
# create an instance of GlobalmapEventaccountratingsError from a JSON string
globalmap_eventaccountratings_error_instance = GlobalmapEventaccountratingsError.from_json(json)
# print the JSON string representation of the object
print(GlobalmapEventaccountratingsError.to_json())

# convert the object into a dict
globalmap_eventaccountratings_error_dict = globalmap_eventaccountratings_error_instance.to_dict()
# create an instance of GlobalmapEventaccountratingsError from a dict
globalmap_eventaccountratings_error_from_dict = GlobalmapEventaccountratingsError.from_dict(globalmap_eventaccountratings_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


