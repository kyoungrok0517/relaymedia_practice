from django.http import HttpResponse
from django.shortcuts import render, redirect
from threads.models import Thread, ThreadForm, ThreadItemForm

def index(request):
    threads = Thread.objects.all()
    return render(request, 'threads/threads.html', {'threads': threads})

def new(request):
    if request.method == 'POST':
        form = ThreadForm(request.POST)
        
        if request.user.is_authenticated() and form.is_valid():
            thread = form.save(commit=False)
            thread.owner = request.user
            thread.save() 
            
            return redirect('/threads/')
    else:
        form = ThreadForm()
    
    return render(request, 'threads/new.html', {'form': form, 'user': request.user})

def show(request, thread_id):
    thread = Thread.objects.get(pk=thread_id)
    
    if request.method == 'POST':
        form = ThreadItemForm(request.POST)
        if form.is_valid():
            thread = Thread.objects.get(pk=thread_id)
            thread_item = form.save(commit=False)
            thread_item.thread = thread
            thread_item.save()
            
            return redirect('/threads/%d/' % int(thread_id))
    else:
        form = ThreadItemForm()
    
    return render(request, 'threads/show.html', {'thread': thread, 'form': form})


