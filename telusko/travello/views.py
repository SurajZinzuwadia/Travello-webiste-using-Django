from django.shortcuts import render,redirect
from .models import Destination
from django.contrib.sessions.models import Session
# Create your views here.
def index(request):

    dests = Destination.objects.all()
    return render(request,'index.html', {'dests': dests})
