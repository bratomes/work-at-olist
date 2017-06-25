from django.conf.urls import url

from channels.views import ChannelList, CategoryList, CategoryDetail

urlpatterns = [
    url(r'^channels/$', ChannelList.as_view(), name='channels-list'),
    url(r'^channels/(?P<channel_slug>[A-Za-z\-_]+)/categories/$',
        CategoryList.as_view(), name='category-list'),
    url(r'^categories/(?P<pk>[0-9A-Za-z]+)/$',
        CategoryDetail.as_view(), name='category-detail'),
]
