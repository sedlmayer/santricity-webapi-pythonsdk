# coding: utf-8

"""
SocDeviceData.py

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


class SocDeviceData(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        SocDeviceData - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'parent': 'SocParent',  # (required parameter)
            'hub_mode': 'bool',  # (required parameter)
            'managed_mode': 'bool',  # (required parameter)
            'collection_elapsed_time': 'int'
        }

        self.attribute_map = {
            'parent': 'parent',  # (required parameter)
            'hub_mode': 'hubMode',  # (required parameter)
            'managed_mode': 'managedMode',  # (required parameter)
            'collection_elapsed_time': 'collectionElapsedTime'
        }

        self._parent = None
        self._hub_mode = None
        self._managed_mode = None
        self._collection_elapsed_time = None

    @property
    def parent(self):
        """
        Gets the parent of this SocDeviceData.
        The parent (either controller or ESM) of the SOC device.

        :return: The parent of this SocDeviceData.
        :rtype: SocParent
        :required/optional: required
        """
        return self._parent

    @parent.setter
    def parent(self, parent):
        """
        Sets the parent of this SocDeviceData.
        The parent (either controller or ESM) of the SOC device.

        :param parent: The parent of this SocDeviceData.
        :type: SocParent
        """
        self._parent = parent

    @property
    def hub_mode(self):
        """
        Gets the hub_mode of this SocDeviceData.
        Set to true if the SOC device is operating in hub mode. Otherwise it is operating in switch mode.

        :return: The hub_mode of this SocDeviceData.
        :rtype: bool
        :required/optional: required
        """
        return self._hub_mode

    @hub_mode.setter
    def hub_mode(self, hub_mode):
        """
        Sets the hub_mode of this SocDeviceData.
        Set to true if the SOC device is operating in hub mode. Otherwise it is operating in switch mode.

        :param hub_mode: The hub_mode of this SocDeviceData.
        :type: bool
        """
        self._hub_mode = hub_mode

    @property
    def managed_mode(self):
        """
        Gets the managed_mode of this SocDeviceData.
        Set to true if the SOC device is operating in managed mode. Otherwise it is operating in unmanaged mode.

        :return: The managed_mode of this SocDeviceData.
        :rtype: bool
        :required/optional: required
        """
        return self._managed_mode

    @managed_mode.setter
    def managed_mode(self, managed_mode):
        """
        Sets the managed_mode of this SocDeviceData.
        Set to true if the SOC device is operating in managed mode. Otherwise it is operating in unmanaged mode.

        :param managed_mode: The managed_mode of this SocDeviceData.
        :type: bool
        """
        self._managed_mode = managed_mode

    @property
    def collection_elapsed_time(self):
        """
        Gets the collection_elapsed_time of this SocDeviceData.
        The length of the time interval, in seconds, during which the reported SOC statistics were collected.

        :return: The collection_elapsed_time of this SocDeviceData.
        :rtype: int
        :required/optional: required
        """
        return self._collection_elapsed_time

    @collection_elapsed_time.setter
    def collection_elapsed_time(self, collection_elapsed_time):
        """
        Sets the collection_elapsed_time of this SocDeviceData.
        The length of the time interval, in seconds, during which the reported SOC statistics were collected.

        :param collection_elapsed_time: The collection_elapsed_time of this SocDeviceData.
        :type: int
        """
        self._collection_elapsed_time = collection_elapsed_time

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
