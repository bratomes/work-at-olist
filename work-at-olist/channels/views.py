from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Channel, Category
from .serializers import (
    ChannelSerializer, ChannelDetailSerializer, CategoryDetailSerializer
)


class ChannelList(APIView):
    """
    List all channels
    """
    def get(self, request, format=None):
        channels = Channel.objects.all()
        serializer = ChannelSerializer(
            channels, context={'request': request}, many=True
        )
        return Response(serializer.data)


class ChannelDetail(APIView):
    """
    Return a channel detail with its name, categories and subcateries.
    """
    def get(self, request, slug, format=None):
        categories = Channel.objects.filter(slug=slug)
        serializer = ChannelDetailSerializer(
            categories, context={'request': request}, many=True
        )
        return Response(serializer.data)


class CategoryDetail(APIView):
    """
    Return a category instance, with its parent and subcategories.
    """
    def get_object(self, pk):
        try:
            return Category.objects.get(pk=pk)
        except Category.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        category = self.get_object(pk)
        serializer = CategoryDetailSerializer(
            category, context={'request': request}
        )
        return Response(serializer.data)
