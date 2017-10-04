# coding: utf-8

"""
StorageSystemStats.py

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


class StorageSystemStats(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        StorageSystemStats - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'observed_time': 'datetime',  # (required parameter)
            'observed_time_in_ms': 'int',  # (required parameter)
            'last_reset_time': 'datetime',  # (required parameter)
            'last_reset_time_in_ms': 'int',  # (required parameter)
            'array_id': 'str',  # (required parameter)
            'array_wwn': 'str',  # (required parameter)
            'member_ids_hash': 'str',  # (required parameter)
            'controller_stats': 'list[StorageSystemControllerStats]',  # (required parameter)
            'total_iops_serviced': 'float',  # (required parameter)
            'total_bytes_serviced': 'float',  # (required parameter)
            'cache_hits_iops_total': 'float',  # (required parameter)
            'cache_hits_bytes_total': 'float',  # (required parameter)
            'random_ios_total': 'float',  # (required parameter)
            'random_bytes_total': 'float',  # (required parameter)
            'read_iops_total': 'float',  # (required parameter)
            'read_bytes_total': 'float',  # (required parameter)
            'write_iops_total': 'float',  # (required parameter)
            'write_bytes_total': 'float',  # (required parameter)
            'mirror_iops_total': 'float',  # (required parameter)
            'mirror_bytes_total': 'float',  # (required parameter)
            'full_stripe_writes_bytes': 'float',  # (required parameter)
            'raid0_bytes_transferred': 'float',  # (required parameter)
            'raid1_bytes_transferred': 'float',  # (required parameter)
            'raid5_bytes_transferred': 'float',  # (required parameter)
            'raid6_bytes_transferred': 'float',  # (required parameter)
            'ddp_bytes_transferred': 'float',  # (required parameter)
            'max_possible_bps_under_current_load': 'float',  # (required parameter)
            'max_possible_iops_under_current_load': 'float'
        }

        self.attribute_map = {
            'observed_time': 'observedTime',  # (required parameter)
            'observed_time_in_ms': 'observedTimeInMS',  # (required parameter)
            'last_reset_time': 'lastResetTime',  # (required parameter)
            'last_reset_time_in_ms': 'lastResetTimeInMS',  # (required parameter)
            'array_id': 'arrayId',  # (required parameter)
            'array_wwn': 'arrayWwn',  # (required parameter)
            'member_ids_hash': 'memberIdsHash',  # (required parameter)
            'controller_stats': 'controllerStats',  # (required parameter)
            'total_iops_serviced': 'totalIopsServiced',  # (required parameter)
            'total_bytes_serviced': 'totalBytesServiced',  # (required parameter)
            'cache_hits_iops_total': 'cacheHitsIopsTotal',  # (required parameter)
            'cache_hits_bytes_total': 'cacheHitsBytesTotal',  # (required parameter)
            'random_ios_total': 'randomIosTotal',  # (required parameter)
            'random_bytes_total': 'randomBytesTotal',  # (required parameter)
            'read_iops_total': 'readIopsTotal',  # (required parameter)
            'read_bytes_total': 'readBytesTotal',  # (required parameter)
            'write_iops_total': 'writeIopsTotal',  # (required parameter)
            'write_bytes_total': 'writeBytesTotal',  # (required parameter)
            'mirror_iops_total': 'mirrorIopsTotal',  # (required parameter)
            'mirror_bytes_total': 'mirrorBytesTotal',  # (required parameter)
            'full_stripe_writes_bytes': 'fullStripeWritesBytes',  # (required parameter)
            'raid0_bytes_transferred': 'raid0BytesTransferred',  # (required parameter)
            'raid1_bytes_transferred': 'raid1BytesTransferred',  # (required parameter)
            'raid5_bytes_transferred': 'raid5BytesTransferred',  # (required parameter)
            'raid6_bytes_transferred': 'raid6BytesTransferred',  # (required parameter)
            'ddp_bytes_transferred': 'ddpBytesTransferred',  # (required parameter)
            'max_possible_bps_under_current_load': 'maxPossibleBpsUnderCurrentLoad',  # (required parameter)
            'max_possible_iops_under_current_load': 'maxPossibleIopsUnderCurrentLoad'
        }

        self._observed_time = None
        self._observed_time_in_ms = None
        self._last_reset_time = None
        self._last_reset_time_in_ms = None
        self._array_id = None
        self._array_wwn = None
        self._member_ids_hash = None
        self._controller_stats = None
        self._total_iops_serviced = None
        self._total_bytes_serviced = None
        self._cache_hits_iops_total = None
        self._cache_hits_bytes_total = None
        self._random_ios_total = None
        self._random_bytes_total = None
        self._read_iops_total = None
        self._read_bytes_total = None
        self._write_iops_total = None
        self._write_bytes_total = None
        self._mirror_iops_total = None
        self._mirror_bytes_total = None
        self._full_stripe_writes_bytes = None
        self._raid0_bytes_transferred = None
        self._raid1_bytes_transferred = None
        self._raid5_bytes_transferred = None
        self._raid6_bytes_transferred = None
        self._ddp_bytes_transferred = None
        self._max_possible_bps_under_current_load = None
        self._max_possible_iops_under_current_load = None

    @property
    def observed_time(self):
        """
        Gets the observed_time of this StorageSystemStats.
        End time for this collection as measured by the number of seconds since baseTime.

        :return: The observed_time of this StorageSystemStats.
        :rtype: datetime
        :required/optional: required
        """
        return self._observed_time

    @observed_time.setter
    def observed_time(self, observed_time):
        """
        Sets the observed_time of this StorageSystemStats.
        End time for this collection as measured by the number of seconds since baseTime.

        :param observed_time: The observed_time of this StorageSystemStats.
        :type: datetime
        """
        self._observed_time = observed_time

    @property
    def observed_time_in_ms(self):
        """
        Gets the observed_time_in_ms of this StorageSystemStats.


        :return: The observed_time_in_ms of this StorageSystemStats.
        :rtype: int
        :required/optional: required
        """
        return self._observed_time_in_ms

    @observed_time_in_ms.setter
    def observed_time_in_ms(self, observed_time_in_ms):
        """
        Sets the observed_time_in_ms of this StorageSystemStats.


        :param observed_time_in_ms: The observed_time_in_ms of this StorageSystemStats.
        :type: int
        """
        self._observed_time_in_ms = observed_time_in_ms

    @property
    def last_reset_time(self):
        """
        Gets the last_reset_time of this StorageSystemStats.


        :return: The last_reset_time of this StorageSystemStats.
        :rtype: datetime
        :required/optional: required
        """
        return self._last_reset_time

    @last_reset_time.setter
    def last_reset_time(self, last_reset_time):
        """
        Sets the last_reset_time of this StorageSystemStats.


        :param last_reset_time: The last_reset_time of this StorageSystemStats.
        :type: datetime
        """
        self._last_reset_time = last_reset_time

    @property
    def last_reset_time_in_ms(self):
        """
        Gets the last_reset_time_in_ms of this StorageSystemStats.


        :return: The last_reset_time_in_ms of this StorageSystemStats.
        :rtype: int
        :required/optional: required
        """
        return self._last_reset_time_in_ms

    @last_reset_time_in_ms.setter
    def last_reset_time_in_ms(self, last_reset_time_in_ms):
        """
        Sets the last_reset_time_in_ms of this StorageSystemStats.


        :param last_reset_time_in_ms: The last_reset_time_in_ms of this StorageSystemStats.
        :type: int
        """
        self._last_reset_time_in_ms = last_reset_time_in_ms

    @property
    def array_id(self):
        """
        Gets the array_id of this StorageSystemStats.


        :return: The array_id of this StorageSystemStats.
        :rtype: str
        :required/optional: required
        """
        return self._array_id

    @array_id.setter
    def array_id(self, array_id):
        """
        Sets the array_id of this StorageSystemStats.


        :param array_id: The array_id of this StorageSystemStats.
        :type: str
        """
        self._array_id = array_id

    @property
    def array_wwn(self):
        """
        Gets the array_wwn of this StorageSystemStats.


        :return: The array_wwn of this StorageSystemStats.
        :rtype: str
        :required/optional: required
        """
        return self._array_wwn

    @array_wwn.setter
    def array_wwn(self, array_wwn):
        """
        Sets the array_wwn of this StorageSystemStats.


        :param array_wwn: The array_wwn of this StorageSystemStats.
        :type: str
        """
        self._array_wwn = array_wwn

    @property
    def member_ids_hash(self):
        """
        Gets the member_ids_hash of this StorageSystemStats.
        Hash of member controller ids.

        :return: The member_ids_hash of this StorageSystemStats.
        :rtype: str
        :required/optional: required
        """
        return self._member_ids_hash

    @member_ids_hash.setter
    def member_ids_hash(self, member_ids_hash):
        """
        Sets the member_ids_hash of this StorageSystemStats.
        Hash of member controller ids.

        :param member_ids_hash: The member_ids_hash of this StorageSystemStats.
        :type: str
        """
        self._member_ids_hash = member_ids_hash

    @property
    def controller_stats(self):
        """
        Gets the controller_stats of this StorageSystemStats.
        Statistics for each controller.

        :return: The controller_stats of this StorageSystemStats.
        :rtype: list[StorageSystemControllerStats]
        :required/optional: required
        """
        return self._controller_stats

    @controller_stats.setter
    def controller_stats(self, controller_stats):
        """
        Sets the controller_stats of this StorageSystemStats.
        Statistics for each controller.

        :param controller_stats: The controller_stats of this StorageSystemStats.
        :type: list[StorageSystemControllerStats]
        """
        self._controller_stats = controller_stats

    @property
    def total_iops_serviced(self):
        """
        Gets the total_iops_serviced of this StorageSystemStats.
        Total number of IO operations serviced by the controller.

        :return: The total_iops_serviced of this StorageSystemStats.
        :rtype: float
        :required/optional: required
        """
        return self._total_iops_serviced

    @total_iops_serviced.setter
    def total_iops_serviced(self, total_iops_serviced):
        """
        Sets the total_iops_serviced of this StorageSystemStats.
        Total number of IO operations serviced by the controller.

        :param total_iops_serviced: The total_iops_serviced of this StorageSystemStats.
        :type: float
        """
        self._total_iops_serviced = total_iops_serviced

    @property
    def total_bytes_serviced(self):
        """
        Gets the total_bytes_serviced of this StorageSystemStats.
        Total number of Bytes serviced by the controller.

        :return: The total_bytes_serviced of this StorageSystemStats.
        :rtype: float
        :required/optional: required
        """
        return self._total_bytes_serviced

    @total_bytes_serviced.setter
    def total_bytes_serviced(self, total_bytes_serviced):
        """
        Sets the total_bytes_serviced of this StorageSystemStats.
        Total number of Bytes serviced by the controller.

        :param total_bytes_serviced: The total_bytes_serviced of this StorageSystemStats.
        :type: float
        """
        self._total_bytes_serviced = total_bytes_serviced

    @property
    def cache_hits_iops_total(self):
        """
        Gets the cache_hits_iops_total of this StorageSystemStats.
        Total number of IO operations that hit cache.

        :return: The cache_hits_iops_total of this StorageSystemStats.
        :rtype: float
        :required/optional: required
        """
        return self._cache_hits_iops_total

    @cache_hits_iops_total.setter
    def cache_hits_iops_total(self, cache_hits_iops_total):
        """
        Sets the cache_hits_iops_total of this StorageSystemStats.
        Total number of IO operations that hit cache.

        :param cache_hits_iops_total: The cache_hits_iops_total of this StorageSystemStats.
        :type: float
        """
        self._cache_hits_iops_total = cache_hits_iops_total

    @property
    def cache_hits_bytes_total(self):
        """
        Gets the cache_hits_bytes_total of this StorageSystemStats.
        Total number of bytes that hit cache.

        :return: The cache_hits_bytes_total of this StorageSystemStats.
        :rtype: float
        :required/optional: required
        """
        return self._cache_hits_bytes_total

    @cache_hits_bytes_total.setter
    def cache_hits_bytes_total(self, cache_hits_bytes_total):
        """
        Sets the cache_hits_bytes_total of this StorageSystemStats.
        Total number of bytes that hit cache.

        :param cache_hits_bytes_total: The cache_hits_bytes_total of this StorageSystemStats.
        :type: float
        """
        self._cache_hits_bytes_total = cache_hits_bytes_total

    @property
    def random_ios_total(self):
        """
        Gets the random_ios_total of this StorageSystemStats.
        Total number of IOs that are categorized as random.

        :return: The random_ios_total of this StorageSystemStats.
        :rtype: float
        :required/optional: required
        """
        return self._random_ios_total

    @random_ios_total.setter
    def random_ios_total(self, random_ios_total):
        """
        Sets the random_ios_total of this StorageSystemStats.
        Total number of IOs that are categorized as random.

        :param random_ios_total: The random_ios_total of this StorageSystemStats.
        :type: float
        """
        self._random_ios_total = random_ios_total

    @property
    def random_bytes_total(self):
        """
        Gets the random_bytes_total of this StorageSystemStats.
        Total number of Bytes that are categorized as random.

        :return: The random_bytes_total of this StorageSystemStats.
        :rtype: float
        :required/optional: required
        """
        return self._random_bytes_total

    @random_bytes_total.setter
    def random_bytes_total(self, random_bytes_total):
        """
        Sets the random_bytes_total of this StorageSystemStats.
        Total number of Bytes that are categorized as random.

        :param random_bytes_total: The random_bytes_total of this StorageSystemStats.
        :type: float
        """
        self._random_bytes_total = random_bytes_total

    @property
    def read_iops_total(self):
        """
        Gets the read_iops_total of this StorageSystemStats.
        Total number of Read IO operations.

        :return: The read_iops_total of this StorageSystemStats.
        :rtype: float
        :required/optional: required
        """
        return self._read_iops_total

    @read_iops_total.setter
    def read_iops_total(self, read_iops_total):
        """
        Sets the read_iops_total of this StorageSystemStats.
        Total number of Read IO operations.

        :param read_iops_total: The read_iops_total of this StorageSystemStats.
        :type: float
        """
        self._read_iops_total = read_iops_total

    @property
    def read_bytes_total(self):
        """
        Gets the read_bytes_total of this StorageSystemStats.
        Total number of Bytes read.

        :return: The read_bytes_total of this StorageSystemStats.
        :rtype: float
        :required/optional: required
        """
        return self._read_bytes_total

    @read_bytes_total.setter
    def read_bytes_total(self, read_bytes_total):
        """
        Sets the read_bytes_total of this StorageSystemStats.
        Total number of Bytes read.

        :param read_bytes_total: The read_bytes_total of this StorageSystemStats.
        :type: float
        """
        self._read_bytes_total = read_bytes_total

    @property
    def write_iops_total(self):
        """
        Gets the write_iops_total of this StorageSystemStats.
        Total number of Write IO operations.

        :return: The write_iops_total of this StorageSystemStats.
        :rtype: float
        :required/optional: required
        """
        return self._write_iops_total

    @write_iops_total.setter
    def write_iops_total(self, write_iops_total):
        """
        Sets the write_iops_total of this StorageSystemStats.
        Total number of Write IO operations.

        :param write_iops_total: The write_iops_total of this StorageSystemStats.
        :type: float
        """
        self._write_iops_total = write_iops_total

    @property
    def write_bytes_total(self):
        """
        Gets the write_bytes_total of this StorageSystemStats.
        Total number of Bytes written.

        :return: The write_bytes_total of this StorageSystemStats.
        :rtype: float
        :required/optional: required
        """
        return self._write_bytes_total

    @write_bytes_total.setter
    def write_bytes_total(self, write_bytes_total):
        """
        Sets the write_bytes_total of this StorageSystemStats.
        Total number of Bytes written.

        :param write_bytes_total: The write_bytes_total of this StorageSystemStats.
        :type: float
        """
        self._write_bytes_total = write_bytes_total

    @property
    def mirror_iops_total(self):
        """
        Gets the mirror_iops_total of this StorageSystemStats.
        Total number of IO operations serviced by the controller that are characterized as cache mirroring related. If cache mirroring is disabled, this counter will not have any value.

        :return: The mirror_iops_total of this StorageSystemStats.
        :rtype: float
        :required/optional: required
        """
        return self._mirror_iops_total

    @mirror_iops_total.setter
    def mirror_iops_total(self, mirror_iops_total):
        """
        Sets the mirror_iops_total of this StorageSystemStats.
        Total number of IO operations serviced by the controller that are characterized as cache mirroring related. If cache mirroring is disabled, this counter will not have any value.

        :param mirror_iops_total: The mirror_iops_total of this StorageSystemStats.
        :type: float
        """
        self._mirror_iops_total = mirror_iops_total

    @property
    def mirror_bytes_total(self):
        """
        Gets the mirror_bytes_total of this StorageSystemStats.
        Total number of Bytes serviced by the controller that are characterized as cache mirroring related. If cache mirroring is disabled, this counter will not have any value.

        :return: The mirror_bytes_total of this StorageSystemStats.
        :rtype: float
        :required/optional: required
        """
        return self._mirror_bytes_total

    @mirror_bytes_total.setter
    def mirror_bytes_total(self, mirror_bytes_total):
        """
        Sets the mirror_bytes_total of this StorageSystemStats.
        Total number of Bytes serviced by the controller that are characterized as cache mirroring related. If cache mirroring is disabled, this counter will not have any value.

        :param mirror_bytes_total: The mirror_bytes_total of this StorageSystemStats.
        :type: float
        """
        self._mirror_bytes_total = mirror_bytes_total

    @property
    def full_stripe_writes_bytes(self):
        """
        Gets the full_stripe_writes_bytes of this StorageSystemStats.
        Bytes written that are categorized as Full stripe writes.

        :return: The full_stripe_writes_bytes of this StorageSystemStats.
        :rtype: float
        :required/optional: required
        """
        return self._full_stripe_writes_bytes

    @full_stripe_writes_bytes.setter
    def full_stripe_writes_bytes(self, full_stripe_writes_bytes):
        """
        Sets the full_stripe_writes_bytes of this StorageSystemStats.
        Bytes written that are categorized as Full stripe writes.

        :param full_stripe_writes_bytes: The full_stripe_writes_bytes of this StorageSystemStats.
        :type: float
        """
        self._full_stripe_writes_bytes = full_stripe_writes_bytes

    @property
    def raid0_bytes_transferred(self):
        """
        Gets the raid0_bytes_transferred of this StorageSystemStats.
        Bytes transferred that are categorized as RAID 0 transfers.

        :return: The raid0_bytes_transferred of this StorageSystemStats.
        :rtype: float
        :required/optional: required
        """
        return self._raid0_bytes_transferred

    @raid0_bytes_transferred.setter
    def raid0_bytes_transferred(self, raid0_bytes_transferred):
        """
        Sets the raid0_bytes_transferred of this StorageSystemStats.
        Bytes transferred that are categorized as RAID 0 transfers.

        :param raid0_bytes_transferred: The raid0_bytes_transferred of this StorageSystemStats.
        :type: float
        """
        self._raid0_bytes_transferred = raid0_bytes_transferred

    @property
    def raid1_bytes_transferred(self):
        """
        Gets the raid1_bytes_transferred of this StorageSystemStats.
        Bytes transferred that are categorized as RAID 1 transfers.

        :return: The raid1_bytes_transferred of this StorageSystemStats.
        :rtype: float
        :required/optional: required
        """
        return self._raid1_bytes_transferred

    @raid1_bytes_transferred.setter
    def raid1_bytes_transferred(self, raid1_bytes_transferred):
        """
        Sets the raid1_bytes_transferred of this StorageSystemStats.
        Bytes transferred that are categorized as RAID 1 transfers.

        :param raid1_bytes_transferred: The raid1_bytes_transferred of this StorageSystemStats.
        :type: float
        """
        self._raid1_bytes_transferred = raid1_bytes_transferred

    @property
    def raid5_bytes_transferred(self):
        """
        Gets the raid5_bytes_transferred of this StorageSystemStats.
        Bytes transferred that are categorized as RAID 5 transfers.

        :return: The raid5_bytes_transferred of this StorageSystemStats.
        :rtype: float
        :required/optional: required
        """
        return self._raid5_bytes_transferred

    @raid5_bytes_transferred.setter
    def raid5_bytes_transferred(self, raid5_bytes_transferred):
        """
        Sets the raid5_bytes_transferred of this StorageSystemStats.
        Bytes transferred that are categorized as RAID 5 transfers.

        :param raid5_bytes_transferred: The raid5_bytes_transferred of this StorageSystemStats.
        :type: float
        """
        self._raid5_bytes_transferred = raid5_bytes_transferred

    @property
    def raid6_bytes_transferred(self):
        """
        Gets the raid6_bytes_transferred of this StorageSystemStats.
        Bytes transferred that are categorized as RAID 6 transfers.

        :return: The raid6_bytes_transferred of this StorageSystemStats.
        :rtype: float
        :required/optional: required
        """
        return self._raid6_bytes_transferred

    @raid6_bytes_transferred.setter
    def raid6_bytes_transferred(self, raid6_bytes_transferred):
        """
        Sets the raid6_bytes_transferred of this StorageSystemStats.
        Bytes transferred that are categorized as RAID 6 transfers.

        :param raid6_bytes_transferred: The raid6_bytes_transferred of this StorageSystemStats.
        :type: float
        """
        self._raid6_bytes_transferred = raid6_bytes_transferred

    @property
    def ddp_bytes_transferred(self):
        """
        Gets the ddp_bytes_transferred of this StorageSystemStats.
        Bytes transferred that are categorized as DDP transfers.

        :return: The ddp_bytes_transferred of this StorageSystemStats.
        :rtype: float
        :required/optional: required
        """
        return self._ddp_bytes_transferred

    @ddp_bytes_transferred.setter
    def ddp_bytes_transferred(self, ddp_bytes_transferred):
        """
        Sets the ddp_bytes_transferred of this StorageSystemStats.
        Bytes transferred that are categorized as DDP transfers.

        :param ddp_bytes_transferred: The ddp_bytes_transferred of this StorageSystemStats.
        :type: float
        """
        self._ddp_bytes_transferred = ddp_bytes_transferred

    @property
    def max_possible_bps_under_current_load(self):
        """
        Gets the max_possible_bps_under_current_load of this StorageSystemStats.
        Theoretical maximum possible Bytes per second under current load.

        :return: The max_possible_bps_under_current_load of this StorageSystemStats.
        :rtype: float
        :required/optional: required
        """
        return self._max_possible_bps_under_current_load

    @max_possible_bps_under_current_load.setter
    def max_possible_bps_under_current_load(self, max_possible_bps_under_current_load):
        """
        Sets the max_possible_bps_under_current_load of this StorageSystemStats.
        Theoretical maximum possible Bytes per second under current load.

        :param max_possible_bps_under_current_load: The max_possible_bps_under_current_load of this StorageSystemStats.
        :type: float
        """
        self._max_possible_bps_under_current_load = max_possible_bps_under_current_load

    @property
    def max_possible_iops_under_current_load(self):
        """
        Gets the max_possible_iops_under_current_load of this StorageSystemStats.
        Theoretical maximum possible IO per second under current load.

        :return: The max_possible_iops_under_current_load of this StorageSystemStats.
        :rtype: float
        :required/optional: required
        """
        return self._max_possible_iops_under_current_load

    @max_possible_iops_under_current_load.setter
    def max_possible_iops_under_current_load(self, max_possible_iops_under_current_load):
        """
        Sets the max_possible_iops_under_current_load of this StorageSystemStats.
        Theoretical maximum possible IO per second under current load.

        :param max_possible_iops_under_current_load: The max_possible_iops_under_current_load of this StorageSystemStats.
        :type: float
        """
        self._max_possible_iops_under_current_load = max_possible_iops_under_current_load

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

