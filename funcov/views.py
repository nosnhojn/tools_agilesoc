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
                  'h1': 'FunCov',
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
                  'title': 'FunCov',
                  'h1': 'FunCov',
                  'h2': 'Functional Coverage Made Easy',
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

    type = request.GET.get('type')
    if type == 'axi4stream':
      context = {
                  'name' : "Streaming AXI-4",
                  'type' : "axi4stream",
                  'covergroups' : {
                                    'activeDataTransfer': {
                                              'enabled'     : True,
                                              'desc'        : "Capture an active data cycle where tReady and tValid are asserted",
                                              'sensitivity' : "Positive clock edge",
                                            },
                                    'tData_toggle': {
                                              'enabled'     : True,
                                              'desc'        : "Toggle coverage of the tData bus",
                                              'sensitivity' : "activeDataTransfer",
                                            },
                                  },
                  'parameters' : {
                                   'tValid' : {
                                               'default' : None,
                                              },
                                   'tReady' : {
                                               'default' : None,
                                              },
                                   'tData'  : {
                                                'default' : '8',
                                                'values'  : [ 8, 16, 32, 64, 128, 256 ],
                                              },
                                   'tStrb'  : {
                                                'default' : '1',
                                                'values'  : [ 1, 2, 4, 8, 16, 32 ],
                                               },
                                   'tLast'  : {
                                                'default' : None,
                                               },
                                   'tKeep'  : {
                                                'default' : '4',
                                                'values'  : range(1,16) 
                                              },
                                   'tId'    : {
                                                'default' : '4',
                                                'values'  : range(1,16) 
                                              },
                                   'tDest'  : {
                                                'default' : '4',
                                                'values'  : range(1,16) 
                                              },
                                   'tUser'  : {
                                                'default' : '4',
                                                'values'  : range(1,16) 
                                              },
                                 },
                }

    elif type == 'ahb':
      context = {
                  'name' : "AHB",
                  'type' : "ahb",
                  'covergroups' : {
                                    'name':'not empty',
                                  },
                }

    elif type == 'apb':
      context = {
                  'name' : "APB",
                  'type' : "apb",
                  'covergroups' : {
                                    'name':'not empty',
                                  },
                }

    else:
      return HttpResponseRedirect(reverse('index'))

    return render(request, 'funcov/editor.html', context)
