# Prolongate200ResponseOneOf


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**meta** | [**GetAccountList200ResponseOneOfMeta**](GetAccountList200ResponseOneOfMeta.md) |  | 
**data** | [**Prolongate200ResponseOneOfData**](Prolongate200ResponseOneOfData.md) |  | 

## Example

```python
from wot_api_client.models.prolongate200_response_one_of import Prolongate200ResponseOneOf

# TODO update the JSON string below
json = "{}"
# create an instance of Prolongate200ResponseOneOf from a JSON string
prolongate200_response_one_of_instance = Prolongate200ResponseOneOf.from_json(json)
# print the JSON string representation of the object
print(Prolongate200ResponseOneOf.to_json())

# convert the object into a dict
prolongate200_response_one_of_dict = prolongate200_response_one_of_instance.to_dict()
# create an instance of Prolongate200ResponseOneOf from a dict
prolongate200_response_one_of_from_dict = Prolongate200ResponseOneOf.from_dict(prolongate200_response_one_of_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


