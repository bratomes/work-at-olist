from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from model_mommy import mommy


class ChannelListTest(APITestCase):
    def setUp(self):
        self.url = reverse('channels-list')
        self.channel = mommy.make(
            'channels.Channel', id='AXNnvXd', name='Wallmart'
        )

    def test_get_channels_list(self):
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.data[0], {'id': 'AXNnvXd', 'name': 'Wallmart'}
        )


class CategoryListTest(APITestCase):
    def setUp(self):
        self.channel = mommy.make(
            'channels.Channel', id='AXNnvXd', name='wallmart'
        )
        self.url_filtered = '{}?channel={}'.format(
            reverse('categories-list'), self.channel.name
        )
        self.url_not_filtered = reverse('categories-list')
        mommy.make('channels.Category', _quantity=5, channel=self.channel)

    def test_get_categories_list_not_filtered(self):
        response = self.client.get(self.url_not_filtered)

        self.assertTrue(status.is_client_error(response.status_code))

    def test_get_categories_list_filtered(self):
        response = self.client.get(self.url_filtered)

        self.assertTrue(status.is_success(response.status_code))
        self.assertEqual(len(response.data), 5)
