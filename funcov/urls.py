from django.conf.urls import patterns, url
from funcov import views

urlpatterns = patterns('',
        url(r'^(?i)$', views.index, name='index'),
        url(r'^(?i)selector/$', views.selector, name='selector'),
        url(r'^(?i)editor/$', views.editor, name='editor'),
        url(r'^(?i)contact/$', views.contact, name='contact'),
        url(r'^(?i)about/$', views.about, name='about'))
