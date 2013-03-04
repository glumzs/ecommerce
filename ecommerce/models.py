'''
Created on Mar 3, 2013

@author: samuelfendell
'''


from django.db import models
import django.contrib.localflavor.us.forms as localflavor

class BrandModel(models.Model):
    brandName = models.CharField()
    
class SupplierModel(models.Model):
    name = models.CharField()
    desc = models.TextField()
    merchantCustomerId = models.CharField()
    
    primaryEmail = models.EmailField()
    secondEmail = models.EmailField()
    phone = localflavor.USPhoneNumberField()
    fax   = localflavor.USPhoneNumberField()
    address = models.CharField()
    city = models.CharField()
    state = localflavor.USStateField()
    zip = localflavor.USZipCodeField()

class ProductModel(models.Model):
    name = models.CharField()
    desc = models.TextField()
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
    
    