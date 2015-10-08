from django import forms

class ParameterForm(forms.Form):
  enable = forms.BooleanField(initial=True)
  name = forms.CharField(widget = forms.HiddenInput())
  select = forms.ChoiceField()
