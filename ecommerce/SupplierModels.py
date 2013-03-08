'''
Created on Mar 7, 2013

@author: samuelfendell
'''
from django.db import models
import django.contrib.localflavor.us.forms as localflavor
from models import EcommerceModel

class SupplierModel(EcommerceModel):
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
    
    def create(self, name, desc, primaryEmail, secondEmail = None, ):
        pass