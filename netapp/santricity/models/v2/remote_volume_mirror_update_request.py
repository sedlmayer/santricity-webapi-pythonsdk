# coding: utf-8

"""
RemoteVolumeMirrorUpdateRequest.py

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


class RemoteVolumeMirrorUpdateRequest(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        RemoteVolumeMirrorUpdateRequest - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'base_volume_id': 'str',  # (required parameter)
            'remote_volume_id': 'str',  # (required parameter)
            'role': 'int',  
            'update_type': 'str',  # (required parameter)
            'priority': 'int',  
            'write_mode': 'int',  
            'auto_resync': 'bool'
        }

        self.attribute_map = {
            'base_volume_id': 'baseVolumeId',  # (required parameter)
            'remote_volume_id': 'remoteVolumeId',  # (required parameter)
            'role': 'role',  
            'update_type': 'updateType',  # (required parameter)
            'priority': 'priority',  
            'write_mode': 'writeMode',  
            'auto_resync': 'autoResync'
        }

        self._base_volume_id = None
        self._remote_volume_id = None
        self._role = None
        self._update_type = None
        self._priority = None
        self._write_mode = None
        self._auto_resync = None

    @property
    def base_volume_id(self):
        """
        Gets the base_volume_id of this RemoteVolumeMirrorUpdateRequest.
        Remote Volume Mirror base volume.

        :return: The base_volume_id of this RemoteVolumeMirrorUpdateRequest.
        :rtype: str
        :required/optional: required
        """
        return self._base_volume_id

    @base_volume_id.setter
    def base_volume_id(self, base_volume_id):
        """
        Sets the base_volume_id of this RemoteVolumeMirrorUpdateRequest.
        Remote Volume Mirror base volume.

        :param base_volume_id: The base_volume_id of this RemoteVolumeMirrorUpdateRequest.
        :type: str
        """
        self._base_volume_id = base_volume_id

    @property
    def remote_volume_id(self):
        """
        Gets the remote_volume_id of this RemoteVolumeMirrorUpdateRequest.
        Remote Volume Mirror remote volume.

        :return: The remote_volume_id of this RemoteVolumeMirrorUpdateRequest.
        :rtype: str
        :required/optional: required
        """
        return self._remote_volume_id

    @remote_volume_id.setter
    def remote_volume_id(self, remote_volume_id):
        """
        Sets the remote_volume_id of this RemoteVolumeMirrorUpdateRequest.
        Remote Volume Mirror remote volume.

        :param remote_volume_id: The remote_volume_id of this RemoteVolumeMirrorUpdateRequest.
        :type: str
        """
        self._remote_volume_id = remote_volume_id

    @property
    def role(self):
        """
        Gets the role of this RemoteVolumeMirrorUpdateRequest.
        Remote Volume Mirror role. 0, set role to primary.  1, set role to secondary

        :return: The role of this RemoteVolumeMirrorUpdateRequest.
        :rtype: int
        :required/optional: optional
        """
        return self._role

    @role.setter
    def role(self, role):
        """
        Sets the role of this RemoteVolumeMirrorUpdateRequest.
        Remote Volume Mirror role. 0, set role to primary.  1, set role to secondary

        :param role: The role of this RemoteVolumeMirrorUpdateRequest.
        :type: int
        """
        self._role = role

    @property
    def update_type(self):
        """
        Gets the update_type of this RemoteVolumeMirrorUpdateRequest.
        Remote Volume Mirror update type request.

        :return: The update_type of this RemoteVolumeMirrorUpdateRequest.
        :rtype: str
        :required/optional: required
        """
        return self._update_type

    @update_type.setter
    def update_type(self, update_type):
        """
        Sets the update_type of this RemoteVolumeMirrorUpdateRequest.
        Remote Volume Mirror update type request.

        :param update_type: The update_type of this RemoteVolumeMirrorUpdateRequest.
        :type: str
        """
        allowed_values = ["suspend", "resume", "resync", "roleChange", "updateParams"]
        if update_type not in allowed_values:
            raise ValueError(
                "Invalid value for `update_type`, must be one of {0}"
                .format(allowed_values)
            )
        self._update_type = update_type

    @property
    def priority(self):
        """
        Gets the priority of this RemoteVolumeMirrorUpdateRequest.


        :return: The priority of this RemoteVolumeMirrorUpdateRequest.
        :rtype: int
        :required/optional: optional
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        """
        Sets the priority of this RemoteVolumeMirrorUpdateRequest.


        :param priority: The priority of this RemoteVolumeMirrorUpdateRequest.
        :type: int
        """
        self._priority = priority

    @property
    def write_mode(self):
        """
        Gets the write_mode of this RemoteVolumeMirrorUpdateRequest.


        :return: The write_mode of this RemoteVolumeMirrorUpdateRequest.
        :rtype: int
        :required/optional: optional
        """
        return self._write_mode

    @write_mode.setter
    def write_mode(self, write_mode):
        """
        Sets the write_mode of this RemoteVolumeMirrorUpdateRequest.


        :param write_mode: The write_mode of this RemoteVolumeMirrorUpdateRequest.
        :type: int
        """
        self._write_mode = write_mode

    @property
    def auto_resync(self):
        """
        Gets the auto_resync of this RemoteVolumeMirrorUpdateRequest.


        :return: The auto_resync of this RemoteVolumeMirrorUpdateRequest.
        :rtype: bool
        :required/optional: optional
        """
        return self._auto_resync

    @auto_resync.setter
    def auto_resync(self, auto_resync):
        """
        Sets the auto_resync of this RemoteVolumeMirrorUpdateRequest.


        :param auto_resync: The auto_resync of this RemoteVolumeMirrorUpdateRequest.
        :type: bool
        """
        self._auto_resync = auto_resync

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

