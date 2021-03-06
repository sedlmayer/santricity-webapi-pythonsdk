# coding: utf-8

"""
ManagementConfigurationRequest.py

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


class ManagementConfigurationRequest(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        ManagementConfigurationRequest - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'controller_ref': 'str',  # (required parameter)
            'enable_remote_access': 'bool',  
            'ipv4_gateway_address': 'str',  
            'ipv6_gateway_address': 'str',  
            'ipv6_static_routable_address': 'str',  
            'interface_ref': 'str',  # (required parameter)
            'interface_name': 'str',  
            'ipv4_enabled': 'bool',  
            'ipv4_address': 'str',  
            'ipv4_subnet_mask': 'str',  
            'ipv4_address_config_method': 'str',  
            'ipv6_enabled': 'bool',  
            'ipv6_local_address': 'str',  
            'ipv6_address_config_method': 'str',  
            'speed_setting': 'str',  
            'dns_acquisition_descriptor': 'DnsAcquisitionDescriptor',  
            'ntp_acquisition_descriptor': 'NtpAcquisitionDescriptor'
        }

        self.attribute_map = {
            'controller_ref': 'controllerRef',  # (required parameter)
            'enable_remote_access': 'enableRemoteAccess',  
            'ipv4_gateway_address': 'ipv4GatewayAddress',  
            'ipv6_gateway_address': 'ipv6GatewayAddress',  
            'ipv6_static_routable_address': 'ipv6StaticRoutableAddress',  
            'interface_ref': 'interfaceRef',  # (required parameter)
            'interface_name': 'interfaceName',  
            'ipv4_enabled': 'ipv4Enabled',  
            'ipv4_address': 'ipv4Address',  
            'ipv4_subnet_mask': 'ipv4SubnetMask',  
            'ipv4_address_config_method': 'ipv4AddressConfigMethod',  
            'ipv6_enabled': 'ipv6Enabled',  
            'ipv6_local_address': 'ipv6LocalAddress',  
            'ipv6_address_config_method': 'ipv6AddressConfigMethod',  
            'speed_setting': 'speedSetting',  
            'dns_acquisition_descriptor': 'dnsAcquisitionDescriptor',  
            'ntp_acquisition_descriptor': 'ntpAcquisitionDescriptor'
        }

        self._controller_ref = None
        self._enable_remote_access = None
        self._ipv4_gateway_address = None
        self._ipv6_gateway_address = None
        self._ipv6_static_routable_address = None
        self._interface_ref = None
        self._interface_name = None
        self._ipv4_enabled = None
        self._ipv4_address = None
        self._ipv4_subnet_mask = None
        self._ipv4_address_config_method = None
        self._ipv6_enabled = None
        self._ipv6_local_address = None
        self._ipv6_address_config_method = None
        self._speed_setting = None
        self._dns_acquisition_descriptor = None
        self._ntp_acquisition_descriptor = None

    @property
    def controller_ref(self):
        """
        Gets the controller_ref of this ManagementConfigurationRequest.


        :return: The controller_ref of this ManagementConfigurationRequest.
        :rtype: str
        :required/optional: required
        """
        return self._controller_ref

    @controller_ref.setter
    def controller_ref(self, controller_ref):
        """
        Sets the controller_ref of this ManagementConfigurationRequest.


        :param controller_ref: The controller_ref of this ManagementConfigurationRequest.
        :type: str
        """
        self._controller_ref = controller_ref

    @property
    def enable_remote_access(self):
        """
        Gets the enable_remote_access of this ManagementConfigurationRequest.
        If set to true, the controller is enabled for establishment of a remote access session. Depending on the controller platform, the method for remote access could be rlogin or telnet

        :return: The enable_remote_access of this ManagementConfigurationRequest.
        :rtype: bool
        :required/optional: optional
        """
        return self._enable_remote_access

    @enable_remote_access.setter
    def enable_remote_access(self, enable_remote_access):
        """
        Sets the enable_remote_access of this ManagementConfigurationRequest.
        If set to true, the controller is enabled for establishment of a remote access session. Depending on the controller platform, the method for remote access could be rlogin or telnet

        :param enable_remote_access: The enable_remote_access of this ManagementConfigurationRequest.
        :type: bool
        """
        self._enable_remote_access = enable_remote_access

    @property
    def ipv4_gateway_address(self):
        """
        Gets the ipv4_gateway_address of this ManagementConfigurationRequest.
        Manually specify the address of the gateway.

        :return: The ipv4_gateway_address of this ManagementConfigurationRequest.
        :rtype: str
        :required/optional: optional
        """
        return self._ipv4_gateway_address

    @ipv4_gateway_address.setter
    def ipv4_gateway_address(self, ipv4_gateway_address):
        """
        Sets the ipv4_gateway_address of this ManagementConfigurationRequest.
        Manually specify the address of the gateway.

        :param ipv4_gateway_address: The ipv4_gateway_address of this ManagementConfigurationRequest.
        :type: str
        """
        self._ipv4_gateway_address = ipv4_gateway_address

    @property
    def ipv6_gateway_address(self):
        """
        Gets the ipv6_gateway_address of this ManagementConfigurationRequest.


        :return: The ipv6_gateway_address of this ManagementConfigurationRequest.
        :rtype: str
        :required/optional: optional
        """
        return self._ipv6_gateway_address

    @ipv6_gateway_address.setter
    def ipv6_gateway_address(self, ipv6_gateway_address):
        """
        Sets the ipv6_gateway_address of this ManagementConfigurationRequest.


        :param ipv6_gateway_address: The ipv6_gateway_address of this ManagementConfigurationRequest.
        :type: str
        """
        self._ipv6_gateway_address = ipv6_gateway_address

    @property
    def ipv6_static_routable_address(self):
        """
        Gets the ipv6_static_routable_address of this ManagementConfigurationRequest.


        :return: The ipv6_static_routable_address of this ManagementConfigurationRequest.
        :rtype: str
        :required/optional: optional
        """
        return self._ipv6_static_routable_address

    @ipv6_static_routable_address.setter
    def ipv6_static_routable_address(self, ipv6_static_routable_address):
        """
        Sets the ipv6_static_routable_address of this ManagementConfigurationRequest.


        :param ipv6_static_routable_address: The ipv6_static_routable_address of this ManagementConfigurationRequest.
        :type: str
        """
        self._ipv6_static_routable_address = ipv6_static_routable_address

    @property
    def interface_ref(self):
        """
        Gets the interface_ref of this ManagementConfigurationRequest.
        Reference to the Ethernet interface to configure

        :return: The interface_ref of this ManagementConfigurationRequest.
        :rtype: str
        :required/optional: required
        """
        return self._interface_ref

    @interface_ref.setter
    def interface_ref(self, interface_ref):
        """
        Sets the interface_ref of this ManagementConfigurationRequest.
        Reference to the Ethernet interface to configure

        :param interface_ref: The interface_ref of this ManagementConfigurationRequest.
        :type: str
        """
        self._interface_ref = interface_ref

    @property
    def interface_name(self):
        """
        Gets the interface_name of this ManagementConfigurationRequest.
        Name of Ethernet port

        :return: The interface_name of this ManagementConfigurationRequest.
        :rtype: str
        :required/optional: optional
        """
        return self._interface_name

    @interface_name.setter
    def interface_name(self, interface_name):
        """
        Sets the interface_name of this ManagementConfigurationRequest.
        Name of Ethernet port

        :param interface_name: The interface_name of this ManagementConfigurationRequest.
        :type: str
        """
        self._interface_name = interface_name

    @property
    def ipv4_enabled(self):
        """
        Gets the ipv4_enabled of this ManagementConfigurationRequest.
        True if 'ipv4' is to be enabled for this interface; otherwise false.

        :return: The ipv4_enabled of this ManagementConfigurationRequest.
        :rtype: bool
        :required/optional: optional
        """
        return self._ipv4_enabled

    @ipv4_enabled.setter
    def ipv4_enabled(self, ipv4_enabled):
        """
        Sets the ipv4_enabled of this ManagementConfigurationRequest.
        True if 'ipv4' is to be enabled for this interface; otherwise false.

        :param ipv4_enabled: The ipv4_enabled of this ManagementConfigurationRequest.
        :type: bool
        """
        self._ipv4_enabled = ipv4_enabled

    @property
    def ipv4_address(self):
        """
        Gets the ipv4_address of this ManagementConfigurationRequest.
        The 'ipv4' address for the interface. Required for static configuration.

        :return: The ipv4_address of this ManagementConfigurationRequest.
        :rtype: str
        :required/optional: optional
        """
        return self._ipv4_address

    @ipv4_address.setter
    def ipv4_address(self, ipv4_address):
        """
        Sets the ipv4_address of this ManagementConfigurationRequest.
        The 'ipv4' address for the interface. Required for static configuration.

        :param ipv4_address: The ipv4_address of this ManagementConfigurationRequest.
        :type: str
        """
        self._ipv4_address = ipv4_address

    @property
    def ipv4_subnet_mask(self):
        """
        Gets the ipv4_subnet_mask of this ManagementConfigurationRequest.
        The 'ipv4' subnet mask for the interface. Required for static configuration.

        :return: The ipv4_subnet_mask of this ManagementConfigurationRequest.
        :rtype: str
        :required/optional: optional
        """
        return self._ipv4_subnet_mask

    @ipv4_subnet_mask.setter
    def ipv4_subnet_mask(self, ipv4_subnet_mask):
        """
        Sets the ipv4_subnet_mask of this ManagementConfigurationRequest.
        The 'ipv4' subnet mask for the interface. Required for static configuration.

        :param ipv4_subnet_mask: The ipv4_subnet_mask of this ManagementConfigurationRequest.
        :type: str
        """
        self._ipv4_subnet_mask = ipv4_subnet_mask

    @property
    def ipv4_address_config_method(self):
        """
        Gets the ipv4_address_config_method of this ManagementConfigurationRequest.
        Setting that determines how the 'ipv4' address is configured. Required if ipv4 is enabled.

        :return: The ipv4_address_config_method of this ManagementConfigurationRequest.
        :rtype: str
        :required/optional: optional
        """
        return self._ipv4_address_config_method

    @ipv4_address_config_method.setter
    def ipv4_address_config_method(self, ipv4_address_config_method):
        """
        Sets the ipv4_address_config_method of this ManagementConfigurationRequest.
        Setting that determines how the 'ipv4' address is configured. Required if ipv4 is enabled.

        :param ipv4_address_config_method: The ipv4_address_config_method of this ManagementConfigurationRequest.
        :type: str
        """
        allowed_values = ["configDhcp", "configStatic", "__UNDEFINED", None]
        if ipv4_address_config_method not in allowed_values:
            raise ValueError(
                "Invalid value for `ipv4_address_config_method`, must be one of {0}"
                .format(allowed_values)
            )
        self._ipv4_address_config_method = ipv4_address_config_method

    @property
    def ipv6_enabled(self):
        """
        Gets the ipv6_enabled of this ManagementConfigurationRequest.
        True if 'ipv6' is to be enabled for this interface; otherwise false.

        :return: The ipv6_enabled of this ManagementConfigurationRequest.
        :rtype: bool
        :required/optional: optional
        """
        return self._ipv6_enabled

    @ipv6_enabled.setter
    def ipv6_enabled(self, ipv6_enabled):
        """
        Sets the ipv6_enabled of this ManagementConfigurationRequest.
        True if 'ipv6' is to be enabled for this interface; otherwise false.

        :param ipv6_enabled: The ipv6_enabled of this ManagementConfigurationRequest.
        :type: bool
        """
        self._ipv6_enabled = ipv6_enabled

    @property
    def ipv6_local_address(self):
        """
        Gets the ipv6_local_address of this ManagementConfigurationRequest.
        The 'ipv6' local address for the interface. 

        :return: The ipv6_local_address of this ManagementConfigurationRequest.
        :rtype: str
        :required/optional: optional
        """
        return self._ipv6_local_address

    @ipv6_local_address.setter
    def ipv6_local_address(self, ipv6_local_address):
        """
        Sets the ipv6_local_address of this ManagementConfigurationRequest.
        The 'ipv6' local address for the interface. 

        :param ipv6_local_address: The ipv6_local_address of this ManagementConfigurationRequest.
        :type: str
        """
        self._ipv6_local_address = ipv6_local_address

    @property
    def ipv6_address_config_method(self):
        """
        Gets the ipv6_address_config_method of this ManagementConfigurationRequest.
        The method by which the 'ipv6' address information is configured for the interface.

        :return: The ipv6_address_config_method of this ManagementConfigurationRequest.
        :rtype: str
        :required/optional: optional
        """
        return self._ipv6_address_config_method

    @ipv6_address_config_method.setter
    def ipv6_address_config_method(self, ipv6_address_config_method):
        """
        Sets the ipv6_address_config_method of this ManagementConfigurationRequest.
        The method by which the 'ipv6' address information is configured for the interface.

        :param ipv6_address_config_method: The ipv6_address_config_method of this ManagementConfigurationRequest.
        :type: str
        """
        allowed_values = ["configStatic", "configStateless", "__UNDEFINED", None]
        if ipv6_address_config_method not in allowed_values:
            raise ValueError(
                "Invalid value for `ipv6_address_config_method`, must be one of {0}"
                .format(allowed_values)
            )
        self._ipv6_address_config_method = ipv6_address_config_method

    @property
    def speed_setting(self):
        """
        Gets the speed_setting of this ManagementConfigurationRequest.
        The configured speed setting for the Ethernet interface.

        :return: The speed_setting of this ManagementConfigurationRequest.
        :rtype: str
        :required/optional: optional
        """
        return self._speed_setting

    @speed_setting.setter
    def speed_setting(self, speed_setting):
        """
        Sets the speed_setting of this ManagementConfigurationRequest.
        The configured speed setting for the Ethernet interface.

        :param speed_setting: The speed_setting of this ManagementConfigurationRequest.
        :type: str
        """
        allowed_values = ["speedNone", "speedAutoNegotiated", "speed10MbitHalfDuplex", "speed10MbitFullDuplex", "speed100MbitHalfDuplex", "speed100MbitFullDuplex", "speed1000MbitHalfDuplex", "speed1000MbitFullDuplex", "__UNDEFINED", None]
        if speed_setting not in allowed_values:
            raise ValueError(
                "Invalid value for `speed_setting`, must be one of {0}"
                .format(allowed_values)
            )
        self._speed_setting = speed_setting

    @property
    def dns_acquisition_descriptor(self):
        """
        Gets the dns_acquisition_descriptor of this ManagementConfigurationRequest.
        The configuration for the DNS on this management interface

        :return: The dns_acquisition_descriptor of this ManagementConfigurationRequest.
        :rtype: DnsAcquisitionDescriptor
        :required/optional: optional
        """
        return self._dns_acquisition_descriptor

    @dns_acquisition_descriptor.setter
    def dns_acquisition_descriptor(self, dns_acquisition_descriptor):
        """
        Sets the dns_acquisition_descriptor of this ManagementConfigurationRequest.
        The configuration for the DNS on this management interface

        :param dns_acquisition_descriptor: The dns_acquisition_descriptor of this ManagementConfigurationRequest.
        :type: DnsAcquisitionDescriptor
        """
        self._dns_acquisition_descriptor = dns_acquisition_descriptor

    @property
    def ntp_acquisition_descriptor(self):
        """
        Gets the ntp_acquisition_descriptor of this ManagementConfigurationRequest.
        The configuration for the NTP on this management interface

        :return: The ntp_acquisition_descriptor of this ManagementConfigurationRequest.
        :rtype: NtpAcquisitionDescriptor
        :required/optional: optional
        """
        return self._ntp_acquisition_descriptor

    @ntp_acquisition_descriptor.setter
    def ntp_acquisition_descriptor(self, ntp_acquisition_descriptor):
        """
        Sets the ntp_acquisition_descriptor of this ManagementConfigurationRequest.
        The configuration for the NTP on this management interface

        :param ntp_acquisition_descriptor: The ntp_acquisition_descriptor of this ManagementConfigurationRequest.
        :type: NtpAcquisitionDescriptor
        """
        self._ntp_acquisition_descriptor = ntp_acquisition_descriptor

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

