# coding: utf-8

"""
IbInterface.py

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


class IbInterface(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        IbInterface - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'interface_ref': 'str',  # (required parameter)
            'channel': 'int',  # (required parameter)
            'channel_port_ref': 'str',  # (required parameter)
            'local_identifier': 'int',  # (required parameter)
            'global_identifier': 'str',  # (required parameter)
            'link_state': 'str',  # (required parameter)
            'port_state': 'str',  # (required parameter)
            'maximum_transmission_unit': 'int',  # (required parameter)
            'current_speed': 'str',  # (required parameter)
            'supported_speed': 'list[str]',  # (required parameter)
            'current_link_width': 'str',  # (required parameter)
            'supported_link_width': 'list[str]',  # (required parameter)
            'current_data_virtual_lanes': 'int',  # (required parameter)
            'maximum_data_virtual_lanes': 'int',  # (required parameter)
            'physical_location': 'Location',  # (required parameter)
            'protection_information_capable': 'bool',  # (required parameter)
            'is_srp_supported': 'bool',  # (required parameter)
            'is_iser_supported': 'bool',  # (required parameter)
            'phys_port_state': 'str',  # (required parameter)
            'one_way_max_rate': 'int',  # (required parameter)
            'bidirectional_max_rate': 'int',  # (required parameter)
            'is_nv_me_supported': 'bool',  # (required parameter)
            'id': 'str'
        }

        self.attribute_map = {
            'interface_ref': 'interfaceRef',  # (required parameter)
            'channel': 'channel',  # (required parameter)
            'channel_port_ref': 'channelPortRef',  # (required parameter)
            'local_identifier': 'localIdentifier',  # (required parameter)
            'global_identifier': 'globalIdentifier',  # (required parameter)
            'link_state': 'linkState',  # (required parameter)
            'port_state': 'portState',  # (required parameter)
            'maximum_transmission_unit': 'maximumTransmissionUnit',  # (required parameter)
            'current_speed': 'currentSpeed',  # (required parameter)
            'supported_speed': 'supportedSpeed',  # (required parameter)
            'current_link_width': 'currentLinkWidth',  # (required parameter)
            'supported_link_width': 'supportedLinkWidth',  # (required parameter)
            'current_data_virtual_lanes': 'currentDataVirtualLanes',  # (required parameter)
            'maximum_data_virtual_lanes': 'maximumDataVirtualLanes',  # (required parameter)
            'physical_location': 'physicalLocation',  # (required parameter)
            'protection_information_capable': 'protectionInformationCapable',  # (required parameter)
            'is_srp_supported': 'isSRPSupported',  # (required parameter)
            'is_iser_supported': 'isISERSupported',  # (required parameter)
            'phys_port_state': 'physPortState',  # (required parameter)
            'one_way_max_rate': 'oneWayMaxRate',  # (required parameter)
            'bidirectional_max_rate': 'bidirectionalMaxRate',  # (required parameter)
            'is_nv_me_supported': 'isNVMeSupported',  # (required parameter)
            'id': 'id'
        }

        self._interface_ref = None
        self._channel = None
        self._channel_port_ref = None
        self._local_identifier = None
        self._global_identifier = None
        self._link_state = None
        self._port_state = None
        self._maximum_transmission_unit = None
        self._current_speed = None
        self._supported_speed = None
        self._current_link_width = None
        self._supported_link_width = None
        self._current_data_virtual_lanes = None
        self._maximum_data_virtual_lanes = None
        self._physical_location = None
        self._protection_information_capable = None
        self._is_srp_supported = None
        self._is_iser_supported = None
        self._phys_port_state = None
        self._one_way_max_rate = None
        self._bidirectional_max_rate = None
        self._is_nv_me_supported = None
        self._id = None

    @property
    def interface_ref(self):
        """
        Gets the interface_ref of this IbInterface.
        The opaque data by which an instance of IbInterface is uniquely identified.

        :return: The interface_ref of this IbInterface.
        :rtype: str
        :required/optional: required
        """
        return self._interface_ref

    @interface_ref.setter
    def interface_ref(self, interface_ref):
        """
        Sets the interface_ref of this IbInterface.
        The opaque data by which an instance of IbInterface is uniquely identified.

        :param interface_ref: The interface_ref of this IbInterface.
        :type: str
        """
        self._interface_ref = interface_ref

    @property
    def channel(self):
        """
        Gets the channel of this IbInterface.
        The number of the host channel associated with this interface.

        :return: The channel of this IbInterface.
        :rtype: int
        :required/optional: required
        """
        return self._channel

    @channel.setter
    def channel(self, channel):
        """
        Sets the channel of this IbInterface.
        The number of the host channel associated with this interface.

        :param channel: The channel of this IbInterface.
        :type: int
        """
        self._channel = channel

    @property
    def channel_port_ref(self):
        """
        Gets the channel_port_ref of this IbInterface.
        A reference to the channel port for the channel associated with this interface.

        :return: The channel_port_ref of this IbInterface.
        :rtype: str
        :required/optional: required
        """
        return self._channel_port_ref

    @channel_port_ref.setter
    def channel_port_ref(self, channel_port_ref):
        """
        Sets the channel_port_ref of this IbInterface.
        A reference to the channel port for the channel associated with this interface.

        :param channel_port_ref: The channel_port_ref of this IbInterface.
        :type: str
        """
        self._channel_port_ref = channel_port_ref

    @property
    def local_identifier(self):
        """
        Gets the local_identifier of this IbInterface.
        The InfiniBand local identifier associated with this interface.

        :return: The local_identifier of this IbInterface.
        :rtype: int
        :required/optional: required
        """
        return self._local_identifier

    @local_identifier.setter
    def local_identifier(self, local_identifier):
        """
        Sets the local_identifier of this IbInterface.
        The InfiniBand local identifier associated with this interface.

        :param local_identifier: The local_identifier of this IbInterface.
        :type: int
        """
        self._local_identifier = local_identifier

    @property
    def global_identifier(self):
        """
        Gets the global_identifier of this IbInterface.
        The InfiniBand global identifier associated with this interface.

        :return: The global_identifier of this IbInterface.
        :rtype: str
        :required/optional: required
        """
        return self._global_identifier

    @global_identifier.setter
    def global_identifier(self, global_identifier):
        """
        Sets the global_identifier of this IbInterface.
        The InfiniBand global identifier associated with this interface.

        :param global_identifier: The global_identifier of this IbInterface.
        :type: str
        """
        self._global_identifier = global_identifier

    @property
    def link_state(self):
        """
        Gets the link_state of this IbInterface.
        The state of the InfiniBand link.

        :return: The link_state of this IbInterface.
        :rtype: str
        :required/optional: required
        """
        return self._link_state

    @link_state.setter
    def link_state(self, link_state):
        """
        Sets the link_state of this IbInterface.
        The state of the InfiniBand link.

        :param link_state: The link_state of this IbInterface.
        :type: str
        """
        allowed_values = ["initialize", "linkArm", "active", "defer", "down", "__UNDEFINED"]
        if link_state not in allowed_values:
            raise ValueError(
                "Invalid value for `link_state`, must be one of {0}"
                .format(allowed_values)
            )
        self._link_state = link_state

    @property
    def port_state(self):
        """
        Gets the port_state of this IbInterface.
        The state of the InfiniBand port.

        :return: The port_state of this IbInterface.
        :rtype: str
        :required/optional: required
        """
        return self._port_state

    @port_state.setter
    def port_state(self, port_state):
        """
        Sets the port_state of this IbInterface.
        The state of the InfiniBand port.

        :param port_state: The port_state of this IbInterface.
        :type: str
        """
        allowed_values = ["unknown", "initialize", "arm", "active", "defer", "down", "__UNDEFINED"]
        if port_state not in allowed_values:
            raise ValueError(
                "Invalid value for `port_state`, must be one of {0}"
                .format(allowed_values)
            )
        self._port_state = port_state

    @property
    def maximum_transmission_unit(self):
        """
        Gets the maximum_transmission_unit of this IbInterface.
        The size in bytes of the largest packet that the interface can transmit.

        :return: The maximum_transmission_unit of this IbInterface.
        :rtype: int
        :required/optional: required
        """
        return self._maximum_transmission_unit

    @maximum_transmission_unit.setter
    def maximum_transmission_unit(self, maximum_transmission_unit):
        """
        Sets the maximum_transmission_unit of this IbInterface.
        The size in bytes of the largest packet that the interface can transmit.

        :param maximum_transmission_unit: The maximum_transmission_unit of this IbInterface.
        :type: int
        """
        self._maximum_transmission_unit = maximum_transmission_unit

    @property
    def current_speed(self):
        """
        Gets the current_speed of this IbInterface.
        The speed at which the interface is currently operating.

        :return: The current_speed of this IbInterface.
        :rtype: str
        :required/optional: required
        """
        return self._current_speed

    @current_speed.setter
    def current_speed(self, current_speed):
        """
        Sets the current_speed of this IbInterface.
        The speed at which the interface is currently operating.

        :param current_speed: The current_speed of this IbInterface.
        :type: str
        """
        allowed_values = ["speedUnknown", "speed1gig", "speed2gig", "speed4gig", "speed10gig", "speed15gig", "speed3gig", "speed10meg", "speed100meg", "speed2pt5Gig", "speed5gig", "speed20gig", "speed30gig", "speed60gig", "speed8gig", "speed6gig", "speed40gig", "speed16gig", "speed56gig", "speed12gig", "speed25gig", "speed32gig", "speed100gig", "__UNDEFINED"]
        if current_speed not in allowed_values:
            raise ValueError(
                "Invalid value for `current_speed`, must be one of {0}"
                .format(allowed_values)
            )
        self._current_speed = current_speed

    @property
    def supported_speed(self):
        """
        Gets the supported_speed of this IbInterface.
        An array containing the different speeds at which the interface is capable of operating.

        :return: The supported_speed of this IbInterface.
        :rtype: list[str]
        :required/optional: required
        """
        return self._supported_speed

    @supported_speed.setter
    def supported_speed(self, supported_speed):
        """
        Sets the supported_speed of this IbInterface.
        An array containing the different speeds at which the interface is capable of operating.

        :param supported_speed: The supported_speed of this IbInterface.
        :type: list[str]
        """
        self._supported_speed = supported_speed

    @property
    def current_link_width(self):
        """
        Gets the current_link_width of this IbInterface.
        The width at which the link is currently operating, e.g., 1 means \"1X,\" 4 means \"4X,\".etc.

        :return: The current_link_width of this IbInterface.
        :rtype: str
        :required/optional: required
        """
        return self._current_link_width

    @current_link_width.setter
    def current_link_width(self, current_link_width):
        """
        Sets the current_link_width of this IbInterface.
        The width at which the link is currently operating, e.g., 1 means \"1X,\" 4 means \"4X,\".etc.

        :param current_link_width: The current_link_width of this IbInterface.
        :type: str
        """
        allowed_values = ["width1x", "width4x", "width8x", "width12x", "__UNDEFINED"]
        if current_link_width not in allowed_values:
            raise ValueError(
                "Invalid value for `current_link_width`, must be one of {0}"
                .format(allowed_values)
            )
        self._current_link_width = current_link_width

    @property
    def supported_link_width(self):
        """
        Gets the supported_link_width of this IbInterface.
        An array containing the different link widths at which the link is capable of operating.

        :return: The supported_link_width of this IbInterface.
        :rtype: list[str]
        :required/optional: required
        """
        return self._supported_link_width

    @supported_link_width.setter
    def supported_link_width(self, supported_link_width):
        """
        Sets the supported_link_width of this IbInterface.
        An array containing the different link widths at which the link is capable of operating.

        :param supported_link_width: The supported_link_width of this IbInterface.
        :type: list[str]
        """
        self._supported_link_width = supported_link_width

    @property
    def current_data_virtual_lanes(self):
        """
        Gets the current_data_virtual_lanes of this IbInterface.
        The number of data virtual lanes that are currently active for this interface.

        :return: The current_data_virtual_lanes of this IbInterface.
        :rtype: int
        :required/optional: required
        """
        return self._current_data_virtual_lanes

    @current_data_virtual_lanes.setter
    def current_data_virtual_lanes(self, current_data_virtual_lanes):
        """
        Sets the current_data_virtual_lanes of this IbInterface.
        The number of data virtual lanes that are currently active for this interface.

        :param current_data_virtual_lanes: The current_data_virtual_lanes of this IbInterface.
        :type: int
        """
        self._current_data_virtual_lanes = current_data_virtual_lanes

    @property
    def maximum_data_virtual_lanes(self):
        """
        Gets the maximum_data_virtual_lanes of this IbInterface.
        The maximum number of data virtual lanes supported by the interface.

        :return: The maximum_data_virtual_lanes of this IbInterface.
        :rtype: int
        :required/optional: required
        """
        return self._maximum_data_virtual_lanes

    @maximum_data_virtual_lanes.setter
    def maximum_data_virtual_lanes(self, maximum_data_virtual_lanes):
        """
        Sets the maximum_data_virtual_lanes of this IbInterface.
        The maximum number of data virtual lanes supported by the interface.

        :param maximum_data_virtual_lanes: The maximum_data_virtual_lanes of this IbInterface.
        :type: int
        """
        self._maximum_data_virtual_lanes = maximum_data_virtual_lanes

    @property
    def physical_location(self):
        """
        Gets the physical_location of this IbInterface.
        The physical location of the Infiniband interface. The parent reference in Location identifies the physical component (e.g., controller or host card) where the interface circuitry is located, and the position field is a firmware-assigned 1-relative number signifying \"1st Infiniband interface relative to the parent,\" \"2nd Infiniband interface relative to the parent,\" etc. This \"interface number\" is independent of the interface's channel association.

        :return: The physical_location of this IbInterface.
        :rtype: Location
        :required/optional: required
        """
        return self._physical_location

    @physical_location.setter
    def physical_location(self, physical_location):
        """
        Sets the physical_location of this IbInterface.
        The physical location of the Infiniband interface. The parent reference in Location identifies the physical component (e.g., controller or host card) where the interface circuitry is located, and the position field is a firmware-assigned 1-relative number signifying \"1st Infiniband interface relative to the parent,\" \"2nd Infiniband interface relative to the parent,\" etc. This \"interface number\" is independent of the interface's channel association.

        :param physical_location: The physical_location of this IbInterface.
        :type: Location
        """
        self._physical_location = physical_location

    @property
    def protection_information_capable(self):
        """
        Gets the protection_information_capable of this IbInterface.
        This field indicates whether or not the I/O interface is PI capable.

        :return: The protection_information_capable of this IbInterface.
        :rtype: bool
        :required/optional: required
        """
        return self._protection_information_capable

    @protection_information_capable.setter
    def protection_information_capable(self, protection_information_capable):
        """
        Sets the protection_information_capable of this IbInterface.
        This field indicates whether or not the I/O interface is PI capable.

        :param protection_information_capable: The protection_information_capable of this IbInterface.
        :type: bool
        """
        self._protection_information_capable = protection_information_capable

    @property
    def is_srp_supported(self):
        """
        Gets the is_srp_supported of this IbInterface.
        This flag is true if SRP (SCSI RDMA Protocol) is currently supported.

        :return: The is_srp_supported of this IbInterface.
        :rtype: bool
        :required/optional: required
        """
        return self._is_srp_supported

    @is_srp_supported.setter
    def is_srp_supported(self, is_srp_supported):
        """
        Sets the is_srp_supported of this IbInterface.
        This flag is true if SRP (SCSI RDMA Protocol) is currently supported.

        :param is_srp_supported: The is_srp_supported of this IbInterface.
        :type: bool
        """
        self._is_srp_supported = is_srp_supported

    @property
    def is_iser_supported(self):
        """
        Gets the is_iser_supported of this IbInterface.
        This flag is true if iSER (iSCSI Extensions for RDMA) is currently supported.

        :return: The is_iser_supported of this IbInterface.
        :rtype: bool
        :required/optional: required
        """
        return self._is_iser_supported

    @is_iser_supported.setter
    def is_iser_supported(self, is_iser_supported):
        """
        Sets the is_iser_supported of this IbInterface.
        This flag is true if iSER (iSCSI Extensions for RDMA) is currently supported.

        :param is_iser_supported: The is_iser_supported of this IbInterface.
        :type: bool
        """
        self._is_iser_supported = is_iser_supported

    @property
    def phys_port_state(self):
        """
        Gets the phys_port_state of this IbInterface.
        This element contains the current state of the physical Infiniband port.

        :return: The phys_port_state of this IbInterface.
        :rtype: str
        :required/optional: required
        """
        return self._phys_port_state

    @phys_port_state.setter
    def phys_port_state(self, phys_port_state):
        """
        Sets the phys_port_state of this IbInterface.
        This element contains the current state of the physical Infiniband port.

        :param phys_port_state: The phys_port_state of this IbInterface.
        :type: str
        """
        allowed_values = ["unknown", "sleep", "polling", "disabled", "cfgTrain", "linkUp", "linkErrRec", "phyTest", "__UNDEFINED"]
        if phys_port_state not in allowed_values:
            raise ValueError(
                "Invalid value for `phys_port_state`, must be one of {0}"
                .format(allowed_values)
            )
        self._phys_port_state = phys_port_state

    @property
    def one_way_max_rate(self):
        """
        Gets the one_way_max_rate of this IbInterface.
        Maximum one way data rate in B/s

        :return: The one_way_max_rate of this IbInterface.
        :rtype: int
        :required/optional: required
        """
        return self._one_way_max_rate

    @one_way_max_rate.setter
    def one_way_max_rate(self, one_way_max_rate):
        """
        Sets the one_way_max_rate of this IbInterface.
        Maximum one way data rate in B/s

        :param one_way_max_rate: The one_way_max_rate of this IbInterface.
        :type: int
        """
        self._one_way_max_rate = one_way_max_rate

    @property
    def bidirectional_max_rate(self):
        """
        Gets the bidirectional_max_rate of this IbInterface.
        Maximum bi-directional data rate in B/s

        :return: The bidirectional_max_rate of this IbInterface.
        :rtype: int
        :required/optional: required
        """
        return self._bidirectional_max_rate

    @bidirectional_max_rate.setter
    def bidirectional_max_rate(self, bidirectional_max_rate):
        """
        Sets the bidirectional_max_rate of this IbInterface.
        Maximum bi-directional data rate in B/s

        :param bidirectional_max_rate: The bidirectional_max_rate of this IbInterface.
        :type: int
        """
        self._bidirectional_max_rate = bidirectional_max_rate

    @property
    def is_nv_me_supported(self):
        """
        Gets the is_nv_me_supported of this IbInterface.
        Indicates if the interface is configured to support NVMe over Fabrics protocol

        :return: The is_nv_me_supported of this IbInterface.
        :rtype: bool
        :required/optional: required
        """
        return self._is_nv_me_supported

    @is_nv_me_supported.setter
    def is_nv_me_supported(self, is_nv_me_supported):
        """
        Sets the is_nv_me_supported of this IbInterface.
        Indicates if the interface is configured to support NVMe over Fabrics protocol

        :param is_nv_me_supported: The is_nv_me_supported of this IbInterface.
        :type: bool
        """
        self._is_nv_me_supported = is_nv_me_supported

    @property
    def id(self):
        """
        Gets the id of this IbInterface.


        :return: The id of this IbInterface.
        :rtype: str
        :required/optional: optional
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this IbInterface.


        :param id: The id of this IbInterface.
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

