# wot_api_client.TankopediaApi

All URIs are relative to *https://api.worldoftanks.eu/wot*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_encyclopedia_achievements**](TankopediaApi.md#get_encyclopedia_achievements) | **GET** /encyclopedia/achievements/ | Achievements
[**get_encyclopedia_arenas**](TankopediaApi.md#get_encyclopedia_arenas) | **GET** /encyclopedia/arenas/ | Maps
[**get_encyclopedia_badges**](TankopediaApi.md#get_encyclopedia_badges) | **GET** /encyclopedia/badges/ | Badges
[**get_encyclopedia_boosters**](TankopediaApi.md#get_encyclopedia_boosters) | **GET** /encyclopedia/boosters/ | Personal Reserves
[**get_encyclopedia_crewroles**](TankopediaApi.md#get_encyclopedia_crewroles) | **GET** /encyclopedia/crewroles/ | Crew qualifications
[**get_encyclopedia_crewskills**](TankopediaApi.md#get_encyclopedia_crewskills) | **GET** /encyclopedia/crewskills/ | Crew skills
[**get_encyclopedia_info**](TankopediaApi.md#get_encyclopedia_info) | **GET** /encyclopedia/info/ | Tankopedia information
[**get_encyclopedia_modules**](TankopediaApi.md#get_encyclopedia_modules) | **GET** /encyclopedia/modules/ | Modules
[**get_encyclopedia_personalmissions**](TankopediaApi.md#get_encyclopedia_personalmissions) | **GET** /encyclopedia/personalmissions/ | Personal Missions
[**get_encyclopedia_provisions**](TankopediaApi.md#get_encyclopedia_provisions) | **GET** /encyclopedia/provisions/ | Equipment and Consumables
[**get_encyclopedia_vehicleprofile**](TankopediaApi.md#get_encyclopedia_vehicleprofile) | **GET** /encyclopedia/vehicleprofile/ | Vehicle characteristics
[**get_encyclopedia_vehicleprofiles**](TankopediaApi.md#get_encyclopedia_vehicleprofiles) | **GET** /encyclopedia/vehicleprofiles/ | Vehicle configurations
[**get_encyclopedia_vehicles**](TankopediaApi.md#get_encyclopedia_vehicles) | **GET** /encyclopedia/vehicles/ | Vehicles


# **get_encyclopedia_achievements**
> GetEncyclopediaAchievements200Response get_encyclopedia_achievements(fields=fields, language=language)

Achievements

Method returns information about achievements.

### Example

* Api Key Authentication (application_id):

```python
import wot_api_client
from wot_api_client.models.get_encyclopedia_achievements200_response import GetEncyclopediaAchievements200Response
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
    api_instance = wot_api_client.TankopediaApi(api_client)
    fields = [] # List[str] | Response field. Embedded fields are separated with dots. To exclude a field, use “-” in front of its name. In case the parameter is not defined, the method returns all fields. (optional) (default to [])
    language = 'language_example' # str | Localization language. (optional)

    try:
        # Achievements
        api_response = api_instance.get_encyclopedia_achievements(fields=fields, language=language)
        print("The response of TankopediaApi->get_encyclopedia_achievements:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TankopediaApi->get_encyclopedia_achievements: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | [**List[str]**](str.md)| Response field. Embedded fields are separated with dots. To exclude a field, use “-” in front of its name. In case the parameter is not defined, the method returns all fields. | [optional] [default to []]
 **language** | **str**| Localization language. | [optional] 

### Return type

[**GetEncyclopediaAchievements200Response**](GetEncyclopediaAchievements200Response.md)

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

# **get_encyclopedia_arenas**
> GetEncyclopediaArenas200Response get_encyclopedia_arenas(fields=fields, language=language)

Maps

Method returns information about maps.

### Example

* Api Key Authentication (application_id):

```python
import wot_api_client
from wot_api_client.models.get_encyclopedia_arenas200_response import GetEncyclopediaArenas200Response
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
    api_instance = wot_api_client.TankopediaApi(api_client)
    fields = [] # List[str] | Response field. Embedded fields are separated with dots. To exclude a field, use “-” in front of its name. In case the parameter is not defined, the method returns all fields. (optional) (default to [])
    language = 'language_example' # str | Localization language. (optional)

    try:
        # Maps
        api_response = api_instance.get_encyclopedia_arenas(fields=fields, language=language)
        print("The response of TankopediaApi->get_encyclopedia_arenas:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TankopediaApi->get_encyclopedia_arenas: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | [**List[str]**](str.md)| Response field. Embedded fields are separated with dots. To exclude a field, use “-” in front of its name. In case the parameter is not defined, the method returns all fields. | [optional] [default to []]
 **language** | **str**| Localization language. | [optional] 

### Return type

[**GetEncyclopediaArenas200Response**](GetEncyclopediaArenas200Response.md)

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

# **get_encyclopedia_badges**
> GetEncyclopediaBadges200Response get_encyclopedia_badges(fields=fields, language=language)

Badges

Method returns list of available badges a player can gain in Ranked Battles.

### Example

* Api Key Authentication (application_id):

```python
import wot_api_client
from wot_api_client.models.get_encyclopedia_badges200_response import GetEncyclopediaBadges200Response
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
    api_instance = wot_api_client.TankopediaApi(api_client)
    fields = [] # List[str] | Response field. Embedded fields are separated with dots. To exclude a field, use “-” in front of its name. In case the parameter is not defined, the method returns all fields. (optional) (default to [])
    language = 'language_example' # str | Localization language. (optional)

    try:
        # Badges
        api_response = api_instance.get_encyclopedia_badges(fields=fields, language=language)
        print("The response of TankopediaApi->get_encyclopedia_badges:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TankopediaApi->get_encyclopedia_badges: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | [**List[str]**](str.md)| Response field. Embedded fields are separated with dots. To exclude a field, use “-” in front of its name. In case the parameter is not defined, the method returns all fields. | [optional] [default to []]
 **language** | **str**| Localization language. | [optional] 

### Return type

[**GetEncyclopediaBadges200Response**](GetEncyclopediaBadges200Response.md)

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

# **get_encyclopedia_boosters**
> GetEncyclopediaBoosters200Response get_encyclopedia_boosters(fields=fields, language=language)

Personal Reserves

Method returns information about Personal Reserves.

### Example

* Api Key Authentication (application_id):

```python
import wot_api_client
from wot_api_client.models.get_encyclopedia_boosters200_response import GetEncyclopediaBoosters200Response
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
    api_instance = wot_api_client.TankopediaApi(api_client)
    fields = [] # List[str] | Response field. Embedded fields are separated with dots. To exclude a field, use “-” in front of its name. In case the parameter is not defined, the method returns all fields. (optional) (default to [])
    language = 'language_example' # str | Localization language. (optional)

    try:
        # Personal Reserves
        api_response = api_instance.get_encyclopedia_boosters(fields=fields, language=language)
        print("The response of TankopediaApi->get_encyclopedia_boosters:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TankopediaApi->get_encyclopedia_boosters: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | [**List[str]**](str.md)| Response field. Embedded fields are separated with dots. To exclude a field, use “-” in front of its name. In case the parameter is not defined, the method returns all fields. | [optional] [default to []]
 **language** | **str**| Localization language. | [optional] 

### Return type

[**GetEncyclopediaBoosters200Response**](GetEncyclopediaBoosters200Response.md)

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

# **get_encyclopedia_crewroles**
> GetEncyclopediaCrewroles200Response get_encyclopedia_crewroles(fields=fields, language=language, role=role)

Crew qualifications

Method returns full description of all crew qualifications.

### Example

* Api Key Authentication (application_id):

```python
import wot_api_client
from wot_api_client.models.get_encyclopedia_crewroles200_response import GetEncyclopediaCrewroles200Response
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
    api_instance = wot_api_client.TankopediaApi(api_client)
    fields = [] # List[str] | Response field. Embedded fields are separated with dots. To exclude a field, use “-” in front of its name. In case the parameter is not defined, the method returns all fields. (optional) (default to [])
    language = 'language_example' # str | Localization language. (optional)
    role = ['role_example'] # List[str] |  (optional)

    try:
        # Crew qualifications
        api_response = api_instance.get_encyclopedia_crewroles(fields=fields, language=language, role=role)
        print("The response of TankopediaApi->get_encyclopedia_crewroles:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TankopediaApi->get_encyclopedia_crewroles: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | [**List[str]**](str.md)| Response field. Embedded fields are separated with dots. To exclude a field, use “-” in front of its name. In case the parameter is not defined, the method returns all fields. | [optional] [default to []]
 **language** | **str**| Localization language. | [optional] 
 **role** | [**List[str]**](str.md)|  | [optional] 

### Return type

[**GetEncyclopediaCrewroles200Response**](GetEncyclopediaCrewroles200Response.md)

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

# **get_encyclopedia_crewskills**
> GetEncyclopediaCrewskills200Response get_encyclopedia_crewskills(fields=fields, language=language, role=role, skill=skill)

Crew skills

Method returns full description of all crew skills.

### Example

* Api Key Authentication (application_id):

```python
import wot_api_client
from wot_api_client.models.get_encyclopedia_crewskills200_response import GetEncyclopediaCrewskills200Response
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
    api_instance = wot_api_client.TankopediaApi(api_client)
    fields = [] # List[str] | Response field. Embedded fields are separated with dots. To exclude a field, use “-” in front of its name. In case the parameter is not defined, the method returns all fields. (optional) (default to [])
    language = 'language_example' # str | Localization language. (optional)
    role = 'role_example' # str |  (optional)
    skill = ['skill_example'] # List[str] |  (optional)

    try:
        # Crew skills
        api_response = api_instance.get_encyclopedia_crewskills(fields=fields, language=language, role=role, skill=skill)
        print("The response of TankopediaApi->get_encyclopedia_crewskills:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TankopediaApi->get_encyclopedia_crewskills: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | [**List[str]**](str.md)| Response field. Embedded fields are separated with dots. To exclude a field, use “-” in front of its name. In case the parameter is not defined, the method returns all fields. | [optional] [default to []]
 **language** | **str**| Localization language. | [optional] 
 **role** | **str**|  | [optional] 
 **skill** | [**List[str]**](str.md)|  | [optional] 

### Return type

[**GetEncyclopediaCrewskills200Response**](GetEncyclopediaCrewskills200Response.md)

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

# **get_encyclopedia_info**
> GetEncyclopediaInfo200Response get_encyclopedia_info(fields=fields, language=language)

Tankopedia information

Method returns information about Tankopedia.

### Example

* Api Key Authentication (application_id):

```python
import wot_api_client
from wot_api_client.models.get_encyclopedia_info200_response import GetEncyclopediaInfo200Response
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
    api_instance = wot_api_client.TankopediaApi(api_client)
    fields = [] # List[str] | Response field. Embedded fields are separated with dots. To exclude a field, use “-” in front of its name. In case the parameter is not defined, the method returns all fields. (optional) (default to [])
    language = 'language_example' # str | Localization language. (optional)

    try:
        # Tankopedia information
        api_response = api_instance.get_encyclopedia_info(fields=fields, language=language)
        print("The response of TankopediaApi->get_encyclopedia_info:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TankopediaApi->get_encyclopedia_info: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | [**List[str]**](str.md)| Response field. Embedded fields are separated with dots. To exclude a field, use “-” in front of its name. In case the parameter is not defined, the method returns all fields. | [optional] [default to []]
 **language** | **str**| Localization language. | [optional] 

### Return type

[**GetEncyclopediaInfo200Response**](GetEncyclopediaInfo200Response.md)

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

# **get_encyclopedia_modules**
> GetEncyclopediaModules200Response get_encyclopedia_modules(extra=extra, fields=fields, language=language, limit=limit, module_id=module_id, nation=nation, page_no=page_no, type=type)

Modules

Method returns list of available modules that can be installed on vehicles, such as engines, turrets, etc. At least one input filter parameter (module ID, type) is required to be indicated.

### Example

* Api Key Authentication (application_id):

```python
import wot_api_client
from wot_api_client.models.get_encyclopedia_modules200_response import GetEncyclopediaModules200Response
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
    api_instance = wot_api_client.TankopediaApi(api_client)
    extra = ['extra_example'] # List[str] |  (optional)
    fields = [] # List[str] | Response field. Embedded fields are separated with dots. To exclude a field, use “-” in front of its name. In case the parameter is not defined, the method returns all fields. (optional) (default to [])
    language = 'language_example' # str | Localization language. (optional)
    limit = 100 # int |  (optional) (default to 100)
    module_id = [56] # List[int] |  (optional)
    nation = ['nation_example'] # List[str] |  (optional)
    page_no = 56 # int |  (optional)
    type = ['type_example'] # List[str] |  (optional)

    try:
        # Modules
        api_response = api_instance.get_encyclopedia_modules(extra=extra, fields=fields, language=language, limit=limit, module_id=module_id, nation=nation, page_no=page_no, type=type)
        print("The response of TankopediaApi->get_encyclopedia_modules:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TankopediaApi->get_encyclopedia_modules: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **extra** | [**List[str]**](str.md)|  | [optional] 
 **fields** | [**List[str]**](str.md)| Response field. Embedded fields are separated with dots. To exclude a field, use “-” in front of its name. In case the parameter is not defined, the method returns all fields. | [optional] [default to []]
 **language** | **str**| Localization language. | [optional] 
 **limit** | **int**|  | [optional] [default to 100]
 **module_id** | [**List[int]**](int.md)|  | [optional] 
 **nation** | [**List[str]**](str.md)|  | [optional] 
 **page_no** | **int**|  | [optional] 
 **type** | [**List[str]**](str.md)|  | [optional] 

### Return type

[**GetEncyclopediaModules200Response**](GetEncyclopediaModules200Response.md)

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

# **get_encyclopedia_personalmissions**
> GetEncyclopediaPersonalmissions200Response get_encyclopedia_personalmissions(campaign_id=campaign_id, fields=fields, language=language, operation_id=operation_id, set_id=set_id, tag=tag)

Personal Missions

Method returns details on Personal Missions on the basis of specified campaign IDs, operation IDs, mission branch and tag IDs.

### Example

* Api Key Authentication (application_id):

```python
import wot_api_client
from wot_api_client.models.get_encyclopedia_personalmissions200_response import GetEncyclopediaPersonalmissions200Response
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
    api_instance = wot_api_client.TankopediaApi(api_client)
    campaign_id = [56] # List[int] |  (optional)
    fields = [] # List[str] | Response field. Embedded fields are separated with dots. To exclude a field, use “-” in front of its name. In case the parameter is not defined, the method returns all fields. (optional) (default to [])
    language = 'language_example' # str | Localization language. (optional)
    operation_id = [56] # List[int] |  (optional)
    set_id = [56] # List[int] |  (optional)
    tag = ['tag_example'] # List[str] |  (optional)

    try:
        # Personal Missions
        api_response = api_instance.get_encyclopedia_personalmissions(campaign_id=campaign_id, fields=fields, language=language, operation_id=operation_id, set_id=set_id, tag=tag)
        print("The response of TankopediaApi->get_encyclopedia_personalmissions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TankopediaApi->get_encyclopedia_personalmissions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **campaign_id** | [**List[int]**](int.md)|  | [optional] 
 **fields** | [**List[str]**](str.md)| Response field. Embedded fields are separated with dots. To exclude a field, use “-” in front of its name. In case the parameter is not defined, the method returns all fields. | [optional] [default to []]
 **language** | **str**| Localization language. | [optional] 
 **operation_id** | [**List[int]**](int.md)|  | [optional] 
 **set_id** | [**List[int]**](int.md)|  | [optional] 
 **tag** | [**List[str]**](str.md)|  | [optional] 

### Return type

[**GetEncyclopediaPersonalmissions200Response**](GetEncyclopediaPersonalmissions200Response.md)

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

# **get_encyclopedia_provisions**
> GetEncyclopediaProvisions200Response get_encyclopedia_provisions(fields=fields, language=language, limit=limit, page_no=page_no, provision_id=provision_id, type=type)

Equipment and Consumables

Method returns a list of available equipment and consumables.

### Example

* Api Key Authentication (application_id):

```python
import wot_api_client
from wot_api_client.models.get_encyclopedia_provisions200_response import GetEncyclopediaProvisions200Response
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
    api_instance = wot_api_client.TankopediaApi(api_client)
    fields = [] # List[str] | Response field. Embedded fields are separated with dots. To exclude a field, use “-” in front of its name. In case the parameter is not defined, the method returns all fields. (optional) (default to [])
    language = 'language_example' # str | Localization language. (optional)
    limit = 100 # int |  (optional) (default to 100)
    page_no = 56 # int |  (optional)
    provision_id = [56] # List[int] |  (optional)
    type = ["equipment","optionalDevice"] # List[str] |  (optional) (default to ["equipment","optionalDevice"])

    try:
        # Equipment and Consumables
        api_response = api_instance.get_encyclopedia_provisions(fields=fields, language=language, limit=limit, page_no=page_no, provision_id=provision_id, type=type)
        print("The response of TankopediaApi->get_encyclopedia_provisions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TankopediaApi->get_encyclopedia_provisions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | [**List[str]**](str.md)| Response field. Embedded fields are separated with dots. To exclude a field, use “-” in front of its name. In case the parameter is not defined, the method returns all fields. | [optional] [default to []]
 **language** | **str**| Localization language. | [optional] 
 **limit** | **int**|  | [optional] [default to 100]
 **page_no** | **int**|  | [optional] 
 **provision_id** | [**List[int]**](int.md)|  | [optional] 
 **type** | [**List[str]**](str.md)|  | [optional] [default to [&quot;equipment&quot;,&quot;optionalDevice&quot;]]

### Return type

[**GetEncyclopediaProvisions200Response**](GetEncyclopediaProvisions200Response.md)

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

# **get_encyclopedia_vehicleprofile**
> GetEncyclopediaVehicleprofile200Response get_encyclopedia_vehicleprofile(tank_id, engine_id=engine_id, fields=fields, gun_id=gun_id, language=language, profile_id=profile_id, radio_id=radio_id, suspension_id=suspension_id, turret_id=turret_id)

Vehicle characteristics

Method returns vehicle configuration characteristics based on the specified module IDs.

### Example

* Api Key Authentication (application_id):

```python
import wot_api_client
from wot_api_client.models.get_encyclopedia_vehicleprofile200_response import GetEncyclopediaVehicleprofile200Response
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
    api_instance = wot_api_client.TankopediaApi(api_client)
    tank_id = 56 # int | 
    engine_id = 56 # int |  (optional)
    fields = [] # List[str] | Response field. Embedded fields are separated with dots. To exclude a field, use “-” in front of its name. In case the parameter is not defined, the method returns all fields. (optional) (default to [])
    gun_id = 56 # int |  (optional)
    language = 'language_example' # str | Localization language. (optional)
    profile_id = 'profile_id_example' # str |  (optional)
    radio_id = 56 # int |  (optional)
    suspension_id = 56 # int |  (optional)
    turret_id = 56 # int |  (optional)

    try:
        # Vehicle characteristics
        api_response = api_instance.get_encyclopedia_vehicleprofile(tank_id, engine_id=engine_id, fields=fields, gun_id=gun_id, language=language, profile_id=profile_id, radio_id=radio_id, suspension_id=suspension_id, turret_id=turret_id)
        print("The response of TankopediaApi->get_encyclopedia_vehicleprofile:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TankopediaApi->get_encyclopedia_vehicleprofile: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tank_id** | **int**|  | 
 **engine_id** | **int**|  | [optional] 
 **fields** | [**List[str]**](str.md)| Response field. Embedded fields are separated with dots. To exclude a field, use “-” in front of its name. In case the parameter is not defined, the method returns all fields. | [optional] [default to []]
 **gun_id** | **int**|  | [optional] 
 **language** | **str**| Localization language. | [optional] 
 **profile_id** | **str**|  | [optional] 
 **radio_id** | **int**|  | [optional] 
 **suspension_id** | **int**|  | [optional] 
 **turret_id** | **int**|  | [optional] 

### Return type

[**GetEncyclopediaVehicleprofile200Response**](GetEncyclopediaVehicleprofile200Response.md)

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

# **get_encyclopedia_vehicleprofiles**
> GetEncyclopediaVehicleprofiles200Response get_encyclopedia_vehicleprofiles(tank_id, fields=fields, language=language, order_by=order_by)

Vehicle configurations

Method returns vehicle configuration characteristics.

### Example

* Api Key Authentication (application_id):

```python
import wot_api_client
from wot_api_client.models.get_encyclopedia_vehicleprofiles200_response import GetEncyclopediaVehicleprofiles200Response
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
    api_instance = wot_api_client.TankopediaApi(api_client)
    tank_id = 56 # int | 
    fields = [] # List[str] | Response field. Embedded fields are separated with dots. To exclude a field, use “-” in front of its name. In case the parameter is not defined, the method returns all fields. (optional) (default to [])
    language = 'language_example' # str | Localization language. (optional)
    order_by = 'order_by_example' # str |  (optional)

    try:
        # Vehicle configurations
        api_response = api_instance.get_encyclopedia_vehicleprofiles(tank_id, fields=fields, language=language, order_by=order_by)
        print("The response of TankopediaApi->get_encyclopedia_vehicleprofiles:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TankopediaApi->get_encyclopedia_vehicleprofiles: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tank_id** | **int**|  | 
 **fields** | [**List[str]**](str.md)| Response field. Embedded fields are separated with dots. To exclude a field, use “-” in front of its name. In case the parameter is not defined, the method returns all fields. | [optional] [default to []]
 **language** | **str**| Localization language. | [optional] 
 **order_by** | **str**|  | [optional] 

### Return type

[**GetEncyclopediaVehicleprofiles200Response**](GetEncyclopediaVehicleprofiles200Response.md)

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

# **get_encyclopedia_vehicles**
> GetEncyclopediaVehicles200Response get_encyclopedia_vehicles(fields=fields, language=language, limit=limit, nation=nation, page_no=page_no, tank_id=tank_id, tier=tier, type=type)

Vehicles

Method returns list of available vehicles.

### Example

* Api Key Authentication (application_id):

```python
import wot_api_client
from wot_api_client.models.get_encyclopedia_vehicles200_response import GetEncyclopediaVehicles200Response
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
    api_instance = wot_api_client.TankopediaApi(api_client)
    fields = [] # List[str] | Response field. Embedded fields are separated with dots. To exclude a field, use “-” in front of its name. In case the parameter is not defined, the method returns all fields. (optional) (default to [])
    language = 'language_example' # str | Localization language. (optional)
    limit = 100 # int |  (optional) (default to 100)
    nation = ['nation_example'] # List[str] |  (optional)
    page_no = 56 # int |  (optional)
    tank_id = [56] # List[int] |  (optional)
    tier = [56] # List[int] |  (optional)
    type = ['type_example'] # List[str] |  (optional)

    try:
        # Vehicles
        api_response = api_instance.get_encyclopedia_vehicles(fields=fields, language=language, limit=limit, nation=nation, page_no=page_no, tank_id=tank_id, tier=tier, type=type)
        print("The response of TankopediaApi->get_encyclopedia_vehicles:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TankopediaApi->get_encyclopedia_vehicles: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | [**List[str]**](str.md)| Response field. Embedded fields are separated with dots. To exclude a field, use “-” in front of its name. In case the parameter is not defined, the method returns all fields. | [optional] [default to []]
 **language** | **str**| Localization language. | [optional] 
 **limit** | **int**|  | [optional] [default to 100]
 **nation** | [**List[str]**](str.md)|  | [optional] 
 **page_no** | **int**|  | [optional] 
 **tank_id** | [**List[int]**](int.md)|  | [optional] 
 **tier** | [**List[int]**](int.md)|  | [optional] 
 **type** | [**List[str]**](str.md)|  | [optional] 

### Return type

[**GetEncyclopediaVehicles200Response**](GetEncyclopediaVehicles200Response.md)

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

