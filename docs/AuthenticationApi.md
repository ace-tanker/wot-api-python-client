# wot_api_client.AuthenticationApi

All URIs are relative to *https://api.worldoftanks.eu/wot*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_auth_login**](AuthenticationApi.md#get_auth_login) | **GET** /auth/login/ | OpenID login
[**logout**](AuthenticationApi.md#logout) | **POST** /auth/logout/ | Log out
[**prolongate**](AuthenticationApi.md#prolongate) | **POST** /auth/prolongate/ | Access Token extension


# **get_auth_login**
> GetAuthLogin200Response get_auth_login(display=display, expires_at=expires_at, nofollow=nofollow, redirect_uri=redirect_uri)

OpenID login

Method authenticates user based on Wargaming.net ID (OpenID) which is used in World of Tanks, World of Tanks Blitz, World of Warships, World of Warplanes, and WarGag.ru. To log in, player must enter email and password used for creating account, or use a social network profile.
Authentication is not available for iOS Game Center users in the following cases:
*  the account is not linked to a social network account, or
*  email and password are not specified in the profile.

Information on authorization status is sent to URL specified in **redirect_uri** parameter.

If authentication is successful, the following parameters are sent to **redirect_uri**:

*  **status: ok** — successful authentication
*  **access_token** — access token is passed in to all methods that require authentication
*  **expires_at** — expiration date of **access_token**
*  **account_id** — user ID
*  **nickname** — user name.

If authentication fails, the following parameters are sent to **redirect_uri**:

*  **status: error** — authentication error
*  **code** — error code
*  **message** — error message.

### Example

* Api Key Authentication (application_id):

```python
import wot_api_client
from wot_api_client.models.get_auth_login200_response import GetAuthLogin200Response
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
    api_instance = wot_api_client.AuthenticationApi(api_client)
    display = 'display_example' # str | Layout for mobile applications. (optional)
    expires_at = 56 # int | **Access_token** expiration time in UNIX. Delta can also be specified in seconds.  Expiration time and delta must not exceed two weeks from the current time. (optional)
    nofollow = 0 # int | If parameter **nofollow=1** is passed in, the user is not redirected. URL is returned in response. (optional) (default to 0)
    redirect_uri = 'redirect_uri_example' # str | URL where user is redirected after authentication.  By default: [{API_HOST}/blank/](https://{API_HOST}/blank/) (optional)

    try:
        # OpenID login
        api_response = api_instance.get_auth_login(display=display, expires_at=expires_at, nofollow=nofollow, redirect_uri=redirect_uri)
        print("The response of AuthenticationApi->get_auth_login:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticationApi->get_auth_login: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **display** | **str**| Layout for mobile applications. | [optional] 
 **expires_at** | **int**| **Access_token** expiration time in UNIX. Delta can also be specified in seconds.  Expiration time and delta must not exceed two weeks from the current time. | [optional] 
 **nofollow** | **int**| If parameter **nofollow&#x3D;1** is passed in, the user is not redirected. URL is returned in response. | [optional] [default to 0]
 **redirect_uri** | **str**| URL where user is redirected after authentication.  By default: [{API_HOST}/blank/](https://{API_HOST}/blank/) | [optional] 

### Return type

[**GetAuthLogin200Response**](GetAuthLogin200Response.md)

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

# **logout**
> Logout200Response logout(access_token)

Log out

Method deletes user's **access_token**.

After this method is called, **access_token** becomes invalid.

### Example

* Api Key Authentication (application_id):

```python
import wot_api_client
from wot_api_client.models.logout200_response import Logout200Response
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
    api_instance = wot_api_client.AuthenticationApi(api_client)
    access_token = 'access_token_example' # str | [Access token](https://developers.wargaming.net/documentation/guide/principles/#access_token) for the private data of a user's account; can be received via the authorization method; valid within a stated time period

    try:
        # Log out
        api_response = api_instance.logout(access_token)
        print("The response of AuthenticationApi->logout:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticationApi->logout: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_token** | **str**| [Access token](https://developers.wargaming.net/documentation/guide/principles/#access_token) for the private data of a user&#39;s account; can be received via the authorization method; valid within a stated time period | 

### Return type

[**Logout200Response**](Logout200Response.md)

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

# **prolongate**
> Prolongate200Response prolongate(access_token, expires_at=expires_at)

Access Token extension

Method generates new **access_token** based on the current token.

This method is used when the player is still using the application but the current **access_token** is about to expire.

### Example

* Api Key Authentication (application_id):

```python
import wot_api_client
from wot_api_client.models.prolongate200_response import Prolongate200Response
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
    api_instance = wot_api_client.AuthenticationApi(api_client)
    access_token = 'access_token_example' # str | [Access token](https://developers.wargaming.net/documentation/guide/principles/#access_token) for the private data of a user's account; can be received via the authorization method; valid within a stated time period
    expires_at = 56 # int | **Access_token** expiration time in UNIX. Delta can also be specified in seconds.  Expiration time and delta must not exceed two weeks from the current time. (optional)

    try:
        # Access Token extension
        api_response = api_instance.prolongate(access_token, expires_at=expires_at)
        print("The response of AuthenticationApi->prolongate:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticationApi->prolongate: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_token** | **str**| [Access token](https://developers.wargaming.net/documentation/guide/principles/#access_token) for the private data of a user&#39;s account; can be received via the authorization method; valid within a stated time period | 
 **expires_at** | **int**| **Access_token** expiration time in UNIX. Delta can also be specified in seconds.  Expiration time and delta must not exceed two weeks from the current time. | [optional] 

### Return type

[**Prolongate200Response**](Prolongate200Response.md)

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

