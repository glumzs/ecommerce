'''
Created on Mar 3, 2013

@author: samuelfendell
'''


from django.db import models


#Generic Model that incorporates much of the functionality of our api.
#Meant to be subclassed.
class EcommerceModel(models.Model):
    
    @classmethod
    def create(cls, **kwargs):
        try:
            a = cls(**kwargs)
            return a._save_getId()
        except:
            return -1
        
    @classmethod
    def update(cls, obj_id, **kwargs):
        try:
            a = cls(index = id, **kwargs)
            return a._save_getId()
        except:
            return -1
    
    @classmethod
    def get(cls, obj_id):
        return cls.objects.get(id = obj_id)
    
    @classmethod
    def delete(cls, obj_id):
        obj = cls.objects.get(id = obj_id)
        if not obj:
            return -1
        try:
            obj.delete()
            return 0
        except:
            return -2
    @classmethod
    def copy():
    
    def _save_getId(self):
        self.save()
        return self.id
    
class PriceField(models.DecimalField):
    def __init__(self, **kwargs):
        super(PriceField, self).__init__(decimal_places = 2)

    
    