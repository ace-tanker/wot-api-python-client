# GetEncyclopediaPersonalmissions200ResponseOneOfDataValue


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**campaign_id** | **int** | Campaign ID | 
**name** | **str** | Campaign name | 
**description** | **str** | Campaign description | 
**operations** | [**Dict[str, GetEncyclopediaPersonalmissions200ResponseOneOfDataValueOperationsValue]**](GetEncyclopediaPersonalmissions200ResponseOneOfDataValueOperationsValue.md) | Campaign operations | 

## Example

```python
from wot_api_client.models.get_encyclopedia_personalmissions200_response_one_of_data_value import GetEncyclopediaPersonalmissions200ResponseOneOfDataValue

# TODO update the JSON string below
json = "{}"
# create an instance of GetEncyclopediaPersonalmissions200ResponseOneOfDataValue from a JSON string
get_encyclopedia_personalmissions200_response_one_of_data_value_instance = GetEncyclopediaPersonalmissions200ResponseOneOfDataValue.from_json(json)
# print the JSON string representation of the object
print(GetEncyclopediaPersonalmissions200ResponseOneOfDataValue.to_json())

# convert the object into a dict
get_encyclopedia_personalmissions200_response_one_of_data_value_dict = get_encyclopedia_personalmissions200_response_one_of_data_value_instance.to_dict()
# create an instance of GetEncyclopediaPersonalmissions200ResponseOneOfDataValue from a dict
get_encyclopedia_personalmissions200_response_one_of_data_value_from_dict = GetEncyclopediaPersonalmissions200ResponseOneOfDataValue.from_dict(get_encyclopedia_personalmissions200_response_one_of_data_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


