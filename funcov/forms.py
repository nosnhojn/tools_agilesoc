from django import forms
from django.forms.formsets import formset_factory

from django.db import models
from django.forms import ModelForm
from funcov.models import Coverpoint, Parameter, ParameterChoice


class ParameterForm(forms.Form):
  enable = forms.BooleanField(initial=True, widget = forms.HiddenInput())
  name = forms.CharField(widget = forms.HiddenInput())
  select = forms.ModelChoiceField(queryset=None)

  def __init__(self, *args, **kwargs):
    super(ParameterForm, self).__init__(*args, **kwargs)
    qs = ParameterChoice.objects.filter(param=self.initial['name'])
    if len(qs) == 0:
      self.fields['select'] = None
    else:
      self.fields['select'].queryset = qs
      self.fields['select'].initial = qs[0]


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
