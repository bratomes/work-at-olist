from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^silk/', include('silk.urls', namespace='silk')),
    url(r'^docs/', include('rest_framework_docs.urls')),
    url(r'^api/v1/', include('channels.urls.urls_v1'))
]
