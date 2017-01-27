from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
import os

def home(request):
    return render(request, 'app/index.html', {})
