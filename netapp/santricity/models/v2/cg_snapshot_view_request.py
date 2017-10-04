# coding: utf-8

"""
CGSnapshotViewRequest.py

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


class CGSnapshotViewRequest(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        CGSnapshotViewRequest - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'pit_id': 'str',  # (required parameter)
            'candidate': 'ConcatVolumeCandidate',  
            'access_mode': 'str',  
            'scan_media': 'bool',  
            'validate_parity': 'bool'
        }

        self.attribute_map = {
            'pit_id': 'pitId',  # (required parameter)
            'candidate': 'candidate',  
            'access_mode': 'accessMode',  
            'scan_media': 'scanMedia',  
            'validate_parity': 'validateParity'
        }

        self._pit_id = None
        self._candidate = None
        self._access_mode = None
        self._scan_media = None
        self._validate_parity = None

    @property
    def pit_id(self):
        """
        Gets the pit_id of this CGSnapshotViewRequest.
        The id of the PIT to create a View for.

        :return: The pit_id of this CGSnapshotViewRequest.
        :rtype: str
        :required/optional: required
        """
        return self._pit_id

    @pit_id.setter
    def pit_id(self, pit_id):
        """
        Sets the pit_id of this CGSnapshotViewRequest.
        The id of the PIT to create a View for.

        :param pit_id: The pit_id of this CGSnapshotViewRequest.
        :type: str
        """
        self._pit_id = pit_id

    @property
    def candidate(self):
        """
        Gets the candidate of this CGSnapshotViewRequest.
        A manually specified ConcatVolumeCandidate of type newVol or existingVols. Required if accessMode == readWrite.

        :return: The candidate of this CGSnapshotViewRequest.
        :rtype: ConcatVolumeCandidate
        :required/optional: optional
        """
        return self._candidate

    @candidate.setter
    def candidate(self, candidate):
        """
        Sets the candidate of this CGSnapshotViewRequest.
        A manually specified ConcatVolumeCandidate of type newVol or existingVols. Required if accessMode == readWrite.

        :param candidate: The candidate of this CGSnapshotViewRequest.
        :type: ConcatVolumeCandidate
        """
        self._candidate = candidate

    @property
    def access_mode(self):
        """
        Gets the access_mode of this CGSnapshotViewRequest.
        The access mode determines whether or not a repository volume should be created.

        :return: The access_mode of this CGSnapshotViewRequest.
        :rtype: str
        :required/optional: optional
        """
        return self._access_mode

    @access_mode.setter
    def access_mode(self, access_mode):
        """
        Sets the access_mode of this CGSnapshotViewRequest.
        The access mode determines whether or not a repository volume should be created.

        :param access_mode: The access_mode of this CGSnapshotViewRequest.
        :type: str
        """
        allowed_values = ["modeUnknown", "readWrite", "readOnly", "__UNDEFINED", None]
        if access_mode not in allowed_values:
            raise ValueError(
                "Invalid value for `access_mode`, must be one of {0}"
                .format(allowed_values)
            )
        self._access_mode = access_mode

    @property
    def scan_media(self):
        """
        Gets the scan_media of this CGSnapshotViewRequest.


        :return: The scan_media of this CGSnapshotViewRequest.
        :rtype: bool
        :required/optional: optional
        """
        return self._scan_media

    @scan_media.setter
    def scan_media(self, scan_media):
        """
        Sets the scan_media of this CGSnapshotViewRequest.


        :param scan_media: The scan_media of this CGSnapshotViewRequest.
        :type: bool
        """
        self._scan_media = scan_media

    @property
    def validate_parity(self):
        """
        Gets the validate_parity of this CGSnapshotViewRequest.


        :return: The validate_parity of this CGSnapshotViewRequest.
        :rtype: bool
        :required/optional: optional
        """
        return self._validate_parity

    @validate_parity.setter
    def validate_parity(self, validate_parity):
        """
        Sets the validate_parity of this CGSnapshotViewRequest.


        :param validate_parity: The validate_parity of this CGSnapshotViewRequest.
        :type: bool
        """
        self._validate_parity = validate_parity

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

