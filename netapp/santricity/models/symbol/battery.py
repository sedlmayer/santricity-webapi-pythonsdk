# coding: utf-8

"""
Battery.py

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


class Battery(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        Battery - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'battery_ref': 'str',  # (required parameter)
            'status': 'str',  # (required parameter)
            'physical_location': 'Location',  # (required parameter)
            'battery_age': 'int',  # (required parameter)
            'battery_life_remaining': 'int',  # (required parameter)
            'battery_type_data': 'BatteryTypeData',  # (required parameter)
            'reserved1': 'str',  
            'reserved2': 'str',  
            'manufacturer_date': 'int',  # (required parameter)
            'vendor_name': 'str',  # (required parameter)
            'vendor_pn': 'str',  # (required parameter)
            'vendor_sn': 'str',  # (required parameter)
            'fru_type': 'str',  # (required parameter)
            'rtr_attributes': 'RTRAttributes',  # (required parameter)
            'repair_policy': 'RepairPolicy',  # (required parameter)
            'battery_can_expire': 'bool',  # (required parameter)
            'automatic_age_reset': 'bool',  # (required parameter)
            'learn_cycle_data': 'SmartBatteryData',  # (required parameter)
            'id': 'str'
        }

        self.attribute_map = {
            'battery_ref': 'batteryRef',  # (required parameter)
            'status': 'status',  # (required parameter)
            'physical_location': 'physicalLocation',  # (required parameter)
            'battery_age': 'batteryAge',  # (required parameter)
            'battery_life_remaining': 'batteryLifeRemaining',  # (required parameter)
            'battery_type_data': 'batteryTypeData',  # (required parameter)
            'reserved1': 'reserved1',  
            'reserved2': 'reserved2',  
            'manufacturer_date': 'manufacturerDate',  # (required parameter)
            'vendor_name': 'vendorName',  # (required parameter)
            'vendor_pn': 'vendorPN',  # (required parameter)
            'vendor_sn': 'vendorSN',  # (required parameter)
            'fru_type': 'fruType',  # (required parameter)
            'rtr_attributes': 'rtrAttributes',  # (required parameter)
            'repair_policy': 'repairPolicy',  # (required parameter)
            'battery_can_expire': 'batteryCanExpire',  # (required parameter)
            'automatic_age_reset': 'automaticAgeReset',  # (required parameter)
            'learn_cycle_data': 'learnCycleData',  # (required parameter)
            'id': 'id'
        }

        self._battery_ref = None
        self._status = None
        self._physical_location = None
        self._battery_age = None
        self._battery_life_remaining = None
        self._battery_type_data = None
        self._reserved1 = None
        self._reserved2 = None
        self._manufacturer_date = None
        self._vendor_name = None
        self._vendor_pn = None
        self._vendor_sn = None
        self._fru_type = None
        self._rtr_attributes = None
        self._repair_policy = None
        self._battery_can_expire = None
        self._automatic_age_reset = None
        self._learn_cycle_data = None
        self._id = None

    @property
    def battery_ref(self):
        """
        Gets the battery_ref of this Battery.
        The reference for this battery.

        :return: The battery_ref of this Battery.
        :rtype: str
        :required/optional: required
        """
        return self._battery_ref

    @battery_ref.setter
    def battery_ref(self, battery_ref):
        """
        Sets the battery_ref of this Battery.
        The reference for this battery.

        :param battery_ref: The battery_ref of this Battery.
        :type: str
        """
        self._battery_ref = battery_ref

    @property
    def status(self):
        """
        Gets the status of this Battery.
        The operational status of the battery.

        :return: The status of this Battery.
        :rtype: str
        :required/optional: required
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this Battery.
        The operational status of the battery.

        :param status: The status of this Battery.
        :type: str
        """
        allowed_values = ["optimal", "fullCharging", "nearExpiration", "failed", "removed", "unknown", "notInConfig", "configMismatch", "learning", "overtemp", "expired", "maintenanceCharging", "replacementRequired", "__UNDEFINED"]
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status`, must be one of {0}"
                .format(allowed_values)
            )
        self._status = status

    @property
    def physical_location(self):
        """
        Gets the physical_location of this Battery.
        The physical location of the battery. The parent reference in Location identifies the CRU that physically houses the battery, and the position field is the parent-relative/like-component relative slot number of the battery, starting at one.

        :return: The physical_location of this Battery.
        :rtype: Location
        :required/optional: required
        """
        return self._physical_location

    @physical_location.setter
    def physical_location(self, physical_location):
        """
        Sets the physical_location of this Battery.
        The physical location of the battery. The parent reference in Location identifies the CRU that physically houses the battery, and the position field is the parent-relative/like-component relative slot number of the battery, starting at one.

        :param physical_location: The physical_location of this Battery.
        :type: Location
        """
        self._physical_location = physical_location

    @property
    def battery_age(self):
        """
        Gets the battery_age of this Battery.
        Current battery age, in days.

        :return: The battery_age of this Battery.
        :rtype: int
        :required/optional: required
        """
        return self._battery_age

    @battery_age.setter
    def battery_age(self, battery_age):
        """
        Sets the battery_age of this Battery.
        Current battery age, in days.

        :param battery_age: The battery_age of this Battery.
        :type: int
        """
        self._battery_age = battery_age

    @property
    def battery_life_remaining(self):
        """
        Gets the battery_life_remaining of this Battery.
        Days of battery life remaining. A value of -1 indicates that the battery life expiration age has been set to 0xFF in NVSRAM, disabling cache battery expiration event notification.

        :return: The battery_life_remaining of this Battery.
        :rtype: int
        :required/optional: required
        """
        return self._battery_life_remaining

    @battery_life_remaining.setter
    def battery_life_remaining(self, battery_life_remaining):
        """
        Sets the battery_life_remaining of this Battery.
        Days of battery life remaining. A value of -1 indicates that the battery life expiration age has been set to 0xFF in NVSRAM, disabling cache battery expiration event notification.

        :param battery_life_remaining: The battery_life_remaining of this Battery.
        :type: int
        """
        self._battery_life_remaining = battery_life_remaining

    @property
    def battery_type_data(self):
        """
        Gets the battery_type_data of this Battery.
        Used to determine the scope of the battery.

        :return: The battery_type_data of this Battery.
        :rtype: BatteryTypeData
        :required/optional: required
        """
        return self._battery_type_data

    @battery_type_data.setter
    def battery_type_data(self, battery_type_data):
        """
        Sets the battery_type_data of this Battery.
        Used to determine the scope of the battery.

        :param battery_type_data: The battery_type_data of this Battery.
        :type: BatteryTypeData
        """
        self._battery_type_data = battery_type_data

    @property
    def reserved1(self):
        """
        Gets the reserved1 of this Battery.


        :return: The reserved1 of this Battery.
        :rtype: str
        :required/optional: optional
        """
        return self._reserved1

    @reserved1.setter
    def reserved1(self, reserved1):
        """
        Sets the reserved1 of this Battery.


        :param reserved1: The reserved1 of this Battery.
        :type: str
        """
        self._reserved1 = reserved1

    @property
    def reserved2(self):
        """
        Gets the reserved2 of this Battery.


        :return: The reserved2 of this Battery.
        :rtype: str
        :required/optional: optional
        """
        return self._reserved2

    @reserved2.setter
    def reserved2(self, reserved2):
        """
        Sets the reserved2 of this Battery.


        :param reserved2: The reserved2 of this Battery.
        :type: str
        """
        self._reserved2 = reserved2

    @property
    def manufacturer_date(self):
        """
        Gets the manufacturer_date of this Battery.
        VPD manufacture date.

        :return: The manufacturer_date of this Battery.
        :rtype: int
        :required/optional: required
        """
        return self._manufacturer_date

    @manufacturer_date.setter
    def manufacturer_date(self, manufacturer_date):
        """
        Sets the manufacturer_date of this Battery.
        VPD manufacture date.

        :param manufacturer_date: The manufacturer_date of this Battery.
        :type: int
        """
        self._manufacturer_date = manufacturer_date

    @property
    def vendor_name(self):
        """
        Gets the vendor_name of this Battery.
        VPD vendor name.

        :return: The vendor_name of this Battery.
        :rtype: str
        :required/optional: required
        """
        return self._vendor_name

    @vendor_name.setter
    def vendor_name(self, vendor_name):
        """
        Sets the vendor_name of this Battery.
        VPD vendor name.

        :param vendor_name: The vendor_name of this Battery.
        :type: str
        """
        self._vendor_name = vendor_name

    @property
    def vendor_pn(self):
        """
        Gets the vendor_pn of this Battery.
        VPD part number.

        :return: The vendor_pn of this Battery.
        :rtype: str
        :required/optional: required
        """
        return self._vendor_pn

    @vendor_pn.setter
    def vendor_pn(self, vendor_pn):
        """
        Sets the vendor_pn of this Battery.
        VPD part number.

        :param vendor_pn: The vendor_pn of this Battery.
        :type: str
        """
        self._vendor_pn = vendor_pn

    @property
    def vendor_sn(self):
        """
        Gets the vendor_sn of this Battery.
        VPD serial number.

        :return: The vendor_sn of this Battery.
        :rtype: str
        :required/optional: required
        """
        return self._vendor_sn

    @vendor_sn.setter
    def vendor_sn(self, vendor_sn):
        """
        Sets the vendor_sn of this Battery.
        VPD serial number.

        :param vendor_sn: The vendor_sn of this Battery.
        :type: str
        """
        self._vendor_sn = vendor_sn

    @property
    def fru_type(self):
        """
        Gets the fru_type of this Battery.
        VPD field replaceable unit type.

        :return: The fru_type of this Battery.
        :rtype: str
        :required/optional: required
        """
        return self._fru_type

    @fru_type.setter
    def fru_type(self, fru_type):
        """
        Sets the fru_type of this Battery.
        VPD field replaceable unit type.

        :param fru_type: The fru_type of this Battery.
        :type: str
        """
        self._fru_type = fru_type

    @property
    def rtr_attributes(self):
        """
        Gets the rtr_attributes of this Battery.
        The CRU type of the battery plus its ready-to-remove attributes, which are based on the CRU type.

        :return: The rtr_attributes of this Battery.
        :rtype: RTRAttributes
        :required/optional: required
        """
        return self._rtr_attributes

    @rtr_attributes.setter
    def rtr_attributes(self, rtr_attributes):
        """
        Sets the rtr_attributes of this Battery.
        The CRU type of the battery plus its ready-to-remove attributes, which are based on the CRU type.

        :param rtr_attributes: The rtr_attributes of this Battery.
        :type: RTRAttributes
        """
        self._rtr_attributes = rtr_attributes

    @property
    def repair_policy(self):
        """
        Gets the repair_policy of this Battery.
        The repair policy for the battery component.

        :return: The repair_policy of this Battery.
        :rtype: RepairPolicy
        :required/optional: required
        """
        return self._repair_policy

    @repair_policy.setter
    def repair_policy(self, repair_policy):
        """
        Sets the repair_policy of this Battery.
        The repair policy for the battery component.

        :param repair_policy: The repair_policy of this Battery.
        :type: RepairPolicy
        """
        self._repair_policy = repair_policy

    @property
    def battery_can_expire(self):
        """
        Gets the battery_can_expire of this Battery.
        This boolean field is set to true when cache battery expired event notification is enabled.

        :return: The battery_can_expire of this Battery.
        :rtype: bool
        :required/optional: required
        """
        return self._battery_can_expire

    @battery_can_expire.setter
    def battery_can_expire(self, battery_can_expire):
        """
        Sets the battery_can_expire of this Battery.
        This boolean field is set to true when cache battery expired event notification is enabled.

        :param battery_can_expire: The battery_can_expire of this Battery.
        :type: bool
        """
        self._battery_can_expire = battery_can_expire

    @property
    def automatic_age_reset(self):
        """
        Gets the automatic_age_reset of this Battery.
        This boolean field is set to true when the batteryCanExpire field in this structure is set to false and when the controller tracks the battery serial number.

        :return: The automatic_age_reset of this Battery.
        :rtype: bool
        :required/optional: required
        """
        return self._automatic_age_reset

    @automatic_age_reset.setter
    def automatic_age_reset(self, automatic_age_reset):
        """
        Sets the automatic_age_reset of this Battery.
        This boolean field is set to true when the batteryCanExpire field in this structure is set to false and when the controller tracks the battery serial number.

        :param automatic_age_reset: The automatic_age_reset of this Battery.
        :type: bool
        """
        self._automatic_age_reset = automatic_age_reset

    @property
    def learn_cycle_data(self):
        """
        Gets the learn_cycle_data of this Battery.
        Contains details about the learn cycle for this battery

        :return: The learn_cycle_data of this Battery.
        :rtype: SmartBatteryData
        :required/optional: required
        """
        return self._learn_cycle_data

    @learn_cycle_data.setter
    def learn_cycle_data(self, learn_cycle_data):
        """
        Sets the learn_cycle_data of this Battery.
        Contains details about the learn cycle for this battery

        :param learn_cycle_data: The learn_cycle_data of this Battery.
        :type: SmartBatteryData
        """
        self._learn_cycle_data = learn_cycle_data

    @property
    def id(self):
        """
        Gets the id of this Battery.


        :return: The id of this Battery.
        :rtype: str
        :required/optional: optional
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Battery.


        :param id: The id of this Battery.
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

