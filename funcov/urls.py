from django.conf.urls import patterns, url
from funcov import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        url(r'^editor/$', views.editor, name='editor'))
