# coding: utf-8

"""
LongLivedOperation.py

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


class LongLivedOperation(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        LongLivedOperation - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'vol_action': 'str',  # (required parameter)
            'copyback': 'VolumeGroupOperation',  
            'reconstruct': 'VolumeGroupOperation',  
            'capacity_expansion': 'VolumeGroupOperation',  
            'raid_migration': 'VolumeGroupOperation',  
            'raid_migrationand_expansion': 'VolumeGroupOperation',  
            'seg_size': 'VolumeGroupOperation',  
            'vol_expansion': 'VolumeGroupOperation',  
            'vol_and_cap_expansion': 'VolumeGroupOperation',  
            'defrag': 'VolumeGroupOperation',  
            'init': 'InitializationOperation',  
            'format': 'InitializationOperation',  
            'sync': 'MirrorSyncOperation',  
            'copy': 'VolumeCopyOperation',  
            'parity_scan': 'VolumeGroupOperation',  
            'rollback': 'SnapshotRollbackOperation',  
            'pit_rollback': 'PITRollbackOperation',  
            'initial_sync': 'AsyncMirrorGroupInitialSyncOperation',  
            'rebalancing': 'VolumeGroupOperation',  
            'copy_then_fail': 'VolumeGroupOperation',  
            'copy_then_fail_pending': 'VolumeGroupOperation',  
            'copy_then_replace': 'VolumeGroupOperation',  
            'copy_then_replace_and_fail': 'VolumeGroupOperation',  
            'reconstruct_critical': 'VolumeGroupOperation',  
            'thin_defrag': 'VolumeOperation',  
            'vol_creation': 'VolumeOperation',  
            'vol_deletion': 'VolumeOperation'
        }

        self.attribute_map = {
            'vol_action': 'volAction',  # (required parameter)
            'copyback': 'copyback',  
            'reconstruct': 'reconstruct',  
            'capacity_expansion': 'capacityExpansion',  
            'raid_migration': 'raidMigration',  
            'raid_migrationand_expansion': 'raidMigrationandExpansion',  
            'seg_size': 'segSize',  
            'vol_expansion': 'volExpansion',  
            'vol_and_cap_expansion': 'volAndCapExpansion',  
            'defrag': 'defrag',  
            'init': 'init',  
            'format': 'format',  
            'sync': 'sync',  
            'copy': 'copy',  
            'parity_scan': 'parityScan',  
            'rollback': 'rollback',  
            'pit_rollback': 'pitRollback',  
            'initial_sync': 'initialSync',  
            'rebalancing': 'rebalancing',  
            'copy_then_fail': 'copyThenFail',  
            'copy_then_fail_pending': 'copyThenFailPending',  
            'copy_then_replace': 'copyThenReplace',  
            'copy_then_replace_and_fail': 'copyThenReplaceAndFail',  
            'reconstruct_critical': 'reconstructCritical',  
            'thin_defrag': 'thinDefrag',  
            'vol_creation': 'volCreation',  
            'vol_deletion': 'volDeletion'
        }

        self._vol_action = None
        self._copyback = None
        self._reconstruct = None
        self._capacity_expansion = None
        self._raid_migration = None
        self._raid_migrationand_expansion = None
        self._seg_size = None
        self._vol_expansion = None
        self._vol_and_cap_expansion = None
        self._defrag = None
        self._init = None
        self._format = None
        self._sync = None
        self._copy = None
        self._parity_scan = None
        self._rollback = None
        self._pit_rollback = None
        self._initial_sync = None
        self._rebalancing = None
        self._copy_then_fail = None
        self._copy_then_fail_pending = None
        self._copy_then_replace = None
        self._copy_then_replace_and_fail = None
        self._reconstruct_critical = None
        self._thin_defrag = None
        self._vol_creation = None
        self._vol_deletion = None

    @property
    def vol_action(self):
        """
        Gets the vol_action of this LongLivedOperation.
        This enumeration object is used to specify one of a set of volume actions that may be active for a volume. These volume actions represent \"long-running\" operations on a volume. Any time such an operation is active, the current progress can be determined using the getVolumeActionProgress procedure.

        :return: The vol_action of this LongLivedOperation.
        :rtype: str
        :required/optional: required
        """
        return self._vol_action

    @vol_action.setter
    def vol_action(self, vol_action):
        """
        Sets the vol_action of this LongLivedOperation.
        This enumeration object is used to specify one of a set of volume actions that may be active for a volume. These volume actions represent \"long-running\" operations on a volume. Any time such an operation is active, the current progress can be determined using the getVolumeActionProgress procedure.

        :param vol_action: The vol_action of this LongLivedOperation.
        :type: str
        """
        allowed_values = ["none", "copyback", "initializing", "reconstructing", "remappingDce", "remappingDrm", "remappingDcedrm", "remappingDseg", "remappingDve", "remappingDcedve", "remappingInternal", "remappingDefrag", "formatting", "synchronizing", "parityScan", "volumeCopy", "snapshotRollback", "pitRollback", "asyncMirrorGroupInitialSync", "reconstructingCritical", "rebalancing", "copyThenFail", "copyThenFailPending", "copyThenReplace", "copyThenReplaceAndFail", "thinDefrag", "creating", "deleting", "__UNDEFINED"]
        if vol_action not in allowed_values:
            raise ValueError(
                "Invalid value for `vol_action`, must be one of {0}"
                .format(allowed_values)
            )
        self._vol_action = vol_action

    @property
    def copyback(self):
        """
        Gets the copyback of this LongLivedOperation.
        This field is present only if volAction is equal to VOL_ACTION_COPYBACK.

        :return: The copyback of this LongLivedOperation.
        :rtype: VolumeGroupOperation
        :required/optional: optional
        """
        return self._copyback

    @copyback.setter
    def copyback(self, copyback):
        """
        Sets the copyback of this LongLivedOperation.
        This field is present only if volAction is equal to VOL_ACTION_COPYBACK.

        :param copyback: The copyback of this LongLivedOperation.
        :type: VolumeGroupOperation
        """
        self._copyback = copyback

    @property
    def reconstruct(self):
        """
        Gets the reconstruct of this LongLivedOperation.
        This field is present only if volAction is equal to VOL_ACTION_RECONSTRUCTING.

        :return: The reconstruct of this LongLivedOperation.
        :rtype: VolumeGroupOperation
        :required/optional: optional
        """
        return self._reconstruct

    @reconstruct.setter
    def reconstruct(self, reconstruct):
        """
        Sets the reconstruct of this LongLivedOperation.
        This field is present only if volAction is equal to VOL_ACTION_RECONSTRUCTING.

        :param reconstruct: The reconstruct of this LongLivedOperation.
        :type: VolumeGroupOperation
        """
        self._reconstruct = reconstruct

    @property
    def capacity_expansion(self):
        """
        Gets the capacity_expansion of this LongLivedOperation.
        This field is present only if volAction is equal to VOL_ACTION_REMAPPING_DCE.

        :return: The capacity_expansion of this LongLivedOperation.
        :rtype: VolumeGroupOperation
        :required/optional: optional
        """
        return self._capacity_expansion

    @capacity_expansion.setter
    def capacity_expansion(self, capacity_expansion):
        """
        Sets the capacity_expansion of this LongLivedOperation.
        This field is present only if volAction is equal to VOL_ACTION_REMAPPING_DCE.

        :param capacity_expansion: The capacity_expansion of this LongLivedOperation.
        :type: VolumeGroupOperation
        """
        self._capacity_expansion = capacity_expansion

    @property
    def raid_migration(self):
        """
        Gets the raid_migration of this LongLivedOperation.
        This field is present only if volAction is equal to VOL_ACTION_REMAPPING_DRM.

        :return: The raid_migration of this LongLivedOperation.
        :rtype: VolumeGroupOperation
        :required/optional: optional
        """
        return self._raid_migration

    @raid_migration.setter
    def raid_migration(self, raid_migration):
        """
        Sets the raid_migration of this LongLivedOperation.
        This field is present only if volAction is equal to VOL_ACTION_REMAPPING_DRM.

        :param raid_migration: The raid_migration of this LongLivedOperation.
        :type: VolumeGroupOperation
        """
        self._raid_migration = raid_migration

    @property
    def raid_migrationand_expansion(self):
        """
        Gets the raid_migrationand_expansion of this LongLivedOperation.
        This field is present only if volAction is equal to VOL_ACTION_REMAPPING_DCEDRM.

        :return: The raid_migrationand_expansion of this LongLivedOperation.
        :rtype: VolumeGroupOperation
        :required/optional: optional
        """
        return self._raid_migrationand_expansion

    @raid_migrationand_expansion.setter
    def raid_migrationand_expansion(self, raid_migrationand_expansion):
        """
        Sets the raid_migrationand_expansion of this LongLivedOperation.
        This field is present only if volAction is equal to VOL_ACTION_REMAPPING_DCEDRM.

        :param raid_migrationand_expansion: The raid_migrationand_expansion of this LongLivedOperation.
        :type: VolumeGroupOperation
        """
        self._raid_migrationand_expansion = raid_migrationand_expansion

    @property
    def seg_size(self):
        """
        Gets the seg_size of this LongLivedOperation.
        This field is present only if volAction is equal to VOL_ACTION_REMAPPING_DSEG.

        :return: The seg_size of this LongLivedOperation.
        :rtype: VolumeGroupOperation
        :required/optional: optional
        """
        return self._seg_size

    @seg_size.setter
    def seg_size(self, seg_size):
        """
        Sets the seg_size of this LongLivedOperation.
        This field is present only if volAction is equal to VOL_ACTION_REMAPPING_DSEG.

        :param seg_size: The seg_size of this LongLivedOperation.
        :type: VolumeGroupOperation
        """
        self._seg_size = seg_size

    @property
    def vol_expansion(self):
        """
        Gets the vol_expansion of this LongLivedOperation.
        This field is present only if volAction is equal to VOL_ACTION_REMAPPING_DVE.

        :return: The vol_expansion of this LongLivedOperation.
        :rtype: VolumeGroupOperation
        :required/optional: optional
        """
        return self._vol_expansion

    @vol_expansion.setter
    def vol_expansion(self, vol_expansion):
        """
        Sets the vol_expansion of this LongLivedOperation.
        This field is present only if volAction is equal to VOL_ACTION_REMAPPING_DVE.

        :param vol_expansion: The vol_expansion of this LongLivedOperation.
        :type: VolumeGroupOperation
        """
        self._vol_expansion = vol_expansion

    @property
    def vol_and_cap_expansion(self):
        """
        Gets the vol_and_cap_expansion of this LongLivedOperation.
        This field is present only if volAction is equal to VOL_ACTION_REMAPPING_DCEDVE.

        :return: The vol_and_cap_expansion of this LongLivedOperation.
        :rtype: VolumeGroupOperation
        :required/optional: optional
        """
        return self._vol_and_cap_expansion

    @vol_and_cap_expansion.setter
    def vol_and_cap_expansion(self, vol_and_cap_expansion):
        """
        Sets the vol_and_cap_expansion of this LongLivedOperation.
        This field is present only if volAction is equal to VOL_ACTION_REMAPPING_DCEDVE.

        :param vol_and_cap_expansion: The vol_and_cap_expansion of this LongLivedOperation.
        :type: VolumeGroupOperation
        """
        self._vol_and_cap_expansion = vol_and_cap_expansion

    @property
    def defrag(self):
        """
        Gets the defrag of this LongLivedOperation.
        This field is present only if volAction is equal to VOL_ACTION_REMAPPING_DEFRAG.

        :return: The defrag of this LongLivedOperation.
        :rtype: VolumeGroupOperation
        :required/optional: optional
        """
        return self._defrag

    @defrag.setter
    def defrag(self, defrag):
        """
        Sets the defrag of this LongLivedOperation.
        This field is present only if volAction is equal to VOL_ACTION_REMAPPING_DEFRAG.

        :param defrag: The defrag of this LongLivedOperation.
        :type: VolumeGroupOperation
        """
        self._defrag = defrag

    @property
    def init(self):
        """
        Gets the init of this LongLivedOperation.
        This field is present only if volAction is equal to VOL_ACTION_INITIALIZING.

        :return: The init of this LongLivedOperation.
        :rtype: InitializationOperation
        :required/optional: optional
        """
        return self._init

    @init.setter
    def init(self, init):
        """
        Sets the init of this LongLivedOperation.
        This field is present only if volAction is equal to VOL_ACTION_INITIALIZING.

        :param init: The init of this LongLivedOperation.
        :type: InitializationOperation
        """
        self._init = init

    @property
    def format(self):
        """
        Gets the format of this LongLivedOperation.
        This field is present only if volAction is equal to VOL_ACTION_FORMATTING.

        :return: The format of this LongLivedOperation.
        :rtype: InitializationOperation
        :required/optional: optional
        """
        return self._format

    @format.setter
    def format(self, format):
        """
        Sets the format of this LongLivedOperation.
        This field is present only if volAction is equal to VOL_ACTION_FORMATTING.

        :param format: The format of this LongLivedOperation.
        :type: InitializationOperation
        """
        self._format = format

    @property
    def sync(self):
        """
        Gets the sync of this LongLivedOperation.
        This field is present only if volAction is equal to VOL_ACTION_SYNCHRONIZING.

        :return: The sync of this LongLivedOperation.
        :rtype: MirrorSyncOperation
        :required/optional: optional
        """
        return self._sync

    @sync.setter
    def sync(self, sync):
        """
        Sets the sync of this LongLivedOperation.
        This field is present only if volAction is equal to VOL_ACTION_SYNCHRONIZING.

        :param sync: The sync of this LongLivedOperation.
        :type: MirrorSyncOperation
        """
        self._sync = sync

    @property
    def copy(self):
        """
        Gets the copy of this LongLivedOperation.
        This field is present only if volAction is equal to VOL_ACTION_VOLUME_COPY.

        :return: The copy of this LongLivedOperation.
        :rtype: VolumeCopyOperation
        :required/optional: optional
        """
        return self._copy

    @copy.setter
    def copy(self, copy):
        """
        Sets the copy of this LongLivedOperation.
        This field is present only if volAction is equal to VOL_ACTION_VOLUME_COPY.

        :param copy: The copy of this LongLivedOperation.
        :type: VolumeCopyOperation
        """
        self._copy = copy

    @property
    def parity_scan(self):
        """
        Gets the parity_scan of this LongLivedOperation.
        This field is present only if volAction is equal to VOL_ACTION_PARITY_SCAN.

        :return: The parity_scan of this LongLivedOperation.
        :rtype: VolumeGroupOperation
        :required/optional: optional
        """
        return self._parity_scan

    @parity_scan.setter
    def parity_scan(self, parity_scan):
        """
        Sets the parity_scan of this LongLivedOperation.
        This field is present only if volAction is equal to VOL_ACTION_PARITY_SCAN.

        :param parity_scan: The parity_scan of this LongLivedOperation.
        :type: VolumeGroupOperation
        """
        self._parity_scan = parity_scan

    @property
    def rollback(self):
        """
        Gets the rollback of this LongLivedOperation.
        This field is present only if volAction is equal to VOL_ACTION_SNAPSHOT_ROLLBACK.

        :return: The rollback of this LongLivedOperation.
        :rtype: SnapshotRollbackOperation
        :required/optional: optional
        """
        return self._rollback

    @rollback.setter
    def rollback(self, rollback):
        """
        Sets the rollback of this LongLivedOperation.
        This field is present only if volAction is equal to VOL_ACTION_SNAPSHOT_ROLLBACK.

        :param rollback: The rollback of this LongLivedOperation.
        :type: SnapshotRollbackOperation
        """
        self._rollback = rollback

    @property
    def pit_rollback(self):
        """
        Gets the pit_rollback of this LongLivedOperation.
        This field is present only if volAction is equal to VOL_ACTION_PIT_ROLLBACK.

        :return: The pit_rollback of this LongLivedOperation.
        :rtype: PITRollbackOperation
        :required/optional: optional
        """
        return self._pit_rollback

    @pit_rollback.setter
    def pit_rollback(self, pit_rollback):
        """
        Sets the pit_rollback of this LongLivedOperation.
        This field is present only if volAction is equal to VOL_ACTION_PIT_ROLLBACK.

        :param pit_rollback: The pit_rollback of this LongLivedOperation.
        :type: PITRollbackOperation
        """
        self._pit_rollback = pit_rollback

    @property
    def initial_sync(self):
        """
        Gets the initial_sync of this LongLivedOperation.
        This field is present only if the value of volAction is equal to VOL_ACTION_ASYNC_MIRROR_GROUP_INITIAL_SYNC.

        :return: The initial_sync of this LongLivedOperation.
        :rtype: AsyncMirrorGroupInitialSyncOperation
        :required/optional: optional
        """
        return self._initial_sync

    @initial_sync.setter
    def initial_sync(self, initial_sync):
        """
        Sets the initial_sync of this LongLivedOperation.
        This field is present only if the value of volAction is equal to VOL_ACTION_ASYNC_MIRROR_GROUP_INITIAL_SYNC.

        :param initial_sync: The initial_sync of this LongLivedOperation.
        :type: AsyncMirrorGroupInitialSyncOperation
        """
        self._initial_sync = initial_sync

    @property
    def rebalancing(self):
        """
        Gets the rebalancing of this LongLivedOperation.
        This field is present only if the value of volAction is equal to VOL_ACTION_REBALANCING.

        :return: The rebalancing of this LongLivedOperation.
        :rtype: VolumeGroupOperation
        :required/optional: optional
        """
        return self._rebalancing

    @rebalancing.setter
    def rebalancing(self, rebalancing):
        """
        Sets the rebalancing of this LongLivedOperation.
        This field is present only if the value of volAction is equal to VOL_ACTION_REBALANCING.

        :param rebalancing: The rebalancing of this LongLivedOperation.
        :type: VolumeGroupOperation
        """
        self._rebalancing = rebalancing

    @property
    def copy_then_fail(self):
        """
        Gets the copy_then_fail of this LongLivedOperation.
        This field is present only if the value of volAction is equal to VOL_ACTION_COPY_THEN_FAIL.

        :return: The copy_then_fail of this LongLivedOperation.
        :rtype: VolumeGroupOperation
        :required/optional: optional
        """
        return self._copy_then_fail

    @copy_then_fail.setter
    def copy_then_fail(self, copy_then_fail):
        """
        Sets the copy_then_fail of this LongLivedOperation.
        This field is present only if the value of volAction is equal to VOL_ACTION_COPY_THEN_FAIL.

        :param copy_then_fail: The copy_then_fail of this LongLivedOperation.
        :type: VolumeGroupOperation
        """
        self._copy_then_fail = copy_then_fail

    @property
    def copy_then_fail_pending(self):
        """
        Gets the copy_then_fail_pending of this LongLivedOperation.
        This field is present only if the value of volAction is equal to VOL_ACTION_COPY_THEN_FAIL_PENDING.

        :return: The copy_then_fail_pending of this LongLivedOperation.
        :rtype: VolumeGroupOperation
        :required/optional: optional
        """
        return self._copy_then_fail_pending

    @copy_then_fail_pending.setter
    def copy_then_fail_pending(self, copy_then_fail_pending):
        """
        Sets the copy_then_fail_pending of this LongLivedOperation.
        This field is present only if the value of volAction is equal to VOL_ACTION_COPY_THEN_FAIL_PENDING.

        :param copy_then_fail_pending: The copy_then_fail_pending of this LongLivedOperation.
        :type: VolumeGroupOperation
        """
        self._copy_then_fail_pending = copy_then_fail_pending

    @property
    def copy_then_replace(self):
        """
        Gets the copy_then_replace of this LongLivedOperation.
        This field is present only if the value of volAction is equal to VOL_ACTION_COPY_THEN_REPLACE.

        :return: The copy_then_replace of this LongLivedOperation.
        :rtype: VolumeGroupOperation
        :required/optional: optional
        """
        return self._copy_then_replace

    @copy_then_replace.setter
    def copy_then_replace(self, copy_then_replace):
        """
        Sets the copy_then_replace of this LongLivedOperation.
        This field is present only if the value of volAction is equal to VOL_ACTION_COPY_THEN_REPLACE.

        :param copy_then_replace: The copy_then_replace of this LongLivedOperation.
        :type: VolumeGroupOperation
        """
        self._copy_then_replace = copy_then_replace

    @property
    def copy_then_replace_and_fail(self):
        """
        Gets the copy_then_replace_and_fail of this LongLivedOperation.
        This field is present only if the value of volAction is equal to VOL_ACTION_COPY_THEN_REPLACE_AND_FAIL.

        :return: The copy_then_replace_and_fail of this LongLivedOperation.
        :rtype: VolumeGroupOperation
        :required/optional: optional
        """
        return self._copy_then_replace_and_fail

    @copy_then_replace_and_fail.setter
    def copy_then_replace_and_fail(self, copy_then_replace_and_fail):
        """
        Sets the copy_then_replace_and_fail of this LongLivedOperation.
        This field is present only if the value of volAction is equal to VOL_ACTION_COPY_THEN_REPLACE_AND_FAIL.

        :param copy_then_replace_and_fail: The copy_then_replace_and_fail of this LongLivedOperation.
        :type: VolumeGroupOperation
        """
        self._copy_then_replace_and_fail = copy_then_replace_and_fail

    @property
    def reconstruct_critical(self):
        """
        Gets the reconstruct_critical of this LongLivedOperation.
        This field is present only if the DDP pool is critical due to two drive failures.

        :return: The reconstruct_critical of this LongLivedOperation.
        :rtype: VolumeGroupOperation
        :required/optional: optional
        """
        return self._reconstruct_critical

    @reconstruct_critical.setter
    def reconstruct_critical(self, reconstruct_critical):
        """
        Sets the reconstruct_critical of this LongLivedOperation.
        This field is present only if the DDP pool is critical due to two drive failures.

        :param reconstruct_critical: The reconstruct_critical of this LongLivedOperation.
        :type: VolumeGroupOperation
        """
        self._reconstruct_critical = reconstruct_critical

    @property
    def thin_defrag(self):
        """
        Gets the thin_defrag of this LongLivedOperation.
        Thin volume defrag operation

        :return: The thin_defrag of this LongLivedOperation.
        :rtype: VolumeOperation
        :required/optional: optional
        """
        return self._thin_defrag

    @thin_defrag.setter
    def thin_defrag(self, thin_defrag):
        """
        Sets the thin_defrag of this LongLivedOperation.
        Thin volume defrag operation

        :param thin_defrag: The thin_defrag of this LongLivedOperation.
        :type: VolumeOperation
        """
        self._thin_defrag = thin_defrag

    @property
    def vol_creation(self):
        """
        Gets the vol_creation of this LongLivedOperation.
        A DDP Volume is in the creating state.

        :return: The vol_creation of this LongLivedOperation.
        :rtype: VolumeOperation
        :required/optional: optional
        """
        return self._vol_creation

    @vol_creation.setter
    def vol_creation(self, vol_creation):
        """
        Sets the vol_creation of this LongLivedOperation.
        A DDP Volume is in the creating state.

        :param vol_creation: The vol_creation of this LongLivedOperation.
        :type: VolumeOperation
        """
        self._vol_creation = vol_creation

    @property
    def vol_deletion(self):
        """
        Gets the vol_deletion of this LongLivedOperation.
        A DDP Volume is in the deleting state.

        :return: The vol_deletion of this LongLivedOperation.
        :rtype: VolumeOperation
        :required/optional: optional
        """
        return self._vol_deletion

    @vol_deletion.setter
    def vol_deletion(self, vol_deletion):
        """
        Sets the vol_deletion of this LongLivedOperation.
        A DDP Volume is in the deleting state.

        :param vol_deletion: The vol_deletion of this LongLivedOperation.
        :type: VolumeOperation
        """
        self._vol_deletion = vol_deletion

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
