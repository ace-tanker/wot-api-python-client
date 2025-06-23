# StrongholdClanreservesDataInnerInStockInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **int** | Number of clan Reserves of each level | 
**bonus_values** | [**List[StrongholdClanreservesDataInnerInStockInnerBonusValuesInner]**](StrongholdClanreservesDataInnerInStockInnerBonusValuesInner.md) | Reserve efficiencies | 
**x_level_only** | **bool** | Indicates if the Reserve is only for Tier X vehicles | 
**status** | **str** | Status of clan Reserves of each level | 
**action_time** | **int** | Duration of clan Reserves of each level | 
**activated_at** | **int** | Activation time of clan Reserves of each level | 
**active_till** | **int** | Expiration time of clan Reserves of each level | 
**level** | **int** | Level of available clan Reserves | 

## Example

```python
from wot_api_client.models.stronghold_clanreserves_data_inner_in_stock_inner import StrongholdClanreservesDataInnerInStockInner

# TODO update the JSON string below
json = "{}"
# create an instance of StrongholdClanreservesDataInnerInStockInner from a JSON string
stronghold_clanreserves_data_inner_in_stock_inner_instance = StrongholdClanreservesDataInnerInStockInner.from_json(json)
# print the JSON string representation of the object
print(StrongholdClanreservesDataInnerInStockInner.to_json())

# convert the object into a dict
stronghold_clanreserves_data_inner_in_stock_inner_dict = stronghold_clanreserves_data_inner_in_stock_inner_instance.to_dict()
# create an instance of StrongholdClanreservesDataInnerInStockInner from a dict
stronghold_clanreserves_data_inner_in_stock_inner_from_dict = StrongholdClanreservesDataInnerInStockInner.from_dict(stronghold_clanreserves_data_inner_in_stock_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


