# GetTanksAchievements200ResponseOneOfDataValueInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **int** | Player account ID | 
**tank_id** | **int** | Vehicle ID | 
**achievements** | **Dict[str, int]** | Achievements earned | 
**series** | **Dict[str, int]** | Current values of Achievement Series | 
**max_series** | **Dict[str, int]** | Maximum values of achievement series | 

## Example

```python
from wot_api_client.models.get_tanks_achievements200_response_one_of_data_value_inner import GetTanksAchievements200ResponseOneOfDataValueInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetTanksAchievements200ResponseOneOfDataValueInner from a JSON string
get_tanks_achievements200_response_one_of_data_value_inner_instance = GetTanksAchievements200ResponseOneOfDataValueInner.from_json(json)
# print the JSON string representation of the object
print(GetTanksAchievements200ResponseOneOfDataValueInner.to_json())

# convert the object into a dict
get_tanks_achievements200_response_one_of_data_value_inner_dict = get_tanks_achievements200_response_one_of_data_value_inner_instance.to_dict()
# create an instance of GetTanksAchievements200ResponseOneOfDataValueInner from a dict
get_tanks_achievements200_response_one_of_data_value_inner_from_dict = GetTanksAchievements200ResponseOneOfDataValueInner.from_dict(get_tanks_achievements200_response_one_of_data_value_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


