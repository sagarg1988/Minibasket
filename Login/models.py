from __future__ import unicode_literals

from django.db import models

# Create your models here

class Item(models.Model):
    name = models.CharField(max_length=30)
    price = models.CharField(max_length=30)
    weight = models.CharField(max_length=30)
    batch_no = models.CharField(max_length=30)
    quantity = models.IntegerField(default=0)
    is_deleted = models.BooleanField(default=False)

    def __unicode__(self):
    	return self.name+" "+self.weight
    
