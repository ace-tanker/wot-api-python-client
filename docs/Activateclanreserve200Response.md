# Activateclanreserve200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**meta** | [**StrongholdActivateclanreserveMeta**](StrongholdActivateclanreserveMeta.md) |  | 
**data** | [**StrongholdActivateclanreserveData**](StrongholdActivateclanreserveData.md) |  | 
**error** | [**StrongholdActivateclanreserveErrorError**](StrongholdActivateclanreserveErrorError.md) |  | 

## Example

```python
from wot_api_client.models.activateclanreserve200_response import Activateclanreserve200Response

# TODO update the JSON string below
json = "{}"
# create an instance of Activateclanreserve200Response from a JSON string
activateclanreserve200_response_instance = Activateclanreserve200Response.from_json(json)
# print the JSON string representation of the object
print(Activateclanreserve200Response.to_json())

# convert the object into a dict
activateclanreserve200_response_dict = activateclanreserve200_response_instance.to_dict()
# create an instance of Activateclanreserve200Response from a dict
activateclanreserve200_response_from_dict = Activateclanreserve200Response.from_dict(activateclanreserve200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


