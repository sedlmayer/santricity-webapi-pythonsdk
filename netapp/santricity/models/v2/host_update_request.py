# coding: utf-8

"""
HostUpdateRequest.py

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


class HostUpdateRequest(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        HostUpdateRequest - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'name': 'str',  
            'group_id': 'str',  
            'ports': 'list[HostPortCreateRequest]',  
            'ports_to_update': 'list[HostPortUpdateRequest]',  
            'ports_to_remove': 'list[str]',  
            'host_type': 'HostType'
        }

        self.attribute_map = {
            'name': 'name',  
            'group_id': 'groupId',  
            'ports': 'ports',  
            'ports_to_update': 'portsToUpdate',  
            'ports_to_remove': 'portsToRemove',  
            'host_type': 'hostType'
        }

        self._name = None
        self._group_id = None
        self._ports = None
        self._ports_to_update = None
        self._ports_to_remove = None
        self._host_type = None

    @property
    def name(self):
        """
        Gets the name of this HostUpdateRequest.
        The user-label to assign to the host (optional).

        :return: The name of this HostUpdateRequest.
        :rtype: str
        :required/optional: optional
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this HostUpdateRequest.
        The user-label to assign to the host (optional).

        :param name: The name of this HostUpdateRequest.
        :type: str
        """
        self._name = name

    @property
    def group_id(self):
        """
        Gets the group_id of this HostUpdateRequest.
        The host group identifier.

        :return: The group_id of this HostUpdateRequest.
        :rtype: str
        :required/optional: optional
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        """
        Sets the group_id of this HostUpdateRequest.
        The host group identifier.

        :param group_id: The group_id of this HostUpdateRequest.
        :type: str
        """
        self._group_id = group_id

    @property
    def ports(self):
        """
        Gets the ports of this HostUpdateRequest.
        A list of host ports to create.

        :return: The ports of this HostUpdateRequest.
        :rtype: list[HostPortCreateRequest]
        :required/optional: optional
        """
        return self._ports

    @ports.setter
    def ports(self, ports):
        """
        Sets the ports of this HostUpdateRequest.
        A list of host ports to create.

        :param ports: The ports of this HostUpdateRequest.
        :type: list[HostPortCreateRequest]
        """
        self._ports = ports

    @property
    def ports_to_update(self):
        """
        Gets the ports_to_update of this HostUpdateRequest.
        A list of host ports to update.

        :return: The ports_to_update of this HostUpdateRequest.
        :rtype: list[HostPortUpdateRequest]
        :required/optional: optional
        """
        return self._ports_to_update

    @ports_to_update.setter
    def ports_to_update(self, ports_to_update):
        """
        Sets the ports_to_update of this HostUpdateRequest.
        A list of host ports to update.

        :param ports_to_update: The ports_to_update of this HostUpdateRequest.
        :type: list[HostPortUpdateRequest]
        """
        self._ports_to_update = ports_to_update

    @property
    def ports_to_remove(self):
        """
        Gets the ports_to_remove of this HostUpdateRequest.
        A list of HostPorts to delete.

        :return: The ports_to_remove of this HostUpdateRequest.
        :rtype: list[str]
        :required/optional: optional
        """
        return self._ports_to_remove

    @ports_to_remove.setter
    def ports_to_remove(self, ports_to_remove):
        """
        Sets the ports_to_remove of this HostUpdateRequest.
        A list of HostPorts to delete.

        :param ports_to_remove: The ports_to_remove of this HostUpdateRequest.
        :type: list[str]
        """
        self._ports_to_remove = ports_to_remove

    @property
    def host_type(self):
        """
        Gets the host_type of this HostUpdateRequest.
        The host type string as returned from /host-types.

        :return: The host_type of this HostUpdateRequest.
        :rtype: HostType
        :required/optional: optional
        """
        return self._host_type

    @host_type.setter
    def host_type(self, host_type):
        """
        Sets the host_type of this HostUpdateRequest.
        The host type string as returned from /host-types.

        :param host_type: The host_type of this HostUpdateRequest.
        :type: HostType
        """
        self._host_type = host_type

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

