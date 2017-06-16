from django.conf.urls import url

from .views import ChannelList

urlpatterns = [
    url(r'^channels/$', ChannelList.as_view(), name='channels-list'),
]
