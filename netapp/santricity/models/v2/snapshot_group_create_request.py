# coding: utf-8

"""
SnapshotGroupCreateRequest.py

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


class SnapshotGroupCreateRequest(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        SnapshotGroupCreateRequest - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'base_mappable_object_id': 'str',  # (required parameter)
            'name': 'str',  # (required parameter)
            'repository_percentage': 'float',  
            'warning_threshold': 'int',  
            'auto_delete_limit': 'int',  
            'full_policy': 'str',  
            'storage_pool_id': 'str',  
            'repository_candidate': 'ConcatVolumeCandidate',  
            'schedule': 'ScheduleCreateRequest'
        }

        self.attribute_map = {
            'base_mappable_object_id': 'baseMappableObjectId',  # (required parameter)
            'name': 'name',  # (required parameter)
            'repository_percentage': 'repositoryPercentage',  
            'warning_threshold': 'warningThreshold',  
            'auto_delete_limit': 'autoDeleteLimit',  
            'full_policy': 'fullPolicy',  
            'storage_pool_id': 'storagePoolId',  
            'repository_candidate': 'repositoryCandidate',  
            'schedule': 'schedule'
        }

        self._base_mappable_object_id = None
        self._name = None
        self._repository_percentage = None
        self._warning_threshold = None
        self._auto_delete_limit = None
        self._full_policy = None
        self._storage_pool_id = None
        self._repository_candidate = None
        self._schedule = None

    @property
    def base_mappable_object_id(self):
        """
        Gets the base_mappable_object_id of this SnapshotGroupCreateRequest.
        The identifier of the volume or thin volume to use as the base for the new snapshot group.

        :return: The base_mappable_object_id of this SnapshotGroupCreateRequest.
        :rtype: str
        :required/optional: required
        """
        return self._base_mappable_object_id

    @base_mappable_object_id.setter
    def base_mappable_object_id(self, base_mappable_object_id):
        """
        Sets the base_mappable_object_id of this SnapshotGroupCreateRequest.
        The identifier of the volume or thin volume to use as the base for the new snapshot group.

        :param base_mappable_object_id: The base_mappable_object_id of this SnapshotGroupCreateRequest.
        :type: str
        """
        self._base_mappable_object_id = base_mappable_object_id

    @property
    def name(self):
        """
        Gets the name of this SnapshotGroupCreateRequest.
        The name of the new snapshot group.

        :return: The name of this SnapshotGroupCreateRequest.
        :rtype: str
        :required/optional: required
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this SnapshotGroupCreateRequest.
        The name of the new snapshot group.

        :param name: The name of this SnapshotGroupCreateRequest.
        :type: str
        """
        self._name = name

    @property
    def repository_percentage(self):
        """
        Gets the repository_percentage of this SnapshotGroupCreateRequest.
        The size of the repository in relation to the size of the base volume.

        :return: The repository_percentage of this SnapshotGroupCreateRequest.
        :rtype: float
        :required/optional: optional
        """
        return self._repository_percentage

    @repository_percentage.setter
    def repository_percentage(self, repository_percentage):
        """
        Sets the repository_percentage of this SnapshotGroupCreateRequest.
        The size of the repository in relation to the size of the base volume.

        :param repository_percentage: The repository_percentage of this SnapshotGroupCreateRequest.
        :type: float
        """
        self._repository_percentage = repository_percentage

    @property
    def warning_threshold(self):
        """
        Gets the warning_threshold of this SnapshotGroupCreateRequest.
        The repository utilization warning threshold, as a percentage of the repository volume capacity.

        :return: The warning_threshold of this SnapshotGroupCreateRequest.
        :rtype: int
        :required/optional: optional
        """
        return self._warning_threshold

    @warning_threshold.setter
    def warning_threshold(self, warning_threshold):
        """
        Sets the warning_threshold of this SnapshotGroupCreateRequest.
        The repository utilization warning threshold, as a percentage of the repository volume capacity.

        :param warning_threshold: The warning_threshold of this SnapshotGroupCreateRequest.
        :type: int
        """
        self._warning_threshold = warning_threshold

    @property
    def auto_delete_limit(self):
        """
        Gets the auto_delete_limit of this SnapshotGroupCreateRequest.
        The automatic deletion indicator. If non-zero, the oldest snapshot image will be automatically deleted when creating a new snapshot image to keep the total number of snapshot images limited to the number specified. This value is overridden by the consistency group setting if this snapshot group is associated with a consistency group.

        :return: The auto_delete_limit of this SnapshotGroupCreateRequest.
        :rtype: int
        :required/optional: optional
        """
        return self._auto_delete_limit

    @auto_delete_limit.setter
    def auto_delete_limit(self, auto_delete_limit):
        """
        Sets the auto_delete_limit of this SnapshotGroupCreateRequest.
        The automatic deletion indicator. If non-zero, the oldest snapshot image will be automatically deleted when creating a new snapshot image to keep the total number of snapshot images limited to the number specified. This value is overridden by the consistency group setting if this snapshot group is associated with a consistency group.

        :param auto_delete_limit: The auto_delete_limit of this SnapshotGroupCreateRequest.
        :type: int
        """
        self._auto_delete_limit = auto_delete_limit

    @property
    def full_policy(self):
        """
        Gets the full_policy of this SnapshotGroupCreateRequest.
        The behavior on when the data repository becomes full. This value is overridden by consistency group setting if this snapshot group is associated with a consistency group.

        :return: The full_policy of this SnapshotGroupCreateRequest.
        :rtype: str
        :required/optional: optional
        """
        return self._full_policy

    @full_policy.setter
    def full_policy(self, full_policy):
        """
        Sets the full_policy of this SnapshotGroupCreateRequest.
        The behavior on when the data repository becomes full. This value is overridden by consistency group setting if this snapshot group is associated with a consistency group.

        :param full_policy: The full_policy of this SnapshotGroupCreateRequest.
        :type: str
        """
        allowed_values = ["unknown", "failbasewrites", "purgepit", "__UNDEFINED", None]
        if full_policy not in allowed_values:
            raise ValueError(
                "Invalid value for `full_policy`, must be one of {0}"
                .format(allowed_values)
            )
        self._full_policy = full_policy

    @property
    def storage_pool_id(self):
        """
        Gets the storage_pool_id of this SnapshotGroupCreateRequest.
        The identifier  of the storage pool on which to allocate the repository volume. Ignored if a repositoryCandidate is provided.

        :return: The storage_pool_id of this SnapshotGroupCreateRequest.
        :rtype: str
        :required/optional: optional
        """
        return self._storage_pool_id

    @storage_pool_id.setter
    def storage_pool_id(self, storage_pool_id):
        """
        Sets the storage_pool_id of this SnapshotGroupCreateRequest.
        The identifier  of the storage pool on which to allocate the repository volume. Ignored if a repositoryCandidate is provided.

        :param storage_pool_id: The storage_pool_id of this SnapshotGroupCreateRequest.
        :type: str
        """
        self._storage_pool_id = storage_pool_id

    @property
    def repository_candidate(self):
        """
        Gets the repository_candidate of this SnapshotGroupCreateRequest.
        Allows a repository candidate to be manually specified for use in the creation. By default, the best candidate will be selected.

        :return: The repository_candidate of this SnapshotGroupCreateRequest.
        :rtype: ConcatVolumeCandidate
        :required/optional: optional
        """
        return self._repository_candidate

    @repository_candidate.setter
    def repository_candidate(self, repository_candidate):
        """
        Sets the repository_candidate of this SnapshotGroupCreateRequest.
        Allows a repository candidate to be manually specified for use in the creation. By default, the best candidate will be selected.

        :param repository_candidate: The repository_candidate of this SnapshotGroupCreateRequest.
        :type: ConcatVolumeCandidate
        """
        self._repository_candidate = repository_candidate

    @property
    def schedule(self):
        """
        Gets the schedule of this SnapshotGroupCreateRequest.
        An optional schedule  to be used to automatically create snapshot images.

        :return: The schedule of this SnapshotGroupCreateRequest.
        :rtype: ScheduleCreateRequest
        :required/optional: optional
        """
        return self._schedule

    @schedule.setter
    def schedule(self, schedule):
        """
        Sets the schedule of this SnapshotGroupCreateRequest.
        An optional schedule  to be used to automatically create snapshot images.

        :param schedule: The schedule of this SnapshotGroupCreateRequest.
        :type: ScheduleCreateRequest
        """
        self._schedule = schedule

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

