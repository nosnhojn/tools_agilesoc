from django.conf.urls import patterns, url
from funcov import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        url(r'^selector/$', views.selector, name='selector'),
        url(r'^editor/$', views.editor, name='editor'))
