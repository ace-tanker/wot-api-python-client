# TanksMasteryData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**distribution** | **Dict[str, Dict[str, int]]** | Values of these percentiles for each piece of equipment | 
**updated_at** | **int** | Date of data update | 

## Example

```python
from wot_api_client.models.tanks_mastery_data import TanksMasteryData

# TODO update the JSON string below
json = "{}"
# create an instance of TanksMasteryData from a JSON string
tanks_mastery_data_instance = TanksMasteryData.from_json(json)
# print the JSON string representation of the object
print(TanksMasteryData.to_json())

# convert the object into a dict
tanks_mastery_data_dict = tanks_mastery_data_instance.to_dict()
# create an instance of TanksMasteryData from a dict
tanks_mastery_data_from_dict = TanksMasteryData.from_dict(tanks_mastery_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


