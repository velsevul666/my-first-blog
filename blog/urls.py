"""blog URL Configuration
"""
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include('sublog.urls')),
    url(r'^auth/', include('loginsys.urls')),
]
