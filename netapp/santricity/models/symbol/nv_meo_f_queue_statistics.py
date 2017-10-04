# coding: utf-8

"""
NVMeoFQueueStatistics.py

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


class NVMeoFQueueStatistics(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        NVMeoFQueueStatistics - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'successful_connect_requests': 'int',  # (required parameter)
            'connection_failures': 'int',  # (required parameter)
            'disconnects': 'int',  # (required parameter)
            'commands_good_status': 'int',  # (required parameter)
            'commands_error_status': 'int'
        }

        self.attribute_map = {
            'successful_connect_requests': 'successfulConnectRequests',  # (required parameter)
            'connection_failures': 'connectionFailures',  # (required parameter)
            'disconnects': 'disconnects',  # (required parameter)
            'commands_good_status': 'commandsGoodStatus',  # (required parameter)
            'commands_error_status': 'commandsErrorStatus'
        }

        self._successful_connect_requests = None
        self._connection_failures = None
        self._disconnects = None
        self._commands_good_status = None
        self._commands_error_status = None

    @property
    def successful_connect_requests(self):
        """
        Gets the successful_connect_requests of this NVMeoFQueueStatistics.
        The number of successful NVMeof Connect requests.

        :return: The successful_connect_requests of this NVMeoFQueueStatistics.
        :rtype: int
        :required/optional: required
        """
        return self._successful_connect_requests

    @successful_connect_requests.setter
    def successful_connect_requests(self, successful_connect_requests):
        """
        Sets the successful_connect_requests of this NVMeoFQueueStatistics.
        The number of successful NVMeof Connect requests.

        :param successful_connect_requests: The successful_connect_requests of this NVMeoFQueueStatistics.
        :type: int
        """
        self._successful_connect_requests = successful_connect_requests

    @property
    def connection_failures(self):
        """
        Gets the connection_failures of this NVMeoFQueueStatistics.
        The number of NVMeof connection failures.

        :return: The connection_failures of this NVMeoFQueueStatistics.
        :rtype: int
        :required/optional: required
        """
        return self._connection_failures

    @connection_failures.setter
    def connection_failures(self, connection_failures):
        """
        Sets the connection_failures of this NVMeoFQueueStatistics.
        The number of NVMeof connection failures.

        :param connection_failures: The connection_failures of this NVMeoFQueueStatistics.
        :type: int
        """
        self._connection_failures = connection_failures

    @property
    def disconnects(self):
        """
        Gets the disconnects of this NVMeoFQueueStatistics.
        The number of NVMeof disconnects.

        :return: The disconnects of this NVMeoFQueueStatistics.
        :rtype: int
        :required/optional: required
        """
        return self._disconnects

    @disconnects.setter
    def disconnects(self, disconnects):
        """
        Sets the disconnects of this NVMeoFQueueStatistics.
        The number of NVMeof disconnects.

        :param disconnects: The disconnects of this NVMeoFQueueStatistics.
        :type: int
        """
        self._disconnects = disconnects

    @property
    def commands_good_status(self):
        """
        Gets the commands_good_status of this NVMeoFQueueStatistics.
        The number of NVMeof commands that returned good status.

        :return: The commands_good_status of this NVMeoFQueueStatistics.
        :rtype: int
        :required/optional: required
        """
        return self._commands_good_status

    @commands_good_status.setter
    def commands_good_status(self, commands_good_status):
        """
        Sets the commands_good_status of this NVMeoFQueueStatistics.
        The number of NVMeof commands that returned good status.

        :param commands_good_status: The commands_good_status of this NVMeoFQueueStatistics.
        :type: int
        """
        self._commands_good_status = commands_good_status

    @property
    def commands_error_status(self):
        """
        Gets the commands_error_status of this NVMeoFQueueStatistics.
        The number of NVMeof commands that returned error status.

        :return: The commands_error_status of this NVMeoFQueueStatistics.
        :rtype: int
        :required/optional: required
        """
        return self._commands_error_status

    @commands_error_status.setter
    def commands_error_status(self, commands_error_status):
        """
        Sets the commands_error_status of this NVMeoFQueueStatistics.
        The number of NVMeof commands that returned error status.

        :param commands_error_status: The commands_error_status of this NVMeoFQueueStatistics.
        :type: int
        """
        self._commands_error_status = commands_error_status

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

