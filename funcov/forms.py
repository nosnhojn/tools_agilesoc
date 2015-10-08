from django import forms

class ParameterForm(forms.Form):
  name = forms.BooleanField(initial=True)
  select = forms.ChoiceField()
  pass
