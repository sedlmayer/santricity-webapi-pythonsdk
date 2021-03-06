# coding: utf-8

"""
PSUFirmwareUpdateDescriptor.py

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


class PSUFirmwareUpdateDescriptor(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        PSUFirmwareUpdateDescriptor - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'force_update': 'bool',  # (required parameter)
            'power_supply_ref': 'list[str]',  # (required parameter)
            'firmware_update_descriptor': 'FirmwareUpdateDescriptor'
        }

        self.attribute_map = {
            'force_update': 'forceUpdate',  # (required parameter)
            'power_supply_ref': 'powerSupplyRef',  # (required parameter)
            'firmware_update_descriptor': 'firmwareUpdateDescriptor'
        }

        self._force_update = None
        self._power_supply_ref = None
        self._firmware_update_descriptor = None

    @property
    def force_update(self):
        """
        Gets the force_update of this PSUFirmwareUpdateDescriptor.
        Force an update of power supplies with the same FW revision as the updated FW or non-optimal power supplies.

        :return: The force_update of this PSUFirmwareUpdateDescriptor.
        :rtype: bool
        :required/optional: required
        """
        return self._force_update

    @force_update.setter
    def force_update(self, force_update):
        """
        Sets the force_update of this PSUFirmwareUpdateDescriptor.
        Force an update of power supplies with the same FW revision as the updated FW or non-optimal power supplies.

        :param force_update: The force_update of this PSUFirmwareUpdateDescriptor.
        :type: bool
        """
        self._force_update = force_update

    @property
    def power_supply_ref(self):
        """
        Gets the power_supply_ref of this PSUFirmwareUpdateDescriptor.
        A list of references to power supply objects.

        :return: The power_supply_ref of this PSUFirmwareUpdateDescriptor.
        :rtype: list[str]
        :required/optional: required
        """
        return self._power_supply_ref

    @power_supply_ref.setter
    def power_supply_ref(self, power_supply_ref):
        """
        Sets the power_supply_ref of this PSUFirmwareUpdateDescriptor.
        A list of references to power supply objects.

        :param power_supply_ref: The power_supply_ref of this PSUFirmwareUpdateDescriptor.
        :type: list[str]
        """
        self._power_supply_ref = power_supply_ref

    @property
    def firmware_update_descriptor(self):
        """
        Gets the firmware_update_descriptor of this PSUFirmwareUpdateDescriptor.
        The firmware update descriptor containing the firmware image and related information.

        :return: The firmware_update_descriptor of this PSUFirmwareUpdateDescriptor.
        :rtype: FirmwareUpdateDescriptor
        :required/optional: required
        """
        return self._firmware_update_descriptor

    @firmware_update_descriptor.setter
    def firmware_update_descriptor(self, firmware_update_descriptor):
        """
        Sets the firmware_update_descriptor of this PSUFirmwareUpdateDescriptor.
        The firmware update descriptor containing the firmware image and related information.

        :param firmware_update_descriptor: The firmware_update_descriptor of this PSUFirmwareUpdateDescriptor.
        :type: FirmwareUpdateDescriptor
        """
        self._firmware_update_descriptor = firmware_update_descriptor

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

