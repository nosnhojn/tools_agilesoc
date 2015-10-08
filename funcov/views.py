from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.core.servers.basehttp import FileWrapper

from funcov.forms import ParameterForm
from django.forms.formsets import formset_factory
from registration.forms import RegistrationForm

# python2,3 compatibility
try:
  from StringIO import StringIO
except ImportError:
  from io import StringIO

from tempCovergroups import axi4StreamContext, axi4StreamParameters

from django import forms



def index(request):
    #filename = 'README.md' # Select your file here.                                
    #text = StringIO.StringIO('what up\n')
    #wrapper = FileWrapper(text)
    #response = HttpResponse(wrapper, content_type='application/octet-stream')
    #response['Content-Disposition'] = 'attachment;filename=\"README.txt\"'
    #print(text.len)
    #response['Content-Length'] = text.len
    #return response

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

    if request.method == 'POST':
      print (request.POST)
      return render(request, 'funcov/editor.html', context)

    else:
      type = request.GET.get('type')
      if type == 'axi4stream':
        parameterFormSet = formset_factory(ParameterForm, extra=0)
        parameterSet = parameterFormSet(initial=axi4StreamParameters)
        print (len(parameterSet))
        for f,s in zip(parameterSet, axi4StreamParameters):
          if s.has_key('choices'):
            f.fields['select'].choices = s['choices']

        context = {
                    'parameters' : parameterSet,
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
