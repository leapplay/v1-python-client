# leapplay_client.AuthApi

All URIs are relative to *https://api.leap-play.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**login**](AuthApi.md#login) | **POST** /api/v1/auth/login | Receive an Access and Refresh Token
[**logout**](AuthApi.md#logout) | **POST** /api/v1/auth/logout | Invalidate the Refresh token (Auth)
[**refresh_token**](AuthApi.md#refresh_token) | **POST** /api/v1/auth/refreshtoken | Receive a new Access token


# **login**
> LoginResponse login(login_request=login_request)

Receive an Access and Refresh Token

### Example
```python
from __future__ import print_function
import time
import leapplay_client
from leapplay_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = leapplay_client.AuthApi()
login_request = leapplay_client.RequestLoginModel() # RequestLoginModel | Login Request Dto (optional)

try:
    # Receive an Access and Refresh Token
    api_response = api_instance.login(login_request=login_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthApi->login: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **login_request** | [**RequestLoginModel**](RequestLoginModel.md)| Login Request Dto | [optional] 

### Return type

[**LoginResponse**](LoginResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **logout**
> logout()

Invalidate the Refresh token (Auth)

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
api_instance = leapplay_client.AuthApi(leapplay_client.ApiClient(configuration))

try:
    # Invalidate the Refresh token (Auth)
    api_instance.logout()
except ApiException as e:
    print("Exception when calling AuthApi->logout: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **refresh_token**
> AccessToken refresh_token(request_token_refresh=request_token_refresh, authorization=authorization)

Receive a new Access token

### Example
```python
from __future__ import print_function
import time
import leapplay_client
from leapplay_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = leapplay_client.AuthApi()
request_token_refresh = leapplay_client.RequestTokenRefresh() # RequestTokenRefresh | Refresh Token Dto (optional)
authorization = 'authorization_example' # str | Any previous Access Token. (optional)

try:
    # Receive a new Access token
    api_response = api_instance.refresh_token(request_token_refresh=request_token_refresh, authorization=authorization)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthApi->refresh_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_token_refresh** | [**RequestTokenRefresh**](RequestTokenRefresh.md)| Refresh Token Dto | [optional] 
 **authorization** | **str**| Any previous Access Token. | [optional] 

### Return type

[**AccessToken**](AccessToken.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

