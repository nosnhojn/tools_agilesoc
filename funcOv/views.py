from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm
from registration.forms import RegistrationForm

def index(request):
    context_dict = {
                     'regForm': RegistrationForm(),
                     'authForm': AuthenticationForm(),
                   }

    return render(request, 'funcOv/index.html', context_dict)
