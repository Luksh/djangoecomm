from django.shortcuts import render
from .models import *
app_name = "home"

# Create your views here.

def home(request):
    return render(request, 'index.html')