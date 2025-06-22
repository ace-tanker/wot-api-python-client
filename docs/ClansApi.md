# wot_api_client.ClansApi

All URIs are relative to *https://api.worldoftanks.eu/wot*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_clans_accountinfo**](ClansApi.md#get_clans_accountinfo) | **GET** /clans/accountinfo/ | Clan member details
[**get_clans_glossary**](ClansApi.md#get_clans_glossary) | **GET** /clans/glossary/ | Clan glossary
[**get_clans_info**](ClansApi.md#get_clans_info) | **GET** /clans/info/ | Clan details
[**get_clans_list**](ClansApi.md#get_clans_list) | **GET** /clans/list/ | Clans
[**get_clans_memberhistory**](ClansApi.md#get_clans_memberhistory) | **GET** /clans/memberhistory/ | Player&#39;s clan history
[**get_clans_messageboard**](ClansApi.md#get_clans_messageboard) | **GET** /clans/messageboard/ | Message board


# **get_clans_accountinfo**
> GetClansAccountinfo200Response get_clans_accountinfo(account_id, fields=fields, language=language)

Clan member details

Method returns detailed clan member information and brief clan details.

### Example

* Api Key Authentication (application_id):

```python
import wot_api_client
from wot_api_client.models.get_clans_accountinfo200_response import GetClansAccountinfo200Response
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
    api_instance = wot_api_client.ClansApi(api_client)
    account_id = [56] # List[int] | Account ID.
    fields = [] # List[str] | Response field. Embedded fields are separated with dots. To exclude a field, use “-” in front of its name. In case the parameter is not defined, the method returns all fields. (optional) (default to [])
    language = 'language_example' # str | Localization language. (optional)

    try:
        # Clan member details
        api_response = api_instance.get_clans_accountinfo(account_id, fields=fields, language=language)
        print("The response of ClansApi->get_clans_accountinfo:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClansApi->get_clans_accountinfo: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | [**List[int]**](int.md)| Account ID. | 
 **fields** | [**List[str]**](str.md)| Response field. Embedded fields are separated with dots. To exclude a field, use “-” in front of its name. In case the parameter is not defined, the method returns all fields. | [optional] [default to []]
 **language** | **str**| Localization language. | [optional] 

### Return type

[**GetClansAccountinfo200Response**](GetClansAccountinfo200Response.md)

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

# **get_clans_glossary**
> GetClansGlossary200Response get_clans_glossary(fields=fields, language=language)

Clan glossary

Method returns information on clan entities.

### Example

* Api Key Authentication (application_id):

```python
import wot_api_client
from wot_api_client.models.get_clans_glossary200_response import GetClansGlossary200Response
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
    api_instance = wot_api_client.ClansApi(api_client)
    fields = [] # List[str] | Response field. Embedded fields are separated with dots. To exclude a field, use “-” in front of its name. In case the parameter is not defined, the method returns all fields. (optional) (default to [])
    language = 'language_example' # str | Localization language. (optional)

    try:
        # Clan glossary
        api_response = api_instance.get_clans_glossary(fields=fields, language=language)
        print("The response of ClansApi->get_clans_glossary:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClansApi->get_clans_glossary: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | [**List[str]**](str.md)| Response field. Embedded fields are separated with dots. To exclude a field, use “-” in front of its name. In case the parameter is not defined, the method returns all fields. | [optional] [default to []]
 **language** | **str**| Localization language. | [optional] 

### Return type

[**GetClansGlossary200Response**](GetClansGlossary200Response.md)

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

# **get_clans_info**
> GetClansInfo200Response get_clans_info(clan_id, access_token=access_token, extra=extra, fields=fields, language=language, members_key=members_key)

Clan details

Method returns detailed clan information.

### Example

* Api Key Authentication (application_id):

```python
import wot_api_client
from wot_api_client.models.get_clans_info200_response import GetClansInfo200Response
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
    api_instance = wot_api_client.ClansApi(api_client)
    clan_id = [56] # List[int] | Clan ID.
    access_token = 'access_token_example' # str | [Access token](https://developers.wargaming.net/documentation/guide/principles/#access_token) for the private data of a user's account; can be received via the authorization method; valid within a stated time period (optional)
    extra = None # object | Extra fields that will be added to the response. (optional)
    fields = [] # List[str] | Response field. Embedded fields are separated with dots. To exclude a field, use “-” in front of its name. In case the parameter is not defined, the method returns all fields. (optional) (default to [])
    language = 'language_example' # str | Localization language. (optional)
    members_key = 'members_key_example' # str | This parameter changes members field type. (optional)

    try:
        # Clan details
        api_response = api_instance.get_clans_info(clan_id, access_token=access_token, extra=extra, fields=fields, language=language, members_key=members_key)
        print("The response of ClansApi->get_clans_info:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClansApi->get_clans_info: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **clan_id** | [**List[int]**](int.md)| Clan ID. | 
 **access_token** | **str**| [Access token](https://developers.wargaming.net/documentation/guide/principles/#access_token) for the private data of a user&#39;s account; can be received via the authorization method; valid within a stated time period | [optional] 
 **extra** | [**object**](.md)| Extra fields that will be added to the response. | [optional] 
 **fields** | [**List[str]**](str.md)| Response field. Embedded fields are separated with dots. To exclude a field, use “-” in front of its name. In case the parameter is not defined, the method returns all fields. | [optional] [default to []]
 **language** | **str**| Localization language. | [optional] 
 **members_key** | **str**| This parameter changes members field type. | [optional] 

### Return type

[**GetClansInfo200Response**](GetClansInfo200Response.md)

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

# **get_clans_list**
> GetClansList200Response get_clans_list(fields=fields, language=language, limit=limit, page_no=page_no, search=search)

Clans

Method searches through clans and sorts them in a specified order.

### Example

* Api Key Authentication (application_id):

```python
import wot_api_client
from wot_api_client.models.get_clans_list200_response import GetClansList200Response
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
    api_instance = wot_api_client.ClansApi(api_client)
    fields = [] # List[str] | Response field. Embedded fields are separated with dots. To exclude a field, use “-” in front of its name. In case the parameter is not defined, the method returns all fields. (optional) (default to [])
    language = 'language_example' # str | Localization language. (optional)
    limit = 100 # int | Number of returned entries. (optional) (default to 100)
    page_no = 1 # int | Page number. (optional) (default to 1)
    search = 'search_example' # str | Part of name or tag for clan search. Minimum 2 characters (optional)

    try:
        # Clans
        api_response = api_instance.get_clans_list(fields=fields, language=language, limit=limit, page_no=page_no, search=search)
        print("The response of ClansApi->get_clans_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClansApi->get_clans_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | [**List[str]**](str.md)| Response field. Embedded fields are separated with dots. To exclude a field, use “-” in front of its name. In case the parameter is not defined, the method returns all fields. | [optional] [default to []]
 **language** | **str**| Localization language. | [optional] 
 **limit** | **int**| Number of returned entries. | [optional] [default to 100]
 **page_no** | **int**| Page number. | [optional] [default to 1]
 **search** | **str**| Part of name or tag for clan search. Minimum 2 characters | [optional] 

### Return type

[**GetClansList200Response**](GetClansList200Response.md)

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

# **get_clans_memberhistory**
> GetClansMemberhistory200Response get_clans_memberhistory(account_id, fields=fields, language=language)

Player's clan history

Method returns information about player's clan history. Data on 10 last clan memberships are presented in the response.<p/>This method will be removed. Use method <a href="/reference/all/wot/clans/memberhistory/">Player's clan history (World of Tanks)</a>

### Example

* Api Key Authentication (application_id):

```python
import wot_api_client
from wot_api_client.models.get_clans_memberhistory200_response import GetClansMemberhistory200Response
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
    api_instance = wot_api_client.ClansApi(api_client)
    account_id = 56 # int | Account ID.
    fields = [] # List[str] | Response field. Embedded fields are separated with dots. To exclude a field, use “-” in front of its name. In case the parameter is not defined, the method returns all fields. (optional) (default to [])
    language = 'language_example' # str | Localization language. (optional)

    try:
        # Player's clan history
        api_response = api_instance.get_clans_memberhistory(account_id, fields=fields, language=language)
        print("The response of ClansApi->get_clans_memberhistory:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClansApi->get_clans_memberhistory: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **int**| Account ID. | 
 **fields** | [**List[str]**](str.md)| Response field. Embedded fields are separated with dots. To exclude a field, use “-” in front of its name. In case the parameter is not defined, the method returns all fields. | [optional] [default to []]
 **language** | **str**| Localization language. | [optional] 

### Return type

[**GetClansMemberhistory200Response**](GetClansMemberhistory200Response.md)

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

# **get_clans_messageboard**
> GetClansMessageboard200Response get_clans_messageboard(access_token, fields=fields)

Message board

Method returns messages of clan message board.<p/>This method will be removed. Use method <a href="/reference/all/wot/clans/messageboard/">Message board (World of Tanks)</a>

### Example

* Api Key Authentication (application_id):

```python
import wot_api_client
from wot_api_client.models.get_clans_messageboard200_response import GetClansMessageboard200Response
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
    api_instance = wot_api_client.ClansApi(api_client)
    access_token = 'access_token_example' # str | [Access token](https://developers.wargaming.net/documentation/guide/principles/#access_token) for the private data of a user's account; can be received via the authorization method; valid within a stated time period
    fields = [] # List[str] | Response field. Embedded fields are separated with dots. To exclude a field, use “-” in front of its name. In case the parameter is not defined, the method returns all fields. (optional) (default to [])

    try:
        # Message board
        api_response = api_instance.get_clans_messageboard(access_token, fields=fields)
        print("The response of ClansApi->get_clans_messageboard:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClansApi->get_clans_messageboard: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_token** | **str**| [Access token](https://developers.wargaming.net/documentation/guide/principles/#access_token) for the private data of a user&#39;s account; can be received via the authorization method; valid within a stated time period | 
 **fields** | [**List[str]**](str.md)| Response field. Embedded fields are separated with dots. To exclude a field, use “-” in front of its name. In case the parameter is not defined, the method returns all fields. | [optional] [default to []]

### Return type

[**GetClansMessageboard200Response**](GetClansMessageboard200Response.md)

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

