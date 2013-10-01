from django.conf.urls import patterns, include, url
from servers import urls
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', include('servers.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
