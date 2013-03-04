'''
Created on Mar 3, 2013

@author: samuelfendell
'''


from django.db import models

class ProductModel(models.Model):
    productName = models.CharField()
    productDesc = models.TextField()
    supplierId  = models.IntegerField()
    supplierProductCode = models.CharField()
    supplierPrice = models.DecimalField(decimal_places = 2)
    merchantPrice = models.DecimalField(decimal_places = 2)
    custFactor = models.FloatField(blank=False) 
    manufacturerName = models.CharField()
    
    createdDate = models.DateTimeField()
    updatedDate = models.DateTimeField()
    lastsoldDate = models.DateTimeField()
    
    numSold = models.PositiveIntegerField()
    numReturned = models.PositiveIntegerField()
    
    published = models.BooleanField()
    categorized = models.BooleanField()
    
    brandId = models.PositiveIntegerField()
    
    availibility = models.CharField()
    
    