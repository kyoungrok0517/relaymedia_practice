from django import forms
from django.contrib.auth.models import User
from django.db import models
from django.forms.models import ModelForm
from django.forms.widgets import TextInput, PasswordInput

class Thread(models.Model):
    owner = models.ForeignKey(User)
    title = models.TextField(max_length="255")
    start_text = models.TextField(max_length="500")
    
class ThreadForm(ModelForm):
    class Meta:
        model = Thread
        widgets = {
            'title': TextInput(),
        }
    
class ThreadItem(models.Model):
    writer = models.ForeignKey(User)
    thread = models.ForeignKey(Thread)
    text = models.TextField(max_length="500")
    vote_count = models.IntegerField()
    is_start = models.BooleanField()
