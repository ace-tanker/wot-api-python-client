# GetTanksMastery200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**meta** | [**TanksMasteryMeta**](TanksMasteryMeta.md) |  | 
**data** | [**TanksMasteryData**](TanksMasteryData.md) |  | 
**error** | **object** |  | 

## Example

```python
from wot_api_client.models.get_tanks_mastery200_response import GetTanksMastery200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetTanksMastery200Response from a JSON string
get_tanks_mastery200_response_instance = GetTanksMastery200Response.from_json(json)
# print the JSON string representation of the object
print(GetTanksMastery200Response.to_json())

# convert the object into a dict
get_tanks_mastery200_response_dict = get_tanks_mastery200_response_instance.to_dict()
# create an instance of GetTanksMastery200Response from a dict
get_tanks_mastery200_response_from_dict = GetTanksMastery200Response.from_dict(get_tanks_mastery200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


