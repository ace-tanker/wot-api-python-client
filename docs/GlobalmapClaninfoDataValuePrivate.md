# GlobalmapClaninfoDataValuePrivate

Restricted clan information on the Global Map

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**daily_wage** | **int** | Influence points spent per day | 
**influence** | **int** | Influence points | 

## Example

```python
from wot_api_client.models.globalmap_claninfo_data_value_private import GlobalmapClaninfoDataValuePrivate

# TODO update the JSON string below
json = "{}"
# create an instance of GlobalmapClaninfoDataValuePrivate from a JSON string
globalmap_claninfo_data_value_private_instance = GlobalmapClaninfoDataValuePrivate.from_json(json)
# print the JSON string representation of the object
print(GlobalmapClaninfoDataValuePrivate.to_json())

# convert the object into a dict
globalmap_claninfo_data_value_private_dict = globalmap_claninfo_data_value_private_instance.to_dict()
# create an instance of GlobalmapClaninfoDataValuePrivate from a dict
globalmap_claninfo_data_value_private_from_dict = GlobalmapClaninfoDataValuePrivate.from_dict(globalmap_claninfo_data_value_private_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


