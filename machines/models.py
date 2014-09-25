from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Machine(models.Model):
    hostname = models.CharField(max_length=50)
    arch     = models.CharField(max_length=50)
    os       = models.CharField(max_length=50)
    location = models.CharField(max_length=20)
    status   = models.CharField(max_length=20)
    note     = models.TextField(null=True, blank=True)
    user     = models.ForeignKey(User, null=True, blank=True)

    def __unicode__(self):
        return self.hostname
