from django.conf.urls import patterns, url

from flights import views

urlpatterns = patterns('',
            url(r'^$', views.index, name='index'),
            # ex: /flights/5/ shows detail of a specific flight
            url(r'^(?P<flight_id>\d+)/$', views.detail, name='detail'),
                       
            )
