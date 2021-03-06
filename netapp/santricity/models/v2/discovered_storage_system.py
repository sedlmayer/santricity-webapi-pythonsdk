# coding: utf-8

"""
DiscoveredStorageSystem.py

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


class DiscoveredStorageSystem(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        DiscoveredStorageSystem - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'serial_number': 'str',  # (required parameter)
            'wwn': 'str',  # (required parameter)
            'label': 'str',  # (required parameter)
            'firmware': 'str',  # (required parameter)
            'nvsram': 'str',  # (required parameter)
            'ip_addresses': 'list[str]',  # (required parameter)
            'needs_attention': 'bool'
        }

        self.attribute_map = {
            'serial_number': 'serialNumber',  # (required parameter)
            'wwn': 'wwn',  # (required parameter)
            'label': 'label',  # (required parameter)
            'firmware': 'firmware',  # (required parameter)
            'nvsram': 'nvsram',  # (required parameter)
            'ip_addresses': 'ipAddresses',  # (required parameter)
            'needs_attention': 'needsAttention'
        }

        self._serial_number = None
        self._wwn = None
        self._label = None
        self._firmware = None
        self._nvsram = None
        self._ip_addresses = None
        self._needs_attention = None

    @property
    def serial_number(self):
        """
        Gets the serial_number of this DiscoveredStorageSystem.
        Serial number for the chassis

        :return: The serial_number of this DiscoveredStorageSystem.
        :rtype: str
        :required/optional: required
        """
        return self._serial_number

    @serial_number.setter
    def serial_number(self, serial_number):
        """
        Sets the serial_number of this DiscoveredStorageSystem.
        Serial number for the chassis

        :param serial_number: The serial_number of this DiscoveredStorageSystem.
        :type: str
        """
        self._serial_number = serial_number

    @property
    def wwn(self):
        """
        Gets the wwn of this DiscoveredStorageSystem.
        WWN for the storage system

        :return: The wwn of this DiscoveredStorageSystem.
        :rtype: str
        :required/optional: required
        """
        return self._wwn

    @wwn.setter
    def wwn(self, wwn):
        """
        Sets the wwn of this DiscoveredStorageSystem.
        WWN for the storage system

        :param wwn: The wwn of this DiscoveredStorageSystem.
        :type: str
        """
        self._wwn = wwn

    @property
    def label(self):
        """
        Gets the label of this DiscoveredStorageSystem.
        Label for the storage system

        :return: The label of this DiscoveredStorageSystem.
        :rtype: str
        :required/optional: required
        """
        return self._label

    @label.setter
    def label(self, label):
        """
        Sets the label of this DiscoveredStorageSystem.
        Label for the storage system

        :param label: The label of this DiscoveredStorageSystem.
        :type: str
        """
        self._label = label

    @property
    def firmware(self):
        """
        Gets the firmware of this DiscoveredStorageSystem.
        Firmware version for the storage system

        :return: The firmware of this DiscoveredStorageSystem.
        :rtype: str
        :required/optional: required
        """
        return self._firmware

    @firmware.setter
    def firmware(self, firmware):
        """
        Sets the firmware of this DiscoveredStorageSystem.
        Firmware version for the storage system

        :param firmware: The firmware of this DiscoveredStorageSystem.
        :type: str
        """
        self._firmware = firmware

    @property
    def nvsram(self):
        """
        Gets the nvsram of this DiscoveredStorageSystem.
        NVSRAM version for the storage system

        :return: The nvsram of this DiscoveredStorageSystem.
        :rtype: str
        :required/optional: required
        """
        return self._nvsram

    @nvsram.setter
    def nvsram(self, nvsram):
        """
        Sets the nvsram of this DiscoveredStorageSystem.
        NVSRAM version for the storage system

        :param nvsram: The nvsram of this DiscoveredStorageSystem.
        :type: str
        """
        self._nvsram = nvsram

    @property
    def ip_addresses(self):
        """
        Gets the ip_addresses of this DiscoveredStorageSystem.
        Discovered controller IP addresses for the storage system

        :return: The ip_addresses of this DiscoveredStorageSystem.
        :rtype: list[str]
        :required/optional: required
        """
        return self._ip_addresses

    @ip_addresses.setter
    def ip_addresses(self, ip_addresses):
        """
        Sets the ip_addresses of this DiscoveredStorageSystem.
        Discovered controller IP addresses for the storage system

        :param ip_addresses: The ip_addresses of this DiscoveredStorageSystem.
        :type: list[str]
        """
        self._ip_addresses = ip_addresses

    @property
    def needs_attention(self):
        """
        Gets the needs_attention of this DiscoveredStorageSystem.
        Needs attention alert for the storage system

        :return: The needs_attention of this DiscoveredStorageSystem.
        :rtype: bool
        :required/optional: required
        """
        return self._needs_attention

    @needs_attention.setter
    def needs_attention(self, needs_attention):
        """
        Sets the needs_attention of this DiscoveredStorageSystem.
        Needs attention alert for the storage system

        :param needs_attention: The needs_attention of this DiscoveredStorageSystem.
        :type: bool
        """
        self._needs_attention = needs_attention

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

