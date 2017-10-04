# coding: utf-8

"""
DriveTemperatureReturned.py

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


class DriveTemperatureReturned(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        DriveTemperatureReturned - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'return_code': 'str',  # (required parameter)
            'drive_temp_data': 'list[DriveTemperatureData]'
        }

        self.attribute_map = {
            'return_code': 'returnCode',  # (required parameter)
            'drive_temp_data': 'driveTempData'
        }

        self._return_code = None
        self._drive_temp_data = None

    @property
    def return_code(self):
        """
        Gets the return_code of this DriveTemperatureReturned.
        An enumeration used to determine the return status of a SYMbol function call.

        :return: The return_code of this DriveTemperatureReturned.
        :rtype: str
        :required/optional: required
        """
        return self._return_code

    @return_code.setter
    def return_code(self, return_code):
        """
        Sets the return_code of this DriveTemperatureReturned.
        An enumeration used to determine the return status of a SYMbol function call.

        :param return_code: The return_code of this DriveTemperatureReturned.
        :type: str
        """
        allowed_values = ["uninitialized", "ok", "error", "busy", "illegalParam", "noHeap", "driveNotExist", "driveNotUnassigned", "noSparesAssigned", "someSparesAssigned", "volumeNotExist", "volumeReconfiguring", "notDualActive", "tryAlternate", "background", "notImplemented", "reservationConflict", "volumeDead", "internalError", "invalidRequest", "iconFailure", "volumeFormatting", "altRemoved", "cacheSyncFailure", "invalidFile", "reconfigSmallDacstore", "reconfigFailure", "nvramError", "flashError", "authFailParam", "authFailPassword", "memParityError", "invalidControllerref", "invalidVolumegroupref", "invalidVolumeref", "invalidDriveref", "invalidFreeextentref", "volumeOffline", "volumeNotOptimal", "modesenseError", "invalidSegmentsize", "invalidCacheblksize", "invalidFlushThreshold", "invalidFlushAmount", "invalidLabel", "invalidCacheModifier", "invalidReadahead", "invalidReconpriority", "invalidScanperiod", "invalidTrayposLength", "invalidRegionid", "invalidFibreid", "invalidEncryption", "invalidRaidlevel", "invalidExpansionList", "noSparesDeassigned", "someSparesDeassigned", "partDupId", "partLabelInvalid", "partNodeNonexistent", "partPortIdInvalid", "partVolumeNonexistent", "partLunCollision", "maxVolMappingExceeded", "partMappingNonexistent", "partNoHostports", "imageTransferred", "fileTooLarge", "invalidOffset", "overrun", "invalidChunksize", "invalidTotalsize", "downloadNotPermitted", "spawnError", "voltransferError", "invalidDlstate", "cacheconfigError", "downloadInProgress", "driveNotOptimal", "driveRemoved", "duplicateDrives", "numdrivesAdditional", "numdrivesGroup", "driveTooSmall", "capacityConstrained", "maxVolumesExceeded", "partIsUtmLun", "someSparesTooSmall", "sparesSmallUnassigned", "tooManyPartitions", "parityScanInProgress", "invalidSafeId", "invalidSafeKey", "invalidSafeCapability", "invalidSafeVersion", "partitionsDisabled", "driveDownloadFailed", "esmDownloadFailed", "esmPartialUpdate", "utmConflict", "noVolumes", "authFailReadpassword", "partCrteFailTblFull", "attemptToSetLocal", "invalidHostTypeIndex", "failVolumeVisible", "noDeleteUtmInUse", "invalidLun", "utmTooManyMaps", "diagReadFailure", "diagSrcLinkDown", "diagWriteFailure", "diagLoopbackError", "diagTimeout", "diagInProgress", "diagNoAlt", "diagIconSendErr", "diagInitErr", "diagModeErr", "diagInvalidTestId", "diagDriveErr", "diagLockErr", "diagConfigErr", "diagNoCacheMem", "diagNotQuiesced", "diagUtmNotEnabled", "invalidModeSwitch", "invalidPortname", "duplicateVolMapping", "maxSnapsPerBaseExceeded", "maxSnapsExceeded", "invalidBasevol", "snapNotAvailable", "notDisabled", "snapshotFeatureDisabled", "repositoryOffline", "repositoryReconfiguring", "rollbackInProgress", "numVolumesGroup", "ghostVolume", "repositoryMissing", "invalidRepositoryLabel", "invalidSnapLabel", "invalidRollbackPriority", "invalidWarnThreshold", "cannotMapVolume", "cannotFormatVolume", "dstNotFibre", "repositoryTooSmall", "repositoryFailed", "baseVolumeFailed", "baseVolumeOffline", "baseVolumeFormatting", "metadataVolNonexistent", "rvmFeatureDisabled", "mirrorsPresent", "rvmFeatureDeactivated", "maxMirrorsExceeded", "invalidMirrorCandidateVol", "invalidMirrorvol", "metadataAlreadyExists", "metadataMissing", "metadataOffline", "metadataReconfiguring", "localRoleChangeFailed", "remoteRoleChangeFailed", "localRoleChangeSuccessful", "onlyLocalMirrorDeleted", "noValidMirrorCandidate", "remoteMaxMirrorsExceeded", "remoteRvmFeatureDisabled", "remoteMetadataVolNonexistent", "notRegistered", "remoteInvalidCfgGen", "localRoleChangedNotForced", "remoteRoleChangedLocalFailed", "rvmSpmError", "remoteAuthFailPassword", "rvmVersionMismatch", "rvmRemoteArrayError", "rvmCommunicationError", "rvmFibreError", "mirrorVolNotPrimary", "secNotPromoteable", "priNotDemoteable", "metadataChildDeletion", "rmtvolOrphanDeletion", "rvmActivateDisallowed", "invalidTrayref", "partialDeletion", "defaultUtmCollision", "invalidCopyPriority", "invalidVolumecopyref", "copyChangeFailed", "copyActive", "copyInactive", "copyIncompatibleSource", "copyIncompatibleTarget", "copyGhostSource", "copyGhostTarget", "copyInvalidSourceRef", "copyInvalidTargetRef", "copyInvalidSourceState", "copyInvalidTargetState", "copySourceReconfig", "copyTargetReconfig", "copyTargetTooSmall", "copyTargetLimit", "maxVolumeCopysExceeded", "copySourceReservation", "copyTargetReservation", "copySourceFormat", "copyTargetFormat", "copyStartFailed", "copyStopFailed", "volcopyFeatureDisabled", "writeLock", "cannotReconfigure", "authFailContLockout", "prReservationConflict", "regDeleteFailed", "batteryNotInConfig", "batteryMissing", "noChannel", "rvmOperNotAllowedOnSec", "dataRedundancyRequired", "copySourceZeroCapacity", "invHostlunDefineMapping", "invHostlunMoveMapping", "invHostlunDefineHosttype", "invHostlunMoveHostport", "fwIncompatible", "mirrorAlreadySuspended", "insuffLocalMirRepResources", "insuffRemtMirRepResources", "ghostHasUnreadableSectors", "rvmCommStatRecoveredTimeout", "rvmCommStatRecoveredDelay", "rvmCommStatNotReady", "rvmCommStatTimeout", "rvmCommStatChannelFailure", "rvmCommStatNetworkFailure", "rvmCommStatDeviceMissing", "rvmCommStatLoginRejected", "rvmCommStatLoginFailure", "rvmCommStatInvNumSamplesReqd", "rvmQuiescenceInProgress", "rvmInvalidRemotevol", "sodInProgress", "invalidDrives", "invalidSetid", "invalidSetsize", "missingData", "quiescenceFailed", "validationError", "downloadHalted", "allFailed", "partialOk", "obsolete", "usmClearFailed", "controllerInServiceMode", "invalidDrive", "databaseError", "backgroundAutocfg", "autocfgInprogress", "unsupportedLhaSataEsm", "parityScanFailed", "parityRepairFailed", "mediaRepairFailed", "mirrorDegraded", "prohibitedByMdtRestrictions", "prohibitedByGoldKeyRestrictions", "safeControllerNotSubjectToGoldKey", "safeMdtNotPremiumFeature", "alarmNotPresent", "dltNotCompleted", "dependancyError", "cdmDatabaseFull", "requiredConditionNotPresent", "ddcUnavail", "ddcIllegalParam", "invalidDdcTag", "hosttypeConflict", "portConflict", "invalidHosttypeString", "invalidProtocol", "portRemoved", "disableNotPermitted", "prohibitedByDriveTrayLimit", "invalidEsmref", "invalidBundleMigration", "invalidBundleKey", "noSparesNeeded", "prohibitedByFeatureBundleViolation", "invalidAuthMethod", "invalidSecret", "secretAlreadyInUse", "manualConfigModeSet", "noIscsiSessions", "invalidInterfaceref", "initiatorConflict", "initiatorRemoved", "basevolSizeChanged", "volumeGroupNotExist", "volumeGroupNotOnline", "volumeGroupHasHotspare", "volumeGroupReconfiguring", "volumeGroupStateNotValid", "controllerNotOptimal", "insufficientCapacity", "volumeGroupExported", "volumeNotConfigurable", "volumeGroupNotConfigurable", "invalidDriveState", "volumeGroupReconstructing", "volumeGroupUndergoingCopyback", "volumeGroupNotComplete", "volumeGroupHasFailedDrives", "volumeGroupHasNonOptimalVols", "volumeGroupHasMirrorRelationship", "volumeGroupHasVolcopyRelationship", "volumeGroupHasMirroringMetadata", "volumeGroupHasMappedVols", "volumeGroupHasReservations", "volumeGroupHasIncompatibleDacstores", "volumeLimitExceeded", "volumeGroupHasUnknownRaidLevel", "volumeGroupHasUnsupportedRaidLevel", "volumeGroupHasCloneOpportunity", "volumeGroupHasInsufficientDrives", "volumeGroupHasFailedVols", "perfTierSafeUpgradeDisabled", "raid6FeatureUnsupported", "raid6FeatureDisabled", "safeControllerNotSubjectToRaid6", "volumeGroupNotContingent", "channelDiagsRunning", "channelDiagsResultsPartial", "volumeGroupHasSnapshotRelationship", "prohibitedBySafeViolation", "legacyVg", "vgNotForceable", "channelDiagsLockErr", "channelDiagsNotQuiesced", "channelDiagsAltCommFailed", "channelDiagsChanSetupFailed", "channelDiagsDeviceBypassFailed", "channelDiagsResultsNotAvailable", "driveSpinUpError", "driveTypeMismatch", "localRemoteArrayHasSameWwn", "volumeGroupHasIncompatibleDrive", "volumeGroupVolumeEncroachesOnDacstore", "volumeGroupImportInProgress", "drivesNeedToBeSpunUp", "noNativeSstor", "noSuchDebugChunk", "debugInfoConfigChanged", "lockdown", "drivesDacstoresOverlap", "volumeHasAsyncMirror", "reconfigLogSpaceError", "volumeGroupInaccessible", "volumeInitializing", "insufficientCache", "volumeInaccessible", "noDrivesAdopted", "someDrivesAdopted", "exportingDrivesDatabaseResynchronizing", "exportingDrivesDatabaseFailed", "exportingDrivesQuiesced", "learnActiveTryLater", "noLockedDrives", "driveSecurityEnabledFailed", "lockkeyFailed", "invalidSecurity", "noFdeDrives", "volumeGroupSecure", "invalidBlob", "unlockFailed", "noKeySet", "rekeyInProgress", "defaultHostGroupMappingNotAllowed", "ssdMediaScanNotAllowed", "premiumFeatureLimitExceedsMaximum", "disableEvaluationFeatureNotPermitted", "requestFailedDueToLun0Restrictions", "externalKmsEnabled", "externalKmsFailed", "externalKmsNotEnabled", "keyNotNeeded", "keyInvalidSequence", "diagNotRunning", "ctrlNotInServiceMode", "invalidFeatureref", "cacheBackupDevNotExist", "noMatchingLockKeyIdFound", "lockKeyValidationFailed", "lockKeyValidationDisabled", "externalKmsNotCompliant", "externalKmsTimeout", "cannotDisableNoKey", "previouslyEnabledForEval", "featureNotKeyable", "evalNotSupported", "rawdataTransferBadType", "rawdataTransferNotStarted", "rawdataTransferAlreadyStarted", "rawdataTransferPreparing", "rawdataTransferReadError", "rawdataTransferNoDrives", "rawdataTransferInvalidImage", "rawdataTransferCrcError", "dbmRestoreWriteError", "dbmRestoreNoDrives", "rawdataBadSeqNum", "invalidCapability", "externalKeyNotInMemory", "invalidLockKeyId", "invalidProtection", "volumeHasSnapshotRelationship", "volumeHasMirrorRelationship", "externalKmsDisabledNoKey", "dbmRestoreAltCtlNotOffline", "copyApptagMismatch", "invalidRequestForEnclosure", "dqRetrieveNothingToTransfer", "invalidIscsiConfiguration", "volumeHasVolcopyRelationship", "partPiIncapable", "requestFailedDueToPiRestrictions", "rawdataTransferUserCancelled", "duplicateIscsiIpAddress", "portSpeedConflict", "factoryDefaultDownloadFailed", "errorWritingToEeprom", "factoryDefaultPartialUpdate", "snapshotNotActive", "cannotRollback", "mirrorSyncNotPossible", "psuFirmwareDownloadFailed", "psuFirmwareUpdateMfgDeviceCodeMismatch", "psuFirmwareUpdateNotAllRedundant", "psuFirmwareUpdateNotAllOptimal", "insufficientRepositoryCapacity", "rollbackStartFailure", "csbReserveFailed", "csbReleaseFailedNoLock", "csbReleaseFailedInvalidKey", "flashcacheAlreadyExists", "flashcacheFeatureDisabled", "flashcacheAlreadySuspended", "flashcacheNotSuspended", "flashcacheInvalidConfigType", "invalidPitGroupLabel", "invalidPitConsistencyGroupLabel", "invalidPitAutoDeleteLimit", "invalidPitRepositoryFullPolicy", "invalidConcatVolMemberLabel", "concatVolMemberTooSmall", "invalidPitGroupRef", "invalidPitRef", "dveNotAllowed", "dssNotAllowed", "dplCoreDumpInvalidTag", "invalidPitViewLabel", "invalidPitViewRef", "invalidConcatVolRef", "notFlashcacheVol", "flashcacheDeleted", "flashcacheEnabled", "flashcacheNotEnabled", "noRepDeletion", "maxPitsPerGroupExceeded", "maxPitsExceeded", "maxPitGroupsPerBaseExceeded", "maxPitGroupsExceeded", "maxViewsPerPitExceeded", "maxViewsExceeded", "maxConsistencyGroupsExceeded", "maxConsistencyGroupMembersExceeded", "maxMappableVolumesExceeded", "notOldestPit", "viewStopped", "concatMemberLimitExceeded", "invalidMemberVol", "memberVolMapped", "invalidMemberVolState", "invalidTrimCount", "pitGroupInConsistencyGroup", "pitInConsistencyGroup", "pitViewInConsistencyGroup", "incompatibleMemberVol", "volumeInUse", "rvmOverIscsiNotSupported", "arvmGroupUserLabelExists", "arvmGroupDoesNotExist", "arvmGroupNotEmpty", "concatVolumeFailed", "invalidPitConsistencyGroupRef", "invalidPitConsistencyGroupViewRef", "invalidPitConsistencyGroupViewLabel", "alternateRequiredForOperation", "invalidPitForView", "consistencyGroupArvmBindingConflict", "attributeFixedByArvm", "operationFailedVolumeCopyClone", "pitCreatePending", "dbmDbSourceUnavailable", "dbmRestoreSourceMismatch", "invalidCriticalThreshold", "volumeGroupHasArvmRelationship", "arvmRecoveryPointDeletionRequired", "volumeGroupHasPitgroupRelationship", "volumeGroupHasPitviewRelationship", "volumeGroupHasConcatRelationship", "flashcacheSuspended", "flashcacheAlreadyEnabled", "dbmDbImageCorrupt", "illegalVolume", "invalidRepositoryCapacity", "invalidProvisionedCapacityQuota", "invalidExpansionPolicy", "invalidVirtualCapacity", "cannotExpandConcatMember", "thresholdBelowUsedCapacity", "invalidExpansionOperation", "repositoryFull", "insufficientExpansionSpace", "invalidExpansionSize", "invalidReinitAction", "invalidReinitCapacity", "invalidIncompleteMemberRef", "arvmGroupNotPrimary", "arvmGroupNotSecondary", "arvmMemberFailed", "arvmGroupNotSuspended", "arvmInvalidMirrorState", "arvmVolumeAlreadyInMirrorRelationship", "arvmMemberLimitExceeded", "arvmSuspendFailure", "arvmResumeFailure", "arvmSynchronizeFailure", "remoteTargetNotFound", "arvmMirrorMemberDoesNotExist", "snapConversionTooManySnaps", "snapConversionMissingLabel", "arvmFeatureDeactivated", "incompatibleRepositorySecurity", "incompatibleSecondarySecurity", "mirrorProtocolMismatch", "arvmAsyncMirrorGroupPresent", "cacheParametersNotChangeable", "flashcacheMaxCapacityExceeded", "flashcacheFailed", "dplCoreDumpRestoreInProgress", "arvmGroupHasIncompleteMember", "arvmConnectivityTestAlreadyInProgress", "arvmConnectivityTestNetworkError", "arvmConnectivityTestRemoteTimeout", "arvmConnectivityTestLoginFailure", "arvmConnectivityTestNameServiceError", "arvmConnectivityTestTurError", "arvmConnectivityTestMissingRemoteAmg", "arvmConnectivityTestAmgMemberMismatch", "invalidSyncPriority", "invalidRecoveryPointAlertThreshold", "invalidSyncAlertThreshold", "mustSpecifyExistingVolumes", "arvmConnectivityTestTimeoutExceeded", "flashcacheMaxLimitExceeded", "volsInVgUsingNonSecureCapableFlashcache", "volsInVgUsingSecureDisabledFlashcache", "invalidSubmodelId", "premiumFeatureLimitMismatch", "volumeGroupNotImportable", "primaryCacheSizeMismatch", "flashcacheUserLabelExists", "maxThinVolumesExceeded", "arvmInvalidSecondaryCapacity", "arvmOnlyPrimaryMemberRemoved", "arvmOnlySecondaryMemberRemoved", "arvmInvalidAmgRequestWhileSuspended", "arvmManualSyncAlreadyInProgress", "arvmManualSyncRetryTooSoon", "diskPoolNotEmpty", "flashCacheInvalidBaseVol", "flashCacheFdeEnablementDisallowed", "remoteArvmFeatureDeactivated", "remoteArvmFeatureDisabled", "arvmOrphanGroup", "arvmOrphanMember", "volumeNotAvailable", "volumeHasUnreadableSectors", "thinProvisioningFeatureDisabled", "pitGroupsFeatureDisabled", "exceedDiskPoolLimit", "flashcacheDegradedState", "flashcacheNonDaCapableDriveDisallowed", "arvmMaxAsyncMirrorGroupsExceeded", "arvmMaxMirrorsPerArrayExceeded", "maxTotalMirrorsPerArrayExceeded", "exceedDiskPoolCapacity", "exceedMaxVolumeCapacity", "arvmRemoteMaxAsyncMirrorGroupsExceeded", "arvmRemoteMaxMirrorsPerArrayExceeded", "remoteMaxTotalMirrorsPerArrayExceeded", "arvmInvalidSyncInterval", "remoteNoHeap", "remoteInternalError", "remoteRvmSpmError", "arvmRemoteMirrorMemberDoesNotExist", "arvmRemoteGroupUserLabelExists", "arvmRemoteGroupNotSecondary", "arvmRemoteGroupDoesNotExist", "remoteInvalidProtection", "remoteDatabaseError", "arvmRemoteGroupNotEmpty", "arvmRemoteSuspendFailure", "arvmRemoteResumeFailure", "arvmRemoteSynchronizeFailure", "flashcacheInvalidAnalyticsState", "arvmExpansionSynchronizationInProgress", "arvmRemoteExpansionSynchronizationInProgress", "faultConditionStillExists", "remoteTryAlternate", "arvmOnlyLocalAmgDeleted", "arvmRoleChangePending", "arvmRoleChangeInProgress", "arvmMemberStopped", "reconstructionInProgress", "copybackInProgress", "adminPasswordNotSet", "keyDoesNotExist", "takeRecoveryActionsFirst", "coredumpBackupInProgress", "legacyRvmAsyncModeUnsupported", "arvmIncorrectVolumeType", "thinVolumeParametersCannotBeModified", "arvmRemoteThinNotSupported", "snmpInvalidCommunityName", "snmpInvalidCommunityPermission", "snmpInvalidCommunityRef", "snmpInvalidTrapDestinationRef", "invalidIpAddress", "snmpMaxCommunitiesExceeded", "snmpMaxTrapDestinationsExceeded", "snmpCommunityNameInUse", "snmpTrapDestinationAddressInUse", "snmpUnknownSystemVariable", "snmpInvalidSystemVariableValue", "snmpIncompatibleFirmware", "snmpAgentDisabled", "snmpAgentInitFailed", "arvmThinVolInitError", "arvmRemoteThinVolInitError", "snmpIncompatibleIpv4Address", "snmpIncompatibleIpv6Address", "drivesNotAvailableForRemoval", "snmpCannotDisableIpv4", "snmpCannotDisableIpv6", "snmpIpv4ConfigError", "iocDumpInProgress", "iocRestoreInProgress", "iocDumpInvalidTag", "unsupportedEsmRequest", "isnsDhcpNotSupported", "dpcVolumeGroupNotRedundant", "dpcVolumeNotInitialized", "dpcExclusiveOperationActive", "dpcUnableToPowerUpDrive", "dpcFormatActive", "dpcUnreadableSectorsPresent", "dpcPowerCycleAlreadyInProgress", "dpcEnclosureHardwareUnsupported", "dpcEnclosureFwDownlevel", "evacInProgress", "noEvacFound", "noHotspareAvailable", "driveServiceInProgress", "hdd4kbSegmentsizeNotAllowed", "diskPoolNoSpareDrives", "diskPoolExceedSpareCapacity", "autoLoadBalanceUserDisabled", "autoLoadBalanceInsufficientStatistics", "invalidLoadBalanceAction", "invalidLoadBalanceDelay", "reservedAddress", "volumeCreationInProgress", "keyValueTagInvalidRef", "keyValueTagInvalidDuplicate", "keyValueTagInUse", "workloadInvalidRef", "invalidKeyValueTagObjectReference", "mappingInvalidDuplicate", "downloadCompleteNoReboot", "downloadCompleteMswOnlyReboot", "workloadInvalidDuplicate", "mappingInvalidRef", "workloadInUse", "embeddedExternalKeyManagementEnabled", "embeddedExternalKeyManagementCertificatesNotInstalled", "illegalOperationOnAllConfigDrives", "databaseResyncInProgress", "embeddedEkmsKeyserverInfoMissing", "embeddedEkmsClientKeyMissing", "embeddedEkmsClientCertMissing", "embeddedEkmsClientCertMismatch", "embeddedEkmsCertExpired", "embeddedEkmsProxyNotResponding", "embeddedEkmsAuthenticationFailure", "embeddedEkmsKeyOwnerRequired", "embeddedEkmsServerError", "embeddedEkmsServerCertMissing", "embeddedEkmsCertDuplicate", "embeddedEkmsCertInvalid", "embeddedEkmsConnectionFailure", "invalidPasswordLength", "__UNDEFINED"]
        if return_code not in allowed_values:
            raise ValueError(
                "Invalid value for `return_code`, must be one of {0}"
                .format(allowed_values)
            )
        self._return_code = return_code

    @property
    def drive_temp_data(self):
        """
        Gets the drive_temp_data of this DriveTemperatureReturned.
        An array of drive temperature data. This field is only valid if returnCode is equal to RETCODE_OK.

        :return: The drive_temp_data of this DriveTemperatureReturned.
        :rtype: list[DriveTemperatureData]
        :required/optional: optional
        """
        return self._drive_temp_data

    @drive_temp_data.setter
    def drive_temp_data(self, drive_temp_data):
        """
        Sets the drive_temp_data of this DriveTemperatureReturned.
        An array of drive temperature data. This field is only valid if returnCode is equal to RETCODE_OK.

        :param drive_temp_data: The drive_temp_data of this DriveTemperatureReturned.
        :type: list[DriveTemperatureData]
        """
        self._drive_temp_data = drive_temp_data

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

