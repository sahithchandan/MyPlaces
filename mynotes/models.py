from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Note(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    created_by = models.ForeignKey(User)
    created_on = models.DateTimeField()
    latitue = models.DecimalField(max_digits=6, decimal_places=4)
    longitude = models.DecimalField(max_digits=6, decimal_places=4)
    
    def __unicode__(self):
        return "Title: "+self.title
    
class User_Registration(models.Model):
    user = models.ForeignKey(User)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    uuid = models.CharField(max_length=20)
    
    def __unicode__(self):
        return "Email: "+self.user.email