from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Channel
from .serializers import ChannelSerializer


class ChannelList(APIView):
    """
    List all channels
    """
    def get(self, request, format=None):
        channels = Channel.objects.all()
        serializer = ChannelSerializer(channels, many=True)
        return Response(serializer.data)
