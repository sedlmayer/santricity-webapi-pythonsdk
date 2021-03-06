# coding: utf-8

"""
LdapDomain.py

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


class LdapDomain(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        LdapDomain - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',  
            'bind_lookup_user': 'BindLookupUser',  
            'group_attributes': 'list[str]',  # (required parameter)
            'ldap_url': 'str',  # (required parameter)
            'names': 'list[str]',  # (required parameter)
            'role_map_collection': 'list[GroupMapping]',  
            'search_base': 'str',  
            'user_attribute': 'str'
        }

        self.attribute_map = {
            'id': 'id',  
            'bind_lookup_user': 'bindLookupUser',  
            'group_attributes': 'groupAttributes',  # (required parameter)
            'ldap_url': 'ldapUrl',  # (required parameter)
            'names': 'names',  # (required parameter)
            'role_map_collection': 'roleMapCollection',  
            'search_base': 'searchBase',  
            'user_attribute': 'userAttribute'
        }

        self._id = None
        self._bind_lookup_user = None
        self._group_attributes = None
        self._ldap_url = None
        self._names = None
        self._role_map_collection = None
        self._search_base = None
        self._user_attribute = None

    @property
    def id(self):
        """
        Gets the id of this LdapDomain.
        Unique ID linked to this domain

        :return: The id of this LdapDomain.
        :rtype: str
        :required/optional: optional
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this LdapDomain.
        Unique ID linked to this domain

        :param id: The id of this LdapDomain.
        :type: str
        """
        self._id = id

    @property
    def bind_lookup_user(self):
        """
        Gets the bind_lookup_user of this LdapDomain.
        If needed, you can configure a specific user to use when looking up the group membership for users. Typically, you would configure this whenever regular users might lack reader permissions to view their own group membership. The bind user information must be specified as a full DN.

        :return: The bind_lookup_user of this LdapDomain.
        :rtype: BindLookupUser
        :required/optional: optional
        """
        return self._bind_lookup_user

    @bind_lookup_user.setter
    def bind_lookup_user(self, bind_lookup_user):
        """
        Sets the bind_lookup_user of this LdapDomain.
        If needed, you can configure a specific user to use when looking up the group membership for users. Typically, you would configure this whenever regular users might lack reader permissions to view their own group membership. The bind user information must be specified as a full DN.

        :param bind_lookup_user: The bind_lookup_user of this LdapDomain.
        :type: BindLookupUser
        """
        self._bind_lookup_user = bind_lookup_user

    @property
    def group_attributes(self):
        """
        Gets the group_attributes of this LdapDomain.
        A list of group attributes on the user that will be searched to for group to role mapping

        :return: The group_attributes of this LdapDomain.
        :rtype: list[str]
        :required/optional: required
        """
        return self._group_attributes

    @group_attributes.setter
    def group_attributes(self, group_attributes):
        """
        Sets the group_attributes of this LdapDomain.
        A list of group attributes on the user that will be searched to for group to role mapping

        :param group_attributes: The group_attributes of this LdapDomain.
        :type: list[str]
        """
        self._group_attributes = group_attributes

    @property
    def ldap_url(self):
        """
        Gets the ldap_url of this LdapDomain.
        The LDAP URL entry must be specified as either ldap or ldaps protocol and contain the IP address. In addition, the port for the LDAP URL must be specified (typically 389 for ldap and 636 for ldaps).

        :return: The ldap_url of this LdapDomain.
        :rtype: str
        :required/optional: required
        """
        return self._ldap_url

    @ldap_url.setter
    def ldap_url(self, ldap_url):
        """
        Sets the ldap_url of this LdapDomain.
        The LDAP URL entry must be specified as either ldap or ldaps protocol and contain the IP address. In addition, the port for the LDAP URL must be specified (typically 389 for ldap and 636 for ldaps).

        :param ldap_url: The ldap_url of this LdapDomain.
        :type: str
        """
        self._ldap_url = ldap_url

    @property
    def names(self):
        """
        Gets the names of this LdapDomain.
        Each domain will have one ormultiple names and it is presumed the name will match the DNS domain for the LDAP server but it is not required. Domains can be named anything as long as they are valid DNS names.

        :return: The names of this LdapDomain.
        :rtype: list[str]
        :required/optional: required
        """
        return self._names

    @names.setter
    def names(self, names):
        """
        Sets the names of this LdapDomain.
        Each domain will have one ormultiple names and it is presumed the name will match the DNS domain for the LDAP server but it is not required. Domains can be named anything as long as they are valid DNS names.

        :param names: The names of this LdapDomain.
        :type: list[str]
        """
        self._names = names

    @property
    def role_map_collection(self):
        """
        Gets the role_map_collection of this LdapDomain.
        A list of regular expression patterns to match to the user's group attributes to match to roles. (TODO: NEED TO FIX FOR A MAPPING TYPE)

        :return: The role_map_collection of this LdapDomain.
        :rtype: list[GroupMapping]
        :required/optional: optional
        """
        return self._role_map_collection

    @role_map_collection.setter
    def role_map_collection(self, role_map_collection):
        """
        Sets the role_map_collection of this LdapDomain.
        A list of regular expression patterns to match to the user's group attributes to match to roles. (TODO: NEED TO FIX FOR A MAPPING TYPE)

        :param role_map_collection: The role_map_collection of this LdapDomain.
        :type: list[GroupMapping]
        """
        self._role_map_collection = role_map_collection

    @property
    def search_base(self):
        """
        Gets the search_base of this LdapDomain.
        The search base is used to find group memberships of the user. The search base is the DN in the directory of a container object of users. The filter base is used to find the user object within this container. After the user object is located, any associated group membership is identified.

        :return: The search_base of this LdapDomain.
        :rtype: str
        :required/optional: optional
        """
        return self._search_base

    @search_base.setter
    def search_base(self, search_base):
        """
        Sets the search_base of this LdapDomain.
        The search base is used to find group memberships of the user. The search base is the DN in the directory of a container object of users. The filter base is used to find the user object within this container. After the user object is located, any associated group membership is identified.

        :param search_base: The search_base of this LdapDomain.
        :type: str
        """
        self._search_base = search_base

    @property
    def user_attribute(self):
        """
        Gets the user_attribute of this LdapDomain.
        The user attribute is used match the username supplied to an object on the server

        :return: The user_attribute of this LdapDomain.
        :rtype: str
        :required/optional: optional
        """
        return self._user_attribute

    @user_attribute.setter
    def user_attribute(self, user_attribute):
        """
        Sets the user_attribute of this LdapDomain.
        The user attribute is used match the username supplied to an object on the server

        :param user_attribute: The user_attribute of this LdapDomain.
        :type: str
        """
        self._user_attribute = user_attribute

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

