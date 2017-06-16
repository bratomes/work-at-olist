from django.urls import reverse
from rest_framework.test import APITestCase
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
