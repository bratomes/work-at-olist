from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Channel, Category
from .serializers import ChannelSerializer, CategorySerializer


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
    List all categories filtered by a channel. If no channel filter is provided
    will return 404
    """
    def get(self, requeset, format=None):
        channel = self.request.query_params.get('channel', None)

        if channel is None:
            return Response(status=status.HTTP_404_NOT_FOUND)

        categories = Category.objects.filter(channel__name=channel)
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)
