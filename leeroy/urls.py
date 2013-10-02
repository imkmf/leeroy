from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic.base import RedirectView
from servers import urls
admin.autodiscover()

urlpatterns = patterns('',
  url(r'^$', RedirectView.as_view(url='servers', permanent=False)),
  url(r'^servers/', include('servers.urls')),
  url(r'^admin/', include(admin.site.urls)),
)
