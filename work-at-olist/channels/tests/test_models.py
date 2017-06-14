from django.test import TestCase

from model_mommy import mommy


class ChannelTest(TestCase):
    """
    Class to test Channel model
    """

    def setUp(self):
        self.channel = mommy.make('channels.Channel')

    def test_channel_attributes(self):
        self.assertEqual(str(self.channel), self.channel.name)


class CategoryTest(TestCase):
    """
    Class to test Category model
    """

    def setUp(self):
        self.category = mommy.make('channels.Category')

    def test_category_attributes(self):
        self.assertEqual(str(self.category), self.category.name)
