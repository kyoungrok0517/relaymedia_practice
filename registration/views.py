from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import render
from registration.models import SignupForm
def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            username = form.clean_username()
            email = form.cleaned_data['email']
            password = form.clean_password2()
            
            # Save
            user = User.objects.create_user(username, email, password)
            user.save()
    else:
        form = SignupForm()

    return render(request, 'registration/signup.html', {'form': form})