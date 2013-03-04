'''
Created on Mar 3, 2013

@author: samuelfendell
'''


from django.db import models

class ProductModel(models.Model):
    productName = models.CharField(max_length=128)
    productDesc = models.TextField()
    supplierId  = models.IntegerField()
    