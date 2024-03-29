from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from registration.models import SignupForm
from threads.models import DivErrorList

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST, error_class=DivErrorList)
        if form.is_valid():
            # Save
            user = form.save()
            
            # Login
            user = authenticate(username=request.POST['username'], password=request.POST['password2'])
            if user is not None:
                login(request, user)
            
            return redirect('/threads/')

    else:
        form = SignupForm(error_class=DivErrorList)

    return render(request, 'registration/signup.html', {'form': form})