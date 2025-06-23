# GlobalmapFrontsDataInnerAvailableExtensionsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**extension_id** | **str** | Consumable ID | 
**cost** | **int** | Cost of modules | 
**wage** | **int** | Modules upkeep cost | 
**name** | **str** | Localized consumable name | 
**description_tactical** | **str** | Localized description of tactical effect | 
**description_strategic** | **str** | Localized description of strategic effect | 

## Example

```python
from wot_api_client.models.globalmap_fronts_data_inner_available_extensions_inner import GlobalmapFrontsDataInnerAvailableExtensionsInner

# TODO update the JSON string below
json = "{}"
# create an instance of GlobalmapFrontsDataInnerAvailableExtensionsInner from a JSON string
globalmap_fronts_data_inner_available_extensions_inner_instance = GlobalmapFrontsDataInnerAvailableExtensionsInner.from_json(json)
# print the JSON string representation of the object
print(GlobalmapFrontsDataInnerAvailableExtensionsInner.to_json())

# convert the object into a dict
globalmap_fronts_data_inner_available_extensions_inner_dict = globalmap_fronts_data_inner_available_extensions_inner_instance.to_dict()
# create an instance of GlobalmapFrontsDataInnerAvailableExtensionsInner from a dict
globalmap_fronts_data_inner_available_extensions_inner_from_dict = GlobalmapFrontsDataInnerAvailableExtensionsInner.from_dict(globalmap_fronts_data_inner_available_extensions_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


