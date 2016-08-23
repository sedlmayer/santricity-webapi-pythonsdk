# coding: utf-8

"""
Dom0SupportDataStartDetails.py

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


class Dom0SupportDataStartDetails(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        Dom0SupportDataStartDetails - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'support_data_type': 'str',  # (required parameter)
            'dom0_support_data_journal_start_details': 'Dom0SupportDataJournalStartDetails'
        }

        self.attribute_map = {
            'support_data_type': 'supportDataType',  # (required parameter)
            'dom0_support_data_journal_start_details': 'dom0SupportDataJournalStartDetails'
        }

        self._support_data_type = None
        self._dom0_support_data_journal_start_details = None

    @property
    def support_data_type(self):
        """
        Gets the support_data_type of this Dom0SupportDataStartDetails.
        Enumerates the types of support data that can be retrieved from Dom0

        :return: The support_data_type of this Dom0SupportDataStartDetails.
        :rtype: str
        :required/optional: required
        """
        return self._support_data_type

    @support_data_type.setter
    def support_data_type(self, support_data_type):
        """
        Sets the support_data_type of this Dom0SupportDataStartDetails.
        Enumerates the types of support data that can be retrieved from Dom0

        :param support_data_type: The support_data_type of this Dom0SupportDataStartDetails.
        :type: str
        """
        allowed_values = ["unknownType", "journalLogs", "miscLogs", "dailyDiagnostics", "weeklyDiagnostics", "dataCoreFiles", "__UNDEFINED"]
        if support_data_type not in allowed_values:
            raise ValueError(
                "Invalid value for `support_data_type`, must be one of {0}"
                .format(allowed_values)
            )
        self._support_data_type = support_data_type

    @property
    def dom0_support_data_journal_start_details(self):
        """
        Gets the dom0_support_data_journal_start_details of this Dom0SupportDataStartDetails.
        This is only valid when the Dom0 support data type is DOM0_SUPPORT_DATA_JOURNAL_LOGS

        :return: The dom0_support_data_journal_start_details of this Dom0SupportDataStartDetails.
        :rtype: Dom0SupportDataJournalStartDetails
        :required/optional: optional
        """
        return self._dom0_support_data_journal_start_details

    @dom0_support_data_journal_start_details.setter
    def dom0_support_data_journal_start_details(self, dom0_support_data_journal_start_details):
        """
        Sets the dom0_support_data_journal_start_details of this Dom0SupportDataStartDetails.
        This is only valid when the Dom0 support data type is DOM0_SUPPORT_DATA_JOURNAL_LOGS

        :param dom0_support_data_journal_start_details: The dom0_support_data_journal_start_details of this Dom0SupportDataStartDetails.
        :type: Dom0SupportDataJournalStartDetails
        """
        self._dom0_support_data_journal_start_details = dom0_support_data_journal_start_details

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
