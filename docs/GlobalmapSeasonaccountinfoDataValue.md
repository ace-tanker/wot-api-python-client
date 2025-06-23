# GlobalmapSeasonaccountinfoDataValue


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**seasons** | **Dict[str, Optional[List[GlobalmapSeasonaccountinfoDataValueSeasonsValueInner]]]** | Account information by seasons and vehicle Tiers | 

## Example

```python
from wot_api_client.models.globalmap_seasonaccountinfo_data_value import GlobalmapSeasonaccountinfoDataValue

# TODO update the JSON string below
json = "{}"
# create an instance of GlobalmapSeasonaccountinfoDataValue from a JSON string
globalmap_seasonaccountinfo_data_value_instance = GlobalmapSeasonaccountinfoDataValue.from_json(json)
# print the JSON string representation of the object
print(GlobalmapSeasonaccountinfoDataValue.to_json())

# convert the object into a dict
globalmap_seasonaccountinfo_data_value_dict = globalmap_seasonaccountinfo_data_value_instance.to_dict()
# create an instance of GlobalmapSeasonaccountinfoDataValue from a dict
globalmap_seasonaccountinfo_data_value_from_dict = GlobalmapSeasonaccountinfoDataValue.from_dict(globalmap_seasonaccountinfo_data_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


