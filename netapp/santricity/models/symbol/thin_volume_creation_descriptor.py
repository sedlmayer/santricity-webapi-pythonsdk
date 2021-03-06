# coding: utf-8

"""
ThinVolumeCreationDescriptor.py

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


class ThinVolumeCreationDescriptor(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        ThinVolumeCreationDescriptor - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'repository_creation_descriptor': 'ConcatVolumeCreationDescriptor',  # (required parameter)
            'volume_label': 'str',  # (required parameter)
            'manager': 'str',  # (required parameter)
            'virtual_capacity': 'int',  # (required parameter)
            'provisioned_capacity_quota': 'int',  # (required parameter)
            'read_ahead': 'int',  # (required parameter)
            'no_mapping': 'bool',  # (required parameter)
            'repository_expansion_policy': 'str',  # (required parameter)
            'growth_alert_threshold': 'int',  # (required parameter)
            'protection_type': 'str'
        }

        self.attribute_map = {
            'repository_creation_descriptor': 'repositoryCreationDescriptor',  # (required parameter)
            'volume_label': 'volumeLabel',  # (required parameter)
            'manager': 'manager',  # (required parameter)
            'virtual_capacity': 'virtualCapacity',  # (required parameter)
            'provisioned_capacity_quota': 'provisionedCapacityQuota',  # (required parameter)
            'read_ahead': 'readAhead',  # (required parameter)
            'no_mapping': 'noMapping',  # (required parameter)
            'repository_expansion_policy': 'repositoryExpansionPolicy',  # (required parameter)
            'growth_alert_threshold': 'growthAlertThreshold',  # (required parameter)
            'protection_type': 'protectionType'
        }

        self._repository_creation_descriptor = None
        self._volume_label = None
        self._manager = None
        self._virtual_capacity = None
        self._provisioned_capacity_quota = None
        self._read_ahead = None
        self._no_mapping = None
        self._repository_expansion_policy = None
        self._growth_alert_threshold = None
        self._protection_type = None

    @property
    def repository_creation_descriptor(self):
        """
        Gets the repository_creation_descriptor of this ThinVolumeCreationDescriptor.
        The repository creation type.

        :return: The repository_creation_descriptor of this ThinVolumeCreationDescriptor.
        :rtype: ConcatVolumeCreationDescriptor
        :required/optional: required
        """
        return self._repository_creation_descriptor

    @repository_creation_descriptor.setter
    def repository_creation_descriptor(self, repository_creation_descriptor):
        """
        Sets the repository_creation_descriptor of this ThinVolumeCreationDescriptor.
        The repository creation type.

        :param repository_creation_descriptor: The repository_creation_descriptor of this ThinVolumeCreationDescriptor.
        :type: ConcatVolumeCreationDescriptor
        """
        self._repository_creation_descriptor = repository_creation_descriptor

    @property
    def volume_label(self):
        """
        Gets the volume_label of this ThinVolumeCreationDescriptor.
        The user assigned volume name.

        :return: The volume_label of this ThinVolumeCreationDescriptor.
        :rtype: str
        :required/optional: required
        """
        return self._volume_label

    @volume_label.setter
    def volume_label(self, volume_label):
        """
        Sets the volume_label of this ThinVolumeCreationDescriptor.
        The user assigned volume name.

        :param volume_label: The volume_label of this ThinVolumeCreationDescriptor.
        :type: str
        """
        self._volume_label = volume_label

    @property
    def manager(self):
        """
        Gets the manager of this ThinVolumeCreationDescriptor.
        The controller that will manage the volume.

        :return: The manager of this ThinVolumeCreationDescriptor.
        :rtype: str
        :required/optional: required
        """
        return self._manager

    @manager.setter
    def manager(self, manager):
        """
        Sets the manager of this ThinVolumeCreationDescriptor.
        The controller that will manage the volume.

        :param manager: The manager of this ThinVolumeCreationDescriptor.
        :type: str
        """
        self._manager = manager

    @property
    def virtual_capacity(self):
        """
        Gets the virtual_capacity of this ThinVolumeCreationDescriptor.
        The thin volume capacity (in bytes).

        :return: The virtual_capacity of this ThinVolumeCreationDescriptor.
        :rtype: int
        :required/optional: required
        """
        return self._virtual_capacity

    @virtual_capacity.setter
    def virtual_capacity(self, virtual_capacity):
        """
        Sets the virtual_capacity of this ThinVolumeCreationDescriptor.
        The thin volume capacity (in bytes).

        :param virtual_capacity: The virtual_capacity of this ThinVolumeCreationDescriptor.
        :type: int
        """
        self._virtual_capacity = virtual_capacity

    @property
    def provisioned_capacity_quota(self):
        """
        Gets the provisioned_capacity_quota of this ThinVolumeCreationDescriptor.
        The maximum capacity to which the Expandable Repository Volume can grow (in bytes).

        :return: The provisioned_capacity_quota of this ThinVolumeCreationDescriptor.
        :rtype: int
        :required/optional: required
        """
        return self._provisioned_capacity_quota

    @provisioned_capacity_quota.setter
    def provisioned_capacity_quota(self, provisioned_capacity_quota):
        """
        Sets the provisioned_capacity_quota of this ThinVolumeCreationDescriptor.
        The maximum capacity to which the Expandable Repository Volume can grow (in bytes).

        :param provisioned_capacity_quota: The provisioned_capacity_quota of this ThinVolumeCreationDescriptor.
        :type: int
        """
        self._provisioned_capacity_quota = provisioned_capacity_quota

    @property
    def read_ahead(self):
        """
        Gets the read_ahead of this ThinVolumeCreationDescriptor.
        If true (non-zero), automatic cache read-ahead is enabled. If false (zero), automatic cache read-ahead is disabled.

        :return: The read_ahead of this ThinVolumeCreationDescriptor.
        :rtype: int
        :required/optional: required
        """
        return self._read_ahead

    @read_ahead.setter
    def read_ahead(self, read_ahead):
        """
        Sets the read_ahead of this ThinVolumeCreationDescriptor.
        If true (non-zero), automatic cache read-ahead is enabled. If false (zero), automatic cache read-ahead is disabled.

        :param read_ahead: The read_ahead of this ThinVolumeCreationDescriptor.
        :type: int
        """
        self._read_ahead = read_ahead

    @property
    def no_mapping(self):
        """
        Gets the no_mapping of this ThinVolumeCreationDescriptor.
        If true, default mapping will not be created.

        :return: The no_mapping of this ThinVolumeCreationDescriptor.
        :rtype: bool
        :required/optional: required
        """
        return self._no_mapping

    @no_mapping.setter
    def no_mapping(self, no_mapping):
        """
        Sets the no_mapping of this ThinVolumeCreationDescriptor.
        If true, default mapping will not be created.

        :param no_mapping: The no_mapping of this ThinVolumeCreationDescriptor.
        :type: bool
        """
        self._no_mapping = no_mapping

    @property
    def repository_expansion_policy(self):
        """
        Gets the repository_expansion_policy of this ThinVolumeCreationDescriptor.
        The expansion policy for the Expandable Repository Volume.

        :return: The repository_expansion_policy of this ThinVolumeCreationDescriptor.
        :rtype: str
        :required/optional: required
        """
        return self._repository_expansion_policy

    @repository_expansion_policy.setter
    def repository_expansion_policy(self, repository_expansion_policy):
        """
        Sets the repository_expansion_policy of this ThinVolumeCreationDescriptor.
        The expansion policy for the Expandable Repository Volume.

        :param repository_expansion_policy: The repository_expansion_policy of this ThinVolumeCreationDescriptor.
        :type: str
        """
        allowed_values = ["unknown", "manual", "automatic", "__UNDEFINED"]
        if repository_expansion_policy not in allowed_values:
            raise ValueError(
                "Invalid value for `repository_expansion_policy`, must be one of {0}"
                .format(allowed_values)
            )
        self._repository_expansion_policy = repository_expansion_policy

    @property
    def growth_alert_threshold(self):
        """
        Gets the growth_alert_threshold of this ThinVolumeCreationDescriptor.
        The alert threshold percent value for the Expandable Repository Volume.

        :return: The growth_alert_threshold of this ThinVolumeCreationDescriptor.
        :rtype: int
        :required/optional: required
        """
        return self._growth_alert_threshold

    @growth_alert_threshold.setter
    def growth_alert_threshold(self, growth_alert_threshold):
        """
        Sets the growth_alert_threshold of this ThinVolumeCreationDescriptor.
        The alert threshold percent value for the Expandable Repository Volume.

        :param growth_alert_threshold: The growth_alert_threshold of this ThinVolumeCreationDescriptor.
        :type: int
        """
        self._growth_alert_threshold = growth_alert_threshold

    @property
    def protection_type(self):
        """
        Gets the protection_type of this ThinVolumeCreationDescriptor.
        Specifies which protection type should be used for the volume.

        :return: The protection_type of this ThinVolumeCreationDescriptor.
        :rtype: str
        :required/optional: required
        """
        return self._protection_type

    @protection_type.setter
    def protection_type(self, protection_type):
        """
        Sets the protection_type of this ThinVolumeCreationDescriptor.
        Specifies which protection type should be used for the volume.

        :param protection_type: The protection_type of this ThinVolumeCreationDescriptor.
        :type: str
        """
        allowed_values = ["type0Protection", "type1Protection", "type2Protection", "type3Protection", "__UNDEFINED"]
        if protection_type not in allowed_values:
            raise ValueError(
                "Invalid value for `protection_type`, must be one of {0}"
                .format(allowed_values)
            )
        self._protection_type = protection_type

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

