# GetAccountInfo200ResponseOneOfDataValuePrivateGroupedContacts

Contact groups.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ungrouped** | **List[int]** | Not grouped | 
**ignored** | **List[int]** | Ignored | 
**blocked** | **List[int]** | The contact was added to the blacklist. Note that the blocked contact still belongs to contact groups or to the ungrouped list of contacts. | 
**muted** | **List[int]** | Muted | 
**groups** | **Dict[str, List[int]]** | Groups | 

## Example

```python
from wot_api_client.models.get_account_info200_response_one_of_data_value_private_grouped_contacts import GetAccountInfo200ResponseOneOfDataValuePrivateGroupedContacts

# TODO update the JSON string below
json = "{}"
# create an instance of GetAccountInfo200ResponseOneOfDataValuePrivateGroupedContacts from a JSON string
get_account_info200_response_one_of_data_value_private_grouped_contacts_instance = GetAccountInfo200ResponseOneOfDataValuePrivateGroupedContacts.from_json(json)
# print the JSON string representation of the object
print(GetAccountInfo200ResponseOneOfDataValuePrivateGroupedContacts.to_json())

# convert the object into a dict
get_account_info200_response_one_of_data_value_private_grouped_contacts_dict = get_account_info200_response_one_of_data_value_private_grouped_contacts_instance.to_dict()
# create an instance of GetAccountInfo200ResponseOneOfDataValuePrivateGroupedContacts from a dict
get_account_info200_response_one_of_data_value_private_grouped_contacts_from_dict = GetAccountInfo200ResponseOneOfDataValuePrivateGroupedContacts.from_dict(get_account_info200_response_one_of_data_value_private_grouped_contacts_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


