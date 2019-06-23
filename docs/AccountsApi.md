# leapplay_client.AccountsApi

All URIs are relative to *https://api.leap-play.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**change_password**](AccountsApi.md#change_password) | **POST** /api/v1/accounts/password/change | Changes the Password and provides a new Refresh Token (Auth)
[**confirm_email**](AccountsApi.md#confirm_email) | **POST** /api/v1/accounts/email/confirmation | Confirms ownership of an E-Mail Address by an E-Mail Confirmation Token
[**register**](AccountsApi.md#register) | **POST** /api/v1/accounts/register | Registers a User Account
[**request_password**](AccountsApi.md#request_password) | **POST** /api/v1/accounts/password/forgot | Receives a Reset Token that is required to reset the Password
[**resend_e_mail_confirmation**](AccountsApi.md#resend_e_mail_confirmation) | **POST** /api/v1/accounts/email/confirmation/send | Re-sends a message with a EMail Confirmation Token.
[**reset_password**](AccountsApi.md#reset_password) | **POST** /api/v1/accounts/password/reset | Resets the Password with an Reset Token


# **change_password**
> ChangedPasswordUser change_password(change_password_request)

Changes the Password and provides a new Refresh Token (Auth)

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
api_instance = leapplay_client.AccountsApi(leapplay_client.ApiClient(configuration))
change_password_request = leapplay_client.RequestChangePassword() # RequestChangePassword | The change password request.

try:
    # Changes the Password and provides a new Refresh Token (Auth)
    api_response = api_instance.change_password(change_password_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountsApi->change_password: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **change_password_request** | [**RequestChangePassword**](RequestChangePassword.md)| The change password request. | 

### Return type

[**ChangedPasswordUser**](ChangedPasswordUser.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **confirm_email**
> confirm_email(email_confirmation_request)

Confirms ownership of an E-Mail Address by an E-Mail Confirmation Token

### Example
```python
from __future__ import print_function
import time
import leapplay_client
from leapplay_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = leapplay_client.AccountsApi()
email_confirmation_request = leapplay_client.RequestEmailConfirmation() # RequestEmailConfirmation | The request email confirmation.

try:
    # Confirms ownership of an E-Mail Address by an E-Mail Confirmation Token
    api_instance.confirm_email(email_confirmation_request)
except ApiException as e:
    print("Exception when calling AccountsApi->confirm_email: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email_confirmation_request** | [**RequestEmailConfirmation**](RequestEmailConfirmation.md)| The request email confirmation. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **register**
> register(register_request)

Registers a User Account

### Example
```python
from __future__ import print_function
import time
import leapplay_client
from leapplay_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = leapplay_client.AccountsApi()
register_request = leapplay_client.RequestRegisterUser() # RequestRegisterUser | 

try:
    # Registers a User Account
    api_instance.register(register_request)
except ApiException as e:
    print("Exception when calling AccountsApi->register: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **register_request** | [**RequestRegisterUser**](RequestRegisterUser.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **request_password**
> request_password(forgot_password_request)

Receives a Reset Token that is required to reset the Password

### Example
```python
from __future__ import print_function
import time
import leapplay_client
from leapplay_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = leapplay_client.AccountsApi()
forgot_password_request = leapplay_client.RequestForgotPassword() # RequestForgotPassword | Request object holding the required parameter

try:
    # Receives a Reset Token that is required to reset the Password
    api_instance.request_password(forgot_password_request)
except ApiException as e:
    print("Exception when calling AccountsApi->request_password: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **forgot_password_request** | [**RequestForgotPassword**](RequestForgotPassword.md)| Request object holding the required parameter | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resend_e_mail_confirmation**
> resend_e_mail_confirmation(resend_confirmation_email_request)

Re-sends a message with a EMail Confirmation Token.

### Example
```python
from __future__ import print_function
import time
import leapplay_client
from leapplay_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = leapplay_client.AccountsApi()
resend_confirmation_email_request = leapplay_client.RequestResendConfirmationEmail() # RequestResendConfirmationEmail | The resend email confirmation request.

try:
    # Re-sends a message with a EMail Confirmation Token.
    api_instance.resend_e_mail_confirmation(resend_confirmation_email_request)
except ApiException as e:
    print("Exception when calling AccountsApi->resend_e_mail_confirmation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resend_confirmation_email_request** | [**RequestResendConfirmationEmail**](RequestResendConfirmationEmail.md)| The resend email confirmation request. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reset_password**
> reset_password(reset_password_request)

Resets the Password with an Reset Token

### Example
```python
from __future__ import print_function
import time
import leapplay_client
from leapplay_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = leapplay_client.AccountsApi()
reset_password_request = leapplay_client.RequestResetPassword() # RequestResetPassword | The request reset password.

try:
    # Resets the Password with an Reset Token
    api_instance.reset_password(reset_password_request)
except ApiException as e:
    print("Exception when calling AccountsApi->reset_password: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **reset_password_request** | [**RequestResetPassword**](RequestResetPassword.md)| The request reset password. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

