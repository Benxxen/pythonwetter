# -*- coding: iso-8859-15 -*-
from django.conf.urls import patterns, include, url
from django.contrib import admin
from rest_framework import routers
from views import WeatherViewSet

admin.autodiscover()

router = routers.DefaultRouter()
router.register(r'weathers', WeatherViewSet)


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'django1.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^weather/$', 'pythonwetter.views.get_weather_list', name='PythonWeather'),
    url(r'^accounts/', include('allauth.urls')),
)