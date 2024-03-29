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


class RequestCreateStation(object):
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
        'display_name': 'str',
        'password': 'str'
    }

    attribute_map = {
        'display_name': 'displayName',
        'password': 'password'
    }

    def __init__(self, display_name=None, password=None):  # noqa: E501
        """RequestCreateStation - a model defined in Swagger"""  # noqa: E501

        self._display_name = None
        self._password = None
        self.discriminator = None

        self.display_name = display_name
        self.password = password

    @property
    def display_name(self):
        """Gets the display_name of this RequestCreateStation.  # noqa: E501


        :return: The display_name of this RequestCreateStation.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this RequestCreateStation.


        :param display_name: The display_name of this RequestCreateStation.  # noqa: E501
        :type: str
        """
        if display_name is None:
            raise ValueError("Invalid value for `display_name`, must not be `None`")  # noqa: E501
        if display_name is not None and len(display_name) > 30:
            raise ValueError("Invalid value for `display_name`, length must be less than or equal to `30`")  # noqa: E501
        if display_name is not None and len(display_name) < 3:
            raise ValueError("Invalid value for `display_name`, length must be greater than or equal to `3`")  # noqa: E501

        self._display_name = display_name

    @property
    def password(self):
        """Gets the password of this RequestCreateStation.  # noqa: E501


        :return: The password of this RequestCreateStation.  # noqa: E501
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this RequestCreateStation.


        :param password: The password of this RequestCreateStation.  # noqa: E501
        :type: str
        """
        if password is None:
            raise ValueError("Invalid value for `password`, must not be `None`")  # noqa: E501
        if password is not None and len(password) > 80:
            raise ValueError("Invalid value for `password`, length must be less than or equal to `80`")  # noqa: E501
        if password is not None and len(password) < 10:
            raise ValueError("Invalid value for `password`, length must be greater than or equal to `10`")  # noqa: E501

        self._password = password

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
        if issubclass(RequestCreateStation, dict):
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
        if not isinstance(other, RequestCreateStation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
