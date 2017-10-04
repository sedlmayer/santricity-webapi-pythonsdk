# coding: utf-8

"""
X509ExternalCertInfo.py

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


class X509ExternalCertInfo(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        X509ExternalCertInfo - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'kms_address': 'NetworkAddress',  
            'kms_port': 'int',  
            'client_kms_type': 'str',  
            'client_subject_dn': 'str',  
            'client_issuer_dn': 'str',  
            'client_start': 'datetime',  
            'client_expire': 'datetime',  
            'server_kms_type': 'str',  
            'server_subject_dn': 'str',  
            'server_issuer_dn': 'str',  
            'server_start': 'datetime',  
            'server_expire': 'datetime'
        }

        self.attribute_map = {
            'kms_address': 'kmsAddress',  
            'kms_port': 'kmsPort',  
            'client_kms_type': 'clientKmsType',  
            'client_subject_dn': 'clientSubjectDN',  
            'client_issuer_dn': 'clientIssuerDN',  
            'client_start': 'clientStart',  
            'client_expire': 'clientExpire',  
            'server_kms_type': 'serverKmsType',  
            'server_subject_dn': 'serverSubjectDN',  
            'server_issuer_dn': 'serverIssuerDN',  
            'server_start': 'serverStart',  
            'server_expire': 'serverExpire'
        }

        self._kms_address = None
        self._kms_port = None
        self._client_kms_type = None
        self._client_subject_dn = None
        self._client_issuer_dn = None
        self._client_start = None
        self._client_expire = None
        self._server_kms_type = None
        self._server_subject_dn = None
        self._server_issuer_dn = None
        self._server_start = None
        self._server_expire = None

    @property
    def kms_address(self):
        """
        Gets the kms_address of this X509ExternalCertInfo.


        :return: The kms_address of this X509ExternalCertInfo.
        :rtype: NetworkAddress
        :required/optional: optional
        """
        return self._kms_address

    @kms_address.setter
    def kms_address(self, kms_address):
        """
        Sets the kms_address of this X509ExternalCertInfo.


        :param kms_address: The kms_address of this X509ExternalCertInfo.
        :type: NetworkAddress
        """
        self._kms_address = kms_address

    @property
    def kms_port(self):
        """
        Gets the kms_port of this X509ExternalCertInfo.


        :return: The kms_port of this X509ExternalCertInfo.
        :rtype: int
        :required/optional: optional
        """
        return self._kms_port

    @kms_port.setter
    def kms_port(self, kms_port):
        """
        Sets the kms_port of this X509ExternalCertInfo.


        :param kms_port: The kms_port of this X509ExternalCertInfo.
        :type: int
        """
        self._kms_port = kms_port

    @property
    def client_kms_type(self):
        """
        Gets the client_kms_type of this X509ExternalCertInfo.


        :return: The client_kms_type of this X509ExternalCertInfo.
        :rtype: str
        :required/optional: optional
        """
        return self._client_kms_type

    @client_kms_type.setter
    def client_kms_type(self, client_kms_type):
        """
        Sets the client_kms_type of this X509ExternalCertInfo.


        :param client_kms_type: The client_kms_type of this X509ExternalCertInfo.
        :type: str
        """
        allowed_values = ["certificateFileTypeUnknown", "clientCertificate", "serverCertificate", "__UNDEFINED", None]
        if client_kms_type not in allowed_values:
            raise ValueError(
                "Invalid value for `client_kms_type`, must be one of {0}"
                .format(allowed_values)
            )
        self._client_kms_type = client_kms_type

    @property
    def client_subject_dn(self):
        """
        Gets the client_subject_dn of this X509ExternalCertInfo.


        :return: The client_subject_dn of this X509ExternalCertInfo.
        :rtype: str
        :required/optional: optional
        """
        return self._client_subject_dn

    @client_subject_dn.setter
    def client_subject_dn(self, client_subject_dn):
        """
        Sets the client_subject_dn of this X509ExternalCertInfo.


        :param client_subject_dn: The client_subject_dn of this X509ExternalCertInfo.
        :type: str
        """
        self._client_subject_dn = client_subject_dn

    @property
    def client_issuer_dn(self):
        """
        Gets the client_issuer_dn of this X509ExternalCertInfo.


        :return: The client_issuer_dn of this X509ExternalCertInfo.
        :rtype: str
        :required/optional: optional
        """
        return self._client_issuer_dn

    @client_issuer_dn.setter
    def client_issuer_dn(self, client_issuer_dn):
        """
        Sets the client_issuer_dn of this X509ExternalCertInfo.


        :param client_issuer_dn: The client_issuer_dn of this X509ExternalCertInfo.
        :type: str
        """
        self._client_issuer_dn = client_issuer_dn

    @property
    def client_start(self):
        """
        Gets the client_start of this X509ExternalCertInfo.


        :return: The client_start of this X509ExternalCertInfo.
        :rtype: datetime
        :required/optional: optional
        """
        return self._client_start

    @client_start.setter
    def client_start(self, client_start):
        """
        Sets the client_start of this X509ExternalCertInfo.


        :param client_start: The client_start of this X509ExternalCertInfo.
        :type: datetime
        """
        self._client_start = client_start

    @property
    def client_expire(self):
        """
        Gets the client_expire of this X509ExternalCertInfo.


        :return: The client_expire of this X509ExternalCertInfo.
        :rtype: datetime
        :required/optional: optional
        """
        return self._client_expire

    @client_expire.setter
    def client_expire(self, client_expire):
        """
        Sets the client_expire of this X509ExternalCertInfo.


        :param client_expire: The client_expire of this X509ExternalCertInfo.
        :type: datetime
        """
        self._client_expire = client_expire

    @property
    def server_kms_type(self):
        """
        Gets the server_kms_type of this X509ExternalCertInfo.


        :return: The server_kms_type of this X509ExternalCertInfo.
        :rtype: str
        :required/optional: optional
        """
        return self._server_kms_type

    @server_kms_type.setter
    def server_kms_type(self, server_kms_type):
        """
        Sets the server_kms_type of this X509ExternalCertInfo.


        :param server_kms_type: The server_kms_type of this X509ExternalCertInfo.
        :type: str
        """
        allowed_values = ["certificateFileTypeUnknown", "clientCertificate", "serverCertificate", "__UNDEFINED", None]
        if server_kms_type not in allowed_values:
            raise ValueError(
                "Invalid value for `server_kms_type`, must be one of {0}"
                .format(allowed_values)
            )
        self._server_kms_type = server_kms_type

    @property
    def server_subject_dn(self):
        """
        Gets the server_subject_dn of this X509ExternalCertInfo.


        :return: The server_subject_dn of this X509ExternalCertInfo.
        :rtype: str
        :required/optional: optional
        """
        return self._server_subject_dn

    @server_subject_dn.setter
    def server_subject_dn(self, server_subject_dn):
        """
        Sets the server_subject_dn of this X509ExternalCertInfo.


        :param server_subject_dn: The server_subject_dn of this X509ExternalCertInfo.
        :type: str
        """
        self._server_subject_dn = server_subject_dn

    @property
    def server_issuer_dn(self):
        """
        Gets the server_issuer_dn of this X509ExternalCertInfo.


        :return: The server_issuer_dn of this X509ExternalCertInfo.
        :rtype: str
        :required/optional: optional
        """
        return self._server_issuer_dn

    @server_issuer_dn.setter
    def server_issuer_dn(self, server_issuer_dn):
        """
        Sets the server_issuer_dn of this X509ExternalCertInfo.


        :param server_issuer_dn: The server_issuer_dn of this X509ExternalCertInfo.
        :type: str
        """
        self._server_issuer_dn = server_issuer_dn

    @property
    def server_start(self):
        """
        Gets the server_start of this X509ExternalCertInfo.


        :return: The server_start of this X509ExternalCertInfo.
        :rtype: datetime
        :required/optional: optional
        """
        return self._server_start

    @server_start.setter
    def server_start(self, server_start):
        """
        Sets the server_start of this X509ExternalCertInfo.


        :param server_start: The server_start of this X509ExternalCertInfo.
        :type: datetime
        """
        self._server_start = server_start

    @property
    def server_expire(self):
        """
        Gets the server_expire of this X509ExternalCertInfo.


        :return: The server_expire of this X509ExternalCertInfo.
        :rtype: datetime
        :required/optional: optional
        """
        return self._server_expire

    @server_expire.setter
    def server_expire(self, server_expire):
        """
        Sets the server_expire of this X509ExternalCertInfo.


        :param server_expire: The server_expire of this X509ExternalCertInfo.
        :type: datetime
        """
        self._server_expire = server_expire

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

