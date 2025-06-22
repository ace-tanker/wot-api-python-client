# wot_api_client.AccountsApi

All URIs are relative to *https://api.worldoftanks.eu/wot*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_account_achievements**](AccountsApi.md#get_account_achievements) | **GET** /account/achievements/ | Player&#39;s achievements
[**get_account_info**](AccountsApi.md#get_account_info) | **GET** /account/info/ | Player personal data
[**get_account_list**](AccountsApi.md#get_account_list) | **GET** /account/list/ | Players
[**get_account_tanks**](AccountsApi.md#get_account_tanks) | **GET** /account/tanks/ | Player&#39;s vehicles


# **get_account_achievements**
> GetAccountAchievements200Response get_account_achievements(account_id, fields=fields)

Player's achievements

Method returns players' achievement details.

Achievement properties define the **achievements** field values:

 * 1-4 for Mastery Badges and Stage Achievements (type: "class");
 * maximum value of Achievement series (type: "series");
 * number of achievements earned from sections: Battle Hero, Epic Achievements, Group Achievements, Special Achievements, etc. (type: "repeatable, single, custom").


### Example

* Api Key Authentication (application_id):

```python
import wot_api_client
from wot_api_client.models.get_account_achievements200_response import GetAccountAchievements200Response
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
    api_instance = wot_api_client.AccountsApi(api_client)
    account_id = [56] # List[int] | Player account ID.
    fields = [] # List[str] | Response field. Embedded fields are separated with dots. To exclude a field, use “-” in front of its name. In case the parameter is not defined, the method returns all fields. (optional) (default to [])

    try:
        # Player's achievements
        api_response = api_instance.get_account_achievements(account_id, fields=fields)
        print("The response of AccountsApi->get_account_achievements:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountsApi->get_account_achievements: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | [**List[int]**](int.md)| Player account ID. | 
 **fields** | [**List[str]**](str.md)| Response field. Embedded fields are separated with dots. To exclude a field, use “-” in front of its name. In case the parameter is not defined, the method returns all fields. | [optional] [default to []]

### Return type

[**GetAccountAchievements200Response**](GetAccountAchievements200Response.md)

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

# **get_account_info**
> GetAccountInfo200Response get_account_info(account_id, access_token=access_token, extra=extra, fields=fields)

Player personal data

Method returns player details.

### Example

* Api Key Authentication (application_id):

```python
import wot_api_client
from wot_api_client.models.get_account_info200_response import GetAccountInfo200Response
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
    api_instance = wot_api_client.AccountsApi(api_client)
    account_id = [56] # List[int] | Player account ID.
    access_token = 'access_token_example' # str | [Access token](https://developers.wargaming.net/documentation/guide/principles/#access_token) for the private data of a user's account; can be received via the authorization method; valid within a stated time period (optional)
    extra = None # object | Extra fields that will be added to the response. (optional)
    fields = [] # List[str] | Response field. Embedded fields are separated with dots. To exclude a field, use “-” in front of its name. In case the parameter is not defined, the method returns all fields. (optional) (default to [])

    try:
        # Player personal data
        api_response = api_instance.get_account_info(account_id, access_token=access_token, extra=extra, fields=fields)
        print("The response of AccountsApi->get_account_info:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountsApi->get_account_info: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | [**List[int]**](int.md)| Player account ID. | 
 **access_token** | **str**| [Access token](https://developers.wargaming.net/documentation/guide/principles/#access_token) for the private data of a user&#39;s account; can be received via the authorization method; valid within a stated time period | [optional] 
 **extra** | [**object**](.md)| Extra fields that will be added to the response. | [optional] 
 **fields** | [**List[str]**](str.md)| Response field. Embedded fields are separated with dots. To exclude a field, use “-” in front of its name. In case the parameter is not defined, the method returns all fields. | [optional] [default to []]

### Return type

[**GetAccountInfo200Response**](GetAccountInfo200Response.md)

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

# **get_account_list**
> GetAccountList200Response get_account_list(search, fields=fields, limit=limit, type=type)

Players

Method returns partial list of players. The list is filtered by initial characters of user name and sorted alphabetically.

### Example

* Api Key Authentication (application_id):

```python
import wot_api_client
from wot_api_client.models.get_account_list200_response import GetAccountList200Response
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
    api_instance = wot_api_client.AccountsApi(api_client)
    search = 'search_example' # str | Player name search string. Parameter \"type\" defines minimum length and type of search. Using the exact search type, you can enter several names, separated with commas. Maximum length: 24.
    fields = [] # List[str] | Response field. Embedded fields are separated with dots. To exclude a field, use “-” in front of its name. In case the parameter is not defined, the method returns all fields. (optional) (default to [])
    limit = 56 # int | Number of returned entries. (optional)
    type = startswith # str | Search type. (optional) (default to startswith)

    try:
        # Players
        api_response = api_instance.get_account_list(search, fields=fields, limit=limit, type=type)
        print("The response of AccountsApi->get_account_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountsApi->get_account_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search** | **str**| Player name search string. Parameter \&quot;type\&quot; defines minimum length and type of search. Using the exact search type, you can enter several names, separated with commas. Maximum length: 24. | 
 **fields** | [**List[str]**](str.md)| Response field. Embedded fields are separated with dots. To exclude a field, use “-” in front of its name. In case the parameter is not defined, the method returns all fields. | [optional] [default to []]
 **limit** | **int**| Number of returned entries. | [optional] 
 **type** | **str**| Search type. | [optional] [default to startswith]

### Return type

[**GetAccountList200Response**](GetAccountList200Response.md)

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

# **get_account_tanks**
> GetAccountTanks200Response get_account_tanks(account_id, access_token=access_token, fields=fields, tank_id=tank_id)

Player's vehicles

Method returns details on player's vehicles.

### Example

* Api Key Authentication (application_id):

```python
import wot_api_client
from wot_api_client.models.get_account_tanks200_response import GetAccountTanks200Response
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
    api_instance = wot_api_client.AccountsApi(api_client)
    account_id = [56] # List[int] | Player account ID.
    access_token = 'access_token_example' # str | [Access token](https://developers.wargaming.net/documentation/guide/principles/#access_token) for the private data of a user's account; can be received via the authorization method; valid within a stated time period (optional)
    fields = [] # List[str] | Response field. Embedded fields are separated with dots. To exclude a field, use “-” in front of its name. In case the parameter is not defined, the method returns all fields. (optional) (default to [])
    tank_id = [56] # List[int] | Player's vehicle ID. (optional)

    try:
        # Player's vehicles
        api_response = api_instance.get_account_tanks(account_id, access_token=access_token, fields=fields, tank_id=tank_id)
        print("The response of AccountsApi->get_account_tanks:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountsApi->get_account_tanks: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | [**List[int]**](int.md)| Player account ID. | 
 **access_token** | **str**| [Access token](https://developers.wargaming.net/documentation/guide/principles/#access_token) for the private data of a user&#39;s account; can be received via the authorization method; valid within a stated time period | [optional] 
 **fields** | [**List[str]**](str.md)| Response field. Embedded fields are separated with dots. To exclude a field, use “-” in front of its name. In case the parameter is not defined, the method returns all fields. | [optional] [default to []]
 **tank_id** | [**List[int]**](int.md)| Player&#39;s vehicle ID. | [optional] 

### Return type

[**GetAccountTanks200Response**](GetAccountTanks200Response.md)

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

