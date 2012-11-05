from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from registration.models import SignupForm

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            # Save
            user = form.save()
            
            # Login
            user = authenticate(username=request.POST['username'], password=request.POST['password2'])
            if user is not None:
                login(request, user)
            
            return redirect('/threads/')

    else:
        form = SignupForm()

    return render(request, 'registration/signup.html', {'form': form})