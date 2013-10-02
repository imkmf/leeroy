from django.conf.urls import patterns, include, url

urlpatterns = patterns('servers.views',
    url(r'^$', 'index'),
    url(r'^(?P<server_id>\d+)/$', 'detail'),
    url(r'^(?P<server_id>\d+)/(?P<build>\w+)/', 'job_detail'),
)
