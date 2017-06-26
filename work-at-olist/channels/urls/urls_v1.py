from django.conf.urls import url

from channels.views import ChannelList, ChannelDetail, CategoryDetail

urlpatterns = [
    url(r'^channels/$', ChannelList.as_view(), name='channel-list'),
    url(r'^channels/(?P<slug>[A-Za-z\-_]+)/$',
        ChannelDetail.as_view(), name='channel-detail'),
    url(r'^categories/(?P<pk>[0-9A-Za-z]+)/$',
        CategoryDetail.as_view(), name='category-detail'),
]
