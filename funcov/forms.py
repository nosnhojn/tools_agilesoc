from django import forms
from django.forms.formsets import formset_factory

class ParameterForm(forms.Form):
  enable = forms.BooleanField(initial=True, widget = forms.HiddenInput())
  name = forms.CharField(widget = forms.HiddenInput())
  select = forms.ChoiceField(required=False)

class CovergroupForm(forms.Form):
  enable = forms.BooleanField(initial=True)
  name = forms.CharField(widget = forms.HiddenInput())
  desc = forms.CharField(widget = forms.HiddenInput())
  sensitivity = forms.CharField(widget = forms.HiddenInput())
