from django.contrib.auth.models import User
from django.db import models

class Thread(models.Model):
    owner = models.ForeignKey(User)
    
class ThreadItem(models.Model):
    writer = models.ForeignKey(User)
    thread = models.ForeignKey(Thread)
    text = models.TextField(max_length="500")