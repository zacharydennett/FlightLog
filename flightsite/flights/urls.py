from django.conf.urls import patterns, url

from flights import views

urlpatterns = patterns('',
            url(r'^$', views.index, name='index'))
