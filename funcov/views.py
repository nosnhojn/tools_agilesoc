from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.core.servers.basehttp import FileWrapper

from funcov.forms import ParameterForm, CoverpointForm, CovergroupForm
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
    cgs = Covergroup.objects.filter(owner = 'root') | Covergroup.objects.filter(owner = request.user.username)
    for cg in cgs:
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

import random
import string
def randomTypeString():
  return ''.join([random.choice(string.ascii_letters + string.digits) for n in range(10)])

def editor(request):
  context = {}

  if request.method == 'POST':
    requestedType = request.POST.get('type')
    formAction = request.POST.get('form-action')

    if formAction == 'download':
      pForm = parameterFormSet(data=request.POST)
      cgForm = coverpointFormSet(data=request.POST)
      if pForm.is_valid() and cgForm.is_valid():
        cg = Covergroup.objects.filter(type = requestedType)[0]
        beginning = cg.beginning
        middle = cg.middle

        cgAsString = coverageModuleAsString(pForm, cgForm, beginning, middle, end)
        return render(request, 'funcov/myCovergroup.html', { 'uri' : quote(cgAsString), 'txt' : cgAsString })

      else:
        #print (pForm.errors)
        #print (cgForm.errors)
        return HttpResponseRedirect(reverse('index'))

    elif formAction == 'save':
      saveas = CovergroupForm(data=request.POST, prefix='covergroup')
      if saveas.is_valid():
        pForm = parameterFormSet(data=request.POST)
        cgForm = coverpointFormSet(data=request.POST)
        if pForm.is_valid() and cgForm.is_valid():
          for f in pForm:
            qs = ParameterChoice.objects.filter(param=f.cleaned_data['name'])
            if len(qs) == 0:
              f.fields['select'] = None
            else:
              f.fields['select'].queryset = qs
              f.fields['select'].initial = qs[0]

          # duplicate and save the new covergroup and dependants
          newCg = Covergroup.objects.filter(type = requestedType)[0]
          newCg.pk = None
          newCg.type = randomTypeString()
          newCg.name = saveas.cleaned_data['name']
          newCg.owner = request.user.username
          newCg.private = True
          newCg.save()

          # !! need the enable here !!
          #newCps = Coverpoint.objects.filter(covergroup = requestedType)
          #for cp in newCps:
          #  cp.pk = None
          #  cp.covergroup = newCg.type
          #  cp.save()
          for cp in cgForm.cleaned_data:
            newEntry = Coverpoint(**cp)
            newEntry.pk = None
            newEntry.covergroup = newCg.type
            newEntry.save()
          newCps = Coverpoint.objects.filter(covergroup = newCg.type)

          # !! need the select here !!
          newPs = Parameter.objects.filter(covergroup = requestedType)
          for p in newPs:
            p.pk = None
            p.covergroup = newCg.type
            p.save()

          context = {
                      'name' : newCg.name,
                      'type' : newCg.type,
                      'parameters' : parameterFormSet(init=newPs.values()),
                      'coverpoints' : coverpointFormSet(init=newCps.values()),
                      'saveas' : CovergroupForm(initial={'name':saveas.cleaned_data['name'], 'private':True}, prefix='covergroup'),
                    }
          return render(request, 'funcov/editor.html', context)
      else:
        pForm = parameterFormSet(data=request.POST)
        cgForm = coverpointFormSet(data=request.POST)
        if pForm.is_valid() and cgForm.is_valid():
          for f in pForm:
            qs = ParameterChoice.objects.filter(param=f.cleaned_data['name'])
            if len(qs) == 0:
              f.fields['select'] = None
            else:
              f.fields['select'].queryset = qs
              f.fields['select'].initial = qs[0]

          cg = Covergroup.objects.filter(type = requestedType)[0]

          context = {
                      'name' : cg.name,
                      'type' : cg.type,
                      'parameters' : pForm,
                      'coverpoints' : cgForm,
                      'saveas' : CovergroupForm(initial={'name':cg.name, 'private':True}, prefix='covergroup'),
                      'errormsg' : saveas.errors,
                      'tab' : 'save',
                    }
          return render(request, 'funcov/editor.html', context)
        else:
          return HttpResponseRedirect(reverse('index'))

  else:
    requestedType = request.GET.get('type')

    cg = Covergroup.objects.filter(type = requestedType)
    if len(cg) != 0:
      cg = cg[0]
      cfs = Coverpoint.objects.filter(covergroup = requestedType)
      pfs = Parameter.objects.filter(covergroup = requestedType)
      context = {
                  'name' : cg.name,
                  'type' : cg.type,
                  'parameters' : parameterFormSet(init=pfs.values()),
                  'coverpoints' : coverpointFormSet(init=cfs.values()),
                  'saveas' : CovergroupForm(initial={'name':cg.name, 'private': True}, prefix='covergroup'),
                }
      return render(request, 'funcov/editor.html', context)

    else:
      return HttpResponseRedirect(reverse('index'))
