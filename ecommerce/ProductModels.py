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
    
    categories = models.ManyToManyField(through = 'CategoryProductModel')

class CategoryProductModel(models.Model):
    categoryId = models.ForeignKey('Category')
    productId  = models.ForeignKey('Product')
    #TODO: what is this field for?
    vorder = models.IntegerField()

class ProductImageModel(EcommerceModel):
    productId = models.ForeignKey('ProductModel')
    imgPath = models.CharField()
    md5sum = models.CharField(max_length = 32)

    
#Simple model to hold category name.
class CategoryModel(EcommerceModel):
    parentCategory = models.ForeignKey("self")
    name = models.CharField()
    
    def getProducts(self, categoryId):
        return ProductModel.objects.filter(categoryId = categoryId)
    
    #TODO: what is product list? Assuming it's an iterable of products for now
    @classmethod
    def addProductsToCategory(cls, categoryId, productList):
        category = cls.objects.get(id = categoryId)
        try:
            for product in productList:
                product.categories.add(category)
            return 0
        except:
            return -1
    
    @classmethod
    def delProductsFromCategory(cls, categoryId, productList):
        category = cls.objects.get(id = categoryId)
        try:
            for product in productList:
                product.categories.remove(category)
            return 0
        except:
            return -1
        
    
#Simple model to hold brand name.
class BrandModel(EcommerceModel):
    brandName = models.CharField()            
    

class ManufacturerModel(EcommerceModel):
    name = models.CharField()    
    #TODO: What is this field for?
    vorder = models.IntegerField() 
    
