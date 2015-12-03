from django import forms
from django.forms.formsets import formset_factory

from django.db import models
from django.forms import ModelForm
from funcov.models import Coverpoint, Parameter, ParameterChoice


class ParameterForm(forms.Form):
  enable = forms.BooleanField(initial=True, widget = forms.HiddenInput())
  name = forms.CharField(widget = forms.HiddenInput())
  #select = forms.ModelChoiceField(queryset=ParameterChoice.objects.all(), to_field_name='choice')
  select = forms.ModelChoiceField(queryset=None)

  def __init__(self, *args, **kwargs):
    super(ParameterForm, self).__init__(*args, **kwargs)
    self.fields['select'].queryset = ParameterChoice.objects.all()

#class ParameterForm(ModelForm):
  #class Meta:
    #model = Parameter
    #fields = [ 'enable', 'name', 'select' ]
    #widgets = {
                #'enable' : forms.HiddenInput(),
                #'name' : forms.HiddenInput(),
                #'select' : forms.Select(choices=[('a','b')]),
              #}
#
# def __init__(self, *args, **kwargs):
#   super(ParameterForm, self).__init__(*args, **kwargs)
#   if self.instance:
#     print(self.instance.paramID)
#     self.fields['select'].queryset = ParameterChoice.objects.filter(paramID=self.instance.paramID)


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
