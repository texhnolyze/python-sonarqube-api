#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author: Jialiang Shi
from sonarqube.utils.rest_client import RestClient
from sonarqube.utils.config import (
    API_WEBHOOKS_CREATE_ENDPOINT,
    API_WEBHOOKS_DELETE_ENDPOINT,
    API_WEBHOOKS_DELIVERIES_ENDPOINT,
    API_WEBHOOKS_DELIVERY_ENDPOINT,
    API_WEBHOOKS_LIST_ENDPOINT,
    API_WEBHOOKS_UPDATE_ENDPOINT
)


class SonarCloudWebhooks(RestClient):
    """
    SonarCloud webhooks Operations
    """
    def __init__(self, **kwargs):
        """

        :param kwargs:
        """
        super(SonarCloudWebhooks, self).__init__(**kwargs)

    def create_webhook(self, name, organization, project=None, secret=None, url=None):
        """
        Create a Webhook.

        :param name: Name displayed in the administration console of webhooks
        :param organization: organization key.
        :param project: The key of the project that will own the webhook
        :param secret: If provided, secret will be used as the key to generate the HMAC hex (lowercase) digest value
          in the 'X-Sonar-Webhook-HMAC-SHA256' header
        :param url: Server endpoint that will receive the webhook payload, for example 'http://my_server/foo'. If HTTP
          Basic authentication is used, HTTPS is recommended to avoid man in the middle attacks.
          Example: 'https://myLogin:myPassword@my_server/foo'
        :return: request response
        """
        params = {
            'name': name,
            'organization': organization
        }

        if project:
            params.update({'project': project})

        if secret:
            params.update({'secret': secret})

        if url:
            params.update({'url': url})

        return self.post(API_WEBHOOKS_CREATE_ENDPOINT, params=params)

    def delete_webhook(self, webhook_key):
        """
        Delete a Webhook.

        :param webhook_key: The key of the webhook to be deleted, auto-generated value can be obtained through
          api/webhooks/create or api/webhooks/list
        :return:
        """
        params = {
            'webhook': webhook_key,
        }

        self.post(API_WEBHOOKS_DELETE_ENDPOINT, params=params)

    def get_webhook_deliveries(self, webhook_key=None, component_key=None, task_id=None):
        """
        Get the recent deliveries for a specified project or Compute Engine task.

        :param webhook_key: Key of the webhook that triggered those deliveries
        :param component_key: Key of the project
        :param task_id: Id of the Compute Engine task
        :return:
        """
        params = {}

        if webhook_key:
            params.update({'webhook': webhook_key})

        if component_key:
            params.update({'componentKey': component_key})

        if task_id:
            params.update({'ceTaskId': task_id})

        page_num = 1
        page_size = 1
        total = 2

        while page_num * page_size < total:
            resp = self.get(API_WEBHOOKS_DELIVERIES_ENDPOINT, params=params)
            response = resp.json()

            page_num = response['paging']['pageIndex']
            page_size = response['paging']['pageSize']
            total = response['paging']['total']

            params['p'] = page_num + 1

            for delivery in response['deliveries']:
                yield delivery

    def get_webhook_delivery(self, delivery_id):
        """
        Get a webhook delivery by its id.

        :param delivery_id: Id of delivery
        :return:
        """
        params = {'deliveryId': delivery_id}

        resp = self.get(API_WEBHOOKS_DELIVERY_ENDPOINT, params=params)
        response = resp.json()
        return response['delivery']

    def search_webhooks(self, organization, project=None):
        """
        Search for global webhooks or project webhooks. Webhooks are ordered by name.

        :param organization: organization key.
        :param project: Project key
        :return:
        """
        params = {'organization': organization}
        if project:
            params.update({'project': project})

        resp = self.get(API_WEBHOOKS_LIST_ENDPOINT, params=params)
        response = resp.json()
        return response['webhooks']

    def update_webhook(self, webhook_key, new_name, new_url, secret=None):
        """
        Update a Webhook.

        :param webhook_key: The key of the webhook to be updated
        :param new_name: new name of the webhook
        :param new_url: new url to be called by the webhook
        :param secret: If provided, secret will be used as the key to generate the HMAC hex (lowercase) digest value
          in the 'X-Sonar-Webhook-HMAC-SHA256' header
        :return:
        """
        params = {
            'webhook': webhook_key,
            'name': new_name,
            'url': new_url
        }

        if secret:
            params.update({'secret': secret})

        self.post(API_WEBHOOKS_UPDATE_ENDPOINT, params=params)
