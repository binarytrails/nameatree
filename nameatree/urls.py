from django.conf.urls import include, url

from frontend.views import home, map, create, info

urlpatterns = [
    url(r'^$',          home,       name='home'),
    url(r'^map/',       map,        name='map'),
    url(r'^create/',    create,     name='create'),
    url(r'^info/',      info,       name='info')
]
