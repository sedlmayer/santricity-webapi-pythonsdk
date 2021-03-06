# coding: utf-8

"""
IscsiConnection.py

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


class IscsiConnection(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        IscsiConnection - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'connection_id': 'int',  # (required parameter)
            'iscsi_interface': 'str',  # (required parameter)
            'max_transmit_data_segment_length': 'int',  # (required parameter)
            'sending_markers': 'bool',  # (required parameter)
            'active_iscsi_version': 'str',  # (required parameter)
            'mutual_authentication': 'bool',  # (required parameter)
            'negotiated_settings': 'IscsiNegotiableConnectionSettings',  # (required parameter)
            'endpoints': 'IscsiConnectionEndpoints'
        }

        self.attribute_map = {
            'connection_id': 'connectionId',  # (required parameter)
            'iscsi_interface': 'iscsiInterface',  # (required parameter)
            'max_transmit_data_segment_length': 'maxTransmitDataSegmentLength',  # (required parameter)
            'sending_markers': 'sendingMarkers',  # (required parameter)
            'active_iscsi_version': 'activeIscsiVersion',  # (required parameter)
            'mutual_authentication': 'mutualAuthentication',  # (required parameter)
            'negotiated_settings': 'negotiatedSettings',  # (required parameter)
            'endpoints': 'endpoints'
        }

        self._connection_id = None
        self._iscsi_interface = None
        self._max_transmit_data_segment_length = None
        self._sending_markers = None
        self._active_iscsi_version = None
        self._mutual_authentication = None
        self._negotiated_settings = None
        self._endpoints = None

    @property
    def connection_id(self):
        """
        Gets the connection_id of this IscsiConnection.
        The unique identifier of the connection within the scope of the parent session.

        :return: The connection_id of this IscsiConnection.
        :rtype: int
        :required/optional: required
        """
        return self._connection_id

    @connection_id.setter
    def connection_id(self, connection_id):
        """
        Sets the connection_id of this IscsiConnection.
        The unique identifier of the connection within the scope of the parent session.

        :param connection_id: The connection_id of this IscsiConnection.
        :type: int
        """
        self._connection_id = connection_id

    @property
    def iscsi_interface(self):
        """
        Gets the iscsi_interface of this IscsiConnection.
        A reference to the physical interface to which this connection is bound.

        :return: The iscsi_interface of this IscsiConnection.
        :rtype: str
        :required/optional: required
        """
        return self._iscsi_interface

    @iscsi_interface.setter
    def iscsi_interface(self, iscsi_interface):
        """
        Sets the iscsi_interface of this IscsiConnection.
        A reference to the physical interface to which this connection is bound.

        :param iscsi_interface: The iscsi_interface of this IscsiConnection.
        :type: str
        """
        self._iscsi_interface = iscsi_interface

    @property
    def max_transmit_data_segment_length(self):
        """
        Gets the max_transmit_data_segment_length of this IscsiConnection.
        The maximum data payload size supported for command or data PDUs to be sent on this connection.

        :return: The max_transmit_data_segment_length of this IscsiConnection.
        :rtype: int
        :required/optional: required
        """
        return self._max_transmit_data_segment_length

    @max_transmit_data_segment_length.setter
    def max_transmit_data_segment_length(self, max_transmit_data_segment_length):
        """
        Sets the max_transmit_data_segment_length of this IscsiConnection.
        The maximum data payload size supported for command or data PDUs to be sent on this connection.

        :param max_transmit_data_segment_length: The max_transmit_data_segment_length of this IscsiConnection.
        :type: int
        """
        self._max_transmit_data_segment_length = max_transmit_data_segment_length

    @property
    def sending_markers(self):
        """
        Gets the sending_markers of this IscsiConnection.
        True if this connection is inserting markers in in its outgoing data stream.

        :return: The sending_markers of this IscsiConnection.
        :rtype: bool
        :required/optional: required
        """
        return self._sending_markers

    @sending_markers.setter
    def sending_markers(self, sending_markers):
        """
        Sets the sending_markers of this IscsiConnection.
        True if this connection is inserting markers in in its outgoing data stream.

        :param sending_markers: The sending_markers of this IscsiConnection.
        :type: bool
        """
        self._sending_markers = sending_markers

    @property
    def active_iscsi_version(self):
        """
        Gets the active_iscsi_version of this IscsiConnection.
        The active version number of the iSCSI specification negotiated on this connection.

        :return: The active_iscsi_version of this IscsiConnection.
        :rtype: str
        :required/optional: required
        """
        return self._active_iscsi_version

    @active_iscsi_version.setter
    def active_iscsi_version(self, active_iscsi_version):
        """
        Sets the active_iscsi_version of this IscsiConnection.
        The active version number of the iSCSI specification negotiated on this connection.

        :param active_iscsi_version: The active_iscsi_version of this IscsiConnection.
        :type: str
        """
        self._active_iscsi_version = active_iscsi_version

    @property
    def mutual_authentication(self):
        """
        Gets the mutual_authentication of this IscsiConnection.
        True if the target is required to authenticate itself to the Initiator, in addition to the Initiator authenticating itself to the target.

        :return: The mutual_authentication of this IscsiConnection.
        :rtype: bool
        :required/optional: required
        """
        return self._mutual_authentication

    @mutual_authentication.setter
    def mutual_authentication(self, mutual_authentication):
        """
        Sets the mutual_authentication of this IscsiConnection.
        True if the target is required to authenticate itself to the Initiator, in addition to the Initiator authenticating itself to the target.

        :param mutual_authentication: The mutual_authentication of this IscsiConnection.
        :type: bool
        """
        self._mutual_authentication = mutual_authentication

    @property
    def negotiated_settings(self):
        """
        Gets the negotiated_settings of this IscsiConnection.
        A collection of connection-level settings that are subject to initiator-target negotiation.

        :return: The negotiated_settings of this IscsiConnection.
        :rtype: IscsiNegotiableConnectionSettings
        :required/optional: required
        """
        return self._negotiated_settings

    @negotiated_settings.setter
    def negotiated_settings(self, negotiated_settings):
        """
        Sets the negotiated_settings of this IscsiConnection.
        A collection of connection-level settings that are subject to initiator-target negotiation.

        :param negotiated_settings: The negotiated_settings of this IscsiConnection.
        :type: IscsiNegotiableConnectionSettings
        """
        self._negotiated_settings = negotiated_settings

    @property
    def endpoints(self):
        """
        Gets the endpoints of this IscsiConnection.
        The TCP protocol endpoints of the connection.

        :return: The endpoints of this IscsiConnection.
        :rtype: IscsiConnectionEndpoints
        :required/optional: required
        """
        return self._endpoints

    @endpoints.setter
    def endpoints(self, endpoints):
        """
        Sets the endpoints of this IscsiConnection.
        The TCP protocol endpoints of the connection.

        :param endpoints: The endpoints of this IscsiConnection.
        :type: IscsiConnectionEndpoints
        """
        self._endpoints = endpoints

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

