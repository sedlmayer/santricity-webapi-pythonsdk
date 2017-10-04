# coding: utf-8

"""
Cluster.py

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


class Cluster(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        Cluster - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'cluster_ref': 'str',  # (required parameter)
            'label': 'str',  # (required parameter)
            'is_sa_controlled': 'bool',  # (required parameter)
            'confirm_lun_mapping_creation': 'bool',  # (required parameter)
            'protection_information_capable_access_method': 'bool',  # (required parameter)
            'is_lun0_restricted': 'bool',  # (required parameter)
            'name': 'str',  
            'id': 'str'
        }

        self.attribute_map = {
            'cluster_ref': 'clusterRef',  # (required parameter)
            'label': 'label',  # (required parameter)
            'is_sa_controlled': 'isSAControlled',  # (required parameter)
            'confirm_lun_mapping_creation': 'confirmLUNMappingCreation',  # (required parameter)
            'protection_information_capable_access_method': 'protectionInformationCapableAccessMethod',  # (required parameter)
            'is_lun0_restricted': 'isLun0Restricted',  # (required parameter)
            'name': 'name',  
            'id': 'id'
        }

        self._cluster_ref = None
        self._label = None
        self._is_sa_controlled = None
        self._confirm_lun_mapping_creation = None
        self._protection_information_capable_access_method = None
        self._is_lun0_restricted = None
        self._name = None
        self._id = None

    @property
    def cluster_ref(self):
        """
        Gets the cluster_ref of this Cluster.
        The unique identification value for this object. Other objects may use this reference value to refer to the cluster.

        :return: The cluster_ref of this Cluster.
        :rtype: str
        :required/optional: required
        """
        return self._cluster_ref

    @cluster_ref.setter
    def cluster_ref(self, cluster_ref):
        """
        Sets the cluster_ref of this Cluster.
        The unique identification value for this object. Other objects may use this reference value to refer to the cluster.

        :param cluster_ref: The cluster_ref of this Cluster.
        :type: str
        """
        self._cluster_ref = cluster_ref

    @property
    def label(self):
        """
        Gets the label of this Cluster.
        The user-assigned, descriptive label string for the cluster.

        :return: The label of this Cluster.
        :rtype: str
        :required/optional: required
        """
        return self._label

    @label.setter
    def label(self, label):
        """
        Sets the label of this Cluster.
        The user-assigned, descriptive label string for the cluster.

        :param label: The label of this Cluster.
        :type: str
        """
        self._label = label

    @property
    def is_sa_controlled(self):
        """
        Gets the is_sa_controlled of this Cluster.
        If true, indicates that I/O accesses from this cluster are subject to the storage array's default LUN-to-volume mappings. If false, indicates that I/O accesses from the cluster are subject to cluster-specific LUN-to-volume mappings.

        :return: The is_sa_controlled of this Cluster.
        :rtype: bool
        :required/optional: required
        """
        return self._is_sa_controlled

    @is_sa_controlled.setter
    def is_sa_controlled(self, is_sa_controlled):
        """
        Sets the is_sa_controlled of this Cluster.
        If true, indicates that I/O accesses from this cluster are subject to the storage array's default LUN-to-volume mappings. If false, indicates that I/O accesses from the cluster are subject to cluster-specific LUN-to-volume mappings.

        :param is_sa_controlled: The is_sa_controlled of this Cluster.
        :type: bool
        """
        self._is_sa_controlled = is_sa_controlled

    @property
    def confirm_lun_mapping_creation(self):
        """
        Gets the confirm_lun_mapping_creation of this Cluster.
        If true, indicates that creation of LUN-to-volume mappings should require careful confirmation from the end-user, since such a mapping will alter the volume access rights of other clusters, in addition to this one.

        :return: The confirm_lun_mapping_creation of this Cluster.
        :rtype: bool
        :required/optional: required
        """
        return self._confirm_lun_mapping_creation

    @confirm_lun_mapping_creation.setter
    def confirm_lun_mapping_creation(self, confirm_lun_mapping_creation):
        """
        Sets the confirm_lun_mapping_creation of this Cluster.
        If true, indicates that creation of LUN-to-volume mappings should require careful confirmation from the end-user, since such a mapping will alter the volume access rights of other clusters, in addition to this one.

        :param confirm_lun_mapping_creation: The confirm_lun_mapping_creation of this Cluster.
        :type: bool
        """
        self._confirm_lun_mapping_creation = confirm_lun_mapping_creation

    @property
    def protection_information_capable_access_method(self):
        """
        Gets the protection_information_capable_access_method of this Cluster.
        This field is true if the host has a PI capable access method.

        :return: The protection_information_capable_access_method of this Cluster.
        :rtype: bool
        :required/optional: required
        """
        return self._protection_information_capable_access_method

    @protection_information_capable_access_method.setter
    def protection_information_capable_access_method(self, protection_information_capable_access_method):
        """
        Sets the protection_information_capable_access_method of this Cluster.
        This field is true if the host has a PI capable access method.

        :param protection_information_capable_access_method: The protection_information_capable_access_method of this Cluster.
        :type: bool
        """
        self._protection_information_capable_access_method = protection_information_capable_access_method

    @property
    def is_lun0_restricted(self):
        """
        Gets the is_lun0_restricted of this Cluster.
        Provides an indication as to whether LUN 0 is restricted (i.e., disallowed) for the associated cluster.

        :return: The is_lun0_restricted of this Cluster.
        :rtype: bool
        :required/optional: required
        """
        return self._is_lun0_restricted

    @is_lun0_restricted.setter
    def is_lun0_restricted(self, is_lun0_restricted):
        """
        Sets the is_lun0_restricted of this Cluster.
        Provides an indication as to whether LUN 0 is restricted (i.e., disallowed) for the associated cluster.

        :param is_lun0_restricted: The is_lun0_restricted of this Cluster.
        :type: bool
        """
        self._is_lun0_restricted = is_lun0_restricted

    @property
    def name(self):
        """
        Gets the name of this Cluster.


        :return: The name of this Cluster.
        :rtype: str
        :required/optional: optional
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this Cluster.


        :param name: The name of this Cluster.
        :type: str
        """
        self._name = name

    @property
    def id(self):
        """
        Gets the id of this Cluster.


        :return: The id of this Cluster.
        :rtype: str
        :required/optional: optional
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Cluster.


        :param id: The id of this Cluster.
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

