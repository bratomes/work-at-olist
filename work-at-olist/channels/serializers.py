from django.conf import settings
from rest_framework import serializers
from hashid_field.rest import HashidSerializerCharField

from .models import Channel, Category


class ChannelSerializer(serializers.HyperlinkedModelSerializer):
    # id = HashidSerializerCharField(source_field='channels.Channel.id')

    class Meta:
        model = Channel
        fields = ('name',)


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ('url', 'name')


class CategoryDetailSerializer(serializers.HyperlinkedModelSerializer):
    parent = CategorySerializer(read_only=True)
    subcategories = CategorySerializer(read_only=True, many=True)

    class Meta:
        model = Category
        fields = ('name', 'parent', 'subcategories')
