# coding: utf-8

"""
ConcatRepositoryVolume.py

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


class ConcatRepositoryVolume(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        ConcatRepositoryVolume - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'concat_vol_ref': 'str',  # (required parameter)
            'status': 'str',  # (required parameter)
            'member_count': 'int',  # (required parameter)
            'aggregate_capacity': 'int',  # (required parameter)
            'media_scan_params': 'VolumeMediaScanParams',  # (required parameter)
            'volume_handle': 'int',  # (required parameter)
            'allowed_operations': 'VolumePerms',  # (required parameter)
            'member_refs': 'list[str]',  
            'base_object_type': 'str',  
            'base_object_id': 'str',  
            'id': 'str'
        }

        self.attribute_map = {
            'concat_vol_ref': 'concatVolRef',  # (required parameter)
            'status': 'status',  # (required parameter)
            'member_count': 'memberCount',  # (required parameter)
            'aggregate_capacity': 'aggregateCapacity',  # (required parameter)
            'media_scan_params': 'mediaScanParams',  # (required parameter)
            'volume_handle': 'volumeHandle',  # (required parameter)
            'allowed_operations': 'allowedOperations',  # (required parameter)
            'member_refs': 'memberRefs',  
            'base_object_type': 'baseObjectType',  
            'base_object_id': 'baseObjectId',  
            'id': 'id'
        }

        self._concat_vol_ref = None
        self._status = None
        self._member_count = None
        self._aggregate_capacity = None
        self._media_scan_params = None
        self._volume_handle = None
        self._allowed_operations = None
        self._member_refs = None
        self._base_object_type = None
        self._base_object_id = None
        self._id = None

    @property
    def concat_vol_ref(self):
        """
        Gets the concat_vol_ref of this ConcatRepositoryVolume.
        A reference (key) for ConcatVolume.

        :return: The concat_vol_ref of this ConcatRepositoryVolume.
        :rtype: str
        :required/optional: required
        """
        return self._concat_vol_ref

    @concat_vol_ref.setter
    def concat_vol_ref(self, concat_vol_ref):
        """
        Sets the concat_vol_ref of this ConcatRepositoryVolume.
        A reference (key) for ConcatVolume.

        :param concat_vol_ref: The concat_vol_ref of this ConcatRepositoryVolume.
        :type: str
        """
        self._concat_vol_ref = concat_vol_ref

    @property
    def status(self):
        """
        Gets the status of this ConcatRepositoryVolume.
        The status/state of the concatenated volume. This will be the worst status among the member volumes.

        :return: The status of this ConcatRepositoryVolume.
        :rtype: str
        :required/optional: required
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this ConcatRepositoryVolume.
        The status/state of the concatenated volume. This will be the worst status among the member volumes.

        :param status: The status of this ConcatRepositoryVolume.
        :type: str
        """
        allowed_values = ["unknown", "optimal", "degraded", "failed", "__UNDEFINED"]
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status`, must be one of {0}"
                .format(allowed_values)
            )
        self._status = status

    @property
    def member_count(self):
        """
        Gets the member_count of this ConcatRepositoryVolume.
        The number of actual storage volumes comprising this volume. Note that this is just for convenience, this information can be derived from member objects.

        :return: The member_count of this ConcatRepositoryVolume.
        :rtype: int
        :required/optional: required
        """
        return self._member_count

    @member_count.setter
    def member_count(self, member_count):
        """
        Sets the member_count of this ConcatRepositoryVolume.
        The number of actual storage volumes comprising this volume. Note that this is just for convenience, this information can be derived from member objects.

        :param member_count: The member_count of this ConcatRepositoryVolume.
        :type: int
        """
        self._member_count = member_count

    @property
    def aggregate_capacity(self):
        """
        Gets the aggregate_capacity of this ConcatRepositoryVolume.
        The aggregate capacity in bytes of all member volumes.

        :return: The aggregate_capacity of this ConcatRepositoryVolume.
        :rtype: int
        :required/optional: required
        """
        return self._aggregate_capacity

    @aggregate_capacity.setter
    def aggregate_capacity(self, aggregate_capacity):
        """
        Sets the aggregate_capacity of this ConcatRepositoryVolume.
        The aggregate capacity in bytes of all member volumes.

        :param aggregate_capacity: The aggregate_capacity of this ConcatRepositoryVolume.
        :type: int
        """
        self._aggregate_capacity = aggregate_capacity

    @property
    def media_scan_params(self):
        """
        Gets the media_scan_params of this ConcatRepositoryVolume.
        Media scan parameters.

        :return: The media_scan_params of this ConcatRepositoryVolume.
        :rtype: VolumeMediaScanParams
        :required/optional: required
        """
        return self._media_scan_params

    @media_scan_params.setter
    def media_scan_params(self, media_scan_params):
        """
        Sets the media_scan_params of this ConcatRepositoryVolume.
        Media scan parameters.

        :param media_scan_params: The media_scan_params of this ConcatRepositoryVolume.
        :type: VolumeMediaScanParams
        """
        self._media_scan_params = media_scan_params

    @property
    def volume_handle(self):
        """
        Gets the volume_handle of this ConcatRepositoryVolume.
        The volume ssid. This is provided primarily for debug purposes.

        :return: The volume_handle of this ConcatRepositoryVolume.
        :rtype: int
        :required/optional: required
        """
        return self._volume_handle

    @volume_handle.setter
    def volume_handle(self, volume_handle):
        """
        Sets the volume_handle of this ConcatRepositoryVolume.
        The volume ssid. This is provided primarily for debug purposes.

        :param volume_handle: The volume_handle of this ConcatRepositoryVolume.
        :type: int
        """
        self._volume_handle = volume_handle

    @property
    def allowed_operations(self):
        """
        Gets the allowed_operations of this ConcatRepositoryVolume.
        Operations allowed on the ConcatVolume. This can be used if ConcatVolume is ever exposed as a host-addressable volume to specify whether the volume is host-mappable or not (repository volumes would never be mappable).

        :return: The allowed_operations of this ConcatRepositoryVolume.
        :rtype: VolumePerms
        :required/optional: required
        """
        return self._allowed_operations

    @allowed_operations.setter
    def allowed_operations(self, allowed_operations):
        """
        Sets the allowed_operations of this ConcatRepositoryVolume.
        Operations allowed on the ConcatVolume. This can be used if ConcatVolume is ever exposed as a host-addressable volume to specify whether the volume is host-mappable or not (repository volumes would never be mappable).

        :param allowed_operations: The allowed_operations of this ConcatRepositoryVolume.
        :type: VolumePerms
        """
        self._allowed_operations = allowed_operations

    @property
    def member_refs(self):
        """
        Gets the member_refs of this ConcatRepositoryVolume.


        :return: The member_refs of this ConcatRepositoryVolume.
        :rtype: list[str]
        :required/optional: optional
        """
        return self._member_refs

    @member_refs.setter
    def member_refs(self, member_refs):
        """
        Sets the member_refs of this ConcatRepositoryVolume.


        :param member_refs: The member_refs of this ConcatRepositoryVolume.
        :type: list[str]
        """
        self._member_refs = member_refs

    @property
    def base_object_type(self):
        """
        Gets the base_object_type of this ConcatRepositoryVolume.


        :return: The base_object_type of this ConcatRepositoryVolume.
        :rtype: str
        :required/optional: optional
        """
        return self._base_object_type

    @base_object_type.setter
    def base_object_type(self, base_object_type):
        """
        Sets the base_object_type of this ConcatRepositoryVolume.


        :param base_object_type: The base_object_type of this ConcatRepositoryVolume.
        :type: str
        """
        allowed_values = ["unknown", "volume", "pool", "host", "lunMapping", "hostGroup", "thinVolume", "drive", "volumeCopy", "pit", "pitView", "snapshotGroup", "snapshot", "accessVolume", "legacySnapshot", "hostType", "metadataTag", "managementUrl", "folder", "asyncMirrorGroup", "asyncMirrorGroupMember", "asyncMirrorGroupIncompleteMember", "consistencyGroup", "consistencyGroupView", "fan", "battery", "storageSystem", "controller", "powerSupply", "minihub", "esm", "drawer", "hostBoard", "interconnectCRU", "cacheBackupDevice", "tray", "supportCRU", "hostPort", "initiator", "snapshotSchedule", "thermalSensor", "sfp", "flashCache", "featureAttribute", "featureState", "lockKeyId", "remoteVolume", "mirrorVolume", "vaultMirrorVolume", "vaultMirrorGroup", "metadataVolume", "sasPort", "sasExpander", "channelPort", "speedNegError", "snmpAgentBundle", "stagedFirmware", "workload", None]
        if base_object_type not in allowed_values:
            raise ValueError(
                "Invalid value for `base_object_type`, must be one of {0}"
                .format(allowed_values)
            )
        self._base_object_type = base_object_type

    @property
    def base_object_id(self):
        """
        Gets the base_object_id of this ConcatRepositoryVolume.


        :return: The base_object_id of this ConcatRepositoryVolume.
        :rtype: str
        :required/optional: optional
        """
        return self._base_object_id

    @base_object_id.setter
    def base_object_id(self, base_object_id):
        """
        Sets the base_object_id of this ConcatRepositoryVolume.


        :param base_object_id: The base_object_id of this ConcatRepositoryVolume.
        :type: str
        """
        self._base_object_id = base_object_id

    @property
    def id(self):
        """
        Gets the id of this ConcatRepositoryVolume.


        :return: The id of this ConcatRepositoryVolume.
        :rtype: str
        :required/optional: optional
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this ConcatRepositoryVolume.


        :param id: The id of this ConcatRepositoryVolume.
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

