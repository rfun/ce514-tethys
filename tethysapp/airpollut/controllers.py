from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from tethys_sdk.gizmos import *
import csv
import os
import random
import string
import urlparse
from datetime import datetime

from tethys_sdk.services import get_spatial_dataset_engine

def home(request):
    context = {}
    return render(request, 'airpollut/home.html', context)

def maps(request):
    context = {}
    return render(request, 'airpollut/map.html', context)

def data(request):
    context = {}
    return render(request, 'airpollut/data.html', context)

def about(request):
    context = {}
    return render(request, 'airpollut/about.html', context)

def mockup(request):
    context = {}
    return render(request, 'airpollut/mockup.html', context)

def proposal(request):
    context = {}
    return render(request, 'airpollut/proposal.html', context)