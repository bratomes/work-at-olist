from rest_framework import serializers
from hashid_field.rest import HashidSerializerCharField

from .models import Channel, Category


class ChannelSerializer(serializers.ModelSerializer):
    id = HashidSerializerCharField(source_field='channels.Channel.id')

    class Meta:
        model = Channel
        fields = '__all__'
