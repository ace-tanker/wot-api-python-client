# TanksStatsOk


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**meta** | [**TanksStatsMeta**](TanksStatsMeta.md) |  | 
**data** | **Dict[str, Optional[List[TanksStatsDataValueInner]]]** |  | 

## Example

```python
from wot_api_client.models.tanks_stats_ok import TanksStatsOk

# TODO update the JSON string below
json = "{}"
# create an instance of TanksStatsOk from a JSON string
tanks_stats_ok_instance = TanksStatsOk.from_json(json)
# print the JSON string representation of the object
print(TanksStatsOk.to_json())

# convert the object into a dict
tanks_stats_ok_dict = tanks_stats_ok_instance.to_dict()
# create an instance of TanksStatsOk from a dict
tanks_stats_ok_from_dict = TanksStatsOk.from_dict(tanks_stats_ok_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


