from django.test import TestCase

from channels.models import Channel, Category


class ChannelTest(TestCase):
    """
    Class to test Channel model
    """
    def setUp(self):
        self.channel = Channel.objects.create(name='Wallmart')

    def test_channel_attributes(self):
        self.assertEqual(str(self.channel), self.channel.name)


class CategoryTest(TestCase):
    """
    Class to test Category model
    """
    def setUp(self):
        self.channel = Channel.objects.create(name='Wallmart')
        self.category = Category.objects.create(
            name='Books', channel=self.channel)

    def test_category_attributes(self):
        self.assertEqual(str(self.category), self.category.name)
