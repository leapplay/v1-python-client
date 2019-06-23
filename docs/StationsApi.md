# leapplay_client.StationsApi

All URIs are relative to *https://api.leap-play.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_station**](StationsApi.md#create_station) | **PUT** /api/v1/stations | Creates a Station (Auth)
[**get_session_logs_all**](StationsApi.md#get_session_logs_all) | **GET** /api/v1/stations/sessions | Gets closed Sessions from all stations (Auth)
[**get_session_logs_by_station_id**](StationsApi.md#get_session_logs_by_station_id) | **GET** /api/v1/stations/{stationId}/sessions | Gets closed Sessions (Auth)
[**get_settings**](StationsApi.md#get_settings) | **GET** /api/v1/stations/settings | Gets the Settings of all Stations (Auth)
[**get_settings_by_station_id**](StationsApi.md#get_settings_by_station_id) | **GET** /api/v1/stations/{stationId}/settings | Get the Settings of an Station (Auth)
[**get_state**](StationsApi.md#get_state) | **GET** /api/v1/stations/{stationId} | Get the Station&#39;s State (Auth)
[**get_states**](StationsApi.md#get_states) | **GET** /api/v1/stations | Gets Collection of Station States (Auth)
[**session_create**](StationsApi.md#session_create) | **PUT** /api/v1/stations/{stationId}/sessions | Creates a Session (Auth)
[**session_stop**](StationsApi.md#session_stop) | **POST** /api/v1/stations/{stationId}/sessions/current/stop | Stops the running Session (Auth)
[**session_update**](StationsApi.md#session_update) | **POST** /api/v1/stations/{stationId}/sessions/current/update | Updates the running Session. (Auth)
[**set_settings**](StationsApi.md#set_settings) | **POST** /api/v1/stations/{stationId}/settings | Sets the Settings for an Station (Auth)
[**set_station_mode**](StationsApi.md#set_station_mode) | **POST** /api/v1/stations/{stationId}/settings/mode | Sets the Operation Mode (Auth)
[**set_station_password**](StationsApi.md#set_station_password) | **POST** /api/v1/stations/{stationId}/settings/password | Changes the Password (Auth)
[**set_station_qr_code**](StationsApi.md#set_station_qr_code) | **POST** /api/v1/stations/{stationId}/settings/qrcode | Sets the QrCode (Auth)


# **create_station**
> StationSettings create_station(create_station=create_station)

Creates a Station (Auth)

### Example
```python
from __future__ import print_function
import time
import leapplay_client
from leapplay_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = leapplay_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = leapplay_client.StationsApi(leapplay_client.ApiClient(configuration))
create_station = leapplay_client.RequestCreateStation() # RequestCreateStation | Create Station Dto (optional)

try:
    # Creates a Station (Auth)
    api_response = api_instance.create_station(create_station=create_station)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StationsApi->create_station: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_station** | [**RequestCreateStation**](RequestCreateStation.md)| Create Station Dto | [optional] 

### Return type

[**StationSettings**](StationSettings.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_session_logs_all**
> list[SessionLog] get_session_logs_all(take=take, skip=skip)

Gets closed Sessions from all stations (Auth)

### Example
```python
from __future__ import print_function
import time
import leapplay_client
from leapplay_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = leapplay_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = leapplay_client.StationsApi(leapplay_client.ApiClient(configuration))
take = 50 # int | Entries to return (optional) (default to 50)
skip = 0 # int | Entries to skip (optional) (default to 0)

try:
    # Gets closed Sessions from all stations (Auth)
    api_response = api_instance.get_session_logs_all(take=take, skip=skip)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StationsApi->get_session_logs_all: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **take** | **int**| Entries to return | [optional] [default to 50]
 **skip** | **int**| Entries to skip | [optional] [default to 0]

### Return type

[**list[SessionLog]**](SessionLog.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_session_logs_by_station_id**
> list[SessionLog] get_session_logs_by_station_id(station_id, take=take, skip=skip)

Gets closed Sessions (Auth)

### Example
```python
from __future__ import print_function
import time
import leapplay_client
from leapplay_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = leapplay_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = leapplay_client.StationsApi(leapplay_client.ApiClient(configuration))
station_id = 'station_id_example' # str | Station Id
take = 50 # int | Entries to return (optional) (default to 50)
skip = 0 # int | Entries to skip (optional) (default to 0)

try:
    # Gets closed Sessions (Auth)
    api_response = api_instance.get_session_logs_by_station_id(station_id, take=take, skip=skip)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StationsApi->get_session_logs_by_station_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **station_id** | [**str**](.md)| Station Id | 
 **take** | **int**| Entries to return | [optional] [default to 50]
 **skip** | **int**| Entries to skip | [optional] [default to 0]

### Return type

[**list[SessionLog]**](SessionLog.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_settings**
> list[StationSettings] get_settings()

Gets the Settings of all Stations (Auth)

### Example
```python
from __future__ import print_function
import time
import leapplay_client
from leapplay_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = leapplay_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = leapplay_client.StationsApi(leapplay_client.ApiClient(configuration))

try:
    # Gets the Settings of all Stations (Auth)
    api_response = api_instance.get_settings()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StationsApi->get_settings: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[StationSettings]**](StationSettings.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_settings_by_station_id**
> StationSettings get_settings_by_station_id(station_id)

Get the Settings of an Station (Auth)

### Example
```python
from __future__ import print_function
import time
import leapplay_client
from leapplay_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = leapplay_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = leapplay_client.StationsApi(leapplay_client.ApiClient(configuration))
station_id = 'station_id_example' # str | Station Id

try:
    # Get the Settings of an Station (Auth)
    api_response = api_instance.get_settings_by_station_id(station_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StationsApi->get_settings_by_station_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **station_id** | [**str**](.md)| Station Id | 

### Return type

[**StationSettings**](StationSettings.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_state**
> StationCurrentState get_state(station_id)

Get the Station's State (Auth)

### Example
```python
from __future__ import print_function
import time
import leapplay_client
from leapplay_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = leapplay_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = leapplay_client.StationsApi(leapplay_client.ApiClient(configuration))
station_id = 'station_id_example' # str | Station Id

try:
    # Get the Station's State (Auth)
    api_response = api_instance.get_state(station_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StationsApi->get_state: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **station_id** | [**str**](.md)| Station Id | 

### Return type

[**StationCurrentState**](StationCurrentState.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_states**
> list[StationCurrentState] get_states(network_state_filter=network_state_filter)

Gets Collection of Station States (Auth)

### Example
```python
from __future__ import print_function
import time
import leapplay_client
from leapplay_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = leapplay_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = leapplay_client.StationsApi(leapplay_client.ApiClient(configuration))
network_state_filter = 'network_state_filter_example' # str | Optional Network State Filter (optional)

try:
    # Gets Collection of Station States (Auth)
    api_response = api_instance.get_states(network_state_filter=network_state_filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StationsApi->get_states: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **network_state_filter** | **str**| Optional Network State Filter | [optional] 

### Return type

[**list[StationCurrentState]**](StationCurrentState.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **session_create**
> CreatedSession session_create(station_id, create_session_request=create_session_request)

Creates a Session (Auth)

### Example
```python
from __future__ import print_function
import time
import leapplay_client
from leapplay_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = leapplay_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = leapplay_client.StationsApi(leapplay_client.ApiClient(configuration))
station_id = 'station_id_example' # str | Station Id
create_session_request = leapplay_client.RequestNewStationSession() # RequestNewStationSession | New Session Request Dto (optional)

try:
    # Creates a Session (Auth)
    api_response = api_instance.session_create(station_id, create_session_request=create_session_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StationsApi->session_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **station_id** | [**str**](.md)| Station Id | 
 **create_session_request** | [**RequestNewStationSession**](RequestNewStationSession.md)| New Session Request Dto | [optional] 

### Return type

[**CreatedSession**](CreatedSession.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **session_stop**
> StoppedSession session_stop(station_id)

Stops the running Session (Auth)

### Example
```python
from __future__ import print_function
import time
import leapplay_client
from leapplay_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = leapplay_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = leapplay_client.StationsApi(leapplay_client.ApiClient(configuration))
station_id = 'station_id_example' # str | Station Id

try:
    # Stops the running Session (Auth)
    api_response = api_instance.session_stop(station_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StationsApi->session_stop: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **station_id** | [**str**](.md)| Station Id | 

### Return type

[**StoppedSession**](StoppedSession.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **session_update**
> UpdatedSession session_update(station_id, update_session_request=update_session_request)

Updates the running Session. (Auth)

### Example
```python
from __future__ import print_function
import time
import leapplay_client
from leapplay_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = leapplay_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = leapplay_client.StationsApi(leapplay_client.ApiClient(configuration))
station_id = 'station_id_example' # str | Station Id
update_session_request = leapplay_client.RequestSessionUpdate() # RequestSessionUpdate | The Update Request Dto (optional)

try:
    # Updates the running Session. (Auth)
    api_response = api_instance.session_update(station_id, update_session_request=update_session_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StationsApi->session_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **station_id** | [**str**](.md)| Station Id | 
 **update_session_request** | [**RequestSessionUpdate**](RequestSessionUpdate.md)| The Update Request Dto | [optional] 

### Return type

[**UpdatedSession**](UpdatedSession.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_settings**
> set_settings(station_id, set_settings_request=set_settings_request)

Sets the Settings for an Station (Auth)

### Example
```python
from __future__ import print_function
import time
import leapplay_client
from leapplay_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = leapplay_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = leapplay_client.StationsApi(leapplay_client.ApiClient(configuration))
station_id = 'station_id_example' # str | Station Id
set_settings_request = leapplay_client.RequestStationSettings() # RequestStationSettings | Settings Dto (optional)

try:
    # Sets the Settings for an Station (Auth)
    api_instance.set_settings(station_id, set_settings_request=set_settings_request)
except ApiException as e:
    print("Exception when calling StationsApi->set_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **station_id** | [**str**](.md)| Station Id | 
 **set_settings_request** | [**RequestStationSettings**](RequestStationSettings.md)| Settings Dto | [optional] 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_station_mode**
> set_station_mode(station_id, set_mode_request=set_mode_request)

Sets the Operation Mode (Auth)

### Example
```python
from __future__ import print_function
import time
import leapplay_client
from leapplay_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = leapplay_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = leapplay_client.StationsApi(leapplay_client.ApiClient(configuration))
station_id = 'station_id_example' # str | Station Id
set_mode_request = leapplay_client.RequestStationMode() # RequestStationMode | The Operation Mode (optional)

try:
    # Sets the Operation Mode (Auth)
    api_instance.set_station_mode(station_id, set_mode_request=set_mode_request)
except ApiException as e:
    print("Exception when calling StationsApi->set_station_mode: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **station_id** | [**str**](.md)| Station Id | 
 **set_mode_request** | [**RequestStationMode**](RequestStationMode.md)| The Operation Mode | [optional] 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_station_password**
> set_station_password(station_id, set_password_request=set_password_request)

Changes the Password (Auth)

### Example
```python
from __future__ import print_function
import time
import leapplay_client
from leapplay_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = leapplay_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = leapplay_client.StationsApi(leapplay_client.ApiClient(configuration))
station_id = 'station_id_example' # str | Station Id
set_password_request = leapplay_client.RequestSetStationPassword() # RequestSetStationPassword | New Password (optional)

try:
    # Changes the Password (Auth)
    api_instance.set_station_password(station_id, set_password_request=set_password_request)
except ApiException as e:
    print("Exception when calling StationsApi->set_station_password: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **station_id** | [**str**](.md)| Station Id | 
 **set_password_request** | [**RequestSetStationPassword**](RequestSetStationPassword.md)| New Password | [optional] 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_station_qr_code**
> set_station_qr_code(station_id, set_qr_code_request=set_qr_code_request)

Sets the QrCode (Auth)

### Example
```python
from __future__ import print_function
import time
import leapplay_client
from leapplay_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = leapplay_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = leapplay_client.StationsApi(leapplay_client.ApiClient(configuration))
station_id = 'station_id_example' # str | Station Id
set_qr_code_request = leapplay_client.RequestStationQrCode() # RequestStationQrCode | QrCode (optional)

try:
    # Sets the QrCode (Auth)
    api_instance.set_station_qr_code(station_id, set_qr_code_request=set_qr_code_request)
except ApiException as e:
    print("Exception when calling StationsApi->set_station_qr_code: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **station_id** | [**str**](.md)| Station Id | 
 **set_qr_code_request** | [**RequestStationQrCode**](RequestStationQrCode.md)| QrCode | [optional] 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

