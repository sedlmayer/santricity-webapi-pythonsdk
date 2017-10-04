# coding: utf-8

"""
ThinVolumeCacheSettings.py

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


class ThinVolumeCacheSettings(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        ThinVolumeCacheSettings - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'read_cache_enable': 'bool',  
            'write_cache_enable': 'bool',  
            'cache_flush_modifier': 'str'
        }

        self.attribute_map = {
            'read_cache_enable': 'readCacheEnable',  
            'write_cache_enable': 'writeCacheEnable',  
            'cache_flush_modifier': 'cacheFlushModifier'
        }

        self._read_cache_enable = None
        self._write_cache_enable = None
        self._cache_flush_modifier = None

    @property
    def read_cache_enable(self):
        """
        Gets the read_cache_enable of this ThinVolumeCacheSettings.
        Indicates whether read caching should be enabled for the volume.

        :return: The read_cache_enable of this ThinVolumeCacheSettings.
        :rtype: bool
        :required/optional: optional
        """
        return self._read_cache_enable

    @read_cache_enable.setter
    def read_cache_enable(self, read_cache_enable):
        """
        Sets the read_cache_enable of this ThinVolumeCacheSettings.
        Indicates whether read caching should be enabled for the volume.

        :param read_cache_enable: The read_cache_enable of this ThinVolumeCacheSettings.
        :type: bool
        """
        self._read_cache_enable = read_cache_enable

    @property
    def write_cache_enable(self):
        """
        Gets the write_cache_enable of this ThinVolumeCacheSettings.
        Indicates whether write-back caching should be enabled for the volume.

        :return: The write_cache_enable of this ThinVolumeCacheSettings.
        :rtype: bool
        :required/optional: optional
        """
        return self._write_cache_enable

    @write_cache_enable.setter
    def write_cache_enable(self, write_cache_enable):
        """
        Sets the write_cache_enable of this ThinVolumeCacheSettings.
        Indicates whether write-back caching should be enabled for the volume.

        :param write_cache_enable: The write_cache_enable of this ThinVolumeCacheSettings.
        :type: bool
        """
        self._write_cache_enable = write_cache_enable

    @property
    def cache_flush_modifier(self):
        """
        Gets the cache_flush_modifier of this ThinVolumeCacheSettings.
        The cache flush modifier value, which is used to specify the maximum amount of time that dirty data for this volume may be retained in the controller's write cache prior to being flushed to disk.

        :return: The cache_flush_modifier of this ThinVolumeCacheSettings.
        :rtype: str
        :required/optional: optional
        """
        return self._cache_flush_modifier

    @cache_flush_modifier.setter
    def cache_flush_modifier(self, cache_flush_modifier):
        """
        Sets the cache_flush_modifier of this ThinVolumeCacheSettings.
        The cache flush modifier value, which is used to specify the maximum amount of time that dirty data for this volume may be retained in the controller's write cache prior to being flushed to disk.

        :param cache_flush_modifier: The cache_flush_modifier of this ThinVolumeCacheSettings.
        :type: str
        """
        allowed_values = ["flushImmediate", "flush250Msec", "flush500Msec", "flush750Msec", "flush1Sec", "flush1500Msec", "flush2Sec", "flush5Sec", "flush10Sec", "flush20Sec", "flush60Sec", "flush120Sec", "flush300Sec", "flush1200Sec", "flush3600Sec", "flushInfinite", "__UNDEFINED", None]
        if cache_flush_modifier not in allowed_values:
            raise ValueError(
                "Invalid value for `cache_flush_modifier`, must be one of {0}"
                .format(allowed_values)
            )
        self._cache_flush_modifier = cache_flush_modifier

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

