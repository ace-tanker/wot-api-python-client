# Activateclanreserve200ResponseOneOf


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**meta** | [**GetAccountList200ResponseOneOfMeta**](GetAccountList200ResponseOneOfMeta.md) |  | 
**data** | [**Activateclanreserve200ResponseOneOfData**](Activateclanreserve200ResponseOneOfData.md) |  | 

## Example

```python
from wot_api_client.models.activateclanreserve200_response_one_of import Activateclanreserve200ResponseOneOf

# TODO update the JSON string below
json = "{}"
# create an instance of Activateclanreserve200ResponseOneOf from a JSON string
activateclanreserve200_response_one_of_instance = Activateclanreserve200ResponseOneOf.from_json(json)
# print the JSON string representation of the object
print(Activateclanreserve200ResponseOneOf.to_json())

# convert the object into a dict
activateclanreserve200_response_one_of_dict = activateclanreserve200_response_one_of_instance.to_dict()
# create an instance of Activateclanreserve200ResponseOneOf from a dict
activateclanreserve200_response_one_of_from_dict = Activateclanreserve200ResponseOneOf.from_dict(activateclanreserve200_response_one_of_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


