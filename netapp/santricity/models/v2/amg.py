# coding: utf-8

"""
Amg.py

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


class Amg(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        Amg - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'group_ref': 'str',  # (required parameter)
            'world_wide_name': 'str',  # (required parameter)
            'label': 'str',  # (required parameter)
            'group_state': 'str',  # (required parameter)
            'local_role': 'str',  # (required parameter)
            'remote_role': 'str',  # (required parameter)
            'role_change_progress': 'str',  # (required parameter)
            'sync_interval_minutes': 'int',  # (required parameter)
            'sync_completion_time_alert_threshold_minutes': 'int',  # (required parameter)
            'recovery_point_age_alert_threshold_minutes': 'int',  # (required parameter)
            'repository_utilization_warn_threshold': 'int',  # (required parameter)
            'mirror_channel_remote_target': 'str',  # (required parameter)
            'sync_activity': 'str',  # (required parameter)
            'orphan_group': 'bool',  # (required parameter)
            'connection_type': 'str',  
            'remote_target_wwn': 'str',  
            'remote_target_name': 'str',  
            'remote_target_id': 'str',  
            'remote_target': 'RemoteTarget',  
            'id': 'str'
        }

        self.attribute_map = {
            'group_ref': 'groupRef',  # (required parameter)
            'world_wide_name': 'worldWideName',  # (required parameter)
            'label': 'label',  # (required parameter)
            'group_state': 'groupState',  # (required parameter)
            'local_role': 'localRole',  # (required parameter)
            'remote_role': 'remoteRole',  # (required parameter)
            'role_change_progress': 'roleChangeProgress',  # (required parameter)
            'sync_interval_minutes': 'syncIntervalMinutes',  # (required parameter)
            'sync_completion_time_alert_threshold_minutes': 'syncCompletionTimeAlertThresholdMinutes',  # (required parameter)
            'recovery_point_age_alert_threshold_minutes': 'recoveryPointAgeAlertThresholdMinutes',  # (required parameter)
            'repository_utilization_warn_threshold': 'repositoryUtilizationWarnThreshold',  # (required parameter)
            'mirror_channel_remote_target': 'mirrorChannelRemoteTarget',  # (required parameter)
            'sync_activity': 'syncActivity',  # (required parameter)
            'orphan_group': 'orphanGroup',  # (required parameter)
            'connection_type': 'connectionType',  
            'remote_target_wwn': 'remoteTargetWwn',  
            'remote_target_name': 'remoteTargetName',  
            'remote_target_id': 'remoteTargetId',  
            'remote_target': 'remoteTarget',  
            'id': 'id'
        }

        self._group_ref = None
        self._world_wide_name = None
        self._label = None
        self._group_state = None
        self._local_role = None
        self._remote_role = None
        self._role_change_progress = None
        self._sync_interval_minutes = None
        self._sync_completion_time_alert_threshold_minutes = None
        self._recovery_point_age_alert_threshold_minutes = None
        self._repository_utilization_warn_threshold = None
        self._mirror_channel_remote_target = None
        self._sync_activity = None
        self._orphan_group = None
        self._connection_type = None
        self._remote_target_wwn = None
        self._remote_target_name = None
        self._remote_target_id = None
        self._remote_target = None
        self._id = None

    @property
    def group_ref(self):
        """
        Gets the group_ref of this Amg.
        The reference (key) for the mirror group.

        :return: The group_ref of this Amg.
        :rtype: str
        :required/optional: required
        """
        return self._group_ref

    @group_ref.setter
    def group_ref(self, group_ref):
        """
        Sets the group_ref of this Amg.
        The reference (key) for the mirror group.

        :param group_ref: The group_ref of this Amg.
        :type: str
        """
        self._group_ref = group_ref

    @property
    def world_wide_name(self):
        """
        Gets the world_wide_name of this Amg.
        The world wide name of the mirror group. This can be used to identify the AMG pair on both arrays. The AsyncMirrorGroupRef is not guaranteed to be unique across multiple arrays.

        :return: The world_wide_name of this Amg.
        :rtype: str
        :required/optional: required
        """
        return self._world_wide_name

    @world_wide_name.setter
    def world_wide_name(self, world_wide_name):
        """
        Sets the world_wide_name of this Amg.
        The world wide name of the mirror group. This can be used to identify the AMG pair on both arrays. The AsyncMirrorGroupRef is not guaranteed to be unique across multiple arrays.

        :param world_wide_name: The world_wide_name of this Amg.
        :type: str
        """
        self._world_wide_name = world_wide_name

    @property
    def label(self):
        """
        Gets the label of this Amg.
        The user assigned name for the mirror group.

        :return: The label of this Amg.
        :rtype: str
        :required/optional: required
        """
        return self._label

    @label.setter
    def label(self, label):
        """
        Sets the label of this Amg.
        The user assigned name for the mirror group.

        :param label: The label of this Amg.
        :type: str
        """
        self._label = label

    @property
    def group_state(self):
        """
        Gets the group_state of this Amg.
        The Mirror Group State. This is determined primarily by the presence or lack of a recovery point.

        :return: The group_state of this Amg.
        :rtype: str
        :required/optional: required
        """
        return self._group_state

    @group_state.setter
    def group_state(self, group_state):
        """
        Sets the group_state of this Amg.
        The Mirror Group State. This is determined primarily by the presence or lack of a recovery point.

        :param group_state: The group_state of this Amg.
        :type: str
        """
        allowed_values = ["unknown", "initialSync", "optimal", "degraded", "rpFailed", "__UNDEFINED"]
        if group_state not in allowed_values:
            raise ValueError(
                "Invalid value for `group_state`, must be one of {0}"
                .format(allowed_values)
            )
        self._group_state = group_state

    @property
    def local_role(self):
        """
        Gets the local_role of this Amg.
        The current role of this (local) array with respect to this mirror group.

        :return: The local_role of this Amg.
        :rtype: str
        :required/optional: required
        """
        return self._local_role

    @local_role.setter
    def local_role(self, local_role):
        """
        Sets the local_role of this Amg.
        The current role of this (local) array with respect to this mirror group.

        :param local_role: The local_role of this Amg.
        :type: str
        """
        allowed_values = ["unknown", "primary", "secondary", "__UNDEFINED"]
        if local_role not in allowed_values:
            raise ValueError(
                "Invalid value for `local_role`, must be one of {0}"
                .format(allowed_values)
            )
        self._local_role = local_role

    @property
    def remote_role(self):
        """
        Gets the remote_role of this Amg.
        The current role of the peer (remote) array with respect to this mirror group.

        :return: The remote_role of this Amg.
        :rtype: str
        :required/optional: required
        """
        return self._remote_role

    @remote_role.setter
    def remote_role(self, remote_role):
        """
        Sets the remote_role of this Amg.
        The current role of the peer (remote) array with respect to this mirror group.

        :param remote_role: The remote_role of this Amg.
        :type: str
        """
        allowed_values = ["unknown", "primary", "secondary", "__UNDEFINED"]
        if remote_role not in allowed_values:
            raise ValueError(
                "Invalid value for `remote_role`, must be one of {0}"
                .format(allowed_values)
            )
        self._remote_role = remote_role

    @property
    def role_change_progress(self):
        """
        Gets the role_change_progress of this Amg.
        This field indicates the current state of the role change process. This may be an extended condition due to the data sync needed for an orderly role change or the recovery point rollback needed for a no-sync or forced role change.

        :return: The role_change_progress of this Amg.
        :rtype: str
        :required/optional: required
        """
        return self._role_change_progress

    @role_change_progress.setter
    def role_change_progress(self, role_change_progress):
        """
        Sets the role_change_progress of this Amg.
        This field indicates the current state of the role change process. This may be an extended condition due to the data sync needed for an orderly role change or the recovery point rollback needed for a no-sync or forced role change.

        :param role_change_progress: The role_change_progress of this Amg.
        :type: str
        """
        allowed_values = ["unknown", "none", "pending", "inProgress", "__UNDEFINED"]
        if role_change_progress not in allowed_values:
            raise ValueError(
                "Invalid value for `role_change_progress`, must be one of {0}"
                .format(allowed_values)
            )
        self._role_change_progress = role_change_progress

    @property
    def sync_interval_minutes(self):
        """
        Gets the sync_interval_minutes of this Amg.
        The time in minutes between starting points of periodic synchronization intervals. A value of ARVM_MANUAL_SYNC_INTERVAL indicates synchronization intervals are manually started by the user.

        :return: The sync_interval_minutes of this Amg.
        :rtype: int
        :required/optional: required
        """
        return self._sync_interval_minutes

    @sync_interval_minutes.setter
    def sync_interval_minutes(self, sync_interval_minutes):
        """
        Sets the sync_interval_minutes of this Amg.
        The time in minutes between starting points of periodic synchronization intervals. A value of ARVM_MANUAL_SYNC_INTERVAL indicates synchronization intervals are manually started by the user.

        :param sync_interval_minutes: The sync_interval_minutes of this Amg.
        :type: int
        """
        self._sync_interval_minutes = sync_interval_minutes

    @property
    def sync_completion_time_alert_threshold_minutes(self):
        """
        Gets the sync_completion_time_alert_threshold_minutes of this Amg.
        The threshold (in minutes) for notifying the user that periodic synchronization has taken too long to complete. A value of ARVM_SYNC_COMPLETION_TIME_THRESHOLD_NONE indicates no threshold is set.

        :return: The sync_completion_time_alert_threshold_minutes of this Amg.
        :rtype: int
        :required/optional: required
        """
        return self._sync_completion_time_alert_threshold_minutes

    @sync_completion_time_alert_threshold_minutes.setter
    def sync_completion_time_alert_threshold_minutes(self, sync_completion_time_alert_threshold_minutes):
        """
        Sets the sync_completion_time_alert_threshold_minutes of this Amg.
        The threshold (in minutes) for notifying the user that periodic synchronization has taken too long to complete. A value of ARVM_SYNC_COMPLETION_TIME_THRESHOLD_NONE indicates no threshold is set.

        :param sync_completion_time_alert_threshold_minutes: The sync_completion_time_alert_threshold_minutes of this Amg.
        :type: int
        """
        self._sync_completion_time_alert_threshold_minutes = sync_completion_time_alert_threshold_minutes

    @property
    def recovery_point_age_alert_threshold_minutes(self):
        """
        Gets the recovery_point_age_alert_threshold_minutes of this Amg.
        The recovery point age objective (in minutes). The user is notified via needs-attention when the age of the last good recovery point exceeds this value. A value of ARVM_RECOVERY_POINT_AGE_THRESHOLD_NONE indicates no threshold is set.

        :return: The recovery_point_age_alert_threshold_minutes of this Amg.
        :rtype: int
        :required/optional: required
        """
        return self._recovery_point_age_alert_threshold_minutes

    @recovery_point_age_alert_threshold_minutes.setter
    def recovery_point_age_alert_threshold_minutes(self, recovery_point_age_alert_threshold_minutes):
        """
        Sets the recovery_point_age_alert_threshold_minutes of this Amg.
        The recovery point age objective (in minutes). The user is notified via needs-attention when the age of the last good recovery point exceeds this value. A value of ARVM_RECOVERY_POINT_AGE_THRESHOLD_NONE indicates no threshold is set.

        :param recovery_point_age_alert_threshold_minutes: The recovery_point_age_alert_threshold_minutes of this Amg.
        :type: int
        """
        self._recovery_point_age_alert_threshold_minutes = recovery_point_age_alert_threshold_minutes

    @property
    def repository_utilization_warn_threshold(self):
        """
        Gets the repository_utilization_warn_threshold of this Amg.
        The repository utilization warning threshold (0-100 percent). A needs attention condition will be generated if the percent of the repository capacity currently utilized exceeds this threshold.

        :return: The repository_utilization_warn_threshold of this Amg.
        :rtype: int
        :required/optional: required
        """
        return self._repository_utilization_warn_threshold

    @repository_utilization_warn_threshold.setter
    def repository_utilization_warn_threshold(self, repository_utilization_warn_threshold):
        """
        Sets the repository_utilization_warn_threshold of this Amg.
        The repository utilization warning threshold (0-100 percent). A needs attention condition will be generated if the percent of the repository capacity currently utilized exceeds this threshold.

        :param repository_utilization_warn_threshold: The repository_utilization_warn_threshold of this Amg.
        :type: int
        """
        self._repository_utilization_warn_threshold = repository_utilization_warn_threshold

    @property
    def mirror_channel_remote_target(self):
        """
        Gets the mirror_channel_remote_target of this Amg.
        The path to the remote array to be used by this AMG (a reference to the associated RemoteTarget).

        :return: The mirror_channel_remote_target of this Amg.
        :rtype: str
        :required/optional: required
        """
        return self._mirror_channel_remote_target

    @mirror_channel_remote_target.setter
    def mirror_channel_remote_target(self, mirror_channel_remote_target):
        """
        Sets the mirror_channel_remote_target of this Amg.
        The path to the remote array to be used by this AMG (a reference to the associated RemoteTarget).

        :param mirror_channel_remote_target: The mirror_channel_remote_target of this Amg.
        :type: str
        """
        self._mirror_channel_remote_target = mirror_channel_remote_target

    @property
    def sync_activity(self):
        """
        Gets the sync_activity of this Amg.
        Current synchronization activity.

        :return: The sync_activity of this Amg.
        :rtype: str
        :required/optional: required
        """
        return self._sync_activity

    @sync_activity.setter
    def sync_activity(self, sync_activity):
        """
        Sets the sync_activity of this Amg.
        Current synchronization activity.

        :param sync_activity: The sync_activity of this Amg.
        :type: str
        """
        allowed_values = ["unknown", "idle", "active", "paused", "userSuspended", "internallySuspended", "__UNDEFINED"]
        if sync_activity not in allowed_values:
            raise ValueError(
                "Invalid value for `sync_activity`, must be one of {0}"
                .format(allowed_values)
            )
        self._sync_activity = sync_activity

    @property
    def orphan_group(self):
        """
        Gets the orphan_group of this Amg.
        If true, the mirror group is an orphan.

        :return: The orphan_group of this Amg.
        :rtype: bool
        :required/optional: required
        """
        return self._orphan_group

    @orphan_group.setter
    def orphan_group(self, orphan_group):
        """
        Sets the orphan_group of this Amg.
        If true, the mirror group is an orphan.

        :param orphan_group: The orphan_group of this Amg.
        :type: bool
        """
        self._orphan_group = orphan_group

    @property
    def connection_type(self):
        """
        Gets the connection_type of this Amg.
        The connection type used to create this mirror group.

        :return: The connection_type of this Amg.
        :rtype: str
        :required/optional: optional
        """
        return self._connection_type

    @connection_type.setter
    def connection_type(self, connection_type):
        """
        Sets the connection_type of this Amg.
        The connection type used to create this mirror group.

        :param connection_type: The connection_type of this Amg.
        :type: str
        """
        allowed_values = ["notImplemented", "scsi", "fc", "sata", "sas", "iscsi", "ib", "fcoe", "nvmeof", "__UNDEFINED", None]
        if connection_type not in allowed_values:
            raise ValueError(
                "Invalid value for `connection_type`, must be one of {0}"
                .format(allowed_values)
            )
        self._connection_type = connection_type

    @property
    def remote_target_wwn(self):
        """
        Gets the remote_target_wwn of this Amg.
        The WWN of the target array in the mirroring relationship. This field may not be immediately available after an AMG is created.

        :return: The remote_target_wwn of this Amg.
        :rtype: str
        :required/optional: optional
        """
        return self._remote_target_wwn

    @remote_target_wwn.setter
    def remote_target_wwn(self, remote_target_wwn):
        """
        Sets the remote_target_wwn of this Amg.
        The WWN of the target array in the mirroring relationship. This field may not be immediately available after an AMG is created.

        :param remote_target_wwn: The remote_target_wwn of this Amg.
        :type: str
        """
        self._remote_target_wwn = remote_target_wwn

    @property
    def remote_target_name(self):
        """
        Gets the remote_target_name of this Amg.
        The user label of the target array in the mirroring relationship. This field may not be immediately available after an AMG is created, and will not be available in embedded mode.

        :return: The remote_target_name of this Amg.
        :rtype: str
        :required/optional: optional
        """
        return self._remote_target_name

    @remote_target_name.setter
    def remote_target_name(self, remote_target_name):
        """
        Sets the remote_target_name of this Amg.
        The user label of the target array in the mirroring relationship. This field may not be immediately available after an AMG is created, and will not be available in embedded mode.

        :param remote_target_name: The remote_target_name of this Amg.
        :type: str
        """
        self._remote_target_name = remote_target_name

    @property
    def remote_target_id(self):
        """
        Gets the remote_target_id of this Amg.
        The id of the target array in the mirroring relationship. This field may not be immediately available after an AMG is created, and will not be available in embedded mode.

        :return: The remote_target_id of this Amg.
        :rtype: str
        :required/optional: optional
        """
        return self._remote_target_id

    @remote_target_id.setter
    def remote_target_id(self, remote_target_id):
        """
        Sets the remote_target_id of this Amg.
        The id of the target array in the mirroring relationship. This field may not be immediately available after an AMG is created, and will not be available in embedded mode.

        :param remote_target_id: The remote_target_id of this Amg.
        :type: str
        """
        self._remote_target_id = remote_target_id

    @property
    def remote_target(self):
        """
        Gets the remote_target of this Amg.
        The connection information for the remote StorageSystem.

        :return: The remote_target of this Amg.
        :rtype: RemoteTarget
        :required/optional: optional
        """
        return self._remote_target

    @remote_target.setter
    def remote_target(self, remote_target):
        """
        Sets the remote_target of this Amg.
        The connection information for the remote StorageSystem.

        :param remote_target: The remote_target of this Amg.
        :type: RemoteTarget
        """
        self._remote_target = remote_target

    @property
    def id(self):
        """
        Gets the id of this Amg.


        :return: The id of this Amg.
        :rtype: str
        :required/optional: optional
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Amg.


        :param id: The id of this Amg.
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

