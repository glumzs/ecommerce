'''
Created on Mar 7, 2013

@author: samuelfendell
'''
from django.db import models
import django.contrib.localflavor.us.forms as localflavor
from models import EcommerceModel
from ProductModels import ProductModel

class SupplierModel(EcommerceModel):
    name = models.CharField()
    desc = models.TextField()
    merchantCustomerId = models.CharField()
    
    primaryEmail = models.EmailField()
    secondEmail = models.EmailField(required = False)
    phone = localflavor.USPhoneNumberField()
    fax   = localflavor.USPhoneNumberField(required = False)
    address = models.CharField()
    city = models.CharField()
    state = localflavor.USStateField()
    zip = localflavor.USZipCodeField()
    
    
    
    @classmethod
    def insertProducts(cls, supplierId, productList):
        if not SupplierModel.get(supplierId):
            return -1
        for product in productList:
            product['supplierId'] = supplierId 
            ProductModel.create(**product)
        return 0
        