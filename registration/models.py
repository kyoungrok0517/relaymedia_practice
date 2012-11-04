from django.contrib.auth.forms import AuthenticationForm
from django.forms.widgets import TextInput
class LoginForm(AuthenticationForm):
    widgets = {
        'username': TextInput(attrs={'class': 'input-medium'})
    }
