from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^$', 'frontend.views.home', name='home'),
    url(r'^map/', 'frontend.views.map', name='map'),
    url(r'^create/', 'frontend.views.create', name='create'),
    url(r'^info/', 'frontend.views.info', name='info'),
)
