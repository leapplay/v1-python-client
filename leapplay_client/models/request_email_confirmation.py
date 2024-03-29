# coding: utf-8

"""
    Leap Play

    Learn more at https://www.leap-play.com  # noqa: E501

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class RequestEmailConfirmation(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'username': 'str',
        'email_confirmation_token': 'str'
    }

    attribute_map = {
        'username': 'username',
        'email_confirmation_token': 'emailConfirmationToken'
    }

    def __init__(self, username=None, email_confirmation_token=None):  # noqa: E501
        """RequestEmailConfirmation - a model defined in Swagger"""  # noqa: E501

        self._username = None
        self._email_confirmation_token = None
        self.discriminator = None

        self.username = username
        self.email_confirmation_token = email_confirmation_token

    @property
    def username(self):
        """Gets the username of this RequestEmailConfirmation.  # noqa: E501


        :return: The username of this RequestEmailConfirmation.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this RequestEmailConfirmation.


        :param username: The username of this RequestEmailConfirmation.  # noqa: E501
        :type: str
        """
        if username is None:
            raise ValueError("Invalid value for `username`, must not be `None`")  # noqa: E501
        if username is not None and len(username) > 30:
            raise ValueError("Invalid value for `username`, length must be less than or equal to `30`")  # noqa: E501
        if username is not None and len(username) < 8:
            raise ValueError("Invalid value for `username`, length must be greater than or equal to `8`")  # noqa: E501

        self._username = username

    @property
    def email_confirmation_token(self):
        """Gets the email_confirmation_token of this RequestEmailConfirmation.  # noqa: E501


        :return: The email_confirmation_token of this RequestEmailConfirmation.  # noqa: E501
        :rtype: str
        """
        return self._email_confirmation_token

    @email_confirmation_token.setter
    def email_confirmation_token(self, email_confirmation_token):
        """Sets the email_confirmation_token of this RequestEmailConfirmation.


        :param email_confirmation_token: The email_confirmation_token of this RequestEmailConfirmation.  # noqa: E501
        :type: str
        """
        if email_confirmation_token is None:
            raise ValueError("Invalid value for `email_confirmation_token`, must not be `None`")  # noqa: E501
        if email_confirmation_token is not None and len(email_confirmation_token) > 350:
            raise ValueError("Invalid value for `email_confirmation_token`, length must be less than or equal to `350`")  # noqa: E501
        if email_confirmation_token is not None and len(email_confirmation_token) < 100:
            raise ValueError("Invalid value for `email_confirmation_token`, length must be greater than or equal to `100`")  # noqa: E501

        self._email_confirmation_token = email_confirmation_token

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(RequestEmailConfirmation, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, RequestEmailConfirmation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
