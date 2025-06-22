# wot_api_client.PlayersVehiclesApi

All URIs are relative to *https://api.worldoftanks.eu/wot*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_tanks_achievements**](PlayersVehiclesApi.md#get_tanks_achievements) | **GET** /tanks/achievements/ | Vehicle achievements
[**get_tanks_mastery**](PlayersVehiclesApi.md#get_tanks_mastery) | **GET** /tanks/mastery/ | Vehicle mastery distribution
[**get_tanks_stats**](PlayersVehiclesApi.md#get_tanks_stats) | **GET** /tanks/stats/ | Vehicle statistics


# **get_tanks_achievements**
> GetTanksAchievements200Response get_tanks_achievements(account_id, access_token=access_token, fields=fields, in_garage=in_garage, tank_id=tank_id)

Vehicle achievements

Method returns list of achievements on all player's vehicles.

Achievement properties define the **achievements** field values:

 * 1-4 for Mastery Badges and Stage Achievements (type: "class");
 * maximum value of Achievement series (type: "series");
 * number of achievements earned from sections: Battle Hero, Epic Achievements, Group Achievements, Special Achievements, etc. (type: "repeatable, single, custom").


### Example

* Api Key Authentication (application_id):

```python
import wot_api_client
from wot_api_client.models.get_tanks_achievements200_response import GetTanksAchievements200Response
from wot_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.worldoftanks.eu/wot
# See configuration.py for a list of all supported configuration parameters.
configuration = wot_api_client.Configuration(
    host = "https://api.worldoftanks.eu/wot"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: application_id
configuration.api_key['application_id'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['application_id'] = 'Bearer'

# Enter a context with an instance of the API client
with wot_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wot_api_client.PlayersVehiclesApi(api_client)
    account_id = 56 # int | Player account ID
    access_token = 'access_token_example' # str | [Access token](https://developers.wargaming.net/documentation/guide/principles/#access_token) for the private data of a user's account; can be received via the authorization method; valid within a stated time period (optional)
    fields = [] # List[str] | Response field. Embedded fields are separated with dots. To exclude a field, use “-” in front of its name. In case the parameter is not defined, the method returns all fields. (optional) (default to [])
    in_garage = 'in_garage_example' # str | Filter by vehicle availability in the Garage. If the parameter is not specified, all vehicles are returned. Parameter processing requires a valid access_token for the specified account_id. (optional)
    tank_id = [56] # List[int] | Player's vehicle ID. (optional)

    try:
        # Vehicle achievements
        api_response = api_instance.get_tanks_achievements(account_id, access_token=access_token, fields=fields, in_garage=in_garage, tank_id=tank_id)
        print("The response of PlayersVehiclesApi->get_tanks_achievements:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlayersVehiclesApi->get_tanks_achievements: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **int**| Player account ID | 
 **access_token** | **str**| [Access token](https://developers.wargaming.net/documentation/guide/principles/#access_token) for the private data of a user&#39;s account; can be received via the authorization method; valid within a stated time period | [optional] 
 **fields** | [**List[str]**](str.md)| Response field. Embedded fields are separated with dots. To exclude a field, use “-” in front of its name. In case the parameter is not defined, the method returns all fields. | [optional] [default to []]
 **in_garage** | **str**| Filter by vehicle availability in the Garage. If the parameter is not specified, all vehicles are returned. Parameter processing requires a valid access_token for the specified account_id. | [optional] 
 **tank_id** | [**List[int]**](int.md)| Player&#39;s vehicle ID. | [optional] 

### Return type

[**GetTanksAchievements200Response**](GetTanksAchievements200Response.md)

### Authorization

[application_id](../README.md#application_id)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tanks_mastery**
> GetTanksMastery200Response get_tanks_mastery(distribution, percentile, fields=fields, tank_id=tank_id)

Vehicle mastery distribution

The method returns percentiles of the distribution of average damage or experience values for each piece of equipment

### Example

* Api Key Authentication (application_id):

```python
import wot_api_client
from wot_api_client.models.get_tanks_mastery200_response import GetTanksMastery200Response
from wot_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.worldoftanks.eu/wot
# See configuration.py for a list of all supported configuration parameters.
configuration = wot_api_client.Configuration(
    host = "https://api.worldoftanks.eu/wot"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: application_id
configuration.api_key['application_id'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['application_id'] = 'Bearer'

# Enter a context with an instance of the API client
with wot_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wot_api_client.PlayersVehiclesApi(api_client)
    distribution = 'distribution_example' # str | Type of data.
    percentile = [56] # List[int] | A list of percentiles to be included in the response.
    fields = [] # List[str] | Response field. Embedded fields are separated with dots. To exclude a field, use “-” in front of its name. In case the parameter is not defined, the method returns all fields. (optional) (default to [])
    tank_id = [56] # List[int] | Player's vehicle ID. (optional)

    try:
        # Vehicle mastery distribution
        api_response = api_instance.get_tanks_mastery(distribution, percentile, fields=fields, tank_id=tank_id)
        print("The response of PlayersVehiclesApi->get_tanks_mastery:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlayersVehiclesApi->get_tanks_mastery: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **distribution** | **str**| Type of data. | 
 **percentile** | [**List[int]**](int.md)| A list of percentiles to be included in the response. | 
 **fields** | [**List[str]**](str.md)| Response field. Embedded fields are separated with dots. To exclude a field, use “-” in front of its name. In case the parameter is not defined, the method returns all fields. | [optional] [default to []]
 **tank_id** | [**List[int]**](int.md)| Player&#39;s vehicle ID. | [optional] 

### Return type

[**GetTanksMastery200Response**](GetTanksMastery200Response.md)

### Authorization

[application_id](../README.md#application_id)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tanks_stats**
> GetTanksStats200Response get_tanks_stats(account_id, access_token=access_token, extra=extra, fields=fields, in_garage=in_garage, tank_id=tank_id)

Vehicle statistics

Method returns overall statistics, Tank Company statistics, and clan statistics per each vehicle for each user.

### Example

* Api Key Authentication (application_id):

```python
import wot_api_client
from wot_api_client.models.get_tanks_stats200_response import GetTanksStats200Response
from wot_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.worldoftanks.eu/wot
# See configuration.py for a list of all supported configuration parameters.
configuration = wot_api_client.Configuration(
    host = "https://api.worldoftanks.eu/wot"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: application_id
configuration.api_key['application_id'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['application_id'] = 'Bearer'

# Enter a context with an instance of the API client
with wot_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wot_api_client.PlayersVehiclesApi(api_client)
    account_id = 56 # int | Player account ID
    access_token = 'access_token_example' # str | [Access token](https://developers.wargaming.net/documentation/guide/principles/#access_token) for the private data of a user's account; can be received via the authorization method; valid within a stated time period (optional)
    extra = None # object | Extra fields that will be added to the response. (optional)
    fields = [] # List[str] | Response field. Embedded fields are separated with dots. To exclude a field, use “-” in front of its name. In case the parameter is not defined, the method returns all fields. (optional) (default to [])
    in_garage = 'in_garage_example' # str | Filter by vehicle availability in the Garage. If the parameter is not specified, all vehicles are returned. Parameter processing requires a valid access_token for the specified account_id. (optional)
    tank_id = [56] # List[int] | Player's vehicle ID. (optional)

    try:
        # Vehicle statistics
        api_response = api_instance.get_tanks_stats(account_id, access_token=access_token, extra=extra, fields=fields, in_garage=in_garage, tank_id=tank_id)
        print("The response of PlayersVehiclesApi->get_tanks_stats:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlayersVehiclesApi->get_tanks_stats: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **int**| Player account ID | 
 **access_token** | **str**| [Access token](https://developers.wargaming.net/documentation/guide/principles/#access_token) for the private data of a user&#39;s account; can be received via the authorization method; valid within a stated time period | [optional] 
 **extra** | [**object**](.md)| Extra fields that will be added to the response. | [optional] 
 **fields** | [**List[str]**](str.md)| Response field. Embedded fields are separated with dots. To exclude a field, use “-” in front of its name. In case the parameter is not defined, the method returns all fields. | [optional] [default to []]
 **in_garage** | **str**| Filter by vehicle availability in the Garage. If the parameter is not specified, all vehicles are returned. Parameter processing requires a valid access_token for the specified account_id. | [optional] 
 **tank_id** | [**List[int]**](int.md)| Player&#39;s vehicle ID. | [optional] 

### Return type

[**GetTanksStats200Response**](GetTanksStats200Response.md)

### Authorization

[application_id](../README.md#application_id)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

