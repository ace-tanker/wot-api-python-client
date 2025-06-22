# wot_api_client.GlobalMapApi

All URIs are relative to *https://api.worldoftanks.eu/wot*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_globalmap_clanbattles**](GlobalMapApi.md#get_globalmap_clanbattles) | **GET** /globalmap/clanbattles/ | Clan&#39;s battles
[**get_globalmap_claninfo**](GlobalMapApi.md#get_globalmap_claninfo) | **GET** /globalmap/claninfo/ | Clan details
[**get_globalmap_clanprovinces**](GlobalMapApi.md#get_globalmap_clanprovinces) | **GET** /globalmap/clanprovinces/ | Clan&#39;s provinces
[**get_globalmap_eventaccountinfo**](GlobalMapApi.md#get_globalmap_eventaccountinfo) | **GET** /globalmap/eventaccountinfo/ | Account event information
[**get_globalmap_eventaccountratingneighbors**](GlobalMapApi.md#get_globalmap_eventaccountratingneighbors) | **GET** /globalmap/eventaccountratingneighbors/ | Adjacent positions in event account rating
[**get_globalmap_eventaccountratings**](GlobalMapApi.md#get_globalmap_eventaccountratings) | **GET** /globalmap/eventaccountratings/ | Event account rating
[**get_globalmap_eventclaninfo**](GlobalMapApi.md#get_globalmap_eventclaninfo) | **GET** /globalmap/eventclaninfo/ | Clan event information
[**get_globalmap_eventclantasks**](GlobalMapApi.md#get_globalmap_eventclantasks) | **GET** /globalmap/eventclantasks/ | Clan event missions
[**get_globalmap_eventrating**](GlobalMapApi.md#get_globalmap_eventrating) | **GET** /globalmap/eventrating/ | Event clan ratings
[**get_globalmap_eventratingneighbors**](GlobalMapApi.md#get_globalmap_eventratingneighbors) | **GET** /globalmap/eventratingneighbors/ | Adjacent position in event clan rating
[**get_globalmap_events**](GlobalMapApi.md#get_globalmap_events) | **GET** /globalmap/events/ | Events
[**get_globalmap_fronts**](GlobalMapApi.md#get_globalmap_fronts) | **GET** /globalmap/fronts/ | Fronts
[**get_globalmap_info**](GlobalMapApi.md#get_globalmap_info) | **GET** /globalmap/info/ | Map status
[**get_globalmap_provinces**](GlobalMapApi.md#get_globalmap_provinces) | **GET** /globalmap/provinces/ | Provinces
[**get_globalmap_seasonaccountinfo**](GlobalMapApi.md#get_globalmap_seasonaccountinfo) | **GET** /globalmap/seasonaccountinfo/ | Account&#39;s season data
[**get_globalmap_seasonrating**](GlobalMapApi.md#get_globalmap_seasonrating) | **GET** /globalmap/seasonrating/ | Season rating
[**get_globalmap_seasonratingneighbors**](GlobalMapApi.md#get_globalmap_seasonratingneighbors) | **GET** /globalmap/seasonratingneighbors/ | Adjacent positions in season clan rating
[**get_globalmap_seasons**](GlobalMapApi.md#get_globalmap_seasons) | **GET** /globalmap/seasons/ | Seasons


# **get_globalmap_clanbattles**
> GetGlobalmapClanbattles200Response get_globalmap_clanbattles(clan_id, fields=fields, language=language, limit=limit, page_no=page_no)

Clan's battles

Method returns list of clan's battles on the Global Map.

### Example

* Api Key Authentication (application_id):

```python
import wot_api_client
from wot_api_client.models.get_globalmap_clanbattles200_response import GetGlobalmapClanbattles200Response
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
    api_instance = wot_api_client.GlobalMapApi(api_client)
    clan_id = 56 # int | 
    fields = [] # List[str] | Response field. Embedded fields are separated with dots. To exclude a field, use “-” in front of its name. In case the parameter is not defined, the method returns all fields. (optional) (default to [])
    language = 'language_example' # str | Language. (optional)
    limit = 100 # int |  (optional) (default to 100)
    page_no = 1 # int |  (optional) (default to 1)

    try:
        # Clan's battles
        api_response = api_instance.get_globalmap_clanbattles(clan_id, fields=fields, language=language, limit=limit, page_no=page_no)
        print("The response of GlobalMapApi->get_globalmap_clanbattles:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GlobalMapApi->get_globalmap_clanbattles: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **clan_id** | **int**|  | 
 **fields** | [**List[str]**](str.md)| Response field. Embedded fields are separated with dots. To exclude a field, use “-” in front of its name. In case the parameter is not defined, the method returns all fields. | [optional] [default to []]
 **language** | **str**| Language. | [optional] 
 **limit** | **int**|  | [optional] [default to 100]
 **page_no** | **int**|  | [optional] [default to 1]

### Return type

[**GetGlobalmapClanbattles200Response**](GetGlobalmapClanbattles200Response.md)

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

# **get_globalmap_claninfo**
> GetGlobalmapClaninfo200Response get_globalmap_claninfo(clan_id, access_token=access_token, fields=fields)

Clan details

Method returns clan data on the Global Map.

### Example

* Api Key Authentication (application_id):

```python
import wot_api_client
from wot_api_client.models.get_globalmap_claninfo200_response import GetGlobalmapClaninfo200Response
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
    api_instance = wot_api_client.GlobalMapApi(api_client)
    clan_id = [56] # List[int] | 
    access_token = 'access_token_example' # str |  (optional)
    fields = [] # List[str] | Response field. Embedded fields are separated with dots. To exclude a field, use “-” in front of its name. In case the parameter is not defined, the method returns all fields. (optional) (default to [])

    try:
        # Clan details
        api_response = api_instance.get_globalmap_claninfo(clan_id, access_token=access_token, fields=fields)
        print("The response of GlobalMapApi->get_globalmap_claninfo:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GlobalMapApi->get_globalmap_claninfo: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **clan_id** | [**List[int]**](int.md)|  | 
 **access_token** | **str**|  | [optional] 
 **fields** | [**List[str]**](str.md)| Response field. Embedded fields are separated with dots. To exclude a field, use “-” in front of its name. In case the parameter is not defined, the method returns all fields. | [optional] [default to []]

### Return type

[**GetGlobalmapClaninfo200Response**](GetGlobalmapClaninfo200Response.md)

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

# **get_globalmap_clanprovinces**
> GetGlobalmapClanprovinces200Response get_globalmap_clanprovinces(clan_id, access_token=access_token, fields=fields, language=language)

Clan's provinces

Method returns lists of clans provinces.

### Example

* Api Key Authentication (application_id):

```python
import wot_api_client
from wot_api_client.models.get_globalmap_clanprovinces200_response import GetGlobalmapClanprovinces200Response
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
    api_instance = wot_api_client.GlobalMapApi(api_client)
    clan_id = [56] # List[int] | 
    access_token = 'access_token_example' # str |  (optional)
    fields = [] # List[str] | Response field. Embedded fields are separated with dots. To exclude a field, use “-” in front of its name. In case the parameter is not defined, the method returns all fields. (optional) (default to [])
    language = 'language_example' # str | Language. (optional)

    try:
        # Clan's provinces
        api_response = api_instance.get_globalmap_clanprovinces(clan_id, access_token=access_token, fields=fields, language=language)
        print("The response of GlobalMapApi->get_globalmap_clanprovinces:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GlobalMapApi->get_globalmap_clanprovinces: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **clan_id** | [**List[int]**](int.md)|  | 
 **access_token** | **str**|  | [optional] 
 **fields** | [**List[str]**](str.md)| Response field. Embedded fields are separated with dots. To exclude a field, use “-” in front of its name. In case the parameter is not defined, the method returns all fields. | [optional] [default to []]
 **language** | **str**| Language. | [optional] 

### Return type

[**GetGlobalmapClanprovinces200Response**](GetGlobalmapClanprovinces200Response.md)

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

# **get_globalmap_eventaccountinfo**
> GetGlobalmapEventaccountinfo200Response get_globalmap_eventaccountinfo(account_id, event_id, front_id, clan_id=clan_id, fields=fields)

Account event information

Method returns player's statistics for a specific event

### Example

* Api Key Authentication (application_id):

```python
import wot_api_client
from wot_api_client.models.get_globalmap_eventaccountinfo200_response import GetGlobalmapEventaccountinfo200Response
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
    api_instance = wot_api_client.GlobalMapApi(api_client)
    account_id = 56 # int | 
    event_id = 'event_id_example' # str | 
    front_id = ['front_id_example'] # List[str] | 
    clan_id = 56 # int |  (optional)
    fields = [] # List[str] | Response field. Embedded fields are separated with dots. To exclude a field, use “-” in front of its name. In case the parameter is not defined, the method returns all fields. (optional) (default to [])

    try:
        # Account event information
        api_response = api_instance.get_globalmap_eventaccountinfo(account_id, event_id, front_id, clan_id=clan_id, fields=fields)
        print("The response of GlobalMapApi->get_globalmap_eventaccountinfo:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GlobalMapApi->get_globalmap_eventaccountinfo: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **int**|  | 
 **event_id** | **str**|  | 
 **front_id** | [**List[str]**](str.md)|  | 
 **clan_id** | **int**|  | [optional] 
 **fields** | [**List[str]**](str.md)| Response field. Embedded fields are separated with dots. To exclude a field, use “-” in front of its name. In case the parameter is not defined, the method returns all fields. | [optional] [default to []]

### Return type

[**GetGlobalmapEventaccountinfo200Response**](GetGlobalmapEventaccountinfo200Response.md)

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

# **get_globalmap_eventaccountratingneighbors**
> GetGlobalmapEventaccountratings200Response get_globalmap_eventaccountratingneighbors(account_id, event_id, front_id, fields=fields, limit=limit, neighbours_count=neighbours_count, page_no=page_no)

Adjacent positions in event account rating

Method returns adjacent position in account event rating.

### Example

* Api Key Authentication (application_id):

```python
import wot_api_client
from wot_api_client.models.get_globalmap_eventaccountratings200_response import GetGlobalmapEventaccountratings200Response
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
    api_instance = wot_api_client.GlobalMapApi(api_client)
    account_id = 56 # int | 
    event_id = 'event_id_example' # str | 
    front_id = 'front_id_example' # str | 
    fields = [] # List[str] | Response field. Embedded fields are separated with dots. To exclude a field, use “-” in front of its name. In case the parameter is not defined, the method returns all fields. (optional) (default to [])
    limit = 20 # int |  (optional) (default to 20)
    neighbours_count = 3 # int |  (optional) (default to 3)
    page_no = 1 # int |  (optional) (default to 1)

    try:
        # Adjacent positions in event account rating
        api_response = api_instance.get_globalmap_eventaccountratingneighbors(account_id, event_id, front_id, fields=fields, limit=limit, neighbours_count=neighbours_count, page_no=page_no)
        print("The response of GlobalMapApi->get_globalmap_eventaccountratingneighbors:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GlobalMapApi->get_globalmap_eventaccountratingneighbors: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **int**|  | 
 **event_id** | **str**|  | 
 **front_id** | **str**|  | 
 **fields** | [**List[str]**](str.md)| Response field. Embedded fields are separated with dots. To exclude a field, use “-” in front of its name. In case the parameter is not defined, the method returns all fields. | [optional] [default to []]
 **limit** | **int**|  | [optional] [default to 20]
 **neighbours_count** | **int**|  | [optional] [default to 3]
 **page_no** | **int**|  | [optional] [default to 1]

### Return type

[**GetGlobalmapEventaccountratings200Response**](GetGlobalmapEventaccountratings200Response.md)

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

# **get_globalmap_eventaccountratings**
> GetGlobalmapEventaccountratings200Response get_globalmap_eventaccountratings(event_id, front_id, fields=fields, in_rating=in_rating, limit=limit, page_no=page_no)

Event account rating

Method returns account event rating.

### Example

* Api Key Authentication (application_id):

```python
import wot_api_client
from wot_api_client.models.get_globalmap_eventaccountratings200_response import GetGlobalmapEventaccountratings200Response
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
    api_instance = wot_api_client.GlobalMapApi(api_client)
    event_id = 'event_id_example' # str | 
    front_id = 'front_id_example' # str | 
    fields = [] # List[str] | Response field. Embedded fields are separated with dots. To exclude a field, use “-” in front of its name. In case the parameter is not defined, the method returns all fields. (optional) (default to [])
    in_rating = 0 # int |  (optional) (default to 0)
    limit = 20 # int |  (optional) (default to 20)
    page_no = 1 # int |  (optional) (default to 1)

    try:
        # Event account rating
        api_response = api_instance.get_globalmap_eventaccountratings(event_id, front_id, fields=fields, in_rating=in_rating, limit=limit, page_no=page_no)
        print("The response of GlobalMapApi->get_globalmap_eventaccountratings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GlobalMapApi->get_globalmap_eventaccountratings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **event_id** | **str**|  | 
 **front_id** | **str**|  | 
 **fields** | [**List[str]**](str.md)| Response field. Embedded fields are separated with dots. To exclude a field, use “-” in front of its name. In case the parameter is not defined, the method returns all fields. | [optional] [default to []]
 **in_rating** | **int**|  | [optional] [default to 0]
 **limit** | **int**|  | [optional] [default to 20]
 **page_no** | **int**|  | [optional] [default to 1]

### Return type

[**GetGlobalmapEventaccountratings200Response**](GetGlobalmapEventaccountratings200Response.md)

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

# **get_globalmap_eventclaninfo**
> GetGlobalmapEventclaninfo200Response get_globalmap_eventclaninfo(clan_id, event_id, front_id, fields=fields)

Clan event information

Method returns clan's statistics for a specific event.

### Example

* Api Key Authentication (application_id):

```python
import wot_api_client
from wot_api_client.models.get_globalmap_eventclaninfo200_response import GetGlobalmapEventclaninfo200Response
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
    api_instance = wot_api_client.GlobalMapApi(api_client)
    clan_id = 56 # int | 
    event_id = 'event_id_example' # str | 
    front_id = ['front_id_example'] # List[str] | 
    fields = [] # List[str] | Response field. Embedded fields are separated with dots. To exclude a field, use “-” in front of its name. In case the parameter is not defined, the method returns all fields. (optional) (default to [])

    try:
        # Clan event information
        api_response = api_instance.get_globalmap_eventclaninfo(clan_id, event_id, front_id, fields=fields)
        print("The response of GlobalMapApi->get_globalmap_eventclaninfo:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GlobalMapApi->get_globalmap_eventclaninfo: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **clan_id** | **int**|  | 
 **event_id** | **str**|  | 
 **front_id** | [**List[str]**](str.md)|  | 
 **fields** | [**List[str]**](str.md)| Response field. Embedded fields are separated with dots. To exclude a field, use “-” in front of its name. In case the parameter is not defined, the method returns all fields. | [optional] [default to []]

### Return type

[**GetGlobalmapEventclaninfo200Response**](GetGlobalmapEventclaninfo200Response.md)

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

# **get_globalmap_eventclantasks**
> GetGlobalmapEventclantasks200Response get_globalmap_eventclantasks(clan_id, event_id, fields=fields, language=language, limit=limit, page_no=page_no)

Clan event missions

Method returns clan's missions for a specific event.

### Example

* Api Key Authentication (application_id):

```python
import wot_api_client
from wot_api_client.models.get_globalmap_eventclantasks200_response import GetGlobalmapEventclantasks200Response
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
    api_instance = wot_api_client.GlobalMapApi(api_client)
    clan_id = 56 # int | 
    event_id = 'event_id_example' # str | 
    fields = [] # List[str] | Response field. Embedded fields are separated with dots. To exclude a field, use “-” in front of its name. In case the parameter is not defined, the method returns all fields. (optional) (default to [])
    language = 'language_example' # str | Language. (optional)
    limit = 5 # int |  (optional) (default to 5)
    page_no = 1 # int |  (optional) (default to 1)

    try:
        # Clan event missions
        api_response = api_instance.get_globalmap_eventclantasks(clan_id, event_id, fields=fields, language=language, limit=limit, page_no=page_no)
        print("The response of GlobalMapApi->get_globalmap_eventclantasks:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GlobalMapApi->get_globalmap_eventclantasks: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **clan_id** | **int**|  | 
 **event_id** | **str**|  | 
 **fields** | [**List[str]**](str.md)| Response field. Embedded fields are separated with dots. To exclude a field, use “-” in front of its name. In case the parameter is not defined, the method returns all fields. | [optional] [default to []]
 **language** | **str**| Language. | [optional] 
 **limit** | **int**|  | [optional] [default to 5]
 **page_no** | **int**|  | [optional] [default to 1]

### Return type

[**GetGlobalmapEventclantasks200Response**](GetGlobalmapEventclantasks200Response.md)

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

# **get_globalmap_eventrating**
> GetGlobalmapEventrating200Response get_globalmap_eventrating(event_id, front_id, fields=fields, limit=limit, page_no=page_no)

Event clan ratings

Method returns event clan rating

### Example

* Api Key Authentication (application_id):

```python
import wot_api_client
from wot_api_client.models.get_globalmap_eventrating200_response import GetGlobalmapEventrating200Response
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
    api_instance = wot_api_client.GlobalMapApi(api_client)
    event_id = 'event_id_example' # str | 
    front_id = 'front_id_example' # str | 
    fields = [] # List[str] | Response field. Embedded fields are separated with dots. To exclude a field, use “-” in front of its name. In case the parameter is not defined, the method returns all fields. (optional) (default to [])
    limit = 10 # int |  (optional) (default to 10)
    page_no = 1 # int |  (optional) (default to 1)

    try:
        # Event clan ratings
        api_response = api_instance.get_globalmap_eventrating(event_id, front_id, fields=fields, limit=limit, page_no=page_no)
        print("The response of GlobalMapApi->get_globalmap_eventrating:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GlobalMapApi->get_globalmap_eventrating: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **event_id** | **str**|  | 
 **front_id** | **str**|  | 
 **fields** | [**List[str]**](str.md)| Response field. Embedded fields are separated with dots. To exclude a field, use “-” in front of its name. In case the parameter is not defined, the method returns all fields. | [optional] [default to []]
 **limit** | **int**|  | [optional] [default to 10]
 **page_no** | **int**|  | [optional] [default to 1]

### Return type

[**GetGlobalmapEventrating200Response**](GetGlobalmapEventrating200Response.md)

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

# **get_globalmap_eventratingneighbors**
> GetGlobalmapEventratingneighbors200Response get_globalmap_eventratingneighbors(clan_id, event_id, front_id, fields=fields, limit=limit)

Adjacent position in event clan rating

Method returns list of adjacent positions in event clan rating

### Example

* Api Key Authentication (application_id):

```python
import wot_api_client
from wot_api_client.models.get_globalmap_eventratingneighbors200_response import GetGlobalmapEventratingneighbors200Response
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
    api_instance = wot_api_client.GlobalMapApi(api_client)
    clan_id = 56 # int | 
    event_id = 'event_id_example' # str | 
    front_id = 'front_id_example' # str | 
    fields = [] # List[str] | Response field. Embedded fields are separated with dots. To exclude a field, use “-” in front of its name. In case the parameter is not defined, the method returns all fields. (optional) (default to [])
    limit = 10 # int |  (optional) (default to 10)

    try:
        # Adjacent position in event clan rating
        api_response = api_instance.get_globalmap_eventratingneighbors(clan_id, event_id, front_id, fields=fields, limit=limit)
        print("The response of GlobalMapApi->get_globalmap_eventratingneighbors:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GlobalMapApi->get_globalmap_eventratingneighbors: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **clan_id** | **int**|  | 
 **event_id** | **str**|  | 
 **front_id** | **str**|  | 
 **fields** | [**List[str]**](str.md)| Response field. Embedded fields are separated with dots. To exclude a field, use “-” in front of its name. In case the parameter is not defined, the method returns all fields. | [optional] [default to []]
 **limit** | **int**|  | [optional] [default to 10]

### Return type

[**GetGlobalmapEventratingneighbors200Response**](GetGlobalmapEventratingneighbors200Response.md)

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

# **get_globalmap_events**
> GetGlobalmapEvents200Response get_globalmap_events(event_id=event_id, fields=fields, language=language, limit=limit, page_no=page_no, status=status)

Events

Method returns events information.

### Example

* Api Key Authentication (application_id):

```python
import wot_api_client
from wot_api_client.models.get_globalmap_events200_response import GetGlobalmapEvents200Response
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
    api_instance = wot_api_client.GlobalMapApi(api_client)
    event_id = 'event_id_example' # str |  (optional)
    fields = [] # List[str] | Response field. Embedded fields are separated with dots. To exclude a field, use “-” in front of its name. In case the parameter is not defined, the method returns all fields. (optional) (default to [])
    language = 'language_example' # str | Language. (optional)
    limit = 5 # int |  (optional) (default to 5)
    page_no = 1 # int |  (optional) (default to 1)
    status = 'status_example' # str |  (optional)

    try:
        # Events
        api_response = api_instance.get_globalmap_events(event_id=event_id, fields=fields, language=language, limit=limit, page_no=page_no, status=status)
        print("The response of GlobalMapApi->get_globalmap_events:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GlobalMapApi->get_globalmap_events: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **event_id** | **str**|  | [optional] 
 **fields** | [**List[str]**](str.md)| Response field. Embedded fields are separated with dots. To exclude a field, use “-” in front of its name. In case the parameter is not defined, the method returns all fields. | [optional] [default to []]
 **language** | **str**| Language. | [optional] 
 **limit** | **int**|  | [optional] [default to 5]
 **page_no** | **int**|  | [optional] [default to 1]
 **status** | **str**|  | [optional] 

### Return type

[**GetGlobalmapEvents200Response**](GetGlobalmapEvents200Response.md)

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

# **get_globalmap_fronts**
> GetGlobalmapFronts200Response get_globalmap_fronts(fields=fields, front_id=front_id, language=language, limit=limit, page_no=page_no)

Fronts

Method returns information about the Global Map Fronts.

### Example

* Api Key Authentication (application_id):

```python
import wot_api_client
from wot_api_client.models.get_globalmap_fronts200_response import GetGlobalmapFronts200Response
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
    api_instance = wot_api_client.GlobalMapApi(api_client)
    fields = [] # List[str] | Response field. Embedded fields are separated with dots. To exclude a field, use “-” in front of its name. In case the parameter is not defined, the method returns all fields. (optional) (default to [])
    front_id = ['front_id_example'] # List[str] |  (optional)
    language = 'language_example' # str | Language. (optional)
    limit = 100 # int |  (optional) (default to 100)
    page_no = 1 # int |  (optional) (default to 1)

    try:
        # Fronts
        api_response = api_instance.get_globalmap_fronts(fields=fields, front_id=front_id, language=language, limit=limit, page_no=page_no)
        print("The response of GlobalMapApi->get_globalmap_fronts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GlobalMapApi->get_globalmap_fronts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | [**List[str]**](str.md)| Response field. Embedded fields are separated with dots. To exclude a field, use “-” in front of its name. In case the parameter is not defined, the method returns all fields. | [optional] [default to []]
 **front_id** | [**List[str]**](str.md)|  | [optional] 
 **language** | **str**| Language. | [optional] 
 **limit** | **int**|  | [optional] [default to 100]
 **page_no** | **int**|  | [optional] [default to 1]

### Return type

[**GetGlobalmapFronts200Response**](GetGlobalmapFronts200Response.md)

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

# **get_globalmap_info**
> GetGlobalmapInfo200Response get_globalmap_info(fields=fields)

Map status

Method returns general information about the Global Map.

### Example

* Api Key Authentication (application_id):

```python
import wot_api_client
from wot_api_client.models.get_globalmap_info200_response import GetGlobalmapInfo200Response
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
    api_instance = wot_api_client.GlobalMapApi(api_client)
    fields = [] # List[str] | Response field. Embedded fields are separated with dots. To exclude a field, use “-” in front of its name. In case the parameter is not defined, the method returns all fields. (optional) (default to [])

    try:
        # Map status
        api_response = api_instance.get_globalmap_info(fields=fields)
        print("The response of GlobalMapApi->get_globalmap_info:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GlobalMapApi->get_globalmap_info: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | [**List[str]**](str.md)| Response field. Embedded fields are separated with dots. To exclude a field, use “-” in front of its name. In case the parameter is not defined, the method returns all fields. | [optional] [default to []]

### Return type

[**GetGlobalmapInfo200Response**](GetGlobalmapInfo200Response.md)

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

# **get_globalmap_provinces**
> GetGlobalmapProvinces200Response get_globalmap_provinces(front_id, arena_id=arena_id, daily_revenue_gte=daily_revenue_gte, daily_revenue_lte=daily_revenue_lte, fields=fields, landing_type=landing_type, language=language, limit=limit, order_by=order_by, page_no=page_no, prime_hour=prime_hour, province_id=province_id)

Provinces

Method returns information about the Global Map provinces.

### Example

* Api Key Authentication (application_id):

```python
import wot_api_client
from wot_api_client.models.get_globalmap_provinces200_response import GetGlobalmapProvinces200Response
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
    api_instance = wot_api_client.GlobalMapApi(api_client)
    front_id = 'front_id_example' # str | 
    arena_id = 'arena_id_example' # str |  (optional)
    daily_revenue_gte = 56 # int |  (optional)
    daily_revenue_lte = 56 # int |  (optional)
    fields = [] # List[str] | Response field. Embedded fields are separated with dots. To exclude a field, use “-” in front of its name. In case the parameter is not defined, the method returns all fields. (optional) (default to [])
    landing_type = 'landing_type_example' # str |  (optional)
    language = 'language_example' # str | Language. (optional)
    limit = 100 # int |  (optional) (default to 100)
    order_by = 'order_by_example' # str |  (optional)
    page_no = 1 # int |  (optional) (default to 1)
    prime_hour = 56 # int |  (optional)
    province_id = ['province_id_example'] # List[str] |  (optional)

    try:
        # Provinces
        api_response = api_instance.get_globalmap_provinces(front_id, arena_id=arena_id, daily_revenue_gte=daily_revenue_gte, daily_revenue_lte=daily_revenue_lte, fields=fields, landing_type=landing_type, language=language, limit=limit, order_by=order_by, page_no=page_no, prime_hour=prime_hour, province_id=province_id)
        print("The response of GlobalMapApi->get_globalmap_provinces:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GlobalMapApi->get_globalmap_provinces: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **front_id** | **str**|  | 
 **arena_id** | **str**|  | [optional] 
 **daily_revenue_gte** | **int**|  | [optional] 
 **daily_revenue_lte** | **int**|  | [optional] 
 **fields** | [**List[str]**](str.md)| Response field. Embedded fields are separated with dots. To exclude a field, use “-” in front of its name. In case the parameter is not defined, the method returns all fields. | [optional] [default to []]
 **landing_type** | **str**|  | [optional] 
 **language** | **str**| Language. | [optional] 
 **limit** | **int**|  | [optional] [default to 100]
 **order_by** | **str**|  | [optional] 
 **page_no** | **int**|  | [optional] [default to 1]
 **prime_hour** | **int**|  | [optional] 
 **province_id** | [**List[str]**](str.md)|  | [optional] 

### Return type

[**GetGlobalmapProvinces200Response**](GetGlobalmapProvinces200Response.md)

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

# **get_globalmap_seasonaccountinfo**
> GetGlobalmapSeasonaccountinfo200Response get_globalmap_seasonaccountinfo(account_id, season_id, vehicle_level, fields=fields)

Account's season data

Method returns player's statistics for a specific season.

### Example

* Api Key Authentication (application_id):

```python
import wot_api_client
from wot_api_client.models.get_globalmap_seasonaccountinfo200_response import GetGlobalmapSeasonaccountinfo200Response
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
    api_instance = wot_api_client.GlobalMapApi(api_client)
    account_id = 56 # int | 
    season_id = 'season_id_example' # str | 
    vehicle_level = ['vehicle_level_example'] # List[str] | 
    fields = [] # List[str] | Response field. Embedded fields are separated with dots. To exclude a field, use “-” in front of its name. In case the parameter is not defined, the method returns all fields. (optional) (default to [])

    try:
        # Account's season data
        api_response = api_instance.get_globalmap_seasonaccountinfo(account_id, season_id, vehicle_level, fields=fields)
        print("The response of GlobalMapApi->get_globalmap_seasonaccountinfo:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GlobalMapApi->get_globalmap_seasonaccountinfo: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **int**|  | 
 **season_id** | **str**|  | 
 **vehicle_level** | [**List[str]**](str.md)|  | 
 **fields** | [**List[str]**](str.md)| Response field. Embedded fields are separated with dots. To exclude a field, use “-” in front of its name. In case the parameter is not defined, the method returns all fields. | [optional] [default to []]

### Return type

[**GetGlobalmapSeasonaccountinfo200Response**](GetGlobalmapSeasonaccountinfo200Response.md)

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

# **get_globalmap_seasonrating**
> GetGlobalmapSeasonrating200Response get_globalmap_seasonrating(season_id, vehicle_level, fields=fields, limit=limit, page_no=page_no)

Season rating

Method returns season clan rating.

### Example

* Api Key Authentication (application_id):

```python
import wot_api_client
from wot_api_client.models.get_globalmap_seasonrating200_response import GetGlobalmapSeasonrating200Response
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
    api_instance = wot_api_client.GlobalMapApi(api_client)
    season_id = 'season_id_example' # str | 
    vehicle_level = 'vehicle_level_example' # str | 
    fields = [] # List[str] | Response field. Embedded fields are separated with dots. To exclude a field, use “-” in front of its name. In case the parameter is not defined, the method returns all fields. (optional) (default to [])
    limit = 10 # int |  (optional) (default to 10)
    page_no = 1 # int |  (optional) (default to 1)

    try:
        # Season rating
        api_response = api_instance.get_globalmap_seasonrating(season_id, vehicle_level, fields=fields, limit=limit, page_no=page_no)
        print("The response of GlobalMapApi->get_globalmap_seasonrating:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GlobalMapApi->get_globalmap_seasonrating: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **season_id** | **str**|  | 
 **vehicle_level** | **str**|  | 
 **fields** | [**List[str]**](str.md)| Response field. Embedded fields are separated with dots. To exclude a field, use “-” in front of its name. In case the parameter is not defined, the method returns all fields. | [optional] [default to []]
 **limit** | **int**|  | [optional] [default to 10]
 **page_no** | **int**|  | [optional] [default to 1]

### Return type

[**GetGlobalmapSeasonrating200Response**](GetGlobalmapSeasonrating200Response.md)

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

# **get_globalmap_seasonratingneighbors**
> GetGlobalmapSeasonratingneighbors200Response get_globalmap_seasonratingneighbors(clan_id, season_id, vehicle_level, fields=fields, limit=limit)

Adjacent positions in season clan rating

Method returns list of adjacent positions in season clan rating.

### Example

* Api Key Authentication (application_id):

```python
import wot_api_client
from wot_api_client.models.get_globalmap_seasonratingneighbors200_response import GetGlobalmapSeasonratingneighbors200Response
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
    api_instance = wot_api_client.GlobalMapApi(api_client)
    clan_id = 56 # int | 
    season_id = 'season_id_example' # str | 
    vehicle_level = 'vehicle_level_example' # str | 
    fields = [] # List[str] | Response field. Embedded fields are separated with dots. To exclude a field, use “-” in front of its name. In case the parameter is not defined, the method returns all fields. (optional) (default to [])
    limit = 10 # int |  (optional) (default to 10)

    try:
        # Adjacent positions in season clan rating
        api_response = api_instance.get_globalmap_seasonratingneighbors(clan_id, season_id, vehicle_level, fields=fields, limit=limit)
        print("The response of GlobalMapApi->get_globalmap_seasonratingneighbors:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GlobalMapApi->get_globalmap_seasonratingneighbors: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **clan_id** | **int**|  | 
 **season_id** | **str**|  | 
 **vehicle_level** | **str**|  | 
 **fields** | [**List[str]**](str.md)| Response field. Embedded fields are separated with dots. To exclude a field, use “-” in front of its name. In case the parameter is not defined, the method returns all fields. | [optional] [default to []]
 **limit** | **int**|  | [optional] [default to 10]

### Return type

[**GetGlobalmapSeasonratingneighbors200Response**](GetGlobalmapSeasonratingneighbors200Response.md)

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

# **get_globalmap_seasons**
> GetGlobalmapSeasons200Response get_globalmap_seasons(fields=fields, language=language, limit=limit, page_no=page_no, season_id=season_id, status=status)

Seasons

Method returns information about seasons.

### Example

* Api Key Authentication (application_id):

```python
import wot_api_client
from wot_api_client.models.get_globalmap_seasons200_response import GetGlobalmapSeasons200Response
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
    api_instance = wot_api_client.GlobalMapApi(api_client)
    fields = [] # List[str] | Response field. Embedded fields are separated with dots. To exclude a field, use “-” in front of its name. In case the parameter is not defined, the method returns all fields. (optional) (default to [])
    language = 'language_example' # str | Language. (optional)
    limit = 5 # int |  (optional) (default to 5)
    page_no = 1 # int |  (optional) (default to 1)
    season_id = 'season_id_example' # str |  (optional)
    status = 'status_example' # str |  (optional)

    try:
        # Seasons
        api_response = api_instance.get_globalmap_seasons(fields=fields, language=language, limit=limit, page_no=page_no, season_id=season_id, status=status)
        print("The response of GlobalMapApi->get_globalmap_seasons:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GlobalMapApi->get_globalmap_seasons: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | [**List[str]**](str.md)| Response field. Embedded fields are separated with dots. To exclude a field, use “-” in front of its name. In case the parameter is not defined, the method returns all fields. | [optional] [default to []]
 **language** | **str**| Language. | [optional] 
 **limit** | **int**|  | [optional] [default to 5]
 **page_no** | **int**|  | [optional] [default to 1]
 **season_id** | **str**|  | [optional] 
 **status** | **str**|  | [optional] 

### Return type

[**GetGlobalmapSeasons200Response**](GetGlobalmapSeasons200Response.md)

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

