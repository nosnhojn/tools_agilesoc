"""tools_agilesoc URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin


from registration.backends.simple.views import RegistrationView

# Create a new class that redirects the user to the index page, if successful at logging
class MyRegistrationView(RegistrationView):
    def get_success_url(self,request, user):
        return '/funcov/'

from django.views.generic import View
from django.http import HttpResponseRedirect
class defaultIndexView(View):
    def get(self, request):
        return HttpResponseRedirect('/funcov/')

import re
re_funcov = re.compile(r'^funcov/', re.I)

urlpatterns = [
    url(r'^$', defaultIndexView.as_view(), name='default_index'),
    url(r'^(?i)admin/', include(admin.site.urls)),
    url(r'^(?i)funcov/', include('funcov.urls')),
    url(r'^(?i)accounts/register/$', MyRegistrationView.as_view(), name='registration_register'),
    url(r'^(?i)accounts/logout/$', 'django.contrib.auth.views.logout', {'next_page': 'index'}),
    url(r'^(?i)accounts/', include('registration.backends.simple.urls')),
]
