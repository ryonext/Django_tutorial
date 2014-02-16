from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('polls.views',
        (r'^$', 'index'),
        (r'^(?P<poll_id>\d+)/$', 'detail'),
        (r'^(?P<poll_id>\d+)/results/$', 'results'),
        (r'^(?P<poll_id>\d+)/vote/$', 'vote'),
    url(r'^admin/', include(admin.site.urls)),
)
