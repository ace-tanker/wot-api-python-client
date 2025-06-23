# StrongholdClanreservesDataInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Reserve name | 
**type** | **str** | Reserve type | 
**disposable** | **bool** | Indicates if the Reserve is a One-Time-Effect Reserve | 
**bonus_type** | **str** | Reserve efficiency type | 
**icon** | **str** | URL to icon | 
**in_stock** | [**List[StrongholdClanreservesDataInnerInStockInner]**](StrongholdClanreservesDataInnerInStockInner.md) | Available clan Reserves and their status | 

## Example

```python
from wot_api_client.models.stronghold_clanreserves_data_inner import StrongholdClanreservesDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of StrongholdClanreservesDataInner from a JSON string
stronghold_clanreserves_data_inner_instance = StrongholdClanreservesDataInner.from_json(json)
# print the JSON string representation of the object
print(StrongholdClanreservesDataInner.to_json())

# convert the object into a dict
stronghold_clanreserves_data_inner_dict = stronghold_clanreserves_data_inner_instance.to_dict()
# create an instance of StrongholdClanreservesDataInner from a dict
stronghold_clanreserves_data_inner_from_dict = StrongholdClanreservesDataInner.from_dict(stronghold_clanreserves_data_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


