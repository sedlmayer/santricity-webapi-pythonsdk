# coding: utf-8

"""
IpVxAddressData.py

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


class IpVxAddressData(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        IpVxAddressData - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'address_type': 'str',  # (required parameter)
            'ipv4_data': 'IpV4AddressData',  
            'ipv6_data': 'IpV6AddressData'
        }

        self.attribute_map = {
            'address_type': 'addressType',  # (required parameter)
            'ipv4_data': 'ipv4Data',  
            'ipv6_data': 'ipv6Data'
        }

        self._address_type = None
        self._ipv4_data = None
        self._ipv6_data = None

    @property
    def address_type(self):
        """
        Gets the address_type of this IpVxAddressData.
        This enumeration defines the different types of IP addresses, corresponding to different versions of the Internet protocol.

        :return: The address_type of this IpVxAddressData.
        :rtype: str
        :required/optional: required
        """
        return self._address_type

    @address_type.setter
    def address_type(self, address_type):
        """
        Sets the address_type of this IpVxAddressData.
        This enumeration defines the different types of IP addresses, corresponding to different versions of the Internet protocol.

        :param address_type: The address_type of this IpVxAddressData.
        :type: str
        """
        allowed_values = ["ipv4", "ipv6", "__UNDEFINED"]
        if address_type not in allowed_values:
            raise ValueError(
                "Invalid value for `address_type`, must be one of {0}"
                .format(allowed_values)
            )
        self._address_type = address_type

    @property
    def ipv4_data(self):
        """
        Gets the ipv4_data of this IpVxAddressData.
        Contains the various IPV4 address elements.

        :return: The ipv4_data of this IpVxAddressData.
        :rtype: IpV4AddressData
        :required/optional: optional
        """
        return self._ipv4_data

    @ipv4_data.setter
    def ipv4_data(self, ipv4_data):
        """
        Sets the ipv4_data of this IpVxAddressData.
        Contains the various IPV4 address elements.

        :param ipv4_data: The ipv4_data of this IpVxAddressData.
        :type: IpV4AddressData
        """
        self._ipv4_data = ipv4_data

    @property
    def ipv6_data(self):
        """
        Gets the ipv6_data of this IpVxAddressData.
        contains the various IPV6 address elements.

        :return: The ipv6_data of this IpVxAddressData.
        :rtype: IpV6AddressData
        :required/optional: optional
        """
        return self._ipv6_data

    @ipv6_data.setter
    def ipv6_data(self, ipv6_data):
        """
        Sets the ipv6_data of this IpVxAddressData.
        contains the various IPV6 address elements.

        :param ipv6_data: The ipv6_data of this IpVxAddressData.
        :type: IpV6AddressData
        """
        self._ipv6_data = ipv6_data

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

