# coding: utf-8

"""
AsyncMirrorPrimarySyncStatisticsSample.py

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


class AsyncMirrorPrimarySyncStatisticsSample(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        AsyncMirrorPrimarySyncStatisticsSample - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'sync_type': 'str',  # (required parameter)
            'sync_start_timestamp': 'int',  # (required parameter)
            'completion_detail': 'AsyncMirrorSyncCompletionDetail',  # (required parameter)
            'owner': 'str',  # (required parameter)
            'sample_start_time_seconds': 'int',  # (required parameter)
            'sample_end_time_seconds': 'int',  # (required parameter)
            'member_state': 'str',  # (required parameter)
            'repository_utilization_warn_threshold': 'int',  # (required parameter)
            'repository_utilization_percentage': 'int',  # (required parameter)
            'sync_interval_minutes': 'int',  # (required parameter)
            'sync_duration_minutes': 'int',  # (required parameter)
            'sync_completion_time_alert_threshold_minutes': 'int',  # (required parameter)
            'recovery_point_age_alert_threshold_minutes': 'int',  # (required parameter)
            'recovery_point_age_minutes': 'int',  # (required parameter)
            'cumulative_bytes_sent': 'int',  # (required parameter)
            'cumulative_io_time': 'int',  # (required parameter)
            'total_io_count': 'int',  # (required parameter)
            'longest_response_time_micro_seconds': 'int',  # (required parameter)
            'longest_response_time_bytes': 'int',  # (required parameter)
            'shortest_response_time_micro_seconds': 'int',  # (required parameter)
            'shortest_response_time_bytes': 'int',  # (required parameter)
            'highest_throughput_in_bytes_per_second': 'int',  # (required parameter)
            'lowest_throughput_in_bytes_per_second': 'int'
        }

        self.attribute_map = {
            'sync_type': 'syncType',  # (required parameter)
            'sync_start_timestamp': 'syncStartTimestamp',  # (required parameter)
            'completion_detail': 'completionDetail',  # (required parameter)
            'owner': 'owner',  # (required parameter)
            'sample_start_time_seconds': 'sampleStartTimeSeconds',  # (required parameter)
            'sample_end_time_seconds': 'sampleEndTimeSeconds',  # (required parameter)
            'member_state': 'memberState',  # (required parameter)
            'repository_utilization_warn_threshold': 'repositoryUtilizationWarnThreshold',  # (required parameter)
            'repository_utilization_percentage': 'repositoryUtilizationPercentage',  # (required parameter)
            'sync_interval_minutes': 'syncIntervalMinutes',  # (required parameter)
            'sync_duration_minutes': 'syncDurationMinutes',  # (required parameter)
            'sync_completion_time_alert_threshold_minutes': 'syncCompletionTimeAlertThresholdMinutes',  # (required parameter)
            'recovery_point_age_alert_threshold_minutes': 'recoveryPointAgeAlertThresholdMinutes',  # (required parameter)
            'recovery_point_age_minutes': 'recoveryPointAgeMinutes',  # (required parameter)
            'cumulative_bytes_sent': 'cumulativeBytesSent',  # (required parameter)
            'cumulative_io_time': 'cumulativeIOTime',  # (required parameter)
            'total_io_count': 'totalIOCount',  # (required parameter)
            'longest_response_time_micro_seconds': 'longestResponseTimeMicroSeconds',  # (required parameter)
            'longest_response_time_bytes': 'longestResponseTimeBytes',  # (required parameter)
            'shortest_response_time_micro_seconds': 'shortestResponseTimeMicroSeconds',  # (required parameter)
            'shortest_response_time_bytes': 'shortestResponseTimeBytes',  # (required parameter)
            'highest_throughput_in_bytes_per_second': 'highestThroughputInBytesPerSecond',  # (required parameter)
            'lowest_throughput_in_bytes_per_second': 'lowestThroughputInBytesPerSecond'
        }

        self._sync_type = None
        self._sync_start_timestamp = None
        self._completion_detail = None
        self._owner = None
        self._sample_start_time_seconds = None
        self._sample_end_time_seconds = None
        self._member_state = None
        self._repository_utilization_warn_threshold = None
        self._repository_utilization_percentage = None
        self._sync_interval_minutes = None
        self._sync_duration_minutes = None
        self._sync_completion_time_alert_threshold_minutes = None
        self._recovery_point_age_alert_threshold_minutes = None
        self._recovery_point_age_minutes = None
        self._cumulative_bytes_sent = None
        self._cumulative_io_time = None
        self._total_io_count = None
        self._longest_response_time_micro_seconds = None
        self._longest_response_time_bytes = None
        self._shortest_response_time_micro_seconds = None
        self._shortest_response_time_bytes = None
        self._highest_throughput_in_bytes_per_second = None
        self._lowest_throughput_in_bytes_per_second = None

    @property
    def sync_type(self):
        """
        Gets the sync_type of this AsyncMirrorPrimarySyncStatisticsSample.
        The type of synchronization being performed during this sample period.

        :return: The sync_type of this AsyncMirrorPrimarySyncStatisticsSample.
        :rtype: str
        :required/optional: required
        """
        return self._sync_type

    @sync_type.setter
    def sync_type(self, sync_type):
        """
        Sets the sync_type of this AsyncMirrorPrimarySyncStatisticsSample.
        The type of synchronization being performed during this sample period.

        :param sync_type: The sync_type of this AsyncMirrorPrimarySyncStatisticsSample.
        :type: str
        """
        allowed_values = ["unknown", "periodic", "manual", "initialSync", "roleChange", "__UNDEFINED"]
        if sync_type not in allowed_values:
            raise ValueError(
                "Invalid value for `sync_type`, must be one of {0}"
                .format(allowed_values)
            )
        self._sync_type = sync_type

    @property
    def sync_start_timestamp(self):
        """
        Gets the sync_start_timestamp of this AsyncMirrorPrimarySyncStatisticsSample.
        The synchronization start timestamp represented in seconds since midnight GMT on January 1, 1970. This can be used to correlate statistics between the primary and secondary for the same interval (time recorded here is driven from the primary). This can also be used to correlate multiple samples for the same synchronization period.

        :return: The sync_start_timestamp of this AsyncMirrorPrimarySyncStatisticsSample.
        :rtype: int
        :required/optional: required
        """
        return self._sync_start_timestamp

    @sync_start_timestamp.setter
    def sync_start_timestamp(self, sync_start_timestamp):
        """
        Sets the sync_start_timestamp of this AsyncMirrorPrimarySyncStatisticsSample.
        The synchronization start timestamp represented in seconds since midnight GMT on January 1, 1970. This can be used to correlate statistics between the primary and secondary for the same interval (time recorded here is driven from the primary). This can also be used to correlate multiple samples for the same synchronization period.

        :param sync_start_timestamp: The sync_start_timestamp of this AsyncMirrorPrimarySyncStatisticsSample.
        :type: int
        """
        self._sync_start_timestamp = sync_start_timestamp

    @property
    def completion_detail(self):
        """
        Gets the completion_detail of this AsyncMirrorPrimarySyncStatisticsSample.
        Indication of whether synchronization failed or completed normally.

        :return: The completion_detail of this AsyncMirrorPrimarySyncStatisticsSample.
        :rtype: AsyncMirrorSyncCompletionDetail
        :required/optional: required
        """
        return self._completion_detail

    @completion_detail.setter
    def completion_detail(self, completion_detail):
        """
        Sets the completion_detail of this AsyncMirrorPrimarySyncStatisticsSample.
        Indication of whether synchronization failed or completed normally.

        :param completion_detail: The completion_detail of this AsyncMirrorPrimarySyncStatisticsSample.
        :type: AsyncMirrorSyncCompletionDetail
        """
        self._completion_detail = completion_detail

    @property
    def owner(self):
        """
        Gets the owner of this AsyncMirrorPrimarySyncStatisticsSample.
        Owning controller for the duration of this sample.

        :return: The owner of this AsyncMirrorPrimarySyncStatisticsSample.
        :rtype: str
        :required/optional: required
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        """
        Sets the owner of this AsyncMirrorPrimarySyncStatisticsSample.
        Owning controller for the duration of this sample.

        :param owner: The owner of this AsyncMirrorPrimarySyncStatisticsSample.
        :type: str
        """
        self._owner = owner

    @property
    def sample_start_time_seconds(self):
        """
        Gets the sample_start_time_seconds of this AsyncMirrorPrimarySyncStatisticsSample.
        When this sample started: > = synchronization start time. Time is expressed in seconds since midnight January 1, 1970 GMT.

        :return: The sample_start_time_seconds of this AsyncMirrorPrimarySyncStatisticsSample.
        :rtype: int
        :required/optional: required
        """
        return self._sample_start_time_seconds

    @sample_start_time_seconds.setter
    def sample_start_time_seconds(self, sample_start_time_seconds):
        """
        Sets the sample_start_time_seconds of this AsyncMirrorPrimarySyncStatisticsSample.
        When this sample started: > = synchronization start time. Time is expressed in seconds since midnight January 1, 1970 GMT.

        :param sample_start_time_seconds: The sample_start_time_seconds of this AsyncMirrorPrimarySyncStatisticsSample.
        :type: int
        """
        self._sample_start_time_seconds = sample_start_time_seconds

    @property
    def sample_end_time_seconds(self):
        """
        Gets the sample_end_time_seconds of this AsyncMirrorPrimarySyncStatisticsSample.
        When this sample ended: synchronization completion time, or time of last update before disruption. Time is expressed in seconds since midnight January 1, 1970 GMT.

        :return: The sample_end_time_seconds of this AsyncMirrorPrimarySyncStatisticsSample.
        :rtype: int
        :required/optional: required
        """
        return self._sample_end_time_seconds

    @sample_end_time_seconds.setter
    def sample_end_time_seconds(self, sample_end_time_seconds):
        """
        Sets the sample_end_time_seconds of this AsyncMirrorPrimarySyncStatisticsSample.
        When this sample ended: synchronization completion time, or time of last update before disruption. Time is expressed in seconds since midnight January 1, 1970 GMT.

        :param sample_end_time_seconds: The sample_end_time_seconds of this AsyncMirrorPrimarySyncStatisticsSample.
        :type: int
        """
        self._sample_end_time_seconds = sample_end_time_seconds

    @property
    def member_state(self):
        """
        Gets the member_state of this AsyncMirrorPrimarySyncStatisticsSample.
        Last known state of the mirror member as of the sample end time.

        :return: The member_state of this AsyncMirrorPrimarySyncStatisticsSample.
        :rtype: str
        :required/optional: required
        """
        return self._member_state

    @member_state.setter
    def member_state(self, member_state):
        """
        Sets the member_state of this AsyncMirrorPrimarySyncStatisticsSample.
        Last known state of the mirror member as of the sample end time.

        :param member_state: The member_state of this AsyncMirrorPrimarySyncStatisticsSample.
        :type: str
        """
        allowed_values = ["unknown", "initialSync", "optimal", "failed", "incomplete", "orphan", "stopped", "__UNDEFINED"]
        if member_state not in allowed_values:
            raise ValueError(
                "Invalid value for `member_state`, must be one of {0}"
                .format(allowed_values)
            )
        self._member_state = member_state

    @property
    def repository_utilization_warn_threshold(self):
        """
        Gets the repository_utilization_warn_threshold of this AsyncMirrorPrimarySyncStatisticsSample.
        The repository utilization warning threshold percentage as of the sample end time.

        :return: The repository_utilization_warn_threshold of this AsyncMirrorPrimarySyncStatisticsSample.
        :rtype: int
        :required/optional: required
        """
        return self._repository_utilization_warn_threshold

    @repository_utilization_warn_threshold.setter
    def repository_utilization_warn_threshold(self, repository_utilization_warn_threshold):
        """
        Sets the repository_utilization_warn_threshold of this AsyncMirrorPrimarySyncStatisticsSample.
        The repository utilization warning threshold percentage as of the sample end time.

        :param repository_utilization_warn_threshold: The repository_utilization_warn_threshold of this AsyncMirrorPrimarySyncStatisticsSample.
        :type: int
        """
        self._repository_utilization_warn_threshold = repository_utilization_warn_threshold

    @property
    def repository_utilization_percentage(self):
        """
        Gets the repository_utilization_percentage of this AsyncMirrorPrimarySyncStatisticsSample.
        The repository utilization percentage as of the sample end time (0-100).

        :return: The repository_utilization_percentage of this AsyncMirrorPrimarySyncStatisticsSample.
        :rtype: int
        :required/optional: required
        """
        return self._repository_utilization_percentage

    @repository_utilization_percentage.setter
    def repository_utilization_percentage(self, repository_utilization_percentage):
        """
        Sets the repository_utilization_percentage of this AsyncMirrorPrimarySyncStatisticsSample.
        The repository utilization percentage as of the sample end time (0-100).

        :param repository_utilization_percentage: The repository_utilization_percentage of this AsyncMirrorPrimarySyncStatisticsSample.
        :type: int
        """
        self._repository_utilization_percentage = repository_utilization_percentage

    @property
    def sync_interval_minutes(self):
        """
        Gets the sync_interval_minutes of this AsyncMirrorPrimarySyncStatisticsSample.
        Synchronization interval configured (in minutes), as of the sample end time.

        :return: The sync_interval_minutes of this AsyncMirrorPrimarySyncStatisticsSample.
        :rtype: int
        :required/optional: required
        """
        return self._sync_interval_minutes

    @sync_interval_minutes.setter
    def sync_interval_minutes(self, sync_interval_minutes):
        """
        Sets the sync_interval_minutes of this AsyncMirrorPrimarySyncStatisticsSample.
        Synchronization interval configured (in minutes), as of the sample end time.

        :param sync_interval_minutes: The sync_interval_minutes of this AsyncMirrorPrimarySyncStatisticsSample.
        :type: int
        """
        self._sync_interval_minutes = sync_interval_minutes

    @property
    def sync_duration_minutes(self):
        """
        Gets the sync_duration_minutes of this AsyncMirrorPrimarySyncStatisticsSample.
        Time spent thus far in the synchronization as of the sample end time.

        :return: The sync_duration_minutes of this AsyncMirrorPrimarySyncStatisticsSample.
        :rtype: int
        :required/optional: required
        """
        return self._sync_duration_minutes

    @sync_duration_minutes.setter
    def sync_duration_minutes(self, sync_duration_minutes):
        """
        Sets the sync_duration_minutes of this AsyncMirrorPrimarySyncStatisticsSample.
        Time spent thus far in the synchronization as of the sample end time.

        :param sync_duration_minutes: The sync_duration_minutes of this AsyncMirrorPrimarySyncStatisticsSample.
        :type: int
        """
        self._sync_duration_minutes = sync_duration_minutes

    @property
    def sync_completion_time_alert_threshold_minutes(self):
        """
        Gets the sync_completion_time_alert_threshold_minutes of this AsyncMirrorPrimarySyncStatisticsSample.
        Configured time allowed for the synchronization as of the sample end time.

        :return: The sync_completion_time_alert_threshold_minutes of this AsyncMirrorPrimarySyncStatisticsSample.
        :rtype: int
        :required/optional: required
        """
        return self._sync_completion_time_alert_threshold_minutes

    @sync_completion_time_alert_threshold_minutes.setter
    def sync_completion_time_alert_threshold_minutes(self, sync_completion_time_alert_threshold_minutes):
        """
        Sets the sync_completion_time_alert_threshold_minutes of this AsyncMirrorPrimarySyncStatisticsSample.
        Configured time allowed for the synchronization as of the sample end time.

        :param sync_completion_time_alert_threshold_minutes: The sync_completion_time_alert_threshold_minutes of this AsyncMirrorPrimarySyncStatisticsSample.
        :type: int
        """
        self._sync_completion_time_alert_threshold_minutes = sync_completion_time_alert_threshold_minutes

    @property
    def recovery_point_age_alert_threshold_minutes(self):
        """
        Gets the recovery_point_age_alert_threshold_minutes of this AsyncMirrorPrimarySyncStatisticsSample.
        The recovery point age warning threshold as of the sample end time.

        :return: The recovery_point_age_alert_threshold_minutes of this AsyncMirrorPrimarySyncStatisticsSample.
        :rtype: int
        :required/optional: required
        """
        return self._recovery_point_age_alert_threshold_minutes

    @recovery_point_age_alert_threshold_minutes.setter
    def recovery_point_age_alert_threshold_minutes(self, recovery_point_age_alert_threshold_minutes):
        """
        Sets the recovery_point_age_alert_threshold_minutes of this AsyncMirrorPrimarySyncStatisticsSample.
        The recovery point age warning threshold as of the sample end time.

        :param recovery_point_age_alert_threshold_minutes: The recovery_point_age_alert_threshold_minutes of this AsyncMirrorPrimarySyncStatisticsSample.
        :type: int
        """
        self._recovery_point_age_alert_threshold_minutes = recovery_point_age_alert_threshold_minutes

    @property
    def recovery_point_age_minutes(self):
        """
        Gets the recovery_point_age_minutes of this AsyncMirrorPrimarySyncStatisticsSample.
        The recovery point age (in minutes) as of the sample end time.

        :return: The recovery_point_age_minutes of this AsyncMirrorPrimarySyncStatisticsSample.
        :rtype: int
        :required/optional: required
        """
        return self._recovery_point_age_minutes

    @recovery_point_age_minutes.setter
    def recovery_point_age_minutes(self, recovery_point_age_minutes):
        """
        Sets the recovery_point_age_minutes of this AsyncMirrorPrimarySyncStatisticsSample.
        The recovery point age (in minutes) as of the sample end time.

        :param recovery_point_age_minutes: The recovery_point_age_minutes of this AsyncMirrorPrimarySyncStatisticsSample.
        :type: int
        """
        self._recovery_point_age_minutes = recovery_point_age_minutes

    @property
    def cumulative_bytes_sent(self):
        """
        Gets the cumulative_bytes_sent of this AsyncMirrorPrimarySyncStatisticsSample.
        The total bytes transferred during the time covered by this sample.

        :return: The cumulative_bytes_sent of this AsyncMirrorPrimarySyncStatisticsSample.
        :rtype: int
        :required/optional: required
        """
        return self._cumulative_bytes_sent

    @cumulative_bytes_sent.setter
    def cumulative_bytes_sent(self, cumulative_bytes_sent):
        """
        Sets the cumulative_bytes_sent of this AsyncMirrorPrimarySyncStatisticsSample.
        The total bytes transferred during the time covered by this sample.

        :param cumulative_bytes_sent: The cumulative_bytes_sent of this AsyncMirrorPrimarySyncStatisticsSample.
        :type: int
        """
        self._cumulative_bytes_sent = cumulative_bytes_sent

    @property
    def cumulative_io_time(self):
        """
        Gets the cumulative_io_time of this AsyncMirrorPrimarySyncStatisticsSample.
        The total time spent sending data to the secondary for the duration of this sample (in microseconds). This is measured from the time each I/O is sent to the secondary until the response is received.

        :return: The cumulative_io_time of this AsyncMirrorPrimarySyncStatisticsSample.
        :rtype: int
        :required/optional: required
        """
        return self._cumulative_io_time

    @cumulative_io_time.setter
    def cumulative_io_time(self, cumulative_io_time):
        """
        Sets the cumulative_io_time of this AsyncMirrorPrimarySyncStatisticsSample.
        The total time spent sending data to the secondary for the duration of this sample (in microseconds). This is measured from the time each I/O is sent to the secondary until the response is received.

        :param cumulative_io_time: The cumulative_io_time of this AsyncMirrorPrimarySyncStatisticsSample.
        :type: int
        """
        self._cumulative_io_time = cumulative_io_time

    @property
    def total_io_count(self):
        """
        Gets the total_io_count of this AsyncMirrorPrimarySyncStatisticsSample.
        The total count of I/O requests to the secondary in this sample.

        :return: The total_io_count of this AsyncMirrorPrimarySyncStatisticsSample.
        :rtype: int
        :required/optional: required
        """
        return self._total_io_count

    @total_io_count.setter
    def total_io_count(self, total_io_count):
        """
        Sets the total_io_count of this AsyncMirrorPrimarySyncStatisticsSample.
        The total count of I/O requests to the secondary in this sample.

        :param total_io_count: The total_io_count of this AsyncMirrorPrimarySyncStatisticsSample.
        :type: int
        """
        self._total_io_count = total_io_count

    @property
    def longest_response_time_micro_seconds(self):
        """
        Gets the longest_response_time_micro_seconds of this AsyncMirrorPrimarySyncStatisticsSample.
        The longest response time from the secondary array observed for one request during the time covered by this sample (in microseconds).

        :return: The longest_response_time_micro_seconds of this AsyncMirrorPrimarySyncStatisticsSample.
        :rtype: int
        :required/optional: required
        """
        return self._longest_response_time_micro_seconds

    @longest_response_time_micro_seconds.setter
    def longest_response_time_micro_seconds(self, longest_response_time_micro_seconds):
        """
        Sets the longest_response_time_micro_seconds of this AsyncMirrorPrimarySyncStatisticsSample.
        The longest response time from the secondary array observed for one request during the time covered by this sample (in microseconds).

        :param longest_response_time_micro_seconds: The longest_response_time_micro_seconds of this AsyncMirrorPrimarySyncStatisticsSample.
        :type: int
        """
        self._longest_response_time_micro_seconds = longest_response_time_micro_seconds

    @property
    def longest_response_time_bytes(self):
        """
        Gets the longest_response_time_bytes of this AsyncMirrorPrimarySyncStatisticsSample.
        The number of bytes transferred on the longest request.

        :return: The longest_response_time_bytes of this AsyncMirrorPrimarySyncStatisticsSample.
        :rtype: int
        :required/optional: required
        """
        return self._longest_response_time_bytes

    @longest_response_time_bytes.setter
    def longest_response_time_bytes(self, longest_response_time_bytes):
        """
        Sets the longest_response_time_bytes of this AsyncMirrorPrimarySyncStatisticsSample.
        The number of bytes transferred on the longest request.

        :param longest_response_time_bytes: The longest_response_time_bytes of this AsyncMirrorPrimarySyncStatisticsSample.
        :type: int
        """
        self._longest_response_time_bytes = longest_response_time_bytes

    @property
    def shortest_response_time_micro_seconds(self):
        """
        Gets the shortest_response_time_micro_seconds of this AsyncMirrorPrimarySyncStatisticsSample.
        The shortest response time from the secondary array observed for one request during the time covered by this sample (in microseconds).

        :return: The shortest_response_time_micro_seconds of this AsyncMirrorPrimarySyncStatisticsSample.
        :rtype: int
        :required/optional: required
        """
        return self._shortest_response_time_micro_seconds

    @shortest_response_time_micro_seconds.setter
    def shortest_response_time_micro_seconds(self, shortest_response_time_micro_seconds):
        """
        Sets the shortest_response_time_micro_seconds of this AsyncMirrorPrimarySyncStatisticsSample.
        The shortest response time from the secondary array observed for one request during the time covered by this sample (in microseconds).

        :param shortest_response_time_micro_seconds: The shortest_response_time_micro_seconds of this AsyncMirrorPrimarySyncStatisticsSample.
        :type: int
        """
        self._shortest_response_time_micro_seconds = shortest_response_time_micro_seconds

    @property
    def shortest_response_time_bytes(self):
        """
        Gets the shortest_response_time_bytes of this AsyncMirrorPrimarySyncStatisticsSample.
        The number of bytes sent on shortest request.

        :return: The shortest_response_time_bytes of this AsyncMirrorPrimarySyncStatisticsSample.
        :rtype: int
        :required/optional: required
        """
        return self._shortest_response_time_bytes

    @shortest_response_time_bytes.setter
    def shortest_response_time_bytes(self, shortest_response_time_bytes):
        """
        Sets the shortest_response_time_bytes of this AsyncMirrorPrimarySyncStatisticsSample.
        The number of bytes sent on shortest request.

        :param shortest_response_time_bytes: The shortest_response_time_bytes of this AsyncMirrorPrimarySyncStatisticsSample.
        :type: int
        """
        self._shortest_response_time_bytes = shortest_response_time_bytes

    @property
    def highest_throughput_in_bytes_per_second(self):
        """
        Gets the highest_throughput_in_bytes_per_second of this AsyncMirrorPrimarySyncStatisticsSample.
        The highest recorded throughput (in bytes/second) to the remote array for this mirror during this sample period.

        :return: The highest_throughput_in_bytes_per_second of this AsyncMirrorPrimarySyncStatisticsSample.
        :rtype: int
        :required/optional: required
        """
        return self._highest_throughput_in_bytes_per_second

    @highest_throughput_in_bytes_per_second.setter
    def highest_throughput_in_bytes_per_second(self, highest_throughput_in_bytes_per_second):
        """
        Sets the highest_throughput_in_bytes_per_second of this AsyncMirrorPrimarySyncStatisticsSample.
        The highest recorded throughput (in bytes/second) to the remote array for this mirror during this sample period.

        :param highest_throughput_in_bytes_per_second: The highest_throughput_in_bytes_per_second of this AsyncMirrorPrimarySyncStatisticsSample.
        :type: int
        """
        self._highest_throughput_in_bytes_per_second = highest_throughput_in_bytes_per_second

    @property
    def lowest_throughput_in_bytes_per_second(self):
        """
        Gets the lowest_throughput_in_bytes_per_second of this AsyncMirrorPrimarySyncStatisticsSample.
        The lowest recorded throughput (in bytes/second) to the remote array for this mirror during this sample period.

        :return: The lowest_throughput_in_bytes_per_second of this AsyncMirrorPrimarySyncStatisticsSample.
        :rtype: int
        :required/optional: required
        """
        return self._lowest_throughput_in_bytes_per_second

    @lowest_throughput_in_bytes_per_second.setter
    def lowest_throughput_in_bytes_per_second(self, lowest_throughput_in_bytes_per_second):
        """
        Sets the lowest_throughput_in_bytes_per_second of this AsyncMirrorPrimarySyncStatisticsSample.
        The lowest recorded throughput (in bytes/second) to the remote array for this mirror during this sample period.

        :param lowest_throughput_in_bytes_per_second: The lowest_throughput_in_bytes_per_second of this AsyncMirrorPrimarySyncStatisticsSample.
        :type: int
        """
        self._lowest_throughput_in_bytes_per_second = lowest_throughput_in_bytes_per_second

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

