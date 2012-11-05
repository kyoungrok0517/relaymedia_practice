from django.http import HttpResponse
from django.shortcuts import render
from threads.models import Thread

def index(request):
    threads = Thread.objects.all()
    
    return render(request, 'threads/threads.html', {'threads': threads})
