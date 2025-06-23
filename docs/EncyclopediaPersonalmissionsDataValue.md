# EncyclopediaPersonalmissionsDataValue


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**campaign_id** | **int** | Campaign ID | 
**name** | **str** | Campaign name | 
**description** | **str** | Campaign description | 
**operations** | [**Dict[str, EncyclopediaPersonalmissionsDataValueOperationsValue]**](EncyclopediaPersonalmissionsDataValueOperationsValue.md) | Campaign operations | 

## Example

```python
from wot_api_client.models.encyclopedia_personalmissions_data_value import EncyclopediaPersonalmissionsDataValue

# TODO update the JSON string below
json = "{}"
# create an instance of EncyclopediaPersonalmissionsDataValue from a JSON string
encyclopedia_personalmissions_data_value_instance = EncyclopediaPersonalmissionsDataValue.from_json(json)
# print the JSON string representation of the object
print(EncyclopediaPersonalmissionsDataValue.to_json())

# convert the object into a dict
encyclopedia_personalmissions_data_value_dict = encyclopedia_personalmissions_data_value_instance.to_dict()
# create an instance of EncyclopediaPersonalmissionsDataValue from a dict
encyclopedia_personalmissions_data_value_from_dict = EncyclopediaPersonalmissionsDataValue.from_dict(encyclopedia_personalmissions_data_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


