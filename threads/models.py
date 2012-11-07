from django import forms
from django.contrib.auth.models import User
from django.db import models
from django.forms.models import ModelForm
from django.forms.util import ErrorList
from django.forms.widgets import TextInput, PasswordInput

class Thread(models.Model):
    owner = models.ForeignKey(User)
    title = models.TextField(max_length="255")
    description = models.TextField(max_length="500")
    start_text = models.TextField(max_length="500")
    
    def __unicode__(self):
        return self.title
    
class ThreadForm(ModelForm):
    class Meta:
        model = Thread
        exclude = ('owner',)
        widgets = {
            'title': TextInput(),
        }
    
class ThreadItem(models.Model):
    writer = models.ForeignKey(User)
    thread = models.ForeignKey(Thread)
    text = models.TextField(max_length="500")
    vote_count = models.IntegerField(default=0)
    is_selected = models.BooleanField(default=False)
    
class ThreadItemForm(ModelForm):
    class Meta:
        model = ThreadItem
        fields = ('text',)

class DivErrorList(ErrorList):
    def __unicode__(self):
        return self.as_divs()
    def as_divs(self):
        if not self: return u''
        return u'<div class="errorlist">%s</div>' % ''.join([u'<div class="alert alert-error">%s</div>' % e for e in self])
