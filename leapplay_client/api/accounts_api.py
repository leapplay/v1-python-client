# coding: utf-8

"""
    Leap Play

    Learn more at https://www.leap-play.com  # noqa: E501

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from leapplay_client.api_client import ApiClient


class AccountsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def change_password(self, change_password_request, **kwargs):  # noqa: E501
        """Changes the Password and provides a new Refresh Token (Auth)  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.change_password(change_password_request, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param RequestChangePassword change_password_request: The change password request. (required)
        :return: ChangedPasswordUser
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.change_password_with_http_info(change_password_request, **kwargs)  # noqa: E501
        else:
            (data) = self.change_password_with_http_info(change_password_request, **kwargs)  # noqa: E501
            return data

    def change_password_with_http_info(self, change_password_request, **kwargs):  # noqa: E501
        """Changes the Password and provides a new Refresh Token (Auth)  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.change_password_with_http_info(change_password_request, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param RequestChangePassword change_password_request: The change password request. (required)
        :return: ChangedPasswordUser
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['change_password_request']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method change_password" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'change_password_request' is set
        if ('change_password_request' not in params or
                params['change_password_request'] is None):
            raise ValueError("Missing the required parameter `change_password_request` when calling `change_password`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'change_password_request' in params:
            body_params = params['change_password_request']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json-patch+json', 'application/json', 'text/json', 'application/*+json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Bearer']  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/accounts/password/change', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ChangedPasswordUser',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def confirm_email(self, email_confirmation_request, **kwargs):  # noqa: E501
        """Confirms ownership of an E-Mail Address by an E-Mail Confirmation Token  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.confirm_email(email_confirmation_request, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param RequestEmailConfirmation email_confirmation_request: The request email confirmation. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.confirm_email_with_http_info(email_confirmation_request, **kwargs)  # noqa: E501
        else:
            (data) = self.confirm_email_with_http_info(email_confirmation_request, **kwargs)  # noqa: E501
            return data

    def confirm_email_with_http_info(self, email_confirmation_request, **kwargs):  # noqa: E501
        """Confirms ownership of an E-Mail Address by an E-Mail Confirmation Token  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.confirm_email_with_http_info(email_confirmation_request, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param RequestEmailConfirmation email_confirmation_request: The request email confirmation. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['email_confirmation_request']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method confirm_email" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'email_confirmation_request' is set
        if ('email_confirmation_request' not in params or
                params['email_confirmation_request'] is None):
            raise ValueError("Missing the required parameter `email_confirmation_request` when calling `confirm_email`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'email_confirmation_request' in params:
            body_params = params['email_confirmation_request']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json-patch+json', 'application/json', 'text/json', 'application/*+json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/accounts/email/confirmation', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def register(self, register_request, **kwargs):  # noqa: E501
        """Registers a User Account  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.register(register_request, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param RequestRegisterUser register_request:  (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.register_with_http_info(register_request, **kwargs)  # noqa: E501
        else:
            (data) = self.register_with_http_info(register_request, **kwargs)  # noqa: E501
            return data

    def register_with_http_info(self, register_request, **kwargs):  # noqa: E501
        """Registers a User Account  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.register_with_http_info(register_request, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param RequestRegisterUser register_request:  (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['register_request']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method register" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'register_request' is set
        if ('register_request' not in params or
                params['register_request'] is None):
            raise ValueError("Missing the required parameter `register_request` when calling `register`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'register_request' in params:
            body_params = params['register_request']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json-patch+json', 'application/json', 'text/json', 'application/*+json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/accounts/register', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def request_password(self, forgot_password_request, **kwargs):  # noqa: E501
        """Receives a Reset Token that is required to reset the Password  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.request_password(forgot_password_request, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param RequestForgotPassword forgot_password_request: Request object holding the required parameter (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.request_password_with_http_info(forgot_password_request, **kwargs)  # noqa: E501
        else:
            (data) = self.request_password_with_http_info(forgot_password_request, **kwargs)  # noqa: E501
            return data

    def request_password_with_http_info(self, forgot_password_request, **kwargs):  # noqa: E501
        """Receives a Reset Token that is required to reset the Password  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.request_password_with_http_info(forgot_password_request, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param RequestForgotPassword forgot_password_request: Request object holding the required parameter (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['forgot_password_request']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method request_password" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'forgot_password_request' is set
        if ('forgot_password_request' not in params or
                params['forgot_password_request'] is None):
            raise ValueError("Missing the required parameter `forgot_password_request` when calling `request_password`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'forgot_password_request' in params:
            body_params = params['forgot_password_request']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json-patch+json', 'application/json', 'text/json', 'application/*+json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/accounts/password/forgot', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def resend_e_mail_confirmation(self, resend_confirmation_email_request, **kwargs):  # noqa: E501
        """Re-sends a message with a EMail Confirmation Token.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.resend_e_mail_confirmation(resend_confirmation_email_request, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param RequestResendConfirmationEmail resend_confirmation_email_request: The resend email confirmation request. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.resend_e_mail_confirmation_with_http_info(resend_confirmation_email_request, **kwargs)  # noqa: E501
        else:
            (data) = self.resend_e_mail_confirmation_with_http_info(resend_confirmation_email_request, **kwargs)  # noqa: E501
            return data

    def resend_e_mail_confirmation_with_http_info(self, resend_confirmation_email_request, **kwargs):  # noqa: E501
        """Re-sends a message with a EMail Confirmation Token.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.resend_e_mail_confirmation_with_http_info(resend_confirmation_email_request, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param RequestResendConfirmationEmail resend_confirmation_email_request: The resend email confirmation request. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['resend_confirmation_email_request']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method resend_e_mail_confirmation" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'resend_confirmation_email_request' is set
        if ('resend_confirmation_email_request' not in params or
                params['resend_confirmation_email_request'] is None):
            raise ValueError("Missing the required parameter `resend_confirmation_email_request` when calling `resend_e_mail_confirmation`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'resend_confirmation_email_request' in params:
            body_params = params['resend_confirmation_email_request']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json-patch+json', 'application/json', 'text/json', 'application/*+json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/accounts/email/confirmation/send', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def reset_password(self, reset_password_request, **kwargs):  # noqa: E501
        """Resets the Password with an Reset Token  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.reset_password(reset_password_request, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param RequestResetPassword reset_password_request: The request reset password. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.reset_password_with_http_info(reset_password_request, **kwargs)  # noqa: E501
        else:
            (data) = self.reset_password_with_http_info(reset_password_request, **kwargs)  # noqa: E501
            return data

    def reset_password_with_http_info(self, reset_password_request, **kwargs):  # noqa: E501
        """Resets the Password with an Reset Token  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.reset_password_with_http_info(reset_password_request, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param RequestResetPassword reset_password_request: The request reset password. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['reset_password_request']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method reset_password" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'reset_password_request' is set
        if ('reset_password_request' not in params or
                params['reset_password_request'] is None):
            raise ValueError("Missing the required parameter `reset_password_request` when calling `reset_password`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'reset_password_request' in params:
            body_params = params['reset_password_request']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json-patch+json', 'application/json', 'text/json', 'application/*+json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/accounts/password/reset', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)