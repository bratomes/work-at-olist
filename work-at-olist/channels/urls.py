from django.conf.urls import url

from .views import ChannelList, CategoryList

urlpatterns = [
    url(r'^channels/$', ChannelList.as_view(), name='channels-list'),
    url(r'^categories/$', CategoryList.as_view(), name='categories-list'),
]
