'''
Created on Mar 7, 2013

@author: samuelfendell
'''
from django.db import models
from models import EcommerceModel, PriceField
from SupplierModels import SupplierModel



class ProductModel(EcommerceModel):
    name = models.CharField()
    desc = models.TextField()
    supplierId  = models.ForeignKey(SupplierModel)
    supplierProductCode = models.CharField()
    supplierPrice = PriceField()
    merchantPrice = PriceField()
    
    custFactor = models.FloatField(blank=False) 
    manufacturerName = models.ForeignKey('ManufacturerModel')
    
    createdDate = models.DateTimeField()
    updatedDate = models.DateTimeField()
    lastsoldDate = models.DateTimeField()
    
    numSold = models.PositiveIntegerField()
    numReturned = models.PositiveIntegerField()
    
    published = models.BooleanField()
    categorized = models.BooleanField()
    
    brandId = models.ForeignKey('BrandModel')
    
    availability = models.CharField()


class ProductImageModel(EcommerceModel):
    productId = models.ForeignKey('ProductModel')
    imgPath = models.CharField()
    md5sum = models.CharField(max_length = 32)
    
#Model for mapping many-to-many relationship
#between categories and products. 
class CategoryProductModel(EcommerceModel):
    category = models.ForeignKey('CategoryModel')
    product = models.ForeignKey(ProductModel)
    
    
#Simple model to hold category name.
class CategoryModel(EcommerceModel):
    parentCategory = models.ForeignKey("self")
    name = models.CharField()
    
#Simple model to hold brand name.
class BrandModel(EcommerceModel):
    brandName = models.CharField()            
    

class ManufacturerModel(EcommerceModel):
    name = models.CharField()    
    #TODO: What is this field for?
    vorder = models.IntegerField() 
    
