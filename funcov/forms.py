from django import forms
from django.forms.formsets import formset_factory

from django.db import models
from django.forms import ModelForm
from funcov.models import Coverpoint, Parameter


class ParameterForm(forms.Form):
  enable = forms.BooleanField(initial=True, widget = forms.HiddenInput())
  name = forms.CharField(widget = forms.HiddenInput())
  select = forms.ChoiceField(required=False)

#class ParameterForm(ModelForm):
  #class Meta:
    #model = Parameter
    #fields = [ 'enable', 'name', 'select' ]
    #widgets = {
                #'enable' : forms.HiddenInput(),
                #'name' : forms.HiddenInput(),
                #'select' : forms.Select(choices=[('a','b')]),
              #}


class CoverpointForm(ModelForm):
  class Meta:
    model = Coverpoint
    fields = [ 'enable', 'name', 'desc', 'type', 'expr', 'sensitivityLabel', 'sensitivity' ]
    widgets = {
                'name' : forms.HiddenInput(),
                'desc' : forms.HiddenInput(),
                'type' : forms.HiddenInput(),
                'expr' : forms.HiddenInput(),
                'sensitivityLabel' : forms.HiddenInput(),
                'sensitivity' : forms.HiddenInput(),
              }
