#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author: Jialiang Shi
import requests
from sonarqube.utils.common import strip_trailing_slash
from sonarqube.cloud.users import SonarCloudUsers
from sonarqube.cloud.projects import SonarCloudProjects
from sonarqube.cloud.user_groups import SonarCloudUserGroups
from sonarqube.cloud.issues import SonarCloudIssues
from sonarqube.cloud.measures import SonarCloudMeasures
from sonarqube.cloud.notifications import SonarCloudNotifications
from sonarqube.cloud.project_links import SonarCloudProjectLinks
from sonarqube.cloud.permissions import SonarCloudPermissions
from sonarqube.cloud.ce import SonarCloudCe
from sonarqube.cloud.project_branches import SonarCloudProjectBranches
from sonarqube.cloud.qualitygates import SonarCloudQualityGates
from sonarqube.cloud.components import SonarCloudComponents
from sonarqube.cloud.rules import SonarCloudRules
from sonarqube.cloud.qualityprofiles import SonarCloudQualityProfiles
from sonarqube.cloud.duplications import SonarCloudDuplications
from sonarqube.cloud.metrics import SonarCloudMetrics
from sonarqube.cloud.settings import SonarCloudSettings
from sonarqube.cloud.sources import SonarCloudSources
from sonarqube.cloud.auth import SonarCloudAuth
from sonarqube.cloud.favorites import SonarCloudFavorites
from sonarqube.cloud.languages import SonarCloudLanguages
from sonarqube.cloud.project_badges import SonarCloudProjectBadges
from sonarqube.cloud.project_tags import SonarCloudProjectTags
from sonarqube.cloud.project_pull_requests import SonarCloudProjectPullRequests
from sonarqube.cloud.project_analyses import SonarCloudProjectAnalyses
from sonarqube.cloud.user_tokens import SonarCloudUserTokens
from sonarqube.cloud.webhooks import SonarCloudWebhooks
from sonarqube.cloud.webservices import SonarCloudWebservices


class SonarCloudClient:
    """
    A Python Client for SonarCloud Server APIs.
    """

    def __init__(self, sonarcloud_url, token):
        self.base_url = strip_trailing_slash(sonarcloud_url)
        _session = requests.Session()
        _session.auth = (token, '')
        self.session = _session

    @property
    def users(self):
        """
        SonarCloud users Operations

        :return:
        """
        return SonarCloudUsers(api=self)

    @property
    def user_groups(self):
        """
        SonarCloud user_groups Operations

        :return:
        """
        return SonarCloudUserGroups(api=self)

    @property
    def projects(self):
        """
        SonarCloud projects Operations

        :return:
        """
        return SonarCloudProjects(api=self)

    @property
    def measures(self):
        """
        SonarCloud measures Operations

        :return:
        """
        return SonarCloudMeasures(api=self)

    @property
    def issues(self):
        """
        SonarCloud issues Operations

        :return:
        """
        return SonarCloudIssues(api=self)

    @property
    def notifications(self):
        """
        SonarCloud notifications Operations

        :return:
        """
        return SonarCloudNotifications(api=self)

    @property
    def project_links(self):
        """
        SonarCloud project links Operations

        :return:
        """
        return SonarCloudProjectLinks(api=self)

    @property
    def permissions(self):
        """
        SonarCloud permissions Operations

        :return:
        """
        return SonarCloudPermissions(api=self)

    @property
    def ce(self):
        """
        SonarCloud ce Operations

        :return:
        """
        return SonarCloudCe(api=self)

    @property
    def project_branches(self):
        """
        SonarCloud project branches Operations

        :return:
        """
        return SonarCloudProjectBranches(api=self)

    @property
    def qualitygates(self):
        """
        SonarCloud quality gates Operations

        :return:
        """
        return SonarCloudQualityGates(api=self)

    @property
    def components(self):
        """
        SonarCloud components Operations

        :return:
        """
        return SonarCloudComponents(api=self)

    @property
    def rules(self):
        """
        SonarCloud rules Operations

        :return:
        """
        return SonarCloudRules(api=self)

    @property
    def qualityprofiles(self):
        """
        SonarCloud quality profiles Operations

        :return:
        """
        return SonarCloudQualityProfiles(api=self)

    @property
    def duplications(self):
        """
        SonarCloud duplications Operations

        :return:
        """
        return SonarCloudDuplications(api=self)

    @property
    def metrics(self):
        """
        SonarCloud metrics Operations

        :return:
        """
        return SonarCloudMetrics(api=self)

    @property
    def settings(self):
        """
        SonarCloud settings Operations

        :return:
        """
        return SonarCloudSettings(api=self)

    @property
    def sources(self):
        """
        SonarCloud sources Operations

        :return:
        """
        return SonarCloudSources(api=self)

    @property
    def auth(self):
        """
        SonarCloud authentication Operations

        :return:
        """
        return SonarCloudAuth(api=self)

    @property
    def favorites(self):
        """
        SonarCloud favorites Operations

        :return:
        """
        return SonarCloudFavorites(api=self)

    @property
    def languages(self):
        """
        SonarCloud languages Operations

        :return:
        """
        return SonarCloudLanguages(api=self)

    @property
    def project_badges(self):
        """
        SonarCloud project badges Operations

        :return:
        """
        return SonarCloudProjectBadges(api=self)

    @property
    def project_tags(self):
        """
        SonarCloud project tags Operations

        :return:
        """
        return SonarCloudProjectTags(api=self)

    @property
    def project_pull_requests(self):
        """
        SonarCloud project pull requests Operations

        :return:
        """
        return SonarCloudProjectPullRequests(api=self)

    @property
    def project_analyses(self):
        """
        SonarCloud project analyses Operations

        :return:
        """
        return SonarCloudProjectAnalyses(api=self)

    @property
    def user_tokens(self):
        """
        SonarCloud user tokens Operations

        :return:
        """
        return SonarCloudUserTokens(api=self)

    @property
    def webhooks(self):
        """
        SonarCloud webhooks Operations

        :return:
        """
        return SonarCloudWebhooks(api=self)

    @property
    def webservices(self):
        """
        SonarCloud webservices Operations

        :return:
        """
        return SonarCloudWebservices(api=self)

    @staticmethod
    def copy_dict(dest, src, option):
        """
        copy a dictionary to anther dictionary

        :param dest:
        :param src:
        :param option:
        :return:
        """
        for k, v in src.items():
            if k in option:
                if isinstance(v, dict):
                    for dict_k, dict_v in v.items():
                        dest['%s[%s]' % (k, dict_k)] = dict_v
                else:
                    dest[k] = v
