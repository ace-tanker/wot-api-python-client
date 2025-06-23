# EncyclopediaModulesDataValueDefaultProfileEngine

Engine characteristics

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**power** | **int** | Engine Power (hp) | 
**fire_chance** | **float** | Chance of engine fire | 

## Example

```python
from wot_api_client.models.encyclopedia_modules_data_value_default_profile_engine import EncyclopediaModulesDataValueDefaultProfileEngine

# TODO update the JSON string below
json = "{}"
# create an instance of EncyclopediaModulesDataValueDefaultProfileEngine from a JSON string
encyclopedia_modules_data_value_default_profile_engine_instance = EncyclopediaModulesDataValueDefaultProfileEngine.from_json(json)
# print the JSON string representation of the object
print(EncyclopediaModulesDataValueDefaultProfileEngine.to_json())

# convert the object into a dict
encyclopedia_modules_data_value_default_profile_engine_dict = encyclopedia_modules_data_value_default_profile_engine_instance.to_dict()
# create an instance of EncyclopediaModulesDataValueDefaultProfileEngine from a dict
encyclopedia_modules_data_value_default_profile_engine_from_dict = EncyclopediaModulesDataValueDefaultProfileEngine.from_dict(encyclopedia_modules_data_value_default_profile_engine_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


