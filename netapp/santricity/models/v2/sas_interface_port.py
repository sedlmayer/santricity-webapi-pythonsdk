# coding: utf-8

"""
SasInterfacePort.py

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


class SasInterfacePort(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        SasInterfacePort - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'channel': 'int',  # (required parameter)
            'current_interface_speed': 'str',  # (required parameter)
            'maximum_interface_speed': 'str',  # (required parameter)
            'part': 'str',  # (required parameter)
            'revision': 'int',  # (required parameter)
            'is_degraded': 'bool',  # (required parameter)
            'ioc_port': 'SasPort',  # (required parameter)
            'interface_ref': 'str',  # (required parameter)
            'physical_location': 'Location',  # (required parameter)
            'protection_information_capable': 'bool',  # (required parameter)
            'one_way_max_rate': 'int',  # (required parameter)
            'bidirectional_max_rate': 'int',  # (required parameter)
            'controller_id': 'str',  
            'interface_id': 'str',  
            'base_port_address': 'str',  
            'address_id': 'str',  
            'nice_address_id': 'str',  
            'id': 'str'
        }

        self.attribute_map = {
            'channel': 'channel',  # (required parameter)
            'current_interface_speed': 'currentInterfaceSpeed',  # (required parameter)
            'maximum_interface_speed': 'maximumInterfaceSpeed',  # (required parameter)
            'part': 'part',  # (required parameter)
            'revision': 'revision',  # (required parameter)
            'is_degraded': 'isDegraded',  # (required parameter)
            'ioc_port': 'iocPort',  # (required parameter)
            'interface_ref': 'interfaceRef',  # (required parameter)
            'physical_location': 'physicalLocation',  # (required parameter)
            'protection_information_capable': 'protectionInformationCapable',  # (required parameter)
            'one_way_max_rate': 'oneWayMaxRate',  # (required parameter)
            'bidirectional_max_rate': 'bidirectionalMaxRate',  # (required parameter)
            'controller_id': 'controllerId',  
            'interface_id': 'interfaceId',  
            'base_port_address': 'basePortAddress',  
            'address_id': 'addressId',  
            'nice_address_id': 'niceAddressId',  
            'id': 'id'
        }

        self._channel = None
        self._current_interface_speed = None
        self._maximum_interface_speed = None
        self._part = None
        self._revision = None
        self._is_degraded = None
        self._ioc_port = None
        self._interface_ref = None
        self._physical_location = None
        self._protection_information_capable = None
        self._one_way_max_rate = None
        self._bidirectional_max_rate = None
        self._controller_id = None
        self._interface_id = None
        self._base_port_address = None
        self._address_id = None
        self._nice_address_id = None
        self._id = None

    @property
    def channel(self):
        """
        Gets the channel of this SasInterfacePort.
        The number of the channel corresponding to this interface.

        :return: The channel of this SasInterfacePort.
        :rtype: int
        :required/optional: required
        """
        return self._channel

    @channel.setter
    def channel(self, channel):
        """
        Sets the channel of this SasInterfacePort.
        The number of the channel corresponding to this interface.

        :param channel: The channel of this SasInterfacePort.
        :type: int
        """
        self._channel = channel

    @property
    def current_interface_speed(self):
        """
        Gets the current_interface_speed of this SasInterfacePort.
        The current interface speed of the SAS interface.

        :return: The current_interface_speed of this SasInterfacePort.
        :rtype: str
        :required/optional: required
        """
        return self._current_interface_speed

    @current_interface_speed.setter
    def current_interface_speed(self, current_interface_speed):
        """
        Sets the current_interface_speed of this SasInterfacePort.
        The current interface speed of the SAS interface.

        :param current_interface_speed: The current_interface_speed of this SasInterfacePort.
        :type: str
        """
        allowed_values = ["speedUnknown", "speed1gig", "speed2gig", "speed4gig", "speed10gig", "speed15gig", "speed3gig", "speed10meg", "speed100meg", "speed2pt5Gig", "speed5gig", "speed20gig", "speed30gig", "speed60gig", "speed8gig", "speed6gig", "speed40gig", "speed16gig", "speed56gig", "speed12gig", "speed25gig", "speed32gig", "speed100gig", "__UNDEFINED"]
        if current_interface_speed not in allowed_values:
            raise ValueError(
                "Invalid value for `current_interface_speed`, must be one of {0}"
                .format(allowed_values)
            )
        self._current_interface_speed = current_interface_speed

    @property
    def maximum_interface_speed(self):
        """
        Gets the maximum_interface_speed of this SasInterfacePort.
        The maximum interface speed of the SAS interface.

        :return: The maximum_interface_speed of this SasInterfacePort.
        :rtype: str
        :required/optional: required
        """
        return self._maximum_interface_speed

    @maximum_interface_speed.setter
    def maximum_interface_speed(self, maximum_interface_speed):
        """
        Sets the maximum_interface_speed of this SasInterfacePort.
        The maximum interface speed of the SAS interface.

        :param maximum_interface_speed: The maximum_interface_speed of this SasInterfacePort.
        :type: str
        """
        allowed_values = ["speedUnknown", "speed1gig", "speed2gig", "speed4gig", "speed10gig", "speed15gig", "speed3gig", "speed10meg", "speed100meg", "speed2pt5Gig", "speed5gig", "speed20gig", "speed30gig", "speed60gig", "speed8gig", "speed6gig", "speed40gig", "speed16gig", "speed56gig", "speed12gig", "speed25gig", "speed32gig", "speed100gig", "__UNDEFINED"]
        if maximum_interface_speed not in allowed_values:
            raise ValueError(
                "Invalid value for `maximum_interface_speed`, must be one of {0}"
                .format(allowed_values)
            )
        self._maximum_interface_speed = maximum_interface_speed

    @property
    def part(self):
        """
        Gets the part of this SasInterfacePort.
        A string indicating the chip type.

        :return: The part of this SasInterfacePort.
        :rtype: str
        :required/optional: required
        """
        return self._part

    @part.setter
    def part(self, part):
        """
        Sets the part of this SasInterfacePort.
        A string indicating the chip type.

        :param part: The part of this SasInterfacePort.
        :type: str
        """
        self._part = part

    @property
    def revision(self):
        """
        Gets the revision of this SasInterfacePort.
        The revision level of the firmware on the SAS I/O controller.

        :return: The revision of this SasInterfacePort.
        :rtype: int
        :required/optional: required
        """
        return self._revision

    @revision.setter
    def revision(self, revision):
        """
        Sets the revision of this SasInterfacePort.
        The revision level of the firmware on the SAS I/O controller.

        :param revision: The revision of this SasInterfacePort.
        :type: int
        """
        self._revision = revision

    @property
    def is_degraded(self):
        """
        Gets the is_degraded of this SasInterfacePort.
        True if the channel corresponding to this interface is degraded.

        :return: The is_degraded of this SasInterfacePort.
        :rtype: bool
        :required/optional: required
        """
        return self._is_degraded

    @is_degraded.setter
    def is_degraded(self, is_degraded):
        """
        Sets the is_degraded of this SasInterfacePort.
        True if the channel corresponding to this interface is degraded.

        :param is_degraded: The is_degraded of this SasInterfacePort.
        :type: bool
        """
        self._is_degraded = is_degraded

    @property
    def ioc_port(self):
        """
        Gets the ioc_port of this SasInterfacePort.
        Information about the SAS I/O controller port corresponding to this interface.

        :return: The ioc_port of this SasInterfacePort.
        :rtype: SasPort
        :required/optional: required
        """
        return self._ioc_port

    @ioc_port.setter
    def ioc_port(self, ioc_port):
        """
        Sets the ioc_port of this SasInterfacePort.
        Information about the SAS I/O controller port corresponding to this interface.

        :param ioc_port: The ioc_port of this SasInterfacePort.
        :type: SasPort
        """
        self._ioc_port = ioc_port

    @property
    def interface_ref(self):
        """
        Gets the interface_ref of this SasInterfacePort.
        The unique identifier for a given instance of this structure.

        :return: The interface_ref of this SasInterfacePort.
        :rtype: str
        :required/optional: required
        """
        return self._interface_ref

    @interface_ref.setter
    def interface_ref(self, interface_ref):
        """
        Sets the interface_ref of this SasInterfacePort.
        The unique identifier for a given instance of this structure.

        :param interface_ref: The interface_ref of this SasInterfacePort.
        :type: str
        """
        self._interface_ref = interface_ref

    @property
    def physical_location(self):
        """
        Gets the physical_location of this SasInterfacePort.
        The physical location of the SAS interface. The parent reference in Location identifies the physical component (e.g., controller or host card) where the interface circuitry is located, and the position field is a firmware-assigned 1-relative number signifying \"1st SAS interface relative to the parent,\" \"2nd SAS interface relative to the parent,\" etc. This \"interface number\" is independent of the interface's channel association.

        :return: The physical_location of this SasInterfacePort.
        :rtype: Location
        :required/optional: required
        """
        return self._physical_location

    @physical_location.setter
    def physical_location(self, physical_location):
        """
        Sets the physical_location of this SasInterfacePort.
        The physical location of the SAS interface. The parent reference in Location identifies the physical component (e.g., controller or host card) where the interface circuitry is located, and the position field is a firmware-assigned 1-relative number signifying \"1st SAS interface relative to the parent,\" \"2nd SAS interface relative to the parent,\" etc. This \"interface number\" is independent of the interface's channel association.

        :param physical_location: The physical_location of this SasInterfacePort.
        :type: Location
        """
        self._physical_location = physical_location

    @property
    def protection_information_capable(self):
        """
        Gets the protection_information_capable of this SasInterfacePort.
        This field indicates whether or not the I/O interface is PI capable.

        :return: The protection_information_capable of this SasInterfacePort.
        :rtype: bool
        :required/optional: required
        """
        return self._protection_information_capable

    @protection_information_capable.setter
    def protection_information_capable(self, protection_information_capable):
        """
        Sets the protection_information_capable of this SasInterfacePort.
        This field indicates whether or not the I/O interface is PI capable.

        :param protection_information_capable: The protection_information_capable of this SasInterfacePort.
        :type: bool
        """
        self._protection_information_capable = protection_information_capable

    @property
    def one_way_max_rate(self):
        """
        Gets the one_way_max_rate of this SasInterfacePort.
        Maximum one way data rate in B/s

        :return: The one_way_max_rate of this SasInterfacePort.
        :rtype: int
        :required/optional: required
        """
        return self._one_way_max_rate

    @one_way_max_rate.setter
    def one_way_max_rate(self, one_way_max_rate):
        """
        Sets the one_way_max_rate of this SasInterfacePort.
        Maximum one way data rate in B/s

        :param one_way_max_rate: The one_way_max_rate of this SasInterfacePort.
        :type: int
        """
        self._one_way_max_rate = one_way_max_rate

    @property
    def bidirectional_max_rate(self):
        """
        Gets the bidirectional_max_rate of this SasInterfacePort.
        Maximum bi-directional data rate in B/s

        :return: The bidirectional_max_rate of this SasInterfacePort.
        :rtype: int
        :required/optional: required
        """
        return self._bidirectional_max_rate

    @bidirectional_max_rate.setter
    def bidirectional_max_rate(self, bidirectional_max_rate):
        """
        Sets the bidirectional_max_rate of this SasInterfacePort.
        Maximum bi-directional data rate in B/s

        :param bidirectional_max_rate: The bidirectional_max_rate of this SasInterfacePort.
        :type: int
        """
        self._bidirectional_max_rate = bidirectional_max_rate

    @property
    def controller_id(self):
        """
        Gets the controller_id of this SasInterfacePort.


        :return: The controller_id of this SasInterfacePort.
        :rtype: str
        :required/optional: optional
        """
        return self._controller_id

    @controller_id.setter
    def controller_id(self, controller_id):
        """
        Sets the controller_id of this SasInterfacePort.


        :param controller_id: The controller_id of this SasInterfacePort.
        :type: str
        """
        self._controller_id = controller_id

    @property
    def interface_id(self):
        """
        Gets the interface_id of this SasInterfacePort.


        :return: The interface_id of this SasInterfacePort.
        :rtype: str
        :required/optional: optional
        """
        return self._interface_id

    @interface_id.setter
    def interface_id(self, interface_id):
        """
        Sets the interface_id of this SasInterfacePort.


        :param interface_id: The interface_id of this SasInterfacePort.
        :type: str
        """
        self._interface_id = interface_id

    @property
    def base_port_address(self):
        """
        Gets the base_port_address of this SasInterfacePort.


        :return: The base_port_address of this SasInterfacePort.
        :rtype: str
        :required/optional: optional
        """
        return self._base_port_address

    @base_port_address.setter
    def base_port_address(self, base_port_address):
        """
        Sets the base_port_address of this SasInterfacePort.


        :param base_port_address: The base_port_address of this SasInterfacePort.
        :type: str
        """
        self._base_port_address = base_port_address

    @property
    def address_id(self):
        """
        Gets the address_id of this SasInterfacePort.


        :return: The address_id of this SasInterfacePort.
        :rtype: str
        :required/optional: optional
        """
        return self._address_id

    @address_id.setter
    def address_id(self, address_id):
        """
        Sets the address_id of this SasInterfacePort.


        :param address_id: The address_id of this SasInterfacePort.
        :type: str
        """
        self._address_id = address_id

    @property
    def nice_address_id(self):
        """
        Gets the nice_address_id of this SasInterfacePort.


        :return: The nice_address_id of this SasInterfacePort.
        :rtype: str
        :required/optional: optional
        """
        return self._nice_address_id

    @nice_address_id.setter
    def nice_address_id(self, nice_address_id):
        """
        Sets the nice_address_id of this SasInterfacePort.


        :param nice_address_id: The nice_address_id of this SasInterfacePort.
        :type: str
        """
        self._nice_address_id = nice_address_id

    @property
    def id(self):
        """
        Gets the id of this SasInterfacePort.


        :return: The id of this SasInterfacePort.
        :rtype: str
        :required/optional: optional
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this SasInterfacePort.


        :param id: The id of this SasInterfacePort.
        :type: str
        """
        self._id = id

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

