from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from registration.forms import RegistrationForm
from django.core.urlresolvers import reverse


def index(request):
    context = {}
    if request.user.is_authenticated():
      context = {
                  'title': request.user.username,
                  'h1': 'FunkOv',
                  'h2': 'Pick an interface to get started',
                  'h3': '',
                  'buttons' : {
                                'AHB': {
                                         'type' : 'ahb',
                                       },
                                'APB': {
                                         'type' : 'apb',
                                       },
                                'AXI4-Stream': {
                                         'type' : 'axi4stream',
                                       },
                              },
                }

    else:
      context = {
                  'title': 'FunkOv',
                  'h1': 'FunkOv',
                  'h2': 'Funktional Coverage Made Easy',
                  'h3': 'For design and verification engineers that care',
                  'buttons' : {
                                'Register':'/accounts/register/',
                                'Login':'/accounts/login/',
                              },
                }

    return render(request, 'funcov/index.html', context)


@login_required
def editor(request):
    context = {}
    if request.method == 'POST':
      type = request.POST.get('type')
      if type == 'ahb':
        context['type'] = "AHB"
        context['covergroups'] = {
                                   'name':'not empty',
                                 }
      elif type == 'apb':
        context['type'] = "APB"
        context['covergroups'] = {
                                   'name':'not empty',
                                 }
      elif type == 'axi4stream':
        context['type'] = "AXI-4 Streaming"
        context['covergroups'] = {
                                   'name':'not empty',
                                 }
      else:
        return HttpResponseRedirect(reverse('index'))

    return render(request, 'funcov/editor.html', context)
