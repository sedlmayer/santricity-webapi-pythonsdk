# coding: utf-8

"""
AsyncMirrorSyncCompletionDetail.py

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


class AsyncMirrorSyncCompletionDetail(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        AsyncMirrorSyncCompletionDetail - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'completion_type': 'str',  # (required parameter)
            'termination_reason': 'str'
        }

        self.attribute_map = {
            'completion_type': 'completionType',  # (required parameter)
            'termination_reason': 'terminationReason'
        }

        self._completion_type = None
        self._termination_reason = None

    @property
    def completion_type(self):
        """
        Gets the completion_type of this AsyncMirrorSyncCompletionDetail.
        This enumeration is used to describe whether synchronization completed or failed during a specific synchronization sample period.

        :return: The completion_type of this AsyncMirrorSyncCompletionDetail.
        :rtype: str
        :required/optional: required
        """
        return self._completion_type

    @completion_type.setter
    def completion_type(self, completion_type):
        """
        Sets the completion_type of this AsyncMirrorSyncCompletionDetail.
        This enumeration is used to describe whether synchronization completed or failed during a specific synchronization sample period.

        :param completion_type: The completion_type of this AsyncMirrorSyncCompletionDetail.
        :type: str
        """
        allowed_values = ["unknown", "terminated", "ok", "__UNDEFINED"]
        if completion_type not in allowed_values:
            raise ValueError(
                "Invalid value for `completion_type`, must be one of {0}"
                .format(allowed_values)
            )
        self._completion_type = completion_type

    @property
    def termination_reason(self):
        """
        Gets the termination_reason of this AsyncMirrorSyncCompletionDetail.
        This field is returned if the value of completionType is equal to ASYNC_MIRROR_SYNC_COMPLETION_TERMINATED.

        :return: The termination_reason of this AsyncMirrorSyncCompletionDetail.
        :rtype: str
        :required/optional: optional
        """
        return self._termination_reason

    @termination_reason.setter
    def termination_reason(self, termination_reason):
        """
        Sets the termination_reason of this AsyncMirrorSyncCompletionDetail.
        This field is returned if the value of completionType is equal to ASYNC_MIRROR_SYNC_COMPLETION_TERMINATED.

        :param termination_reason: The termination_reason of this AsyncMirrorSyncCompletionDetail.
        :type: str
        """
        allowed_values = ["reasonUnknown", "primaryRepositoryFull", "secondaryRepositoryFull", "primaryError", "secondaryError", "interruption", "configError", "userSuspend", "__UNDEFINED", None]
        if termination_reason not in allowed_values:
            raise ValueError(
                "Invalid value for `termination_reason`, must be one of {0}"
                .format(allowed_values)
            )
        self._termination_reason = termination_reason

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

