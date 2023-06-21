#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author: Jialiang Shi
from sonarqube.utils.rest_client import RestClient
from sonarqube.utils.config import (
    API_QUALITYGATES_LIST,
    API_QUALITYGATES_PROJECT_STATUS,
    API_QUALITYGATES_SELECT,
    API_QUALITYGATES_DESELECT,
    API_QUALITYGATES_SHOW,
    API_QUALITYGATES_GET_BY_PROJECT,
    API_QUALITYGATES_COPY,
    API_QUALITYGATES_CREATE,
    API_QUALITYGATES_DESTROY,
    API_QUALITYGATES_RENAME,
    API_QUALITYGATES_CREATE_CONDITION,
    API_QUALITYGATES_DELETE_CONDITION,
    API_QUALITYGATES_UPDATE_CONDITION,
    API_QUALITYGATES_SEARCH,
    API_QUALITYGATES_SET_AS_DEFAULT,
    API_QUALITYGATES_ADD_USER,
    API_QUALITYGATES_ADD_GROUP,
)
from sonarqube.utils.common import GET, POST


class SonarQubeQualityGates(RestClient):
    """
    SonarQube quality gates Operations
    """

    def __init__(self, **kwargs):
        """

        :param kwargs:
        """
        super(SonarQubeQualityGates, self).__init__(**kwargs)

    @POST(API_QUALITYGATES_ADD_USER)
    def add_user_to_gate(self, gateName, login):
        """
        SINCE 9.2
        Allow a user to edit a Quality Gate.

        :param gateName: The name of the quality gate
        :param login: User login
        :return:
        """

    @POST(API_QUALITYGATES_ADD_GROUP)
    def add_group_to_gate(self, gateName, groupName):
        """
        SINCE 9.2
        Allow a group of users to edit a Quality Gate.

        :param gateName: The name of the quality gate
        :param groupName: The name of the group that can administer the gate
        :return:
        """

    @POST(API_QUALITYGATES_COPY)
    def copy_quality_gate(self, id, name, organization=None):
        """
        SINCE 4.3
        Copy a Quality Gate.

        :param id: The ID of the source quality gate
        :param name: The name of the quality gate to create
        :param organization: Organization key. If no organization is provided, the default organization is used.
        :return:
        """

    @POST(API_QUALITYGATES_CREATE)
    def create_quality_gate(self, name, organization=None):
        """
        SINCE 4.3
        Create a Quality Gate.

        :param name: The name of the quality gate to create
        :param organization: Organization key. If no organization is provided, the default organization is used.
        :return: request response
        """

    @POST(API_QUALITYGATES_DESTROY)
    def delete_quality_gate(self, id, organization=None):
        """
        SINCE 4.3
        Delete a Quality Gate.

        :param id: ID of the quality gate to delete
        :param organization: Organization key. If no organization is provided, the default organization is used.
        :return:
        """

    @POST(API_QUALITYGATES_RENAME)
    def rename_quality_gate(self, id, name, organization=None):
        """
        SINCE 4.3
        Rename a Quality Gate.

        :param id: ID of the quality gate to rename
        :param name: New name of the quality gate
        :param organization: Organization key. If no organization is provided, the default organization is used.
        :return:
        """

    @POST(API_QUALITYGATES_CREATE_CONDITION)
    def create_condition_to_quality_gate(self, gateId, metric, error, op=None, organization=None):
        """
        SINCE 4.3
        Add a new condition to a quality gate.

        :param gateId: ID of the quality gate
        :param metric: Condition metric.
          Only metric of the following types are allowed:
            * INT
            * MILLISEC
            * RATING
            * WORK_DUR
            * FLOAT
            * PERCENT
            * LEVEL
        :param error: Condition error threshold
        :param op: Condition operator
          Possible values are for:
            * LT = is lower than
            * GT = is greater than
        :param organization: Organization key. If no organization is provided, the default organization is used.
        :return: request response
        """

    @POST(API_QUALITYGATES_DELETE_CONDITION)
    def delete_condition_from_quality_gate(self, id, organization=None):
        """
        SINCE 4.3
        Delete a condition from a quality gate.

        :param id: Condition ID
        :param organization: Organization key. If no organization is provided, the default organization is used.
        :return:
        """

    @POST(API_QUALITYGATES_UPDATE_CONDITION)
    def update_condition_to_quality_gate(self, id, metric, error, op=None, organization=None):
        """
        SINCE 4.3
        Update a condition attached to a quality gate.

        :param id: Condition ID
        :param metric: Condition metric.
          Only metric of the following types are allowed:
            * INT
            * MILLISEC
            * RATING
            * WORK_DUR
            * FLOAT
            * PERCENT
            * LEVEL
        :param error: Condition error threshold
        :param op: Condition operator
          Possible values are for:
            * LT = is lower than
            * GT = is greater than
        :param organization: Organization key. If no organization is provided, the default organization is used.
        :return:
        """

    @GET(API_QUALITYGATES_SEARCH)
    def get_qualitygate_projects(self, gateId, selected="selected", query=None, organization=None, page=None, pageSize=None):
        """
        SINCE 4.3
        Search for projects associated (or not) to a quality gate.

        :param gateId: Quality Gate ID
        :param selected: Depending on the value, show only selected items (selected=selected),
          deselected items (selected=deselected), or all items with their selection status (selected=all).
          Possible values are for:
            * all
            * deselected
            * selected
          default value is selected
        :param query: To search for projects containing this string.
          If this parameter is set, "selected" is set to "all".
        :param organization: Organization key. If no organization is provided, the default organization is used.
        :param page: page number.
        :param pageSize: Page size.
        :return:
        """

    @POST(API_QUALITYGATES_SET_AS_DEFAULT)
    def set_default_qualitygate(self, id, organization=None):
        """
        SINCE 4.3
        Set a quality gate as the default quality gate.

        :param id: ID of the quality gate to set as default
        :param organization: Organization key. If no organization is provided, the default organization is used.
        :return:
        """

    @GET(API_QUALITYGATES_PROJECT_STATUS)
    def get_project_qualitygates_status(self, projectKey=None, analysisId=None, branch=None, pullRequest=None):
        """
        SINCE 5.3
        Get the quality gate status of a project or a Compute Engine task. return 'ok','WARN','ERROR'
        The NONE status is returned when there is no quality gate associated with the analysis.
        Returns an HTTP code 404 if the analysis associated with the task is not found or does not exist.

        :param projectKey: Project key
        :param analysisId: Analysis id
        :param branch: Branch key
        :param pullRequest:
        :return:
        """

    @GET(API_QUALITYGATES_LIST)
    def get_quality_gates(self, organization=None):
        """
        SINCE 4.3
        Get a list of quality gates

        :param organization: Organization key. If no organization is provided, the default organization is used.
        :return:
        """

    @POST(API_QUALITYGATES_SELECT)
    def select_quality_gate_for_project(self, projectKey, gateName, organization=None):
        """
        SINCE 4.3
        Associate a project to a quality gate.

        :param projectKey: Project key
        :param gateName: Quality gate name (since version 8.4). Refer https://sonarqube.inria.fr/sonarqube/web_api/api/qualitygates
        :param organization: Organization key. If no organization is provided, the default organization is used.
        :return:
        """

    @POST(API_QUALITYGATES_DESELECT)
    def remove_project_from_quality_gate(self, projectKey, organization=None):
        """
        SINCE 4.3
        Remove the association of a project from a quality gate.

        :param projectKey: Project key
        :param organization: Organization key. If no organization is provided, the default organization is used.
        :return:
        """

    @GET(API_QUALITYGATES_SHOW)
    def show_quality_gate(self, name, organization=None):
        """
        SINCE 4.3
        Display the details of a quality gate.

        :param name: Name of the quality gate.
        :param organization: Organization key. If no organization is provided, the default organization is used.
        :return:
        """

    @GET(API_QUALITYGATES_GET_BY_PROJECT)
    def get_quality_gate_of_project(self, project, organization=None):
        """
        SINCE 6.1
        Get the quality gate of a project.

        :param project: Project key
        :param organization: Organization key. If no organization is provided, the default organization is used.
        :return:
        """
