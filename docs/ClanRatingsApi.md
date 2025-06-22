# wot_api_client.ClanRatingsApi

All URIs are relative to *https://api.worldoftanks.eu/wot*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_clanratings_clans**](ClanRatingsApi.md#get_clanratings_clans) | **GET** /clanratings/clans/ | Clan ratings
[**get_clanratings_dates**](ClanRatingsApi.md#get_clanratings_dates) | **GET** /clanratings/dates/ | Dates with available ratings
[**get_clanratings_neighbors**](ClanRatingsApi.md#get_clanratings_neighbors) | **GET** /clanratings/neighbors/ | Adjacent positions in clan rating
[**get_clanratings_top**](ClanRatingsApi.md#get_clanratings_top) | **GET** /clanratings/top/ | Top Clans
[**get_clanratings_types**](ClanRatingsApi.md#get_clanratings_types) | **GET** /clanratings/types/ | Types of ratings


# **get_clanratings_clans**
> GetClanratingsClans200Response get_clanratings_clans(clan_id, var_date=var_date, fields=fields)

Clan ratings

Method returns clan ratings by specified IDs.

### Example

* Api Key Authentication (application_id):

```python
import wot_api_client
from wot_api_client.models.get_clanratings_clans200_response import GetClanratingsClans200Response
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
    api_instance = wot_api_client.ClanRatingsApi(api_client)
    clan_id = [56] # List[int] | 
    var_date = wot_api_client.GetClanratingsClansDateParameter() # GetClanratingsClansDateParameter | Ratings calculation date. Date in UNIX timestamp or ISO 8601 format. E.g.: 1376542800 or 2013-08-15T00:00:00 (optional)
    fields = [] # List[str] | Response field. Embedded fields are separated with dots. To exclude a field, use “-” in front of its name. In case the parameter is not defined, the method returns all fields. (optional) (default to [])

    try:
        # Clan ratings
        api_response = api_instance.get_clanratings_clans(clan_id, var_date=var_date, fields=fields)
        print("The response of ClanRatingsApi->get_clanratings_clans:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClanRatingsApi->get_clanratings_clans: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **clan_id** | [**List[int]**](int.md)|  | 
 **var_date** | [**GetClanratingsClansDateParameter**](.md)| Ratings calculation date. Date in UNIX timestamp or ISO 8601 format. E.g.: 1376542800 or 2013-08-15T00:00:00 | [optional] 
 **fields** | [**List[str]**](str.md)| Response field. Embedded fields are separated with dots. To exclude a field, use “-” in front of its name. In case the parameter is not defined, the method returns all fields. | [optional] [default to []]

### Return type

[**GetClanratingsClans200Response**](GetClanratingsClans200Response.md)

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

# **get_clanratings_dates**
> GetClanratingsDates200Response get_clanratings_dates(limit=limit)

Dates with available ratings

Method returns dates with available rating data.

### Example

* Api Key Authentication (application_id):

```python
import wot_api_client
from wot_api_client.models.get_clanratings_dates200_response import GetClanratingsDates200Response
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
    api_instance = wot_api_client.ClanRatingsApi(api_client)
    limit = 7 # int |  (optional) (default to 7)

    try:
        # Dates with available ratings
        api_response = api_instance.get_clanratings_dates(limit=limit)
        print("The response of ClanRatingsApi->get_clanratings_dates:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClanRatingsApi->get_clanratings_dates: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**|  | [optional] [default to 7]

### Return type

[**GetClanratingsDates200Response**](GetClanratingsDates200Response.md)

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

# **get_clanratings_neighbors**
> GetClanratingsNeighbors200Response get_clanratings_neighbors(clan_id, rank_field, var_date=var_date, fields=fields, limit=limit)

Adjacent positions in clan rating

Method returns list of adjacent positions in specified clan rating.

### Example

* Api Key Authentication (application_id):

```python
import wot_api_client
from wot_api_client.models.get_clanratings_neighbors200_response import GetClanratingsNeighbors200Response
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
    api_instance = wot_api_client.ClanRatingsApi(api_client)
    clan_id = 56 # int | 
    rank_field = 'rank_field_example' # str | 
    var_date = wot_api_client.GetClanratingsClansDateParameter() # GetClanratingsClansDateParameter | Ratings calculation date. Date in UNIX timestamp or ISO 8601 format. E.g.: 1376542800 or 2013-08-15T00:00:00 (optional)
    fields = [] # List[str] | Response field. Embedded fields are separated with dots. To exclude a field, use “-” in front of its name. In case the parameter is not defined, the method returns all fields. (optional) (default to [])
    limit = 5 # int |  (optional) (default to 5)

    try:
        # Adjacent positions in clan rating
        api_response = api_instance.get_clanratings_neighbors(clan_id, rank_field, var_date=var_date, fields=fields, limit=limit)
        print("The response of ClanRatingsApi->get_clanratings_neighbors:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClanRatingsApi->get_clanratings_neighbors: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **clan_id** | **int**|  | 
 **rank_field** | **str**|  | 
 **var_date** | [**GetClanratingsClansDateParameter**](.md)| Ratings calculation date. Date in UNIX timestamp or ISO 8601 format. E.g.: 1376542800 or 2013-08-15T00:00:00 | [optional] 
 **fields** | [**List[str]**](str.md)| Response field. Embedded fields are separated with dots. To exclude a field, use “-” in front of its name. In case the parameter is not defined, the method returns all fields. | [optional] [default to []]
 **limit** | **int**|  | [optional] [default to 5]

### Return type

[**GetClanratingsNeighbors200Response**](GetClanratingsNeighbors200Response.md)

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

# **get_clanratings_top**
> GetClanratingsTop200Response get_clanratings_top(rank_field, var_date=var_date, fields=fields, limit=limit, page_no=page_no)

Top Clans

Method returns the list of top clans by specified parameters.

### Example

* Api Key Authentication (application_id):

```python
import wot_api_client
from wot_api_client.models.get_clanratings_top200_response import GetClanratingsTop200Response
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
    api_instance = wot_api_client.ClanRatingsApi(api_client)
    rank_field = 'rank_field_example' # str | 
    var_date = wot_api_client.GetClanratingsClansDateParameter() # GetClanratingsClansDateParameter | Ratings calculation date. Date in UNIX timestamp or ISO 8601 format. E.g.: 1376542800 or 2013-08-15T00:00:00 (optional)
    fields = [] # List[str] | Response field. Embedded fields are separated with dots. To exclude a field, use “-” in front of its name. In case the parameter is not defined, the method returns all fields. (optional) (default to [])
    limit = 10 # int |  (optional) (default to 10)
    page_no = 1 # int |  (optional) (default to 1)

    try:
        # Top Clans
        api_response = api_instance.get_clanratings_top(rank_field, var_date=var_date, fields=fields, limit=limit, page_no=page_no)
        print("The response of ClanRatingsApi->get_clanratings_top:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClanRatingsApi->get_clanratings_top: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rank_field** | **str**|  | 
 **var_date** | [**GetClanratingsClansDateParameter**](.md)| Ratings calculation date. Date in UNIX timestamp or ISO 8601 format. E.g.: 1376542800 or 2013-08-15T00:00:00 | [optional] 
 **fields** | [**List[str]**](str.md)| Response field. Embedded fields are separated with dots. To exclude a field, use “-” in front of its name. In case the parameter is not defined, the method returns all fields. | [optional] [default to []]
 **limit** | **int**|  | [optional] [default to 10]
 **page_no** | **int**|  | [optional] [default to 1]

### Return type

[**GetClanratingsTop200Response**](GetClanratingsTop200Response.md)

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

# **get_clanratings_types**
> GetClanratingsTypes200Response get_clanratings_types()

Types of ratings

Method returns details on ratings types and categories.

### Example

* Api Key Authentication (application_id):

```python
import wot_api_client
from wot_api_client.models.get_clanratings_types200_response import GetClanratingsTypes200Response
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
    api_instance = wot_api_client.ClanRatingsApi(api_client)

    try:
        # Types of ratings
        api_response = api_instance.get_clanratings_types()
        print("The response of ClanRatingsApi->get_clanratings_types:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClanRatingsApi->get_clanratings_types: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**GetClanratingsTypes200Response**](GetClanratingsTypes200Response.md)

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

