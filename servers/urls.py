from django.conf.urls import patterns, include, url

urlpatterns = patterns('servers.views',
  url(r'^$', 'index'),
  url(r'^servers/(?P<server_id>\d+)/$', 'detail'),
)
