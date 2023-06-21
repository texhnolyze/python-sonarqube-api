#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author: Jialiang Shi
from sonarqube.utils.rest_client import RestClient
from sonarqube.utils.config import API_MONITORING_METRICS
from sonarqube.utils.common import GET


class SonarQubeMonitoring(RestClient):
    """
    SonarQube monitoring Operations
    """

    def __init__(self, **kwargs):
        """

        :param kwargs:
        """
        super(SonarQubeMonitoring, self).__init__(**kwargs)

    @GET(API_MONITORING_METRICS)
    def get_monitoring_metrics(self):
        """
        SINCE 9.3
        Return monitoring metrics in Prometheus format. Support content type 'text/plain' (default) and
        'application/openmetrics-text'. this endpoint can be access using a Bearer token, that needs to
        be defined in sonar.properties with the 'sonar.web.systemPasscode' key.

        :return:
        """
