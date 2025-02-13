#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author: Jialiang Shi
from sonarqube.utils.rest_client import RestClient
from sonarqube.utils.config import (
    API_WEBHOOKS_CREATE,
    API_WEBHOOKS_DELETE,
    API_WEBHOOKS_DELIVERIES,
    API_WEBHOOKS_DELIVERY,
    API_WEBHOOKS_LIST,
    API_WEBHOOKS_UPDATE,
)
from sonarqube.utils.common import GET, POST


class SonarQubeWebhooks(RestClient):
    """
    SonarQube webhooks Operations
    """

    def __init__(self, **kwargs):
        """

        :param kwargs:
        """
        super(SonarQubeWebhooks, self).__init__(**kwargs)

    @POST(API_WEBHOOKS_CREATE)
    def create_webhook(self, name, url, organization=None, project=None, secret=None):
        """
        SINCE 7.1
        Create a Webhook.

        :param name: Name displayed in the administration console of webhooks
        :param url: Server endpoint that will receive the webhook payload, for example 'http://my_server/foo'. If HTTP
          Basic authentication is used, HTTPS is recommended to avoid man in the middle attacks.
          Example: 'https://myLogin:myPassword@my_server/foo'
        :param organization: organization key.
        :param project: The key of the project that will own the webhook
        :param secret: If provided, secret will be used as the key to generate the HMAC hex (lowercase) digest value
          in the 'X-Sonar-Webhook-HMAC-SHA256' header
        :return: request response
        """

    @POST(API_WEBHOOKS_DELETE)
    def delete_webhook(self, webhook):
        """
        SINCE 7.1
        Delete a Webhook.

        :param webhook: The key of the webhook to be deleted, auto-generated value can be obtained through
          api/webhooks/create or api/webhooks/list
        :return:
        """

    @GET(API_WEBHOOKS_DELIVERIES)
    def get_webhook_deliveries(self, webhook=None, componentKey=None, ceTaskId=None, p=None, ps=None):
        """
        SINCE 6.2
        Get the recent deliveries for a specified project or Compute Engine task.

        :param webhook: Key of the webhook that triggered those deliveries
        :param componentKey: Key of the project
        :param ceTaskId: Id of the Compute Engine task
        :param p: page number.
        :param ps: Page size. Must be greater than 0 and less or equal than 500
        :return:
        """

    @GET(API_WEBHOOKS_DELIVERY)
    def get_webhook_delivery(self, deliveryId):
        """
        SINCE 6.2
        Get a webhook delivery by its id.

        :param deliveryId: Id of delivery
        :return:
        """

    @GET(API_WEBHOOKS_LIST)
    def search_webhooks(self, organization=None, project=None):
        """
        SINCE 7.1
        Search for global webhooks or project webhooks. Webhooks are ordered by name.

        :param organization: organization key.
        :param project: Project key
        :return:
        """

    @POST(API_WEBHOOKS_UPDATE)
    def update_webhook(self, webhook, name, url, secret=None):
        """
        SINCE 7.1
        Update a Webhook.

        :param webhook: The key of the webhook to be updated
        :param name: new name of the webhook
        :param url: new url to be called by the webhook
        :param secret: If provided, secret will be used as the key to generate the HMAC hex (lowercase) digest value
          in the 'X-Sonar-Webhook-HMAC-SHA256' header
        :return:
        """
