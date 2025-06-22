# wot_api_client.StrongholdsApi

All URIs are relative to *https://api.worldoftanks.eu/wot*

Method | HTTP request | Description
------------- | ------------- | -------------
[**activateclanreserve**](StrongholdsApi.md#activateclanreserve) | **POST** /stronghold/activateclanreserve/ | Activate available clan Reserve
[**get_stronghold_claninfo**](StrongholdsApi.md#get_stronghold_claninfo) | **GET** /stronghold/claninfo/ | Information about the clan&#39;s Stronghold
[**get_stronghold_clanreserves**](StrongholdsApi.md#get_stronghold_clanreserves) | **GET** /stronghold/clanreserves/ | Clan Reserves


# **activateclanreserve**
> Activateclanreserve200Response activateclanreserve(access_token, reserve_level, reserve_type, fields=fields, language=language)

Activate available clan Reserve

This method activates an available clan Reserve. A clan Reserve can be activated only by a clan member with the required permission.

### Example

* Api Key Authentication (application_id):

```python
import wot_api_client
from wot_api_client.models.activateclanreserve200_response import Activateclanreserve200Response
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
    api_instance = wot_api_client.StrongholdsApi(api_client)
    access_token = 'access_token_example' # str | [Access token](https://developers.wargaming.net/documentation/guide/principles/#access_token) for the private data of a user's account; can be received via the authorization method; valid within a stated time period
    reserve_level = 56 # int | Level of clan Reserve to be activated
    reserve_type = 'reserve_type_example' # str | Type of clan Reserve to be activated
    fields = None # object | Response field. The fields are separated with commas. Embedded fields are separated with dots. To exclude a field, use “-” in front of its name. In case the parameter is not defined, the method returns all fields. (optional)
    language = en # str | Localization language. (optional) (default to en)

    try:
        # Activate available clan Reserve
        api_response = api_instance.activateclanreserve(access_token, reserve_level, reserve_type, fields=fields, language=language)
        print("The response of StrongholdsApi->activateclanreserve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StrongholdsApi->activateclanreserve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_token** | **str**| [Access token](https://developers.wargaming.net/documentation/guide/principles/#access_token) for the private data of a user&#39;s account; can be received via the authorization method; valid within a stated time period | 
 **reserve_level** | **int**| Level of clan Reserve to be activated | 
 **reserve_type** | **str**| Type of clan Reserve to be activated | 
 **fields** | [**object**](object.md)| Response field. The fields are separated with commas. Embedded fields are separated with dots. To exclude a field, use “-” in front of its name. In case the parameter is not defined, the method returns all fields. | [optional] 
 **language** | **str**| Localization language. | [optional] [default to en]

### Return type

[**Activateclanreserve200Response**](Activateclanreserve200Response.md)

### Authorization

[application_id](../README.md#application_id)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_stronghold_claninfo**
> GetStrongholdClaninfo200Response get_stronghold_claninfo(clan_id, fields=fields, language=language)

Information about the clan's Stronghold

Method returns general information and the battle statistics of clans in the Stronghold mode. Please note that information about the number of battles fought as well as the number of defeats and victories is updated once every 24 hours.

### Example

* Api Key Authentication (application_id):

```python
import wot_api_client
from wot_api_client.models.get_stronghold_claninfo200_response import GetStrongholdClaninfo200Response
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
    api_instance = wot_api_client.StrongholdsApi(api_client)
    clan_id = [56] # List[int] | Clan ID. To get a clan ID, use the [Clans](https://developers.wargaming.net/reference/all/wgn/clans/list) method.
    fields = [] # List[str] | Response field. Embedded fields are separated with dots. To exclude a field, use “-” in front of its name. In case the parameter is not defined, the method returns all fields. (optional) (default to [])
    language = 'language_example' # str | Localization language. (optional)

    try:
        # Information about the clan's Stronghold
        api_response = api_instance.get_stronghold_claninfo(clan_id, fields=fields, language=language)
        print("The response of StrongholdsApi->get_stronghold_claninfo:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StrongholdsApi->get_stronghold_claninfo: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **clan_id** | [**List[int]**](int.md)| Clan ID. To get a clan ID, use the [Clans](https://developers.wargaming.net/reference/all/wgn/clans/list) method. | 
 **fields** | [**List[str]**](str.md)| Response field. Embedded fields are separated with dots. To exclude a field, use “-” in front of its name. In case the parameter is not defined, the method returns all fields. | [optional] [default to []]
 **language** | **str**| Localization language. | [optional] 

### Return type

[**GetStrongholdClaninfo200Response**](GetStrongholdClaninfo200Response.md)

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

# **get_stronghold_clanreserves**
> GetStrongholdClanreserves200Response get_stronghold_clanreserves(access_token, fields=fields, language=language)

Clan Reserves

Method returns information about available Reserves and their current status.

### Example

* Api Key Authentication (application_id):

```python
import wot_api_client
from wot_api_client.models.get_stronghold_clanreserves200_response import GetStrongholdClanreserves200Response
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
    api_instance = wot_api_client.StrongholdsApi(api_client)
    access_token = 'access_token_example' # str | [Access token](https://developers.wargaming.net/documentation/guide/principles/#access_token) for the private data of a user's account; can be received via the authorization method; valid within a stated time period
    fields = [] # List[str] | Response field. Embedded fields are separated with dots. To exclude a field, use “-” in front of its name. In case the parameter is not defined, the method returns all fields. (optional) (default to [])
    language = 'language_example' # str | Localization language. (optional)

    try:
        # Clan Reserves
        api_response = api_instance.get_stronghold_clanreserves(access_token, fields=fields, language=language)
        print("The response of StrongholdsApi->get_stronghold_clanreserves:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StrongholdsApi->get_stronghold_clanreserves: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_token** | **str**| [Access token](https://developers.wargaming.net/documentation/guide/principles/#access_token) for the private data of a user&#39;s account; can be received via the authorization method; valid within a stated time period | 
 **fields** | [**List[str]**](str.md)| Response field. Embedded fields are separated with dots. To exclude a field, use “-” in front of its name. In case the parameter is not defined, the method returns all fields. | [optional] [default to []]
 **language** | **str**| Localization language. | [optional] 

### Return type

[**GetStrongholdClanreserves200Response**](GetStrongholdClanreserves200Response.md)

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

