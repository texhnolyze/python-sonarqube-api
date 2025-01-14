#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author: Jialiang Shi
from sonarqube.utils.rest_client import RestClient
from sonarqube.utils.config import (
    API_USER_GROUPS_SEARCH,
    API_USER_GROUPS_CREATE,
    API_USER_GROUPS_DELETE,
    API_USER_GROUPS_UPDATE,
    API_USER_GROUPS_USERS,
    API_USER_GROUPS_ADD_USER,
    API_USER_GROUPS_REMOVE_USER,
)
from sonarqube.utils.common import GET, POST


class SonarQubeUserGroups(RestClient):
    """
    SonarQube user_groups Operations
    """

    def __init__(self, **kwargs):
        """

        :param kwargs:
        """
        super(SonarQubeUserGroups, self).__init__(**kwargs)

    def get(self, name):
        result = self.search_user_groups(q=name)
        groups = result.get("groups", [])

        for group in groups:
            if group["name"] == name:
                return group

    @GET(API_USER_GROUPS_SEARCH)
    def search_user_groups(self, organization=None, f=None, managed=None, q=None, p=None, ps=None):
        """
        SINCE 5.2
        Search for user groups.

        :param organization: organization key.
        :param f: Comma-separated list of the fields to be returned in response.
          All the fields are returned by default. Possible values are for:
            * name
            * description
            * membersCount
        :param managed: Return managed or non-managed groups.
          Only available for managed instances, throws for non-managed instances. (since 10.0)
        :param p: page number.
        :param ps: Page size. Must be greater than 0 and less or equal than 500
        :param q: Limit search to names that contain the supplied string.
        :return:
        """

    @POST(API_USER_GROUPS_CREATE)
    def create_group(self, name, organization=None, description=None):
        """
        SINCE 5.2
        Create a group.

        :param name: Name for the new group. A group name cannot be larger than 255 characters and must be unique.
          The value 'anyone' (whatever the case) is reserved and cannot be used.
        :param organization: organization key.
        :param description: Description for the new group. A group description cannot be larger than 200 characters.
        :return: request response
        """

    @POST(API_USER_GROUPS_DELETE)
    def delete_group(self, name, organization=None):
        """
        SINCE 5.2
        Delete a group. The default groups cannot be deleted.

        :param name: group name
        :param organization: organization key.
        :return:
        """

    @POST(API_USER_GROUPS_UPDATE)
    def update_group(self, currentName, name=None, description=None):
        """
        SINCE 5.2
        Update a group.

        :param currentName: Name of the group to be updated. (since 8.5)
        :param name: New optional name for the group. A group name cannot be larger than 255 characters and must
          be unique. Value 'anyone' (whatever the case) is reserved and cannot be used. If value is empty or not
          defined, then name is not changed.
        :param description: New optional description for the group. A group description cannot be larger than
          200 characters. If value is not defined, then description is not changed.
        :return:
        """

    @POST(API_USER_GROUPS_ADD_USER)
    def add_user_to_group(self, name, login, organization=None):
        """
        SINCE 5.2
        Add a user to a group.

        :param name: Group name
        :param organization: organization key.
        :param login: User login
        :return:
        """

    @POST(API_USER_GROUPS_REMOVE_USER)
    def remove_user_from_group(self, name, login, organization=None):
        """
        SINCE 5.2
        Remove a user from a group.

        :param name: Group name
        :param login: User login
        :param organization: organization key.
        :return:
        """

    @GET(API_USER_GROUPS_USERS)
    def search_users_belong_to_group(self, name, organization=None, q=None, selected="selected", p=None, ps=None):
        """
        SINCE 5.2
        Search for users with membership information with respect to a group.

        :param name: Group name
        :param organization: organization key.
        :param q: Limit search to names or logins that contain the supplied string.
        :param selected: Depending on the value, show only selected items (selected=selected), deselected items
          (selected=deselected), or all items with their selection status (selected=all).Possible values are for:
            * all
            * deselected
            * selected
          default value is selected.
        :param p: page number.
        :param ps: Page size. Must be greater than 0 and less or equal than 500
        :return:
        """
