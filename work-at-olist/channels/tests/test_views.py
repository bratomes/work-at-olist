from django.urls import reverse
from django.conf import settings
from rest_framework.test import APITestCase
from rest_framework import status
from model_mommy import mommy


class ChannelListTest(APITestCase):
    def setUp(self):
        self.url = reverse('channel-list')
        self.channel = mommy.make('channels.Channel', name='Wallmart')

    def test_get_channels_list(self):
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, 200)
        self.assertTrue('Wallmart' in response.data[0]['name'])


class ChannelDetailTest(APITestCase):
    def setUp(self):
        self.url = reverse('channel-detail', kwargs={'slug': 'wallmart'})
        self.channel = mommy.make('channels.Channel', name='Wallmart')
        mommy.make('channels.Category', _quantity=15, channel=self.channel)

    def test_get_channel_detail(self):
        response = self.client.get(self.url)

        self.assertTrue(status.is_success(response.status_code))
        self.assertEqual(response.data[0]['name'], 'Wallmart')
        self.assertEqual(len(response.data[0]['categories']), 15)
