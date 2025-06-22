# Prolongate200ResponseOneOfData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_token** | **str** | Access token is passed to all methods requiring authorization. | 
**expires_at** | **int** | **Access_token** expiration time | 
**account_id** | **int** | Player account ID | 

## Example

```python
from wot_api_client.models.prolongate200_response_one_of_data import Prolongate200ResponseOneOfData

# TODO update the JSON string below
json = "{}"
# create an instance of Prolongate200ResponseOneOfData from a JSON string
prolongate200_response_one_of_data_instance = Prolongate200ResponseOneOfData.from_json(json)
# print the JSON string representation of the object
print(Prolongate200ResponseOneOfData.to_json())

# convert the object into a dict
prolongate200_response_one_of_data_dict = prolongate200_response_one_of_data_instance.to_dict()
# create an instance of Prolongate200ResponseOneOfData from a dict
prolongate200_response_one_of_data_from_dict = Prolongate200ResponseOneOfData.from_dict(prolongate200_response_one_of_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


