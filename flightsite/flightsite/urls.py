from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'flightsite.views.home', name='home'),
    # url(r'^flightsite/', include('flightsite.foo.urls')),
    url(r'^flights/', include('flights.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
                       
    # These views are used for the authentication
    url(r'^login/', 'flightsite.views.loginview'),
    url(r'^auth/', 'flightsite.views.auth_and_login'),
    url(r'^signup/', 'flightsite.views.sign_up_in'),
    url(r'^$', 'flightsite.views.secured'),
)
