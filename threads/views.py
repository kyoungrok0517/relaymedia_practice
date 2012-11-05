from django.http import HttpResponse
from django.shortcuts import render, redirect
from threads.models import Thread, ThreadForm

def index(request):
    threads = Thread.objects.all()
    return render(request, 'threads/threads.html', {'threads': threads})

def new(request):
    if request.method == 'POST':
        form = ThreadForm(request.POST)
        if form.is_valid():
            owner = form.cleaned_data['owner']
            title = form.cleaned_data['title']
            
            thread = Thread(owner=owner, title=title)
            thread.save()
            
            return redirect('/threads/')
    else:
        form = ThreadForm()
    
    return render(request, 'threads/new.html', {'form': form})

def show(request, id):
    thread = Thread.objects.get(pk=id)
    
    return render(request, 'threads/show.html', {'thread': thread})
    
