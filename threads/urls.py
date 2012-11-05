from django.conf.urls import patterns, include, url

urlpatterns = patterns('threads.views',
    url(r'^$', 'index'),
    url(r'^new/$', 'new'),
    url(r'^(?P<id>\d+)/$', 'show')
)