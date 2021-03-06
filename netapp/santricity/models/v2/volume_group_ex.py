# coding: utf-8

"""
VolumeGroupEx.py

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


class VolumeGroupEx(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        VolumeGroupEx - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'sequence_num': 'int',  # (required parameter)
            'offline': 'bool',  # (required parameter)
            'raid_level': 'str',  # (required parameter)
            'world_wide_name': 'str',  # (required parameter)
            'volume_group_ref': 'str',  # (required parameter)
            'reserved1': 'str',  
            'reserved2': 'str',  
            'tray_loss_protection': 'bool',  # (required parameter)
            'label': 'str',  # (required parameter)
            'state': 'str',  # (required parameter)
            'spindle_speed_match': 'bool',  # (required parameter)
            'spindle_speed': 'int',  
            'is_inaccessible': 'bool',  # (required parameter)
            'security_type': 'str',  # (required parameter)
            'drawer_loss_protection': 'bool',  # (required parameter)
            'protection_information_capable': 'bool',  # (required parameter)
            'protection_information_capabilities': 'ProtectionInformationCapabilities',  # (required parameter)
            'volume_group_data': 'VolumeGroupTypeData',  # (required parameter)
            'usage': 'str',  # (required parameter)
            'drive_block_format': 'str',  # (required parameter)
            'reserved_space_allocated': 'bool',  # (required parameter)
            'security_level': 'str',  # (required parameter)
            'used_space': 'int',  
            'total_raided_space': 'int',  
            'extents': 'list[FreeExtent]',  
            'largest_free_extent_size': 'int',  
            'raid_status': 'str',  
            'free_space': 'int',  
            'drive_physical_type': 'str',  
            'drive_media_type': 'str',  
            'normalized_spindle_speed': 'str',  
            'disk_pool': 'bool',  
            'id': 'str',  
            'name': 'str'
        }

        self.attribute_map = {
            'sequence_num': 'sequenceNum',  # (required parameter)
            'offline': 'offline',  # (required parameter)
            'raid_level': 'raidLevel',  # (required parameter)
            'world_wide_name': 'worldWideName',  # (required parameter)
            'volume_group_ref': 'volumeGroupRef',  # (required parameter)
            'reserved1': 'reserved1',  
            'reserved2': 'reserved2',  
            'tray_loss_protection': 'trayLossProtection',  # (required parameter)
            'label': 'label',  # (required parameter)
            'state': 'state',  # (required parameter)
            'spindle_speed_match': 'spindleSpeedMatch',  # (required parameter)
            'spindle_speed': 'spindleSpeed',  
            'is_inaccessible': 'isInaccessible',  # (required parameter)
            'security_type': 'securityType',  # (required parameter)
            'drawer_loss_protection': 'drawerLossProtection',  # (required parameter)
            'protection_information_capable': 'protectionInformationCapable',  # (required parameter)
            'protection_information_capabilities': 'protectionInformationCapabilities',  # (required parameter)
            'volume_group_data': 'volumeGroupData',  # (required parameter)
            'usage': 'usage',  # (required parameter)
            'drive_block_format': 'driveBlockFormat',  # (required parameter)
            'reserved_space_allocated': 'reservedSpaceAllocated',  # (required parameter)
            'security_level': 'securityLevel',  # (required parameter)
            'used_space': 'usedSpace',  
            'total_raided_space': 'totalRaidedSpace',  
            'extents': 'extents',  
            'largest_free_extent_size': 'largestFreeExtentSize',  
            'raid_status': 'raidStatus',  
            'free_space': 'freeSpace',  
            'drive_physical_type': 'drivePhysicalType',  
            'drive_media_type': 'driveMediaType',  
            'normalized_spindle_speed': 'normalizedSpindleSpeed',  
            'disk_pool': 'diskPool',  
            'id': 'id',  
            'name': 'name'
        }

        self._sequence_num = None
        self._offline = None
        self._raid_level = None
        self._world_wide_name = None
        self._volume_group_ref = None
        self._reserved1 = None
        self._reserved2 = None
        self._tray_loss_protection = None
        self._label = None
        self._state = None
        self._spindle_speed_match = None
        self._spindle_speed = None
        self._is_inaccessible = None
        self._security_type = None
        self._drawer_loss_protection = None
        self._protection_information_capable = None
        self._protection_information_capabilities = None
        self._volume_group_data = None
        self._usage = None
        self._drive_block_format = None
        self._reserved_space_allocated = None
        self._security_level = None
        self._used_space = None
        self._total_raided_space = None
        self._extents = None
        self._largest_free_extent_size = None
        self._raid_status = None
        self._free_space = None
        self._drive_physical_type = None
        self._drive_media_type = None
        self._normalized_spindle_speed = None
        self._disk_pool = None
        self._id = None
        self._name = None

    @property
    def sequence_num(self):
        """
        Gets the sequence_num of this VolumeGroupEx.
        A sequence number that uniquely identifies this volume group within the array in which it resides. Sequence numbers are assigned to volume groups when they are created or imported into a storage array. The controller assigns the lowest unused sequence number during a creation or import operation.

        :return: The sequence_num of this VolumeGroupEx.
        :rtype: int
        :required/optional: required
        """
        return self._sequence_num

    @sequence_num.setter
    def sequence_num(self, sequence_num):
        """
        Sets the sequence_num of this VolumeGroupEx.
        A sequence number that uniquely identifies this volume group within the array in which it resides. Sequence numbers are assigned to volume groups when they are created or imported into a storage array. The controller assigns the lowest unused sequence number during a creation or import operation.

        :param sequence_num: The sequence_num of this VolumeGroupEx.
        :type: int
        """
        self._sequence_num = sequence_num

    @property
    def offline(self):
        """
        Gets the offline of this VolumeGroupEx.
        An indication of whether the volume group is currently offline. A volume group can be taken offline by the operator in preparation for removing its drives and transporting them to another storage array.

        :return: The offline of this VolumeGroupEx.
        :rtype: bool
        :required/optional: required
        """
        return self._offline

    @offline.setter
    def offline(self, offline):
        """
        Sets the offline of this VolumeGroupEx.
        An indication of whether the volume group is currently offline. A volume group can be taken offline by the operator in preparation for removing its drives and transporting them to another storage array.

        :param offline: The offline of this VolumeGroupEx.
        :type: bool
        """
        self._offline = offline

    @property
    def raid_level(self):
        """
        Gets the raid_level of this VolumeGroupEx.
        The RAID level associated with this volume group. If the storage array supports multiple RAID levels per volume group, this value will be set to RAID_ALL. Otherwise, it will indicate the precise RAID level defined for the volume group.

        :return: The raid_level of this VolumeGroupEx.
        :rtype: str
        :required/optional: required
        """
        return self._raid_level

    @raid_level.setter
    def raid_level(self, raid_level):
        """
        Sets the raid_level of this VolumeGroupEx.
        The RAID level associated with this volume group. If the storage array supports multiple RAID levels per volume group, this value will be set to RAID_ALL. Otherwise, it will indicate the precise RAID level defined for the volume group.

        :param raid_level: The raid_level of this VolumeGroupEx.
        :type: str
        """
        allowed_values = ["raidUnsupported", "raidAll", "raid0", "raid1", "raid3", "raid5", "raid6", "raidDiskPool", "__UNDEFINED"]
        if raid_level not in allowed_values:
            raise ValueError(
                "Invalid value for `raid_level`, must be one of {0}"
                .format(allowed_values)
            )
        self._raid_level = raid_level

    @property
    def world_wide_name(self):
        """
        Gets the world_wide_name of this VolumeGroupEx.
        A variable-length opaque field that provides the volume group's worldwide unique identification value.

        :return: The world_wide_name of this VolumeGroupEx.
        :rtype: str
        :required/optional: required
        """
        return self._world_wide_name

    @world_wide_name.setter
    def world_wide_name(self, world_wide_name):
        """
        Sets the world_wide_name of this VolumeGroupEx.
        A variable-length opaque field that provides the volume group's worldwide unique identification value.

        :param world_wide_name: The world_wide_name of this VolumeGroupEx.
        :type: str
        """
        self._world_wide_name = world_wide_name

    @property
    def volume_group_ref(self):
        """
        Gets the volume_group_ref of this VolumeGroupEx.
        The unique identification value for this volume group. Other objects may use this reference value to refer to the volume group.

        :return: The volume_group_ref of this VolumeGroupEx.
        :rtype: str
        :required/optional: required
        """
        return self._volume_group_ref

    @volume_group_ref.setter
    def volume_group_ref(self, volume_group_ref):
        """
        Sets the volume_group_ref of this VolumeGroupEx.
        The unique identification value for this volume group. Other objects may use this reference value to refer to the volume group.

        :param volume_group_ref: The volume_group_ref of this VolumeGroupEx.
        :type: str
        """
        self._volume_group_ref = volume_group_ref

    @property
    def reserved1(self):
        """
        Gets the reserved1 of this VolumeGroupEx.


        :return: The reserved1 of this VolumeGroupEx.
        :rtype: str
        :required/optional: optional
        """
        return self._reserved1

    @reserved1.setter
    def reserved1(self, reserved1):
        """
        Sets the reserved1 of this VolumeGroupEx.


        :param reserved1: The reserved1 of this VolumeGroupEx.
        :type: str
        """
        self._reserved1 = reserved1

    @property
    def reserved2(self):
        """
        Gets the reserved2 of this VolumeGroupEx.


        :return: The reserved2 of this VolumeGroupEx.
        :rtype: str
        :required/optional: optional
        """
        return self._reserved2

    @reserved2.setter
    def reserved2(self, reserved2):
        """
        Sets the reserved2 of this VolumeGroupEx.


        :param reserved2: The reserved2 of this VolumeGroupEx.
        :type: str
        """
        self._reserved2 = reserved2

    @property
    def tray_loss_protection(self):
        """
        Gets the tray_loss_protection of this VolumeGroupEx.
        An indication as to whether the volume group has tray loss protection.

        :return: The tray_loss_protection of this VolumeGroupEx.
        :rtype: bool
        :required/optional: required
        """
        return self._tray_loss_protection

    @tray_loss_protection.setter
    def tray_loss_protection(self, tray_loss_protection):
        """
        Sets the tray_loss_protection of this VolumeGroupEx.
        An indication as to whether the volume group has tray loss protection.

        :param tray_loss_protection: The tray_loss_protection of this VolumeGroupEx.
        :type: bool
        """
        self._tray_loss_protection = tray_loss_protection

    @property
    def label(self):
        """
        Gets the label of this VolumeGroupEx.
        The volume group label, which can be set by the user.

        :return: The label of this VolumeGroupEx.
        :rtype: str
        :required/optional: required
        """
        return self._label

    @label.setter
    def label(self, label):
        """
        Sets the label of this VolumeGroupEx.
        The volume group label, which can be set by the user.

        :param label: The label of this VolumeGroupEx.
        :type: str
        """
        self._label = label

    @property
    def state(self):
        """
        Gets the state of this VolumeGroupEx.
        The state of the volume group.

        :return: The state of this VolumeGroupEx.
        :rtype: str
        :required/optional: required
        """
        return self._state

    @state.setter
    def state(self, state):
        """
        Sets the state of this VolumeGroupEx.
        The state of the volume group.

        :param state: The state of this VolumeGroupEx.
        :type: str
        """
        allowed_values = ["contingent", "exported", "forced", "complete", "partial", "incomplete", "missing", "__UNDEFINED"]
        if state not in allowed_values:
            raise ValueError(
                "Invalid value for `state`, must be one of {0}"
                .format(allowed_values)
            )
        self._state = state

    @property
    def spindle_speed_match(self):
        """
        Gets the spindle_speed_match of this VolumeGroupEx.
        Set to true if all of the drives in the group have matching normalized spindle speeds. (Normalized spindle speeds are standardized norms (e.g., 5400, 7200, etc.) that are used for spindle speed matching, even though actual spindle speeds may be within a designated delta of the normalized speed.)

        :return: The spindle_speed_match of this VolumeGroupEx.
        :rtype: bool
        :required/optional: required
        """
        return self._spindle_speed_match

    @spindle_speed_match.setter
    def spindle_speed_match(self, spindle_speed_match):
        """
        Sets the spindle_speed_match of this VolumeGroupEx.
        Set to true if all of the drives in the group have matching normalized spindle speeds. (Normalized spindle speeds are standardized norms (e.g., 5400, 7200, etc.) that are used for spindle speed matching, even though actual spindle speeds may be within a designated delta of the normalized speed.)

        :param spindle_speed_match: The spindle_speed_match of this VolumeGroupEx.
        :type: bool
        """
        self._spindle_speed_match = spindle_speed_match

    @property
    def spindle_speed(self):
        """
        Gets the spindle_speed of this VolumeGroupEx.
        The spindle speed of the drives composing the pool (RPM)

        :return: The spindle_speed of this VolumeGroupEx.
        :rtype: int
        :required/optional: optional
        """
        return self._spindle_speed

    @spindle_speed.setter
    def spindle_speed(self, spindle_speed):
        """
        Sets the spindle_speed of this VolumeGroupEx.
        The spindle speed of the drives composing the pool (RPM)

        :param spindle_speed: The spindle_speed of this VolumeGroupEx.
        :type: int
        """
        self._spindle_speed = spindle_speed

    @property
    def is_inaccessible(self):
        """
        Gets the is_inaccessible of this VolumeGroupEx.
        True if the volume group contains incompatible drives that have been locked out.

        :return: The is_inaccessible of this VolumeGroupEx.
        :rtype: bool
        :required/optional: required
        """
        return self._is_inaccessible

    @is_inaccessible.setter
    def is_inaccessible(self, is_inaccessible):
        """
        Sets the is_inaccessible of this VolumeGroupEx.
        True if the volume group contains incompatible drives that have been locked out.

        :param is_inaccessible: The is_inaccessible of this VolumeGroupEx.
        :type: bool
        """
        self._is_inaccessible = is_inaccessible

    @property
    def security_type(self):
        """
        Gets the security_type of this VolumeGroupEx.
        security status of the drive group

        :return: The security_type of this VolumeGroupEx.
        :rtype: str
        :required/optional: required
        """
        return self._security_type

    @security_type.setter
    def security_type(self, security_type):
        """
        Sets the security_type of this VolumeGroupEx.
        security status of the drive group

        :param security_type: The security_type of this VolumeGroupEx.
        :type: str
        """
        allowed_values = ["unknown", "none", "capable", "enabled", "__UNDEFINED"]
        if security_type not in allowed_values:
            raise ValueError(
                "Invalid value for `security_type`, must be one of {0}"
                .format(allowed_values)
            )
        self._security_type = security_type

    @property
    def drawer_loss_protection(self):
        """
        Gets the drawer_loss_protection of this VolumeGroupEx.
        This field is set to true when the volume group has drawer loss protection; otherwise it is set to false

        :return: The drawer_loss_protection of this VolumeGroupEx.
        :rtype: bool
        :required/optional: required
        """
        return self._drawer_loss_protection

    @drawer_loss_protection.setter
    def drawer_loss_protection(self, drawer_loss_protection):
        """
        Sets the drawer_loss_protection of this VolumeGroupEx.
        This field is set to true when the volume group has drawer loss protection; otherwise it is set to false

        :param drawer_loss_protection: The drawer_loss_protection of this VolumeGroupEx.
        :type: bool
        """
        self._drawer_loss_protection = drawer_loss_protection

    @property
    def protection_information_capable(self):
        """
        Gets the protection_information_capable of this VolumeGroupEx.
        This field is no longer used.

        :return: The protection_information_capable of this VolumeGroupEx.
        :rtype: bool
        :required/optional: required
        """
        return self._protection_information_capable

    @protection_information_capable.setter
    def protection_information_capable(self, protection_information_capable):
        """
        Sets the protection_information_capable of this VolumeGroupEx.
        This field is no longer used.

        :param protection_information_capable: The protection_information_capable of this VolumeGroupEx.
        :type: bool
        """
        self._protection_information_capable = protection_information_capable

    @property
    def protection_information_capabilities(self):
        """
        Gets the protection_information_capabilities of this VolumeGroupEx.
        This structure contains a protectionInformationCapable field which is set to true if all drives in the volume group are Protection Information (PI) capable. It also contains a field that is set to the protection type for the volume group.

        :return: The protection_information_capabilities of this VolumeGroupEx.
        :rtype: ProtectionInformationCapabilities
        :required/optional: required
        """
        return self._protection_information_capabilities

    @protection_information_capabilities.setter
    def protection_information_capabilities(self, protection_information_capabilities):
        """
        Sets the protection_information_capabilities of this VolumeGroupEx.
        This structure contains a protectionInformationCapable field which is set to true if all drives in the volume group are Protection Information (PI) capable. It also contains a field that is set to the protection type for the volume group.

        :param protection_information_capabilities: The protection_information_capabilities of this VolumeGroupEx.
        :type: ProtectionInformationCapabilities
        """
        self._protection_information_capabilities = protection_information_capabilities

    @property
    def volume_group_data(self):
        """
        Gets the volume_group_data of this VolumeGroupEx.
        Information about the Volume Group.

        :return: The volume_group_data of this VolumeGroupEx.
        :rtype: VolumeGroupTypeData
        :required/optional: required
        """
        return self._volume_group_data

    @volume_group_data.setter
    def volume_group_data(self, volume_group_data):
        """
        Sets the volume_group_data of this VolumeGroupEx.
        Information about the Volume Group.

        :param volume_group_data: The volume_group_data of this VolumeGroupEx.
        :type: VolumeGroupTypeData
        """
        self._volume_group_data = volume_group_data

    @property
    def usage(self):
        """
        Gets the usage of this VolumeGroupEx.
        the volume group usage.

        :return: The usage of this VolumeGroupEx.
        :rtype: str
        :required/optional: required
        """
        return self._usage

    @usage.setter
    def usage(self, usage):
        """
        Sets the usage of this VolumeGroupEx.
        the volume group usage.

        :param usage: The usage of this VolumeGroupEx.
        :type: str
        """
        allowed_values = ["unknown", "standard", "flashcache", "__UNDEFINED"]
        if usage not in allowed_values:
            raise ValueError(
                "Invalid value for `usage`, must be one of {0}"
                .format(allowed_values)
            )
        self._usage = usage

    @property
    def drive_block_format(self):
        """
        Gets the drive_block_format of this VolumeGroupEx.
        Identifies the drive block format of the volume candidate.

        :return: The drive_block_format of this VolumeGroupEx.
        :rtype: str
        :required/optional: required
        """
        return self._drive_block_format

    @drive_block_format.setter
    def drive_block_format(self, drive_block_format):
        """
        Sets the drive_block_format of this VolumeGroupEx.
        Identifies the drive block format of the volume candidate.

        :param drive_block_format: The drive_block_format of this VolumeGroupEx.
        :type: str
        """
        allowed_values = ["unknown", "allNative", "allEmulated", "mixed", "__UNDEFINED"]
        if drive_block_format not in allowed_values:
            raise ValueError(
                "Invalid value for `drive_block_format`, must be one of {0}"
                .format(allowed_values)
            )
        self._drive_block_format = drive_block_format

    @property
    def reserved_space_allocated(self):
        """
        Gets the reserved_space_allocated of this VolumeGroupEx.
        This field will be used to report whether or not reserved space has been claimed on all drives in the volume group. The recovery-volume script will include this field for each volume group record it creates, so that during volume recovery the volume group is recreated correctly.

        :return: The reserved_space_allocated of this VolumeGroupEx.
        :rtype: bool
        :required/optional: required
        """
        return self._reserved_space_allocated

    @reserved_space_allocated.setter
    def reserved_space_allocated(self, reserved_space_allocated):
        """
        Sets the reserved_space_allocated of this VolumeGroupEx.
        This field will be used to report whether or not reserved space has been claimed on all drives in the volume group. The recovery-volume script will include this field for each volume group record it creates, so that during volume recovery the volume group is recreated correctly.

        :param reserved_space_allocated: The reserved_space_allocated of this VolumeGroupEx.
        :type: bool
        """
        self._reserved_space_allocated = reserved_space_allocated

    @property
    def security_level(self):
        """
        Gets the security_level of this VolumeGroupEx.
        Refines the information in the securityType field to describe the set of drives.

        :return: The security_level of this VolumeGroupEx.
        :rtype: str
        :required/optional: required
        """
        return self._security_level

    @security_level.setter
    def security_level(self, security_level):
        """
        Sets the security_level of this VolumeGroupEx.
        Refines the information in the securityType field to describe the set of drives.

        :param security_level: The security_level of this VolumeGroupEx.
        :type: str
        """
        allowed_values = ["unknown", "none", "mixed", "fde", "fips", "__UNDEFINED"]
        if security_level not in allowed_values:
            raise ValueError(
                "Invalid value for `security_level`, must be one of {0}"
                .format(allowed_values)
            )
        self._security_level = security_level

    @property
    def used_space(self):
        """
        Gets the used_space of this VolumeGroupEx.


        :return: The used_space of this VolumeGroupEx.
        :rtype: int
        :required/optional: optional
        """
        return self._used_space

    @used_space.setter
    def used_space(self, used_space):
        """
        Sets the used_space of this VolumeGroupEx.


        :param used_space: The used_space of this VolumeGroupEx.
        :type: int
        """
        self._used_space = used_space

    @property
    def total_raided_space(self):
        """
        Gets the total_raided_space of this VolumeGroupEx.
        Raw capacity of the volumeGroup

        :return: The total_raided_space of this VolumeGroupEx.
        :rtype: int
        :required/optional: optional
        """
        return self._total_raided_space

    @total_raided_space.setter
    def total_raided_space(self, total_raided_space):
        """
        Sets the total_raided_space of this VolumeGroupEx.
        Raw capacity of the volumeGroup

        :param total_raided_space: The total_raided_space of this VolumeGroupEx.
        :type: int
        """
        self._total_raided_space = total_raided_space

    @property
    def extents(self):
        """
        Gets the extents of this VolumeGroupEx.


        :return: The extents of this VolumeGroupEx.
        :rtype: list[FreeExtent]
        :required/optional: optional
        """
        return self._extents

    @extents.setter
    def extents(self, extents):
        """
        Sets the extents of this VolumeGroupEx.


        :param extents: The extents of this VolumeGroupEx.
        :type: list[FreeExtent]
        """
        self._extents = extents

    @property
    def largest_free_extent_size(self):
        """
        Gets the largest_free_extent_size of this VolumeGroupEx.


        :return: The largest_free_extent_size of this VolumeGroupEx.
        :rtype: int
        :required/optional: optional
        """
        return self._largest_free_extent_size

    @largest_free_extent_size.setter
    def largest_free_extent_size(self, largest_free_extent_size):
        """
        Sets the largest_free_extent_size of this VolumeGroupEx.


        :param largest_free_extent_size: The largest_free_extent_size of this VolumeGroupEx.
        :type: int
        """
        self._largest_free_extent_size = largest_free_extent_size

    @property
    def raid_status(self):
        """
        Gets the raid_status of this VolumeGroupEx.
        The raid status reflects the worst case raid level of any volume on the group

        :return: The raid_status of this VolumeGroupEx.
        :rtype: str
        :required/optional: optional
        """
        return self._raid_status

    @raid_status.setter
    def raid_status(self, raid_status):
        """
        Sets the raid_status of this VolumeGroupEx.
        The raid status reflects the worst case raid level of any volume on the group

        :param raid_status: The raid_status of this VolumeGroupEx.
        :type: str
        """
        allowed_values = ["optimal", "degraded", "failed", "impaired", "creating", "deleting", "__UNDEFINED", None]
        if raid_status not in allowed_values:
            raise ValueError(
                "Invalid value for `raid_status`, must be one of {0}"
                .format(allowed_values)
            )
        self._raid_status = raid_status

    @property
    def free_space(self):
        """
        Gets the free_space of this VolumeGroupEx.


        :return: The free_space of this VolumeGroupEx.
        :rtype: int
        :required/optional: optional
        """
        return self._free_space

    @free_space.setter
    def free_space(self, free_space):
        """
        Sets the free_space of this VolumeGroupEx.


        :param free_space: The free_space of this VolumeGroupEx.
        :type: int
        """
        self._free_space = free_space

    @property
    def drive_physical_type(self):
        """
        Gets the drive_physical_type of this VolumeGroupEx.
        Defines the physical interface type of the underlying drives.

        :return: The drive_physical_type of this VolumeGroupEx.
        :rtype: str
        :required/optional: optional
        """
        return self._drive_physical_type

    @drive_physical_type.setter
    def drive_physical_type(self, drive_physical_type):
        """
        Sets the drive_physical_type of this VolumeGroupEx.
        Defines the physical interface type of the underlying drives.

        :param drive_physical_type: The drive_physical_type of this VolumeGroupEx.
        :type: str
        """
        allowed_values = ["all", "scsi", "fibre", "sata", "pata", "fibre520b", "sas", "unknown", "sas4k", "__UNDEFINED", None]
        if drive_physical_type not in allowed_values:
            raise ValueError(
                "Invalid value for `drive_physical_type`, must be one of {0}"
                .format(allowed_values)
            )
        self._drive_physical_type = drive_physical_type

    @property
    def drive_media_type(self):
        """
        Gets the drive_media_type of this VolumeGroupEx.
        Defines whether is an SSD or a spinning drive.

        :return: The drive_media_type of this VolumeGroupEx.
        :rtype: str
        :required/optional: optional
        """
        return self._drive_media_type

    @drive_media_type.setter
    def drive_media_type(self, drive_media_type):
        """
        Sets the drive_media_type of this VolumeGroupEx.
        Defines whether is an SSD or a spinning drive.

        :param drive_media_type: The drive_media_type of this VolumeGroupEx.
        :type: str
        """
        allowed_values = ["all", "unknown", "hdd", "ssd", "__UNDEFINED", None]
        if drive_media_type not in allowed_values:
            raise ValueError(
                "Invalid value for `drive_media_type`, must be one of {0}"
                .format(allowed_values)
            )
        self._drive_media_type = drive_media_type

    @property
    def normalized_spindle_speed(self):
        """
        Gets the normalized_spindle_speed of this VolumeGroupEx.
        The normalized spindle speed of the drives composing the pool. Ex: 7200, 5400, 15000. If drives have mismatched spindle speeds, this value may not be accurate.

        :return: The normalized_spindle_speed of this VolumeGroupEx.
        :rtype: str
        :required/optional: optional
        """
        return self._normalized_spindle_speed

    @normalized_spindle_speed.setter
    def normalized_spindle_speed(self, normalized_spindle_speed):
        """
        Sets the normalized_spindle_speed of this VolumeGroupEx.
        The normalized spindle speed of the drives composing the pool. Ex: 7200, 5400, 15000. If drives have mismatched spindle speeds, this value may not be accurate.

        :param normalized_spindle_speed: The normalized_spindle_speed of this VolumeGroupEx.
        :type: str
        """
        allowed_values = ["spindleSpeedUnknown", "spindleSpeedSSD", "spindleSpeed5400", "spindleSpeed7200", "spindleSpeed10k", "spindleSpeed15k", None]
        if normalized_spindle_speed not in allowed_values:
            raise ValueError(
                "Invalid value for `normalized_spindle_speed`, must be one of {0}"
                .format(allowed_values)
            )
        self._normalized_spindle_speed = normalized_spindle_speed

    @property
    def disk_pool(self):
        """
        Gets the disk_pool of this VolumeGroupEx.
        True if the RAID Level is defined as raidDiskPool.

        :return: The disk_pool of this VolumeGroupEx.
        :rtype: bool
        :required/optional: optional
        """
        return self._disk_pool

    @disk_pool.setter
    def disk_pool(self, disk_pool):
        """
        Sets the disk_pool of this VolumeGroupEx.
        True if the RAID Level is defined as raidDiskPool.

        :param disk_pool: The disk_pool of this VolumeGroupEx.
        :type: bool
        """
        self._disk_pool = disk_pool

    @property
    def id(self):
        """
        Gets the id of this VolumeGroupEx.


        :return: The id of this VolumeGroupEx.
        :rtype: str
        :required/optional: optional
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this VolumeGroupEx.


        :param id: The id of this VolumeGroupEx.
        :type: str
        """
        self._id = id

    @property
    def name(self):
        """
        Gets the name of this VolumeGroupEx.


        :return: The name of this VolumeGroupEx.
        :rtype: str
        :required/optional: optional
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this VolumeGroupEx.


        :param name: The name of this VolumeGroupEx.
        :type: str
        """
        self._name = name

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

