from django import forms
from django.contrib.auth.models import User
from django.db import models
from django.forms.models import ModelForm
from django.forms.widgets import TextInput, PasswordInput

class Thread(models.Model):
    owner = models.ForeignKey(User)
    
class ThreadItem(models.Model):
    writer = models.ForeignKey(User)
    thread = models.ForeignKey(Thread)
    text = models.TextField(max_length="500")
