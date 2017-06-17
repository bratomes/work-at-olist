from django.conf import settings
from rest_framework import serializers
from hashid_field.rest import HashidSerializerCharField

from .models import Channel, Category


class ChannelSerializer(serializers.ModelSerializer):
    id = HashidSerializerCharField(source_field='channels.Channel.id')

    class Meta:
        model = Channel
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    id = HashidSerializerCharField(source_field='channels.Category.id')

    class Meta:
        model = Category
        fields = ('id', 'name')


class CategoryDetailSerializer(serializers.ModelSerializer):
    parent = HashidSerializerCharField(source_field='channels.Category.id')
    subcategories = CategorySerializer(read_only=True, many=True)

    class Meta:
        model = Category
        fields = ('name', 'parent', 'subcategories')
