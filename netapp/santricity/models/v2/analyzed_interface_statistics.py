# coding: utf-8

"""
AnalyzedInterfaceStatistics.py

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


class AnalyzedInterfaceStatistics(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        AnalyzedInterfaceStatistics - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'observed_time': 'datetime',  # (required parameter)
            'observed_time_in_ms': 'int',  # (required parameter)
            'read_i_ops': 'float',  # (required parameter)
            'write_i_ops': 'float',  # (required parameter)
            'other_i_ops': 'float',  # (required parameter)
            'combined_i_ops': 'float',  # (required parameter)
            'read_throughput': 'float',  # (required parameter)
            'write_throughput': 'float',  # (required parameter)
            'combined_throughput': 'float',  # (required parameter)
            'read_response_time': 'float',  # (required parameter)
            'write_response_time': 'float',  # (required parameter)
            'combined_response_time': 'float',  # (required parameter)
            'average_read_op_size': 'float',  # (required parameter)
            'average_write_op_size': 'float',  # (required parameter)
            'read_ops': 'float',  # (required parameter)
            'write_ops': 'float',  # (required parameter)
            'interface_id': 'str',  # (required parameter)
            'channel_type': 'str',  # (required parameter)
            'queue_depth_total': 'float',  # (required parameter)
            'queue_depth_max': 'float'
        }

        self.attribute_map = {
            'observed_time': 'observedTime',  # (required parameter)
            'observed_time_in_ms': 'observedTimeInMS',  # (required parameter)
            'read_i_ops': 'readIOps',  # (required parameter)
            'write_i_ops': 'writeIOps',  # (required parameter)
            'other_i_ops': 'otherIOps',  # (required parameter)
            'combined_i_ops': 'combinedIOps',  # (required parameter)
            'read_throughput': 'readThroughput',  # (required parameter)
            'write_throughput': 'writeThroughput',  # (required parameter)
            'combined_throughput': 'combinedThroughput',  # (required parameter)
            'read_response_time': 'readResponseTime',  # (required parameter)
            'write_response_time': 'writeResponseTime',  # (required parameter)
            'combined_response_time': 'combinedResponseTime',  # (required parameter)
            'average_read_op_size': 'averageReadOpSize',  # (required parameter)
            'average_write_op_size': 'averageWriteOpSize',  # (required parameter)
            'read_ops': 'readOps',  # (required parameter)
            'write_ops': 'writeOps',  # (required parameter)
            'interface_id': 'interfaceId',  # (required parameter)
            'channel_type': 'channelType',  # (required parameter)
            'queue_depth_total': 'queueDepthTotal',  # (required parameter)
            'queue_depth_max': 'queueDepthMax'
        }

        self._observed_time = None
        self._observed_time_in_ms = None
        self._read_i_ops = None
        self._write_i_ops = None
        self._other_i_ops = None
        self._combined_i_ops = None
        self._read_throughput = None
        self._write_throughput = None
        self._combined_throughput = None
        self._read_response_time = None
        self._write_response_time = None
        self._combined_response_time = None
        self._average_read_op_size = None
        self._average_write_op_size = None
        self._read_ops = None
        self._write_ops = None
        self._interface_id = None
        self._channel_type = None
        self._queue_depth_total = None
        self._queue_depth_max = None

    @property
    def observed_time(self):
        """
        Gets the observed_time of this AnalyzedInterfaceStatistics.
        A timestamp representing when the data was collected

        :return: The observed_time of this AnalyzedInterfaceStatistics.
        :rtype: datetime
        :required/optional: required
        """
        return self._observed_time

    @observed_time.setter
    def observed_time(self, observed_time):
        """
        Sets the observed_time of this AnalyzedInterfaceStatistics.
        A timestamp representing when the data was collected

        :param observed_time: The observed_time of this AnalyzedInterfaceStatistics.
        :type: datetime
        """
        self._observed_time = observed_time

    @property
    def observed_time_in_ms(self):
        """
        Gets the observed_time_in_ms of this AnalyzedInterfaceStatistics.
        The time in which this data was polled and generated in milliseconds

        :return: The observed_time_in_ms of this AnalyzedInterfaceStatistics.
        :rtype: int
        :required/optional: required
        """
        return self._observed_time_in_ms

    @observed_time_in_ms.setter
    def observed_time_in_ms(self, observed_time_in_ms):
        """
        Sets the observed_time_in_ms of this AnalyzedInterfaceStatistics.
        The time in which this data was polled and generated in milliseconds

        :param observed_time_in_ms: The observed_time_in_ms of this AnalyzedInterfaceStatistics.
        :type: int
        """
        self._observed_time_in_ms = observed_time_in_ms

    @property
    def read_i_ops(self):
        """
        Gets the read_i_ops of this AnalyzedInterfaceStatistics.
        Read operations per second.

        :return: The read_i_ops of this AnalyzedInterfaceStatistics.
        :rtype: float
        :required/optional: required
        """
        return self._read_i_ops

    @read_i_ops.setter
    def read_i_ops(self, read_i_ops):
        """
        Sets the read_i_ops of this AnalyzedInterfaceStatistics.
        Read operations per second.

        :param read_i_ops: The read_i_ops of this AnalyzedInterfaceStatistics.
        :type: float
        """
        self._read_i_ops = read_i_ops

    @property
    def write_i_ops(self):
        """
        Gets the write_i_ops of this AnalyzedInterfaceStatistics.
        Write operations per second.

        :return: The write_i_ops of this AnalyzedInterfaceStatistics.
        :rtype: float
        :required/optional: required
        """
        return self._write_i_ops

    @write_i_ops.setter
    def write_i_ops(self, write_i_ops):
        """
        Sets the write_i_ops of this AnalyzedInterfaceStatistics.
        Write operations per second.

        :param write_i_ops: The write_i_ops of this AnalyzedInterfaceStatistics.
        :type: float
        """
        self._write_i_ops = write_i_ops

    @property
    def other_i_ops(self):
        """
        Gets the other_i_ops of this AnalyzedInterfaceStatistics.
        SCSI Operations to the disk that are not read/write operations. Example: Test Unit Ready.

        :return: The other_i_ops of this AnalyzedInterfaceStatistics.
        :rtype: float
        :required/optional: required
        """
        return self._other_i_ops

    @other_i_ops.setter
    def other_i_ops(self, other_i_ops):
        """
        Sets the other_i_ops of this AnalyzedInterfaceStatistics.
        SCSI Operations to the disk that are not read/write operations. Example: Test Unit Ready.

        :param other_i_ops: The other_i_ops of this AnalyzedInterfaceStatistics.
        :type: float
        """
        self._other_i_ops = other_i_ops

    @property
    def combined_i_ops(self):
        """
        Gets the combined_i_ops of this AnalyzedInterfaceStatistics.
        All operations per second.

        :return: The combined_i_ops of this AnalyzedInterfaceStatistics.
        :rtype: float
        :required/optional: required
        """
        return self._combined_i_ops

    @combined_i_ops.setter
    def combined_i_ops(self, combined_i_ops):
        """
        Sets the combined_i_ops of this AnalyzedInterfaceStatistics.
        All operations per second.

        :param combined_i_ops: The combined_i_ops of this AnalyzedInterfaceStatistics.
        :type: float
        """
        self._combined_i_ops = combined_i_ops

    @property
    def read_throughput(self):
        """
        Gets the read_throughput of this AnalyzedInterfaceStatistics.
        Read throughput in MB/s.

        :return: The read_throughput of this AnalyzedInterfaceStatistics.
        :rtype: float
        :required/optional: required
        """
        return self._read_throughput

    @read_throughput.setter
    def read_throughput(self, read_throughput):
        """
        Sets the read_throughput of this AnalyzedInterfaceStatistics.
        Read throughput in MB/s.

        :param read_throughput: The read_throughput of this AnalyzedInterfaceStatistics.
        :type: float
        """
        self._read_throughput = read_throughput

    @property
    def write_throughput(self):
        """
        Gets the write_throughput of this AnalyzedInterfaceStatistics.
        Write throughput in MB/s.

        :return: The write_throughput of this AnalyzedInterfaceStatistics.
        :rtype: float
        :required/optional: required
        """
        return self._write_throughput

    @write_throughput.setter
    def write_throughput(self, write_throughput):
        """
        Sets the write_throughput of this AnalyzedInterfaceStatistics.
        Write throughput in MB/s.

        :param write_throughput: The write_throughput of this AnalyzedInterfaceStatistics.
        :type: float
        """
        self._write_throughput = write_throughput

    @property
    def combined_throughput(self):
        """
        Gets the combined_throughput of this AnalyzedInterfaceStatistics.
        Combined read/write throughput in MB/s.

        :return: The combined_throughput of this AnalyzedInterfaceStatistics.
        :rtype: float
        :required/optional: required
        """
        return self._combined_throughput

    @combined_throughput.setter
    def combined_throughput(self, combined_throughput):
        """
        Sets the combined_throughput of this AnalyzedInterfaceStatistics.
        Combined read/write throughput in MB/s.

        :param combined_throughput: The combined_throughput of this AnalyzedInterfaceStatistics.
        :type: float
        """
        self._combined_throughput = combined_throughput

    @property
    def read_response_time(self):
        """
        Gets the read_response_time of this AnalyzedInterfaceStatistics.
        Read response time average in milliseconds.

        :return: The read_response_time of this AnalyzedInterfaceStatistics.
        :rtype: float
        :required/optional: required
        """
        return self._read_response_time

    @read_response_time.setter
    def read_response_time(self, read_response_time):
        """
        Sets the read_response_time of this AnalyzedInterfaceStatistics.
        Read response time average in milliseconds.

        :param read_response_time: The read_response_time of this AnalyzedInterfaceStatistics.
        :type: float
        """
        self._read_response_time = read_response_time

    @property
    def write_response_time(self):
        """
        Gets the write_response_time of this AnalyzedInterfaceStatistics.
        Write response time average in milliseconds.

        :return: The write_response_time of this AnalyzedInterfaceStatistics.
        :rtype: float
        :required/optional: required
        """
        return self._write_response_time

    @write_response_time.setter
    def write_response_time(self, write_response_time):
        """
        Sets the write_response_time of this AnalyzedInterfaceStatistics.
        Write response time average in milliseconds.

        :param write_response_time: The write_response_time of this AnalyzedInterfaceStatistics.
        :type: float
        """
        self._write_response_time = write_response_time

    @property
    def combined_response_time(self):
        """
        Gets the combined_response_time of this AnalyzedInterfaceStatistics.
        Combined average response time in milliseconds.

        :return: The combined_response_time of this AnalyzedInterfaceStatistics.
        :rtype: float
        :required/optional: required
        """
        return self._combined_response_time

    @combined_response_time.setter
    def combined_response_time(self, combined_response_time):
        """
        Sets the combined_response_time of this AnalyzedInterfaceStatistics.
        Combined average response time in milliseconds.

        :param combined_response_time: The combined_response_time of this AnalyzedInterfaceStatistics.
        :type: float
        """
        self._combined_response_time = combined_response_time

    @property
    def average_read_op_size(self):
        """
        Gets the average_read_op_size of this AnalyzedInterfaceStatistics.
        Average read operation size in bytes.

        :return: The average_read_op_size of this AnalyzedInterfaceStatistics.
        :rtype: float
        :required/optional: required
        """
        return self._average_read_op_size

    @average_read_op_size.setter
    def average_read_op_size(self, average_read_op_size):
        """
        Sets the average_read_op_size of this AnalyzedInterfaceStatistics.
        Average read operation size in bytes.

        :param average_read_op_size: The average_read_op_size of this AnalyzedInterfaceStatistics.
        :type: float
        """
        self._average_read_op_size = average_read_op_size

    @property
    def average_write_op_size(self):
        """
        Gets the average_write_op_size of this AnalyzedInterfaceStatistics.
        Average write operation size in bytes.

        :return: The average_write_op_size of this AnalyzedInterfaceStatistics.
        :rtype: float
        :required/optional: required
        """
        return self._average_write_op_size

    @average_write_op_size.setter
    def average_write_op_size(self, average_write_op_size):
        """
        Sets the average_write_op_size of this AnalyzedInterfaceStatistics.
        Average write operation size in bytes.

        :param average_write_op_size: The average_write_op_size of this AnalyzedInterfaceStatistics.
        :type: float
        """
        self._average_write_op_size = average_write_op_size

    @property
    def read_ops(self):
        """
        Gets the read_ops of this AnalyzedInterfaceStatistics.
        The amount of read operations in this analysed interval.

        :return: The read_ops of this AnalyzedInterfaceStatistics.
        :rtype: float
        :required/optional: required
        """
        return self._read_ops

    @read_ops.setter
    def read_ops(self, read_ops):
        """
        Sets the read_ops of this AnalyzedInterfaceStatistics.
        The amount of read operations in this analysed interval.

        :param read_ops: The read_ops of this AnalyzedInterfaceStatistics.
        :type: float
        """
        self._read_ops = read_ops

    @property
    def write_ops(self):
        """
        Gets the write_ops of this AnalyzedInterfaceStatistics.
        The amount of write operations in this analysed interval.

        :return: The write_ops of this AnalyzedInterfaceStatistics.
        :rtype: float
        :required/optional: required
        """
        return self._write_ops

    @write_ops.setter
    def write_ops(self, write_ops):
        """
        Sets the write_ops of this AnalyzedInterfaceStatistics.
        The amount of write operations in this analysed interval.

        :param write_ops: The write_ops of this AnalyzedInterfaceStatistics.
        :type: float
        """
        self._write_ops = write_ops

    @property
    def interface_id(self):
        """
        Gets the interface_id of this AnalyzedInterfaceStatistics.


        :return: The interface_id of this AnalyzedInterfaceStatistics.
        :rtype: str
        :required/optional: required
        """
        return self._interface_id

    @interface_id.setter
    def interface_id(self, interface_id):
        """
        Sets the interface_id of this AnalyzedInterfaceStatistics.


        :param interface_id: The interface_id of this AnalyzedInterfaceStatistics.
        :type: str
        """
        self._interface_id = interface_id

    @property
    def channel_type(self):
        """
        Gets the channel_type of this AnalyzedInterfaceStatistics.
        The channel type for the interface.

        :return: The channel_type of this AnalyzedInterfaceStatistics.
        :rtype: str
        :required/optional: required
        """
        return self._channel_type

    @channel_type.setter
    def channel_type(self, channel_type):
        """
        Sets the channel_type of this AnalyzedInterfaceStatistics.
        The channel type for the interface.

        :param channel_type: The channel_type of this AnalyzedInterfaceStatistics.
        :type: str
        """
        allowed_values = ["hostside", "driveside", "management", "__UNDEFINED"]
        if channel_type not in allowed_values:
            raise ValueError(
                "Invalid value for `channel_type`, must be one of {0}"
                .format(allowed_values)
            )
        self._channel_type = channel_type

    @property
    def queue_depth_total(self):
        """
        Gets the queue_depth_total of this AnalyzedInterfaceStatistics.
        Total channel queue depth.

        :return: The queue_depth_total of this AnalyzedInterfaceStatistics.
        :rtype: float
        :required/optional: required
        """
        return self._queue_depth_total

    @queue_depth_total.setter
    def queue_depth_total(self, queue_depth_total):
        """
        Sets the queue_depth_total of this AnalyzedInterfaceStatistics.
        Total channel queue depth.

        :param queue_depth_total: The queue_depth_total of this AnalyzedInterfaceStatistics.
        :type: float
        """
        self._queue_depth_total = queue_depth_total

    @property
    def queue_depth_max(self):
        """
        Gets the queue_depth_max of this AnalyzedInterfaceStatistics.
        Maximum channel queue depth.

        :return: The queue_depth_max of this AnalyzedInterfaceStatistics.
        :rtype: float
        :required/optional: required
        """
        return self._queue_depth_max

    @queue_depth_max.setter
    def queue_depth_max(self, queue_depth_max):
        """
        Sets the queue_depth_max of this AnalyzedInterfaceStatistics.
        Maximum channel queue depth.

        :param queue_depth_max: The queue_depth_max of this AnalyzedInterfaceStatistics.
        :type: float
        """
        self._queue_depth_max = queue_depth_max

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

