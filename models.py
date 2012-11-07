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


#class Type(models.Model):
#    name = models.CharField(max_length=100)
#    
#    def __unicode__(self):
#        return self.name
#    
#class Reporter(models.Model):
#    name = models.CharField(max_length=100)
#    
#    def __unicode__(self):
#        return self.name
#
#class Project(models.Model):
#    name = models.CharField(max_length=100)
#    
#    def __unicode__(self):
#        return self.name
#
#    
#class Domain(models.Model):
#    name = models.CharField(max_length=100)
#    
#    def __unicode__(self):
#        return self.name
#
#    
#class Use(models.Model):
#    name = models.CharField(max_length=100)
#    
#    def __unicode__(self):
#        return self.name
#
#           
#class VocabData(models.Model):
#    timestamp = models.DateTimeField()
#    name = models.CharField(max_length=100)
#    url = models.CharField(max_length=100)
#    
#    types = models.ManyToManyField(Type)
#    reporters = models.ManyToManyField(Reporter)
#    projects = models.ManyToManyField(Project)
#    domains = models.ManyToManyField(Domain)
#    usage = models.ManyToManyField(Use)
#    
#    def __unicode__(self):
#        return self.name

    
