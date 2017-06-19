from django.conf.urls import url

from channels.views import ChannelList, CategoryList, CategoryDetail

urlpatterns = [
    url(r'^channels/$', ChannelList.as_view(), name='channels-list'),
    url(r'^categories/$', CategoryList.as_view(), name='categories-list'),
    url(r'^categories/(?P<pk>[0-9A-Za-z]+)/$', CategoryDetail.as_view(),
        name='category-detail'
    ),
]
