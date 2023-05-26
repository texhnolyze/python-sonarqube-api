#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author: Jialiang Shi
from sonarqube.utils.rest_client import RestClient
from sonarqube.utils.config import (
    API_COMPONTENTS_SHOW_ENDPOINT,
    API_COMPONTENTS_SEARCH_ENDPOINT,
    API_COMPONTENTS_TREE_ENDPOINT,
)
from sonarqube.utils.common import GET


class SonarQubeComponents(RestClient):
    """
    SonarQube components Operations
    """

    def __init__(self, **kwargs):
        """

        :param kwargs:
        """
        super(SonarQubeComponents, self).__init__(**kwargs)

    @GET(API_COMPONTENTS_SHOW_ENDPOINT)
    def get_project_component_and_ancestors(
        self, component, branch=None, pullRequest=None
    ):
        """
        SINCE 5.4
        Returns a component (file, directory, project, view…) and its ancestors. The ancestors are ordered from the
        parent to the root project.

        :param component: Component key
        :param branch: Branch key.
        :param pullRequest: Pull request id
        :return:
        """

    @GET(API_COMPONTENTS_SEARCH_ENDPOINT)
    def search_components(self, qualifiers, organization=None, language=None, q=None, p=None, ps=None):
        """
        SINCE 6.3
        Search for components

        :param qualifiers: Comma-separated list of component qualifiers. Filter the results with
          the specified qualifiers. Possible values are:

          * BRC - Sub-projects
          * DIR - Directories
          * FIL - Files
          * TRK - Projects
          * UTS - Test Files
        :param organization: Organization key
        :param language: Language key. If provided, only components for the given language are returned.
        :param q: Limit search to:

          * component names that contain the supplied string
          * component keys that are exactly the same as the supplied string
        :param p: page number.
        :param ps: Page size. Must be greater than 0 and less or equal than 500

        :return:
        """

    @GET(API_COMPONTENTS_TREE_ENDPOINT)
    def get_components_tree(
        self,
        component,
        branch=None,
        pullRequest=None,
        asc="true",
        p=None,
        ps=None,
        q=None,
        qualifiers=None,
        s="name",
        strategy="all",
    ):
        """
        SINCE 5.4
        Navigate through components based on the chosen strategy.
        When limiting search with the q parameter, directories are not returned.

        :param component: Base component key. The search is based on this component.
        :param asc: Ascending sort. default value is true.
        :param p: page number.
        :param ps: Page size. Must be greater than 0 and less or equal than 500
        :param branch: Branch key.
        :param pullRequest: Pull request id.
        :param q: Limit search to:

            * component names that contain the supplied string
            * component keys that are exactly the same as the supplied string

        :param qualifiers:Comma-separated list of component qualifiers. Filter the results with
            the specified qualifiers. Possible values are:

              * BRC - Sub-projects
              * DIR - Directories
              * FIL - Files
              * TRK - Projects
              * UTS - Test Files

        :param s: Comma-separated list of sort fields,Possible values are for: name, path, qualifier,
            and default value is name
        :param strategy: Strategy to search for base component descendants:

            * children: return the children components of the base component. Grandchildren components are not returned
            * all: return all the descendants components of the base component. Grandchildren are returned.
            * leaves: return all the descendant components (files, in general) which don't have other children.
              They are the leaves of the component tree.

            default value is all.

        :return:
        """
