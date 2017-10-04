# coding: utf-8

"""
MelEntry.py

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


class MelEntry(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        MelEntry - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'sequence_number': 'int',  # (required parameter)
            'event_type': 'int',  # (required parameter)
            'time_stamp': 'int',  # (required parameter)
            'category': 'str',  # (required parameter)
            'component_type': 'str',  # (required parameter)
            'component_location': 'ComponentLocation',  # (required parameter)
            'location_valid': 'bool',  # (required parameter)
            'priority': 'str',  # (required parameter)
            'event_source_controller': 'int',  # (required parameter)
            'sense_key': 'int',  # (required parameter)
            'raw_data': 'str',  # (required parameter)
            'ext_component_location': 'ExtendedComponentLocation',  # (required parameter)
            'control_params': 'EventControl',  # (required parameter)
            'asc': 'int',  
            'ascq': 'int'
        }

        self.attribute_map = {
            'sequence_number': 'sequenceNumber',  # (required parameter)
            'event_type': 'eventType',  # (required parameter)
            'time_stamp': 'timeStamp',  # (required parameter)
            'category': 'category',  # (required parameter)
            'component_type': 'componentType',  # (required parameter)
            'component_location': 'componentLocation',  # (required parameter)
            'location_valid': 'locationValid',  # (required parameter)
            'priority': 'priority',  # (required parameter)
            'event_source_controller': 'eventSourceController',  # (required parameter)
            'sense_key': 'senseKey',  # (required parameter)
            'raw_data': 'rawData',  # (required parameter)
            'ext_component_location': 'extComponentLocation',  # (required parameter)
            'control_params': 'controlParams',  # (required parameter)
            'asc': 'asc',  
            'ascq': 'ascq'
        }

        self._sequence_number = None
        self._event_type = None
        self._time_stamp = None
        self._category = None
        self._component_type = None
        self._component_location = None
        self._location_valid = None
        self._priority = None
        self._event_source_controller = None
        self._sense_key = None
        self._raw_data = None
        self._ext_component_location = None
        self._control_params = None
        self._asc = None
        self._ascq = None

    @property
    def sequence_number(self):
        """
        Gets the sequence_number of this MelEntry.
        The sequence number of the MEL entry. The controller maintains a unique, monotonically increasing 64-bit sequence number value and stamps each MEL entry with the next value of this counter.

        :return: The sequence_number of this MelEntry.
        :rtype: int
        :required/optional: required
        """
        return self._sequence_number

    @sequence_number.setter
    def sequence_number(self, sequence_number):
        """
        Sets the sequence_number of this MelEntry.
        The sequence number of the MEL entry. The controller maintains a unique, monotonically increasing 64-bit sequence number value and stamps each MEL entry with the next value of this counter.

        :param sequence_number: The sequence_number of this MelEntry.
        :type: int
        """
        self._sequence_number = sequence_number

    @property
    def event_type(self):
        """
        Gets the event_type of this MelEntry.
        An integer value that indicates the specific type of event being reported.

        :return: The event_type of this MelEntry.
        :rtype: int
        :required/optional: required
        """
        return self._event_type

    @event_type.setter
    def event_type(self, event_type):
        """
        Sets the event_type of this MelEntry.
        An integer value that indicates the specific type of event being reported.

        :param event_type: The event_type of this MelEntry.
        :type: int
        """
        self._event_type = event_type

    @property
    def time_stamp(self):
        """
        Gets the time_stamp of this MelEntry.
        The time at which the MEL entry was generated. This value is defined in terms of the number of seconds since midnight GMT on January 1, 1970.

        :return: The time_stamp of this MelEntry.
        :rtype: int
        :required/optional: required
        """
        return self._time_stamp

    @time_stamp.setter
    def time_stamp(self, time_stamp):
        """
        Sets the time_stamp of this MelEntry.
        The time at which the MEL entry was generated. This value is defined in terms of the number of seconds since midnight GMT on January 1, 1970.

        :param time_stamp: The time_stamp of this MelEntry.
        :type: int
        """
        self._time_stamp = time_stamp

    @property
    def category(self):
        """
        Gets the category of this MelEntry.
        The category into which this event falls. This value identifies the general type of activity or event that occurred and caused the entry to be generated.

        :return: The category of this MelEntry.
        :rtype: str
        :required/optional: required
        """
        return self._category

    @category.setter
    def category(self, category):
        """
        Sets the category of this MelEntry.
        The category into which this event falls. This value identifies the general type of activity or event that occurred and caused the entry to be generated.

        :param category: The category of this MelEntry.
        :type: str
        """
        allowed_values = ["error", "failure", "command", "notification", "stateChange", "hostEntry", "general", "__UNDEFINED"]
        if category not in allowed_values:
            raise ValueError(
                "Invalid value for `category`, must be one of {0}"
                .format(allowed_values)
            )
        self._category = category

    @property
    def component_type(self):
        """
        Gets the component_type of this MelEntry.
        The type of component that is associated with this entry.

        :return: The component_type of this MelEntry.
        :rtype: str
        :required/optional: required
        """
        return self._component_type

    @component_type.setter
    def component_type(self, component_type):
        """
        Sets the component_type of this MelEntry.
        The type of component that is associated with this entry.

        :param component_type: The component_type of this MelEntry.
        :type: str
        """
        allowed_values = ["unknown", "drive", "powerSply", "fan", "minihub", "tempSensor", "channel", "esm", "controller", "battery", "enclosure", "ups", "chip", "volume", "volumeGrp", "portCru", "interconnectCru", "supportCru", "alarm", "channelPort", "sfpPort", "hostBoard", "newFormat", "ctlrSfp", "ctlrSoc", "initiator", "target", "isnsServer", "hostIoCard", "cacheBackupDevice", "cacheMemDimm", "host", "hostPort", "drawer", "relative", "schedule", "asyncMirrorGroup", "diskPool", "pit", "pitConsistencyGroup", "cgpit", "cgview", "flashCache", "snmpCommunity", "snmpTrapDestination", "fcTarget", "blankOne", "blankTwo", "fanOnlyCru", "psuCru", "nvmeInitiator", "__UNDEFINED"]
        if component_type not in allowed_values:
            raise ValueError(
                "Invalid value for `component_type`, must be one of {0}"
                .format(allowed_values)
            )
        self._component_type = component_type

    @property
    def component_location(self):
        """
        Gets the component_location of this MelEntry.
        The location, or other identifying value, of the component associated with this entry.

        :return: The component_location of this MelEntry.
        :rtype: ComponentLocation
        :required/optional: required
        """
        return self._component_location

    @component_location.setter
    def component_location(self, component_location):
        """
        Sets the component_location of this MelEntry.
        The location, or other identifying value, of the component associated with this entry.

        :param component_location: The component_location of this MelEntry.
        :type: ComponentLocation
        """
        self._component_location = component_location

    @property
    def location_valid(self):
        """
        Gets the location_valid of this MelEntry.
        A true/false indication of whether the ComponentLocation field is valid for this entry.

        :return: The location_valid of this MelEntry.
        :rtype: bool
        :required/optional: required
        """
        return self._location_valid

    @location_valid.setter
    def location_valid(self, location_valid):
        """
        Sets the location_valid of this MelEntry.
        A true/false indication of whether the ComponentLocation field is valid for this entry.

        :param location_valid: The location_valid of this MelEntry.
        :type: bool
        """
        self._location_valid = location_valid

    @property
    def priority(self):
        """
        Gets the priority of this MelEntry.
        The priority code associated with this event.

        :return: The priority of this MelEntry.
        :rtype: str
        :required/optional: required
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        """
        Sets the priority of this MelEntry.
        The priority code associated with this event.

        :param priority: The priority of this MelEntry.
        :type: str
        """
        allowed_values = ["priorityDefault", "priorityCritical", "priorityInfo", "priorityEmergency", "priorityAlert", "priorityError", "priorityWarning", "priorityNotice", "priorityDebug", "__UNDEFINED"]
        if priority not in allowed_values:
            raise ValueError(
                "Invalid value for `priority`, must be one of {0}"
                .format(allowed_values)
            )
        self._priority = priority

    @property
    def event_source_controller(self):
        """
        Gets the event_source_controller of this MelEntry.
        The controller that is the source of the event (Controller 1 or 2).

        :return: The event_source_controller of this MelEntry.
        :rtype: int
        :required/optional: required
        """
        return self._event_source_controller

    @event_source_controller.setter
    def event_source_controller(self, event_source_controller):
        """
        Sets the event_source_controller of this MelEntry.
        The controller that is the source of the event (Controller 1 or 2).

        :param event_source_controller: The event_source_controller of this MelEntry.
        :type: int
        """
        self._event_source_controller = event_source_controller

    @property
    def sense_key(self):
        """
        Gets the sense_key of this MelEntry.
        The Sense Key value associated with this event, or zero if no key is applicable.

        :return: The sense_key of this MelEntry.
        :rtype: int
        :required/optional: required
        """
        return self._sense_key

    @sense_key.setter
    def sense_key(self, sense_key):
        """
        Sets the sense_key of this MelEntry.
        The Sense Key value associated with this event, or zero if no key is applicable.

        :param sense_key: The sense_key of this MelEntry.
        :type: int
        """
        self._sense_key = sense_key

    @property
    def raw_data(self):
        """
        Gets the raw_data of this MelEntry.
        The raw data stored for this event. This information may be useful for debugging or troubleshooting problems with the assistance of a field support or development representative.

        :return: The raw_data of this MelEntry.
        :rtype: str
        :required/optional: required
        """
        return self._raw_data

    @raw_data.setter
    def raw_data(self, raw_data):
        """
        Sets the raw_data of this MelEntry.
        The raw data stored for this event. This information may be useful for debugging or troubleshooting problems with the assistance of a field support or development representative.

        :param raw_data: The raw_data of this MelEntry.
        :type: str
        """
        self._raw_data = raw_data

    @property
    def ext_component_location(self):
        """
        Gets the ext_component_location of this MelEntry.
        Extended component location information for this entry. This data type of this field is a union with discriminator extLocType. If the discriminator is set to something other than EXT_COMP_LOCTYPE_UNKNOWN, then the location information in this field overrides what is in the componentLocation field.

        :return: The ext_component_location of this MelEntry.
        :rtype: ExtendedComponentLocation
        :required/optional: required
        """
        return self._ext_component_location

    @ext_component_location.setter
    def ext_component_location(self, ext_component_location):
        """
        Sets the ext_component_location of this MelEntry.
        Extended component location information for this entry. This data type of this field is a union with discriminator extLocType. If the discriminator is set to something other than EXT_COMP_LOCTYPE_UNKNOWN, then the location information in this field overrides what is in the componentLocation field.

        :param ext_component_location: The ext_component_location of this MelEntry.
        :type: ExtendedComponentLocation
        """
        self._ext_component_location = ext_component_location

    @property
    def control_params(self):
        """
        Gets the control_params of this MelEntry.
        This field allows customized control over the handling of MEL events.

        :return: The control_params of this MelEntry.
        :rtype: EventControl
        :required/optional: required
        """
        return self._control_params

    @control_params.setter
    def control_params(self, control_params):
        """
        Sets the control_params of this MelEntry.
        This field allows customized control over the handling of MEL events.

        :param control_params: The control_params of this MelEntry.
        :type: EventControl
        """
        self._control_params = control_params

    @property
    def asc(self):
        """
        Gets the asc of this MelEntry.


        :return: The asc of this MelEntry.
        :rtype: int
        :required/optional: optional
        """
        return self._asc

    @asc.setter
    def asc(self, asc):
        """
        Sets the asc of this MelEntry.


        :param asc: The asc of this MelEntry.
        :type: int
        """
        self._asc = asc

    @property
    def ascq(self):
        """
        Gets the ascq of this MelEntry.


        :return: The ascq of this MelEntry.
        :rtype: int
        :required/optional: optional
        """
        return self._ascq

    @ascq.setter
    def ascq(self, ascq):
        """
        Sets the ascq of this MelEntry.


        :param ascq: The ascq of this MelEntry.
        :type: int
        """
        self._ascq = ascq

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

