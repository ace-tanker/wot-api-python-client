# EncyclopediaCrewskillsOk


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**meta** | [**EncyclopediaCrewskillsMeta**](EncyclopediaCrewskillsMeta.md) |  | 
**data** | [**Dict[str, EncyclopediaCrewskillsDataValue]**](EncyclopediaCrewskillsDataValue.md) |  | 

## Example

```python
from wot_api_client.models.encyclopedia_crewskills_ok import EncyclopediaCrewskillsOk

# TODO update the JSON string below
json = "{}"
# create an instance of EncyclopediaCrewskillsOk from a JSON string
encyclopedia_crewskills_ok_instance = EncyclopediaCrewskillsOk.from_json(json)
# print the JSON string representation of the object
print(EncyclopediaCrewskillsOk.to_json())

# convert the object into a dict
encyclopedia_crewskills_ok_dict = encyclopedia_crewskills_ok_instance.to_dict()
# create an instance of EncyclopediaCrewskillsOk from a dict
encyclopedia_crewskills_ok_from_dict = EncyclopediaCrewskillsOk.from_dict(encyclopedia_crewskills_ok_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


