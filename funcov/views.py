from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.core.servers.basehttp import FileWrapper

from funcov.forms import ParameterForm, CoverpointForm
from django.forms.formsets import formset_factory
from registration.forms import RegistrationForm

from funcov.models import Covergroup, Coverpoint, Parameter, ParameterChoice

# python2,3 compatibility
try:
  from StringIO import StringIO
except ImportError:
  from io import StringIO

from funcov.cgHandler import coverageModuleAsString, coverageModuleAsString
from funcov.tempDataTypes import axi4StreamParameters, ahbParameters, apbParameters
from django import forms


def about(request):
    return render(request, 'funcov/about.html')

def contact(request):
    return render(request, 'funcov/contact.html')

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

def coverpointFormSet(init=None, data=None):
  formSet = formset_factory(CoverpointForm, extra=0)
  if data == None:
    form = formSet(initial=init, prefix='covergroups')
  else:
    form = formSet(data, prefix='covergroups')
  return form

def parameterFormSet(init=None, data=None):
  formSet = formset_factory(ParameterForm, extra=0)
  if data == None:
    fs = formSet(initial=init, prefix='parameters')
    for f in fs:
      qs = ParameterChoice.objects.filter(param=f.initial['name'])
      if len(qs) == 0:
        f.fields['select'] = None
      else:
        f.fields['select'].queryset = qs
        f.fields['select'].initial = qs[0]
  else:
    fs = formSet(data, prefix='parameters')

  return fs

try:  
  from urllib.parse import quote
except ImportError:
  from urllib import quote

def editor(request):
    context = {}

    if request.method == 'POST':
      p = None
      cg = None
      type = request.POST.get('type')
      e = 'end.sv'
      if type == 'axi4stream':
        p = Parameter.objects.filter(covergroup = type)
        cg = Coverpoint.objects.filter(covergroup = type)
        b = 'axi4begin.sv'
        m = 'axi4middle.sv'
      elif type == 'ahb':
        p = Parameter.objects.filter(covergroup = type)
        cg = Coverpoint.objects.filter(covergroup = type)
        b = 'ahbbegin.sv'
        m = 'ahbmiddle.sv'
      elif type == 'apb':
        p = Parameter.objects.filter(covergroup = type)
        cg = Coverpoint.objects.filter(covergroup = type)
        b = 'apbbegin.sv'
        m = 'apbmiddle.sv'

      pForm = parameterFormSet(data=request.POST)
      cgForm = coverpointFormSet(data=request.POST)
      if pForm.is_valid() and cgForm.is_valid():
        # do stuff here
        cg = coverageModuleAsString(pForm, cgForm, b, m, e)
        return render(request, 'funcov/myCovergroup.html', { 'uri' : quote(cg), 'txt' : cg })

      else:
        #print (pForm.errors)
        #print (cgForm.errors)
        return HttpResponseRedirect(reverse('index'))

    else:
      type = request.GET.get('type')

      cg = Covergroup.objects.filter(type = type)
      if len(cg) != 0:
        cg = cg[0]
        cfs = Coverpoint.objects.filter(covergroup = type)
        pfs = Parameter.objects.filter(covergroup = type)
        context = {
                    'name' : cg.name,
                    'type' : cg.type,
                    'parameters' : parameterFormSet(init=pfs.values()),
                    'coverpoints' : coverpointFormSet(init=cfs.values()),
                  }
        return render(request, 'funcov/editor.html', context)

      else:
        return HttpResponseRedirect(reverse('index'))
