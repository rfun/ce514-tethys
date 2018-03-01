from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from tethys_sdk.gizmos import *
import csv, os, random, string, urlparse
from datetime import datetime

from tethys_sdk.services import get_spatial_dataset_engine

def home(request):
    context = {       
    }
    return render(request, 'mapapp/home.html', context)

def maps(request):

    context = {}
    return render(request, 'mapapp/map.html', context)

def data(request):
    context = {}
    return render(request, 'mapapp/data.html', context)

def about(request):
    context = {}
    return render(request, 'mapapp/about.html', context)
