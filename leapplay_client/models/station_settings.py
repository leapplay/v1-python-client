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


class StationSettings(object):
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
        'station_id': 'str',
        'display_name': 'str',
        'qr_code': 'str',
        'control_mode': 'str'
    }

    attribute_map = {
        'station_id': 'stationId',
        'display_name': 'displayName',
        'qr_code': 'qrCode',
        'control_mode': 'controlMode'
    }

    def __init__(self, station_id=None, display_name=None, qr_code=None, control_mode=None):  # noqa: E501
        """StationSettings - a model defined in Swagger"""  # noqa: E501

        self._station_id = None
        self._display_name = None
        self._qr_code = None
        self._control_mode = None
        self.discriminator = None

        if station_id is not None:
            self.station_id = station_id
        if display_name is not None:
            self.display_name = display_name
        if qr_code is not None:
            self.qr_code = qr_code
        if control_mode is not None:
            self.control_mode = control_mode

    @property
    def station_id(self):
        """Gets the station_id of this StationSettings.  # noqa: E501


        :return: The station_id of this StationSettings.  # noqa: E501
        :rtype: str
        """
        return self._station_id

    @station_id.setter
    def station_id(self, station_id):
        """Sets the station_id of this StationSettings.


        :param station_id: The station_id of this StationSettings.  # noqa: E501
        :type: str
        """

        self._station_id = station_id

    @property
    def display_name(self):
        """Gets the display_name of this StationSettings.  # noqa: E501


        :return: The display_name of this StationSettings.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this StationSettings.


        :param display_name: The display_name of this StationSettings.  # noqa: E501
        :type: str
        """

        self._display_name = display_name

    @property
    def qr_code(self):
        """Gets the qr_code of this StationSettings.  # noqa: E501


        :return: The qr_code of this StationSettings.  # noqa: E501
        :rtype: str
        """
        return self._qr_code

    @qr_code.setter
    def qr_code(self, qr_code):
        """Sets the qr_code of this StationSettings.


        :param qr_code: The qr_code of this StationSettings.  # noqa: E501
        :type: str
        """

        self._qr_code = qr_code

    @property
    def control_mode(self):
        """Gets the control_mode of this StationSettings.  # noqa: E501


        :return: The control_mode of this StationSettings.  # noqa: E501
        :rtype: str
        """
        return self._control_mode

    @control_mode.setter
    def control_mode(self, control_mode):
        """Sets the control_mode of this StationSettings.


        :param control_mode: The control_mode of this StationSettings.  # noqa: E501
        :type: str
        """
        allowed_values = ["Undefined", "Local", "Remote", "RemoteWithQrCode"]  # noqa: E501
        if control_mode not in allowed_values:
            raise ValueError(
                "Invalid value for `control_mode` ({0}), must be one of {1}"  # noqa: E501
                .format(control_mode, allowed_values)
            )

        self._control_mode = control_mode

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
        if issubclass(StationSettings, dict):
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
        if not isinstance(other, StationSettings):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
