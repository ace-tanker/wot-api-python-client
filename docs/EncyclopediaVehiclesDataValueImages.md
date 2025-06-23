# EncyclopediaVehiclesDataValueImages

Image links

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**big_icon** | **str** | URL to 160 x 100 px image of vehicle | 
**small_icon** | **str** | URL to 124 x 31 px image of vehicle | 
**contour_icon** | **str** | URL to outline image of vehicle | 

## Example

```python
from wot_api_client.models.encyclopedia_vehicles_data_value_images import EncyclopediaVehiclesDataValueImages

# TODO update the JSON string below
json = "{}"
# create an instance of EncyclopediaVehiclesDataValueImages from a JSON string
encyclopedia_vehicles_data_value_images_instance = EncyclopediaVehiclesDataValueImages.from_json(json)
# print the JSON string representation of the object
print(EncyclopediaVehiclesDataValueImages.to_json())

# convert the object into a dict
encyclopedia_vehicles_data_value_images_dict = encyclopedia_vehicles_data_value_images_instance.to_dict()
# create an instance of EncyclopediaVehiclesDataValueImages from a dict
encyclopedia_vehicles_data_value_images_from_dict = EncyclopediaVehiclesDataValueImages.from_dict(encyclopedia_vehicles_data_value_images_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


