# EncyclopediaCrewrolesOk


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**meta** | [**EncyclopediaCrewrolesMeta**](EncyclopediaCrewrolesMeta.md) |  | 
**data** | [**Dict[str, EncyclopediaCrewrolesDataValue]**](EncyclopediaCrewrolesDataValue.md) |  | 

## Example

```python
from wot_api_client.models.encyclopedia_crewroles_ok import EncyclopediaCrewrolesOk

# TODO update the JSON string below
json = "{}"
# create an instance of EncyclopediaCrewrolesOk from a JSON string
encyclopedia_crewroles_ok_instance = EncyclopediaCrewrolesOk.from_json(json)
# print the JSON string representation of the object
print(EncyclopediaCrewrolesOk.to_json())

# convert the object into a dict
encyclopedia_crewroles_ok_dict = encyclopedia_crewroles_ok_instance.to_dict()
# create an instance of EncyclopediaCrewrolesOk from a dict
encyclopedia_crewroles_ok_from_dict = EncyclopediaCrewrolesOk.from_dict(encyclopedia_crewroles_ok_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


