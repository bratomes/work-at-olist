from django.conf import settings
from rest_framework import serializers
from hashid_field.rest import HashidSerializerCharField

from .models import Channel, Category


class ChannelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Channel
        fields = ('name', 'url')
        extra_kwargs = {
            'url': {'lookup_field': 'slug'}
        }


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ('url', 'name')


class ChannelDetailSerializer(serializers.HyperlinkedModelSerializer):
    categories = CategorySerializer(read_only=True, many=True)

    class Meta:
        model = Channel
        fields = ('name', 'categories')


class CategoryDetailSerializer(serializers.HyperlinkedModelSerializer):
    parent = CategorySerializer(read_only=True)
    subcategories = CategorySerializer(read_only=True, many=True)

    class Meta:
        model = Category
        fields = ('name', 'parent', 'subcategories')
