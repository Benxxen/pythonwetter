# -*- coding: iso-8859-15 -*-
from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'django1.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^weather/$', 'PythonWetter.views.get_weather_list', name='PythonWeather'),
)