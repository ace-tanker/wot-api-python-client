# GetStrongholdClanreserves200ResponseOneOfDataInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Reserve name | 
**type** | **str** | Reserve type | 
**disposable** | **bool** | Indicates if the Reserve is a One-Time-Effect Reserve | 
**bonus_type** | **str** | Reserve efficiency type | 
**icon** | **str** | URL to icon | 
**in_stock** | [**List[GetStrongholdClanreserves200ResponseOneOfDataInnerInStockInner]**](GetStrongholdClanreserves200ResponseOneOfDataInnerInStockInner.md) | Available clan Reserves and their status | 

## Example

```python
from wot_api_client.models.get_stronghold_clanreserves200_response_one_of_data_inner import GetStrongholdClanreserves200ResponseOneOfDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetStrongholdClanreserves200ResponseOneOfDataInner from a JSON string
get_stronghold_clanreserves200_response_one_of_data_inner_instance = GetStrongholdClanreserves200ResponseOneOfDataInner.from_json(json)
# print the JSON string representation of the object
print(GetStrongholdClanreserves200ResponseOneOfDataInner.to_json())

# convert the object into a dict
get_stronghold_clanreserves200_response_one_of_data_inner_dict = get_stronghold_clanreserves200_response_one_of_data_inner_instance.to_dict()
# create an instance of GetStrongholdClanreserves200ResponseOneOfDataInner from a dict
get_stronghold_clanreserves200_response_one_of_data_inner_from_dict = GetStrongholdClanreserves200ResponseOneOfDataInner.from_dict(get_stronghold_clanreserves200_response_one_of_data_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


