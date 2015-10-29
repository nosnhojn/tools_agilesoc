from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.core.servers.basehttp import FileWrapper

from funcov.forms import ParameterForm, CovergroupForm
from django.forms.formsets import formset_factory
from registration.forms import RegistrationForm

# python2,3 compatibility
try:
  from StringIO import StringIO
except ImportError:
  from io import StringIO

from funcov.cgHandler import coverageModuleAsString, coverageModuleAsString
from funcov.tempDataTypes import axi4StreamParameters, axi4StreamCovergroups, ahbParameters, ahbCovergroups, apbParameters, apbCovergroups
from django import forms



def selector(request):
    context = {
                'title': '',
                'h1': 'FunCov',
                'h2': 'Pick an interface to get started',
                'h3': '',
                'buttons' : {
                              'AXI4-Stream': {
                                       'type' : 'axi4stream',
                                     },
                              'AHB': {
                                       'type' : 'ahb',
                                     },
                              'APB': {
                                       'type' : 'apb',
                                     },
                            },
              }

    return render(request, 'funcov/selector.html', context)

def index(request):
    context = {
                'title': 'FunCov',
                'h1': 'FunCov',
                'h2': 'Pick an interface to get started',
                'h3': 'For design and verification engineers that care',
                'buttons' : {
                              'Register':'/accounts/register/',
                              'Login':'/accounts/login/',
                            },
              }

    return render(request, 'funcov/index.html', context)

def covergroupForm(init=None, data=None):
  formSet = formset_factory(CovergroupForm, extra=0)
  if data == None:
    form = formSet(initial=init, prefix='covergroups')
  else:
    form = formSet(data, prefix='covergroups')
  return form

def parameterForm(init=None, data=None):
  formSet = formset_factory(ParameterForm, extra=0)
  if data == None:
    form = formSet(initial=init, prefix='parameters')
    for i in range(0, len(form)):
      if 'choices' in init[i]:
        form[i].fields['select'].choices = init[i]['choices']
  else:
    form = formSet(data, prefix='parameters')
    for i in range(0, len(form)):
      if 'choices' in init[i]:
        form[i].fields['select'].choices = init[i]['choices']
  return form
  
import urllib
def editor(request):
    context = {}

    if request.method == 'POST':
      p = None
      cg = None
      type = request.POST.get('type')
      if type == 'axi4stream':
        p = axi4StreamParameters
        cg = axi4StreamCovergroups
      elif type == 'ahb':
        p = ahbParameters
        cg = ahbCovergroups
      elif type == 'apb':
        p = apbParameters
        cg = apbCovergroups

      pForm = parameterForm(data=request.POST, init=p)
      cgForm = covergroupForm(data=request.POST, init=cg)
      if pForm.is_valid() and cgForm.is_valid():
        # do stuff here
        cg = coverageModuleAsString(pForm, cgForm)
        return render(request, 'funcov/myCovergroup.html', { 'uri' : urllib.quote(cg), 'txt' : cg })

      else:
        print (pForm.errors)
        print (cgForm.errors)
        return HttpResponseRedirect(reverse('index'))

    else:
      type = request.GET.get('type')
      if type == 'axi4stream':
        context = {
                    'name' : 'Streaming AXI-4',
                    'type' : 'axi4stream',
                    'parameters' : parameterForm(init=axi4StreamParameters),
                    'covergroups' : covergroupForm(init=axi4StreamCovergroups),
                  }

      elif type == 'ahb':
        context = {
                    'name' : "AHB",
                    'type' : "ahb",
                    'parameters' : parameterForm(init=ahbParameters),
                    'covergroups' : covergroupForm(init=ahbCovergroups),
                  }

      elif type == 'apb':
        context = {
                    'name' : "APB",
                    'type' : "apb",
                    'parameters' : parameterForm(init=apbParameters),
                    'covergroups' : covergroupForm(init=apbCovergroups),
                  }

      else:
        return HttpResponseRedirect(reverse('index'))

      return render(request, 'funcov/editor.html', context)
