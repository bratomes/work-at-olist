from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status

from channels.models import Category


class ChannelListTest(APITestCase):
    fixtures = ['channels.json']

    def setUp(self):
        self.url = reverse('channel-list')

    def test_get_channels_list(self):
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data[0]['name'], 'Wallmart')


class ChannelDetailTest(APITestCase):
    fixtures = ['channels.json']

    def setUp(self):
        self.url = reverse('channel-detail', kwargs={'slug': 'wallmart'})

    def test_get_channel_detail(self):
        response = self.client.get(self.url)

        self.assertTrue(status.is_success(response.status_code))
        self.assertEqual(response.data[0]['name'], 'Wallmart')
        self.assertEqual(len(response.data[0]['categories']), 23)


class CategoryDetailTest(APITestCase):
    fixtures = ['channels.json']

    def test_get_category_by_hashid(self):
        category = Category.objects.all()[2]
        url = reverse('category-detail', kwargs={'pk': category.pk})
        response = self.client.get(url)

        self.assertTrue(status.is_success(response.status_code))

    def test_get_category_by_id(self):
        url = reverse('category-detail', kwargs={'pk': 3})
        response = self.client.get(url)

        self.assertTrue(status.is_client_error(response.status_code))
