from django.http import HttpResponse
from django.shortcuts import render
from threads.models import Thread, ThreadForm

def index(request):
    threads = Thread.objects.all()
    
    return render(request, 'threads/threads.html', {'threads': threads})

def new(request):
    form = ThreadForm()
    
    return render(request, 'threads/new.html', {'form': form})
