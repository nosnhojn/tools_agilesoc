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
from funcov.tempStrings import apbbegin, apbmiddle, ahbbegin, ahbmiddle, axi4begin, axi4middle, end

# python2,3 compatibility
try:
  from StringIO import StringIO
except ImportError:
  from io import StringIO

try:  
  from urllib.parse import quote
except ImportError:
  from urllib import quote


from funcov.cgHandler import coverageModuleAsString, coverageModuleAsString
from django import forms


def about(request):
    return render(request, 'funcov/about.html')

def contact(request):
    return render(request, 'funcov/contact.html')

def selector(request):
    buttons = {}
    for cg in Covergroup.objects.all():
      buttons[cg.name] = { 'type' : cg.type }

    context = {
                'title': '',
                'h1': 'FunCov',
                'h2': 'Pick an interface to get started',
                'h3': '',
                'buttons' : buttons,
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

def editor(request):
    context = {}

    if request.method == 'POST':
      p = None
      cg = None
      type = request.POST.get('type')
      e = end
      if type == 'axi4stream':
        p = Parameter.objects.filter(covergroup = type)
        cg = Coverpoint.objects.filter(covergroup = type)
        b = axi4begin
        m = axi4middle
      elif type == 'ahb':
        p = Parameter.objects.filter(covergroup = type)
        cg = Coverpoint.objects.filter(covergroup = type)
        b = ahbbegin
        m = ahbmiddle
      elif type == 'apb':
        p = Parameter.objects.filter(covergroup = type)
        cg = Coverpoint.objects.filter(covergroup = type)
        b = apbbegin
        m = apbmiddle

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
