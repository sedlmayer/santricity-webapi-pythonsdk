# coding: utf-8

"""
LegacySnapshotUpdateRequest.py

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


class LegacySnapshotUpdateRequest(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        LegacySnapshotUpdateRequest - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'warning_threshold': 'int',  
            'full_policy': 'str',  
            'new_name': 'str',  
            'recreate_snapshot': 'bool'
        }

        self.attribute_map = {
            'warning_threshold': 'warningThreshold',  
            'full_policy': 'fullPolicy',  
            'new_name': 'newName',  
            'recreate_snapshot': 'recreateSnapshot'
        }

        self._warning_threshold = None
        self._full_policy = None
        self._new_name = None
        self._recreate_snapshot = None

    @property
    def warning_threshold(self):
        """
        Gets the warning_threshold of this LegacySnapshotUpdateRequest.
        Warn the user when the repository is % full.

        :return: The warning_threshold of this LegacySnapshotUpdateRequest.
        :rtype: int
        :required/optional: optional
        """
        return self._warning_threshold

    @warning_threshold.setter
    def warning_threshold(self, warning_threshold):
        """
        Sets the warning_threshold of this LegacySnapshotUpdateRequest.
        Warn the user when the repository is % full.

        :param warning_threshold: The warning_threshold of this LegacySnapshotUpdateRequest.
        :type: int
        """
        self._warning_threshold = warning_threshold

    @property
    def full_policy(self):
        """
        Gets the full_policy of this LegacySnapshotUpdateRequest.
        The behavior on when the data repository becomes full.

        :return: The full_policy of this LegacySnapshotUpdateRequest.
        :rtype: str
        :required/optional: optional
        """
        return self._full_policy

    @full_policy.setter
    def full_policy(self, full_policy):
        """
        Sets the full_policy of this LegacySnapshotUpdateRequest.
        The behavior on when the data repository becomes full.

        :param full_policy: The full_policy of this LegacySnapshotUpdateRequest.
        :type: str
        """
        allowed_values = ["failwrites", "failsnap", "__UNDEFINED", None]
        if full_policy not in allowed_values:
            raise ValueError(
                "Invalid value for `full_policy`, must be one of {0}"
                .format(allowed_values)
            )
        self._full_policy = full_policy

    @property
    def new_name(self):
        """
        Gets the new_name of this LegacySnapshotUpdateRequest.
        New name for the snapshot.

        :return: The new_name of this LegacySnapshotUpdateRequest.
        :rtype: str
        :required/optional: optional
        """
        return self._new_name

    @new_name.setter
    def new_name(self, new_name):
        """
        Sets the new_name of this LegacySnapshotUpdateRequest.
        New name for the snapshot.

        :param new_name: The new_name of this LegacySnapshotUpdateRequest.
        :type: str
        """
        self._new_name = new_name

    @property
    def recreate_snapshot(self):
        """
        Gets the recreate_snapshot of this LegacySnapshotUpdateRequest.
        Recreate the snapshot.

        :return: The recreate_snapshot of this LegacySnapshotUpdateRequest.
        :rtype: bool
        :required/optional: optional
        """
        return self._recreate_snapshot

    @recreate_snapshot.setter
    def recreate_snapshot(self, recreate_snapshot):
        """
        Sets the recreate_snapshot of this LegacySnapshotUpdateRequest.
        Recreate the snapshot.

        :param recreate_snapshot: The recreate_snapshot of this LegacySnapshotUpdateRequest.
        :type: bool
        """
        self._recreate_snapshot = recreate_snapshot

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

