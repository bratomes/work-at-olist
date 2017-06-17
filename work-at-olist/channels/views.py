from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics

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


class CategoryList(generics.ListAPIView):
    """
    List all categories filtered by a channel. If no channel filter is provided
    will return None
    """
    serializer_class = CategorySerializer

    def get_queryset(self):
        queryset = None
        channel = self.request.query_params.get('channel', None)
        if channel is not None:
            queryset = Category.objects.filter(channel__name=channel)

        return queryset
