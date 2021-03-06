# coding: utf-8

"""
ScsiRemoteTargetConnections.py

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


class ScsiRemoteTargetConnections(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        ScsiRemoteTargetConnections - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'io_interface_type': 'str',  # (required parameter)
            'iscsi_connection_detail': 'IscsiRemoteTargetConnections',  
            'fibre_connection_detail': 'FibreRemoteTargetConnections'
        }

        self.attribute_map = {
            'io_interface_type': 'ioInterfaceType',  # (required parameter)
            'iscsi_connection_detail': 'iscsiConnectionDetail',  
            'fibre_connection_detail': 'fibreConnectionDetail'
        }

        self._io_interface_type = None
        self._iscsi_connection_detail = None
        self._fibre_connection_detail = None

    @property
    def io_interface_type(self):
        """
        Gets the io_interface_type of this ScsiRemoteTargetConnections.
        This enumeration defines the different I/O interface types that may be reported as part of the configuration information associated with a controller.

        :return: The io_interface_type of this ScsiRemoteTargetConnections.
        :rtype: str
        :required/optional: required
        """
        return self._io_interface_type

    @io_interface_type.setter
    def io_interface_type(self, io_interface_type):
        """
        Sets the io_interface_type of this ScsiRemoteTargetConnections.
        This enumeration defines the different I/O interface types that may be reported as part of the configuration information associated with a controller.

        :param io_interface_type: The io_interface_type of this ScsiRemoteTargetConnections.
        :type: str
        """
        allowed_values = ["notImplemented", "scsi", "fc", "sata", "sas", "iscsi", "ib", "fcoe", "nvmeof", "__UNDEFINED"]
        if io_interface_type not in allowed_values:
            raise ValueError(
                "Invalid value for `io_interface_type`, must be one of {0}"
                .format(allowed_values)
            )
        self._io_interface_type = io_interface_type

    @property
    def iscsi_connection_detail(self):
        """
        Gets the iscsi_connection_detail of this ScsiRemoteTargetConnections.
        This field is returned if the value of ioInterfaceType is equal to IO_IF_ISCSI.

        :return: The iscsi_connection_detail of this ScsiRemoteTargetConnections.
        :rtype: IscsiRemoteTargetConnections
        :required/optional: optional
        """
        return self._iscsi_connection_detail

    @iscsi_connection_detail.setter
    def iscsi_connection_detail(self, iscsi_connection_detail):
        """
        Sets the iscsi_connection_detail of this ScsiRemoteTargetConnections.
        This field is returned if the value of ioInterfaceType is equal to IO_IF_ISCSI.

        :param iscsi_connection_detail: The iscsi_connection_detail of this ScsiRemoteTargetConnections.
        :type: IscsiRemoteTargetConnections
        """
        self._iscsi_connection_detail = iscsi_connection_detail

    @property
    def fibre_connection_detail(self):
        """
        Gets the fibre_connection_detail of this ScsiRemoteTargetConnections.
        This field is returned if the value of ioInterfaceType is equal to IO_IF_FC.

        :return: The fibre_connection_detail of this ScsiRemoteTargetConnections.
        :rtype: FibreRemoteTargetConnections
        :required/optional: optional
        """
        return self._fibre_connection_detail

    @fibre_connection_detail.setter
    def fibre_connection_detail(self, fibre_connection_detail):
        """
        Sets the fibre_connection_detail of this ScsiRemoteTargetConnections.
        This field is returned if the value of ioInterfaceType is equal to IO_IF_FC.

        :param fibre_connection_detail: The fibre_connection_detail of this ScsiRemoteTargetConnections.
        :type: FibreRemoteTargetConnections
        """
        self._fibre_connection_detail = fibre_connection_detail

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

