from django import forms
from django.forms.formsets import formset_factory

from django.db import models
from django.forms import ModelForm
from funcov.models import Coverpoint, Parameter, ParameterChoice


class CovergroupForm(forms.Form):
  name = forms.CharField(label='Save As', initial='', max_length=50)
  private = forms.BooleanField(initial=True)


class ParameterForm(forms.Form):
  enable = forms.BooleanField(initial=True, widget = forms.HiddenInput())
  name = forms.CharField(widget = forms.HiddenInput())
  select = forms.ModelChoiceField(queryset=ParameterChoice.objects.all(), required=False)


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
