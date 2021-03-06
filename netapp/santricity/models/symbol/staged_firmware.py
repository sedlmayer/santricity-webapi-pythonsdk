# coding: utf-8

"""
StagedFirmware.py

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


class StagedFirmware(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        StagedFirmware - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'staged_fw_valid': 'bool',  # (required parameter)
            'fw_version': 'str',  # (required parameter)
            'app_version': 'str',  # (required parameter)
            'boot_version': 'str',  # (required parameter)
            'nvsram_version': 'str',  # (required parameter)
            'time_stamp': 'int',  # (required parameter)
            'nvsram_version_string': 'str',  # (required parameter)
            'code_versions': 'list[VersionDescriptor]'
        }

        self.attribute_map = {
            'staged_fw_valid': 'stagedFwValid',  # (required parameter)
            'fw_version': 'fwVersion',  # (required parameter)
            'app_version': 'appVersion',  # (required parameter)
            'boot_version': 'bootVersion',  # (required parameter)
            'nvsram_version': 'nvsramVersion',  # (required parameter)
            'time_stamp': 'timeStamp',  # (required parameter)
            'nvsram_version_string': 'nvsramVersionString',  # (required parameter)
            'code_versions': 'codeVersions'
        }

        self._staged_fw_valid = None
        self._fw_version = None
        self._app_version = None
        self._boot_version = None
        self._nvsram_version = None
        self._time_stamp = None
        self._nvsram_version_string = None
        self._code_versions = None

    @property
    def staged_fw_valid(self):
        """
        Gets the staged_fw_valid of this StagedFirmware.
        False, staged FW areas on the controllers are not valid and cannot be activated. True, the staged FW areas on the controllers are valid and can be activated.

        :return: The staged_fw_valid of this StagedFirmware.
        :rtype: bool
        :required/optional: required
        """
        return self._staged_fw_valid

    @staged_fw_valid.setter
    def staged_fw_valid(self, staged_fw_valid):
        """
        Sets the staged_fw_valid of this StagedFirmware.
        False, staged FW areas on the controllers are not valid and cannot be activated. True, the staged FW areas on the controllers are valid and can be activated.

        :param staged_fw_valid: The staged_fw_valid of this StagedFirmware.
        :type: bool
        """
        self._staged_fw_valid = staged_fw_valid

    @property
    def fw_version(self):
        """
        Gets the fw_version of this StagedFirmware.
        The firmware package version identifier.

        :return: The fw_version of this StagedFirmware.
        :rtype: str
        :required/optional: required
        """
        return self._fw_version

    @fw_version.setter
    def fw_version(self, fw_version):
        """
        Sets the fw_version of this StagedFirmware.
        The firmware package version identifier.

        :param fw_version: The fw_version of this StagedFirmware.
        :type: str
        """
        self._fw_version = fw_version

    @property
    def app_version(self):
        """
        Gets the app_version of this StagedFirmware.
        The application code version number.

        :return: The app_version of this StagedFirmware.
        :rtype: str
        :required/optional: required
        """
        return self._app_version

    @app_version.setter
    def app_version(self, app_version):
        """
        Sets the app_version of this StagedFirmware.
        The application code version number.

        :param app_version: The app_version of this StagedFirmware.
        :type: str
        """
        self._app_version = app_version

    @property
    def boot_version(self):
        """
        Gets the boot_version of this StagedFirmware.
        The boot code version number.

        :return: The boot_version of this StagedFirmware.
        :rtype: str
        :required/optional: required
        """
        return self._boot_version

    @boot_version.setter
    def boot_version(self, boot_version):
        """
        Sets the boot_version of this StagedFirmware.
        The boot code version number.

        :param boot_version: The boot_version of this StagedFirmware.
        :type: str
        """
        self._boot_version = boot_version

    @property
    def nvsram_version(self):
        """
        Gets the nvsram_version of this StagedFirmware.
        The NVSRAM version number.

        :return: The nvsram_version of this StagedFirmware.
        :rtype: str
        :required/optional: required
        """
        return self._nvsram_version

    @nvsram_version.setter
    def nvsram_version(self, nvsram_version):
        """
        Sets the nvsram_version of this StagedFirmware.
        The NVSRAM version number.

        :param nvsram_version: The nvsram_version of this StagedFirmware.
        :type: str
        """
        self._nvsram_version = nvsram_version

    @property
    def time_stamp(self):
        """
        Gets the time_stamp of this StagedFirmware.
        Timestamp when the staged FW was downloaded

        :return: The time_stamp of this StagedFirmware.
        :rtype: int
        :required/optional: required
        """
        return self._time_stamp

    @time_stamp.setter
    def time_stamp(self, time_stamp):
        """
        Sets the time_stamp of this StagedFirmware.
        Timestamp when the staged FW was downloaded

        :param time_stamp: The time_stamp of this StagedFirmware.
        :type: int
        """
        self._time_stamp = time_stamp

    @property
    def nvsram_version_string(self):
        """
        Gets the nvsram_version_string of this StagedFirmware.
        The field is deprecated. The nvsramVersion field should be used instead.

        :return: The nvsram_version_string of this StagedFirmware.
        :rtype: str
        :required/optional: required
        """
        return self._nvsram_version_string

    @nvsram_version_string.setter
    def nvsram_version_string(self, nvsram_version_string):
        """
        Sets the nvsram_version_string of this StagedFirmware.
        The field is deprecated. The nvsramVersion field should be used instead.

        :param nvsram_version_string: The nvsram_version_string of this StagedFirmware.
        :type: str
        """
        self._nvsram_version_string = nvsram_version_string

    @property
    def code_versions(self):
        """
        Gets the code_versions of this StagedFirmware.
        Version descriptors for staged code modules

        :return: The code_versions of this StagedFirmware.
        :rtype: list[VersionDescriptor]
        :required/optional: required
        """
        return self._code_versions

    @code_versions.setter
    def code_versions(self, code_versions):
        """
        Sets the code_versions of this StagedFirmware.
        Version descriptors for staged code modules

        :param code_versions: The code_versions of this StagedFirmware.
        :type: list[VersionDescriptor]
        """
        self._code_versions = code_versions

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

