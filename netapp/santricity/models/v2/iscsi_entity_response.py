# coding: utf-8

"""
IscsiEntityResponse.py

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


class IscsiEntityResponse(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        IscsiEntityResponse - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'icmp_ping_response_enabled': 'bool',  
            'unnamed_discovery_sessions_enabled': 'bool',  
            'isns_server_tcp_listen_port': 'int',  
            'ipv4_isns_server_address': 'str',  
            'ipv6_isns_server_address': 'str',  
            'isns_server_registration_enabled': 'bool',  
            'host_ports_configured_dhcp': 'bool',  
            'ipv4_isns_server_address_config_method': 'str',  
            'ipv6_isns_server_address_config_method': 'str',  
            'isns_registration_state': 'str'
        }

        self.attribute_map = {
            'icmp_ping_response_enabled': 'icmpPingResponseEnabled',  
            'unnamed_discovery_sessions_enabled': 'unnamedDiscoverySessionsEnabled',  
            'isns_server_tcp_listen_port': 'isnsServerTcpListenPort',  
            'ipv4_isns_server_address': 'ipv4IsnsServerAddress',  
            'ipv6_isns_server_address': 'ipv6IsnsServerAddress',  
            'isns_server_registration_enabled': 'isnsServerRegistrationEnabled',  
            'host_ports_configured_dhcp': 'hostPortsConfiguredDHCP',  
            'ipv4_isns_server_address_config_method': 'ipv4IsnsServerAddressConfigMethod',  
            'ipv6_isns_server_address_config_method': 'ipv6IsnsServerAddressConfigMethod',  
            'isns_registration_state': 'isnsRegistrationState'
        }

        self._icmp_ping_response_enabled = None
        self._unnamed_discovery_sessions_enabled = None
        self._isns_server_tcp_listen_port = None
        self._ipv4_isns_server_address = None
        self._ipv6_isns_server_address = None
        self._isns_server_registration_enabled = None
        self._host_ports_configured_dhcp = None
        self._ipv4_isns_server_address_config_method = None
        self._ipv6_isns_server_address_config_method = None
        self._isns_registration_state = None

    @property
    def icmp_ping_response_enabled(self):
        """
        Gets the icmp_ping_response_enabled of this IscsiEntityResponse.


        :return: The icmp_ping_response_enabled of this IscsiEntityResponse.
        :rtype: bool
        :required/optional: optional
        """
        return self._icmp_ping_response_enabled

    @icmp_ping_response_enabled.setter
    def icmp_ping_response_enabled(self, icmp_ping_response_enabled):
        """
        Sets the icmp_ping_response_enabled of this IscsiEntityResponse.


        :param icmp_ping_response_enabled: The icmp_ping_response_enabled of this IscsiEntityResponse.
        :type: bool
        """
        self._icmp_ping_response_enabled = icmp_ping_response_enabled

    @property
    def unnamed_discovery_sessions_enabled(self):
        """
        Gets the unnamed_discovery_sessions_enabled of this IscsiEntityResponse.


        :return: The unnamed_discovery_sessions_enabled of this IscsiEntityResponse.
        :rtype: bool
        :required/optional: optional
        """
        return self._unnamed_discovery_sessions_enabled

    @unnamed_discovery_sessions_enabled.setter
    def unnamed_discovery_sessions_enabled(self, unnamed_discovery_sessions_enabled):
        """
        Sets the unnamed_discovery_sessions_enabled of this IscsiEntityResponse.


        :param unnamed_discovery_sessions_enabled: The unnamed_discovery_sessions_enabled of this IscsiEntityResponse.
        :type: bool
        """
        self._unnamed_discovery_sessions_enabled = unnamed_discovery_sessions_enabled

    @property
    def isns_server_tcp_listen_port(self):
        """
        Gets the isns_server_tcp_listen_port of this IscsiEntityResponse.


        :return: The isns_server_tcp_listen_port of this IscsiEntityResponse.
        :rtype: int
        :required/optional: optional
        """
        return self._isns_server_tcp_listen_port

    @isns_server_tcp_listen_port.setter
    def isns_server_tcp_listen_port(self, isns_server_tcp_listen_port):
        """
        Sets the isns_server_tcp_listen_port of this IscsiEntityResponse.


        :param isns_server_tcp_listen_port: The isns_server_tcp_listen_port of this IscsiEntityResponse.
        :type: int
        """
        self._isns_server_tcp_listen_port = isns_server_tcp_listen_port

    @property
    def ipv4_isns_server_address(self):
        """
        Gets the ipv4_isns_server_address of this IscsiEntityResponse.


        :return: The ipv4_isns_server_address of this IscsiEntityResponse.
        :rtype: str
        :required/optional: optional
        """
        return self._ipv4_isns_server_address

    @ipv4_isns_server_address.setter
    def ipv4_isns_server_address(self, ipv4_isns_server_address):
        """
        Sets the ipv4_isns_server_address of this IscsiEntityResponse.


        :param ipv4_isns_server_address: The ipv4_isns_server_address of this IscsiEntityResponse.
        :type: str
        """
        self._ipv4_isns_server_address = ipv4_isns_server_address

    @property
    def ipv6_isns_server_address(self):
        """
        Gets the ipv6_isns_server_address of this IscsiEntityResponse.


        :return: The ipv6_isns_server_address of this IscsiEntityResponse.
        :rtype: str
        :required/optional: optional
        """
        return self._ipv6_isns_server_address

    @ipv6_isns_server_address.setter
    def ipv6_isns_server_address(self, ipv6_isns_server_address):
        """
        Sets the ipv6_isns_server_address of this IscsiEntityResponse.


        :param ipv6_isns_server_address: The ipv6_isns_server_address of this IscsiEntityResponse.
        :type: str
        """
        self._ipv6_isns_server_address = ipv6_isns_server_address

    @property
    def isns_server_registration_enabled(self):
        """
        Gets the isns_server_registration_enabled of this IscsiEntityResponse.


        :return: The isns_server_registration_enabled of this IscsiEntityResponse.
        :rtype: bool
        :required/optional: optional
        """
        return self._isns_server_registration_enabled

    @isns_server_registration_enabled.setter
    def isns_server_registration_enabled(self, isns_server_registration_enabled):
        """
        Sets the isns_server_registration_enabled of this IscsiEntityResponse.


        :param isns_server_registration_enabled: The isns_server_registration_enabled of this IscsiEntityResponse.
        :type: bool
        """
        self._isns_server_registration_enabled = isns_server_registration_enabled

    @property
    def host_ports_configured_dhcp(self):
        """
        Gets the host_ports_configured_dhcp of this IscsiEntityResponse.


        :return: The host_ports_configured_dhcp of this IscsiEntityResponse.
        :rtype: bool
        :required/optional: optional
        """
        return self._host_ports_configured_dhcp

    @host_ports_configured_dhcp.setter
    def host_ports_configured_dhcp(self, host_ports_configured_dhcp):
        """
        Sets the host_ports_configured_dhcp of this IscsiEntityResponse.


        :param host_ports_configured_dhcp: The host_ports_configured_dhcp of this IscsiEntityResponse.
        :type: bool
        """
        self._host_ports_configured_dhcp = host_ports_configured_dhcp

    @property
    def ipv4_isns_server_address_config_method(self):
        """
        Gets the ipv4_isns_server_address_config_method of this IscsiEntityResponse.


        :return: The ipv4_isns_server_address_config_method of this IscsiEntityResponse.
        :rtype: str
        :required/optional: optional
        """
        return self._ipv4_isns_server_address_config_method

    @ipv4_isns_server_address_config_method.setter
    def ipv4_isns_server_address_config_method(self, ipv4_isns_server_address_config_method):
        """
        Sets the ipv4_isns_server_address_config_method of this IscsiEntityResponse.


        :param ipv4_isns_server_address_config_method: The ipv4_isns_server_address_config_method of this IscsiEntityResponse.
        :type: str
        """
        allowed_values = ["configDhcp", "configStatic", "__UNDEFINED", None]
        if ipv4_isns_server_address_config_method not in allowed_values:
            raise ValueError(
                "Invalid value for `ipv4_isns_server_address_config_method`, must be one of {0}"
                .format(allowed_values)
            )
        self._ipv4_isns_server_address_config_method = ipv4_isns_server_address_config_method

    @property
    def ipv6_isns_server_address_config_method(self):
        """
        Gets the ipv6_isns_server_address_config_method of this IscsiEntityResponse.


        :return: The ipv6_isns_server_address_config_method of this IscsiEntityResponse.
        :rtype: str
        :required/optional: optional
        """
        return self._ipv6_isns_server_address_config_method

    @ipv6_isns_server_address_config_method.setter
    def ipv6_isns_server_address_config_method(self, ipv6_isns_server_address_config_method):
        """
        Sets the ipv6_isns_server_address_config_method of this IscsiEntityResponse.


        :param ipv6_isns_server_address_config_method: The ipv6_isns_server_address_config_method of this IscsiEntityResponse.
        :type: str
        """
        allowed_values = ["configStatic", "configStateless", "__UNDEFINED", None]
        if ipv6_isns_server_address_config_method not in allowed_values:
            raise ValueError(
                "Invalid value for `ipv6_isns_server_address_config_method`, must be one of {0}"
                .format(allowed_values)
            )
        self._ipv6_isns_server_address_config_method = ipv6_isns_server_address_config_method

    @property
    def isns_registration_state(self):
        """
        Gets the isns_registration_state of this IscsiEntityResponse.


        :return: The isns_registration_state of this IscsiEntityResponse.
        :rtype: str
        :required/optional: optional
        """
        return self._isns_registration_state

    @isns_registration_state.setter
    def isns_registration_state(self, isns_registration_state):
        """
        Sets the isns_registration_state of this IscsiEntityResponse.


        :param isns_registration_state: The isns_registration_state of this IscsiEntityResponse.
        :type: str
        """
        allowed_values = ["disabled", "locatingServer", "connectingToServer", "completed", "__UNDEFINED", None]
        if isns_registration_state not in allowed_values:
            raise ValueError(
                "Invalid value for `isns_registration_state`, must be one of {0}"
                .format(allowed_values)
            )
        self._isns_registration_state = isns_registration_state

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

