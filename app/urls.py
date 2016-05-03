from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^', include('front.urls')),
    url(r'^api/v1/', include('apiv1.urls')),
    url(r'^admin/', admin.site.urls),
]
