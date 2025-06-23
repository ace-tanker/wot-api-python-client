# ClansListDataInnerEmblems

Information on clan emblems in games and on clan portal

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**x24** | **Dict[str, str]** | List of links to 24x24 px emblems | 
**x32** | **Dict[str, str]** | List of links to 32x32 px emblems | 
**x64** | **Dict[str, str]** | List of links to 64x64 px emblems | 
**x195** | **Dict[str, str]** | List of links to 195x195 px emblems | 
**x256** | **Dict[str, str]** | List of links to 256x256 px emblems | 

## Example

```python
from wot_api_client.models.clans_list_data_inner_emblems import ClansListDataInnerEmblems

# TODO update the JSON string below
json = "{}"
# create an instance of ClansListDataInnerEmblems from a JSON string
clans_list_data_inner_emblems_instance = ClansListDataInnerEmblems.from_json(json)
# print the JSON string representation of the object
print(ClansListDataInnerEmblems.to_json())

# convert the object into a dict
clans_list_data_inner_emblems_dict = clans_list_data_inner_emblems_instance.to_dict()
# create an instance of ClansListDataInnerEmblems from a dict
clans_list_data_inner_emblems_from_dict = ClansListDataInnerEmblems.from_dict(clans_list_data_inner_emblems_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


