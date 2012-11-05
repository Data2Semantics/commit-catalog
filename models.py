'''
Created on Nov 5, 2012

@author: hoekstra
'''
from django.db import models

class Entry(models.Model):
    name = models.CharField(max_length=100)
    timestamp = models.DateTimeField()
    
    class Meta:
        app_label = 'catalog'