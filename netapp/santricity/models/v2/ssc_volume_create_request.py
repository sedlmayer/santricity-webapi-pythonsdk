# coding: utf-8

"""
SscVolumeCreateRequest.py

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


class SscVolumeCreateRequest(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        SscVolumeCreateRequest - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'pool_id': 'str',  # (required parameter)
            'name': 'str',  # (required parameter)
            'size_unit': 'str',  
            'size': 'int',  # (required parameter)
            'read_cache_enable': 'bool',  
            'write_cache_enable': 'bool',  
            'flash_cache_enable': 'bool',  
            'data_assurance_enable': 'bool',  
            'thin_provision': 'bool',  
            'meta_tags': 'list[VolumeMetadataItem]'
        }

        self.attribute_map = {
            'pool_id': 'poolId',  # (required parameter)
            'name': 'name',  # (required parameter)
            'size_unit': 'sizeUnit',  
            'size': 'size',  # (required parameter)
            'read_cache_enable': 'readCacheEnable',  
            'write_cache_enable': 'writeCacheEnable',  
            'flash_cache_enable': 'flashCacheEnable',  
            'data_assurance_enable': 'dataAssuranceEnable',  
            'thin_provision': 'thinProvision',  
            'meta_tags': 'metaTags'
        }

        self._pool_id = None
        self._name = None
        self._size_unit = None
        self._size = None
        self._read_cache_enable = None
        self._write_cache_enable = None
        self._flash_cache_enable = None
        self._data_assurance_enable = None
        self._thin_provision = None
        self._meta_tags = None

    @property
    def pool_id(self):
        """
        Gets the pool_id of this SscVolumeCreateRequest.
        The id of the storage pool to create the volume on

        :return: The pool_id of this SscVolumeCreateRequest.
        :rtype: str
        :required/optional: required
        """
        return self._pool_id

    @pool_id.setter
    def pool_id(self, pool_id):
        """
        Sets the pool_id of this SscVolumeCreateRequest.
        The id of the storage pool to create the volume on

        :param pool_id: The pool_id of this SscVolumeCreateRequest.
        :type: str
        """
        self._pool_id = pool_id

    @property
    def name(self):
        """
        Gets the name of this SscVolumeCreateRequest.
        The name of the volume

        :return: The name of this SscVolumeCreateRequest.
        :rtype: str
        :required/optional: required
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this SscVolumeCreateRequest.
        The name of the volume

        :param name: The name of this SscVolumeCreateRequest.
        :type: str
        """
        self._name = name

    @property
    def size_unit(self):
        """
        Gets the size_unit of this SscVolumeCreateRequest.
        The unit for the request capacity

        :return: The size_unit of this SscVolumeCreateRequest.
        :rtype: str
        :required/optional: optional
        """
        return self._size_unit

    @size_unit.setter
    def size_unit(self, size_unit):
        """
        Sets the size_unit of this SscVolumeCreateRequest.
        The unit for the request capacity

        :param size_unit: The size_unit of this SscVolumeCreateRequest.
        :type: str
        """
        allowed_values = ["bytes", "b", "kb", "mb", "gb", "tb", "pb", "eb", "zb", "yb", None]
        if size_unit not in allowed_values:
            raise ValueError(
                "Invalid value for `size_unit`, must be one of {0}"
                .format(allowed_values)
            )
        self._size_unit = size_unit

    @property
    def size(self):
        """
        Gets the size of this SscVolumeCreateRequest.
        The requested capacity of the volume in units

        :return: The size of this SscVolumeCreateRequest.
        :rtype: int
        :required/optional: required
        """
        return self._size

    @size.setter
    def size(self, size):
        """
        Sets the size of this SscVolumeCreateRequest.
        The requested capacity of the volume in units

        :param size: The size of this SscVolumeCreateRequest.
        :type: int
        """
        self._size = size

    @property
    def read_cache_enable(self):
        """
        Gets the read_cache_enable of this SscVolumeCreateRequest.


        :return: The read_cache_enable of this SscVolumeCreateRequest.
        :rtype: bool
        :required/optional: optional
        """
        return self._read_cache_enable

    @read_cache_enable.setter
    def read_cache_enable(self, read_cache_enable):
        """
        Sets the read_cache_enable of this SscVolumeCreateRequest.


        :param read_cache_enable: The read_cache_enable of this SscVolumeCreateRequest.
        :type: bool
        """
        self._read_cache_enable = read_cache_enable

    @property
    def write_cache_enable(self):
        """
        Gets the write_cache_enable of this SscVolumeCreateRequest.


        :return: The write_cache_enable of this SscVolumeCreateRequest.
        :rtype: bool
        :required/optional: optional
        """
        return self._write_cache_enable

    @write_cache_enable.setter
    def write_cache_enable(self, write_cache_enable):
        """
        Sets the write_cache_enable of this SscVolumeCreateRequest.


        :param write_cache_enable: The write_cache_enable of this SscVolumeCreateRequest.
        :type: bool
        """
        self._write_cache_enable = write_cache_enable

    @property
    def flash_cache_enable(self):
        """
        Gets the flash_cache_enable of this SscVolumeCreateRequest.
        Add this volume to a flashCache

        :return: The flash_cache_enable of this SscVolumeCreateRequest.
        :rtype: bool
        :required/optional: optional
        """
        return self._flash_cache_enable

    @flash_cache_enable.setter
    def flash_cache_enable(self, flash_cache_enable):
        """
        Sets the flash_cache_enable of this SscVolumeCreateRequest.
        Add this volume to a flashCache

        :param flash_cache_enable: The flash_cache_enable of this SscVolumeCreateRequest.
        :type: bool
        """
        self._flash_cache_enable = flash_cache_enable

    @property
    def data_assurance_enable(self):
        """
        Gets the data_assurance_enable of this SscVolumeCreateRequest.
        Enable the dataAssurance capability

        :return: The data_assurance_enable of this SscVolumeCreateRequest.
        :rtype: bool
        :required/optional: optional
        """
        return self._data_assurance_enable

    @data_assurance_enable.setter
    def data_assurance_enable(self, data_assurance_enable):
        """
        Sets the data_assurance_enable of this SscVolumeCreateRequest.
        Enable the dataAssurance capability

        :param data_assurance_enable: The data_assurance_enable of this SscVolumeCreateRequest.
        :type: bool
        """
        self._data_assurance_enable = data_assurance_enable

    @property
    def thin_provision(self):
        """
        Gets the thin_provision of this SscVolumeCreateRequest.
        Define a thinProvisioned volume

        :return: The thin_provision of this SscVolumeCreateRequest.
        :rtype: bool
        :required/optional: optional
        """
        return self._thin_provision

    @thin_provision.setter
    def thin_provision(self, thin_provision):
        """
        Sets the thin_provision of this SscVolumeCreateRequest.
        Define a thinProvisioned volume

        :param thin_provision: The thin_provision of this SscVolumeCreateRequest.
        :type: bool
        """
        self._thin_provision = thin_provision

    @property
    def meta_tags(self):
        """
        Gets the meta_tags of this SscVolumeCreateRequest.
        Optional list of MetaData tags to assign to the volume.

        :return: The meta_tags of this SscVolumeCreateRequest.
        :rtype: list[VolumeMetadataItem]
        :required/optional: optional
        """
        return self._meta_tags

    @meta_tags.setter
    def meta_tags(self, meta_tags):
        """
        Sets the meta_tags of this SscVolumeCreateRequest.
        Optional list of MetaData tags to assign to the volume.

        :param meta_tags: The meta_tags of this SscVolumeCreateRequest.
        :type: list[VolumeMetadataItem]
        """
        self._meta_tags = meta_tags

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

