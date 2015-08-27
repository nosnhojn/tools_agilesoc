from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    context_dict = {
                   }

    return render(request, 'funcOv/index.html', context_dict)
