from django.conf.urls import patterns, include, url
from django.contrib import admin


urlpatterns = patterns('',
    url(r'^math/', include('mathapp.urls', namespace='m')),
    url(r'^admin/', include(admin.site.urls)),
)
