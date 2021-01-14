#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author: Jialiang Shi
from sonarqube.utils.rest_client import RestClient
from sonarqube.utils.config import (
    API_WEBSERVICES_LIST_ENDPOINT,
    API_WEBSERVICES_RESPONSE_EXAMPLE_ENDPOINT
)


class SonarQubeWebservices(RestClient):
    """
    SonarQube webservices Operations
    """
    def __init__(self, **kwargs):
        """

        :param kwargs:
        """
        super(SonarQubeWebservices, self).__init__(**kwargs)

    def list_web_services(self, include_internals=False):
        """
        List web services

        :param include_internals: Include web services that are implemented for internal use only.
          Their forward-compatibility is not assured. Possible values are for: True or False. default value is False.
        :return:
        """
        params = {
            'include_internals': include_internals and 'true' or 'false'
        }

        resp = self.get(API_WEBSERVICES_LIST_ENDPOINT, params=params)
        response = resp.json()
        return response['webServices']

    def web_service_response_example(self, action, controller):
        """
        Display web service response example

        :param action: Action of the web service
        :param controller: Controller of the web service
        :return:
        """
        params = {
            'action': action,
            'controller': controller
        }

        return self.post(API_WEBSERVICES_RESPONSE_EXAMPLE_ENDPOINT, params=params)
