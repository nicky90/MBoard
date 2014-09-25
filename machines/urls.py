from django.conf.urls import patterns, url

import machines

urlpatterns = patterns('',
    url('^$', 'machines.views.mainpage', name='mainpage'),
)
