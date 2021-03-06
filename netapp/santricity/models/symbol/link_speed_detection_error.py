# coding: utf-8

"""
LinkSpeedDetectionError.py

 The Clear BSD License

 Copyright (c) – 2016, NetApp, Inc. All rights reserved.

 Redistribution and use in source and binary forms, with or without modification, are permitted (subject to the limitations in the disclaimer below) provided that the following conditions are met:

 * Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.

 * Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.

 * Neither the name of NetApp, Inc. nor the names of its contributors may be used to endorse or promote products derived from this software without specific prior written permission.

 NO EXPRESS OR IMPLIED LICENSES TO ANY PARTY'S PATENT RIGHTS ARE GRANTED BY THIS LICENSE. THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
"""

from pprint import pformat
from six import iteritems


class LinkSpeedDetectionError(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        LinkSpeedDetectionError - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'parent_ref': 'str',  # (required parameter)
            'channel': 'int',  # (required parameter)
            'channel_port': 'int',  # (required parameter)
            'connector': 'str',  # (required parameter)
            'supported_link_speeds': 'list[str]',  # (required parameter)
            'current_link_speed': 'int',  # (required parameter)
            'manually_bypassed': 'bool',  # (required parameter)
            'supports_speed': 'bool',  # (required parameter)
            'channel_port_ref': 'str'
        }

        self.attribute_map = {
            'parent_ref': 'parentRef',  # (required parameter)
            'channel': 'channel',  # (required parameter)
            'channel_port': 'channelPort',  # (required parameter)
            'connector': 'connector',  # (required parameter)
            'supported_link_speeds': 'supportedLinkSpeeds',  # (required parameter)
            'current_link_speed': 'currentLinkSpeed',  # (required parameter)
            'manually_bypassed': 'manuallyBypassed',  # (required parameter)
            'supports_speed': 'supportsSpeed',  # (required parameter)
            'channel_port_ref': 'channelPortRef'
        }

        self._parent_ref = None
        self._channel = None
        self._channel_port = None
        self._connector = None
        self._supported_link_speeds = None
        self._current_link_speed = None
        self._manually_bypassed = None
        self._supports_speed = None
        self._channel_port_ref = None

    @property
    def parent_ref(self):
        """
        Gets the parent_ref of this LinkSpeedDetectionError.
        The reference for the controller.

        :return: The parent_ref of this LinkSpeedDetectionError.
        :rtype: str
        :required/optional: required
        """
        return self._parent_ref

    @parent_ref.setter
    def parent_ref(self, parent_ref):
        """
        Sets the parent_ref of this LinkSpeedDetectionError.
        The reference for the controller.

        :param parent_ref: The parent_ref of this LinkSpeedDetectionError.
        :type: str
        """
        self._parent_ref = parent_ref

    @property
    def channel(self):
        """
        Gets the channel of this LinkSpeedDetectionError.
        The drive channel identifier.

        :return: The channel of this LinkSpeedDetectionError.
        :rtype: int
        :required/optional: required
        """
        return self._channel

    @channel.setter
    def channel(self, channel):
        """
        Sets the channel of this LinkSpeedDetectionError.
        The drive channel identifier.

        :param channel: The channel of this LinkSpeedDetectionError.
        :type: int
        """
        self._channel = channel

    @property
    def channel_port(self):
        """
        Gets the channel_port of this LinkSpeedDetectionError.
        The channel port identifier.

        :return: The channel_port of this LinkSpeedDetectionError.
        :rtype: int
        :required/optional: required
        """
        return self._channel_port

    @channel_port.setter
    def channel_port(self, channel_port):
        """
        Sets the channel_port of this LinkSpeedDetectionError.
        The channel port identifier.

        :param channel_port: The channel_port of this LinkSpeedDetectionError.
        :type: int
        """
        self._channel_port = channel_port

    @property
    def connector(self):
        """
        Gets the connector of this LinkSpeedDetectionError.
        Connector type from VPD data.

        :return: The connector of this LinkSpeedDetectionError.
        :rtype: str
        :required/optional: required
        """
        return self._connector

    @connector.setter
    def connector(self, connector):
        """
        Sets the connector of this LinkSpeedDetectionError.
        Connector type from VPD data.

        :param connector: The connector of this LinkSpeedDetectionError.
        :type: str
        """
        allowed_values = ["unknown", "sc", "fcs1cc", "fcs2cc", "bncortnc", "fcCoax", "fJack", "lc", "mtRj", "mu", "sg", "optPigtail", "hssdcii", "copPigtail", "rj45", "noSeparableConnector", "__UNDEFINED"]
        if connector not in allowed_values:
            raise ValueError(
                "Invalid value for `connector`, must be one of {0}"
                .format(allowed_values)
            )
        self._connector = connector

    @property
    def supported_link_speeds(self):
        """
        Gets the supported_link_speeds of this LinkSpeedDetectionError.
        Link speeds supported by device.

        :return: The supported_link_speeds of this LinkSpeedDetectionError.
        :rtype: list[str]
        :required/optional: required
        """
        return self._supported_link_speeds

    @supported_link_speeds.setter
    def supported_link_speeds(self, supported_link_speeds):
        """
        Sets the supported_link_speeds of this LinkSpeedDetectionError.
        Link speeds supported by device.

        :param supported_link_speeds: The supported_link_speeds of this LinkSpeedDetectionError.
        :type: list[str]
        """
        self._supported_link_speeds = supported_link_speeds

    @property
    def current_link_speed(self):
        """
        Gets the current_link_speed of this LinkSpeedDetectionError.
        Actual link speed.

        :return: The current_link_speed of this LinkSpeedDetectionError.
        :rtype: int
        :required/optional: required
        """
        return self._current_link_speed

    @current_link_speed.setter
    def current_link_speed(self, current_link_speed):
        """
        Sets the current_link_speed of this LinkSpeedDetectionError.
        Actual link speed.

        :param current_link_speed: The current_link_speed of this LinkSpeedDetectionError.
        :type: int
        """
        self._current_link_speed = current_link_speed

    @property
    def manually_bypassed(self):
        """
        Gets the manually_bypassed of this LinkSpeedDetectionError.
        True if manually bypassed.

        :return: The manually_bypassed of this LinkSpeedDetectionError.
        :rtype: bool
        :required/optional: required
        """
        return self._manually_bypassed

    @manually_bypassed.setter
    def manually_bypassed(self, manually_bypassed):
        """
        Sets the manually_bypassed of this LinkSpeedDetectionError.
        True if manually bypassed.

        :param manually_bypassed: The manually_bypassed of this LinkSpeedDetectionError.
        :type: bool
        """
        self._manually_bypassed = manually_bypassed

    @property
    def supports_speed(self):
        """
        Gets the supports_speed of this LinkSpeedDetectionError.
        True if currentLinkSpeed is also supported

        :return: The supports_speed of this LinkSpeedDetectionError.
        :rtype: bool
        :required/optional: required
        """
        return self._supports_speed

    @supports_speed.setter
    def supports_speed(self, supports_speed):
        """
        Sets the supports_speed of this LinkSpeedDetectionError.
        True if currentLinkSpeed is also supported

        :param supports_speed: The supports_speed of this LinkSpeedDetectionError.
        :type: bool
        """
        self._supports_speed = supports_speed

    @property
    def channel_port_ref(self):
        """
        Gets the channel_port_ref of this LinkSpeedDetectionError.
        A reference to the channel port object identifying where the link speed detection occurred. This field is currently not used.

        :return: The channel_port_ref of this LinkSpeedDetectionError.
        :rtype: str
        :required/optional: required
        """
        return self._channel_port_ref

    @channel_port_ref.setter
    def channel_port_ref(self, channel_port_ref):
        """
        Sets the channel_port_ref of this LinkSpeedDetectionError.
        A reference to the channel port object identifying where the link speed detection occurred. This field is currently not used.

        :param channel_port_ref: The channel_port_ref of this LinkSpeedDetectionError.
        :type: str
        """
        self._channel_port_ref = channel_port_ref

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        if self is None:
           return None
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if self is None or other is None:
            return None
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other

