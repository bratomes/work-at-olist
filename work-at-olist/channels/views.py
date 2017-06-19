from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Channel, Category
from .serializers import (
    ChannelSerializer, CategorySerializer, CategoryDetailSerializer
)


class ChannelList(APIView):
    """
    List all channels
    """
    def get(self, request, format=None):
        channels = Channel.objects.all()
        serializer = ChannelSerializer(channels, many=True)
        return Response(serializer.data)


class CategoryList(APIView):
    """
    List all categories filtered by a channel query parameter.
    If no channel parameter is provided will return 404.
    (e.g. /api/v1/categories/?channel=wallmart)
    """
    def get(self, request, format=None):
        channel = self.request.query_params.get('channel', None)

        if channel is None:
            return Response(status=status.HTTP_404_NOT_FOUND)

        categories = Category.objects.filter(channel__name=channel)
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)


class CategoryDetail(APIView):
    """
    Return a category instance of a channel, with its parent and subcategories.
    You must filter by a channel query parameter, otherwise will return 404.
    (e.g. /api/v1/categories/<pk>/?channel=wallmart)
    """
    def get_object(self, pk):
        try:
            return Category.objects.get(pk=pk)
        except Category.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):

        channel = self.request.query_params.get('channel', None)

        if channel is None:
            return Response(status=status.HTTP_404_NOT_FOUND)

        category = self.get_object(pk)
        serializer = CategoryDetailSerializer(category)
        return Response(serializer.data)
