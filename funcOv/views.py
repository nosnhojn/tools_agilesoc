from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm
from registration.forms import RegistrationForm
from django.core.urlresolvers import reverse


def index(request):
    if request.user.is_authenticated():
      context_dict = {
                       'title': request.user.username,
                       'h1': 'FunkOv',
                       'h2': 'Pick an interface to get started',
                       'h3': '',
                       'buttons' : {
                                     'AHB':reverse('index'),
                                     'APB':reverse('index'),
                                     'AXI4-Stream':reverse('index'),
                                   },
                     }

    else:
      context_dict = {
                       'title': 'FunkOv',
                       'h1': 'FunkOv',
                       'h2': 'Funktional Coverage Made Easy',
                       'h3': 'For design and verification engineers that care',
                       'buttons' : {
                                     'Register':'/accounts/register/',
                                     'Login':'/accounts/login/',
                                   },
                     }

    return render(request, 'funcOv/index.html', context_dict)
