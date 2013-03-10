'''
Created on Mar 8, 2013

@author: samuelfendell
'''
import random
from django.utils import unittest
from ecommerce.SupplierModels import SupplierModel
from ecommerce.ProductModels import ProductModel, ManufacturerModel, BrandModel

class SupplierModelTest(unittest.TestCase):


    def setUp(self):
        self.supplierId = SupplierModel.create(name = 'SupplierName',
                             desc = 'SupplierDesc',
                             merchantCustomerId = 'mci',
                             primaryEmail = 'primary@email.com',
                             phone = '123-456-7890',
                             address = '1234 Fakestreet Ave',
                             city = 'Fakecity',
                             state = 'CA',
                             zip = '94536')

        self.manufacturerId = ManufacturerModel.create(name = 'ManuName',
                          vorder = 1)
        self.brandId = BrandModel.create(name = 'BrandName')
        
    #Simple function to randomly generate a product dict.
    def _genTestProduct(self):
        return {'name' : 'productName',
               'desc' : 'productDesc',
               'supplierProductCode' : 'asdf',
               'supplierPrice' : random.randint(1,100)/100,
               'merchantPrice' : random.randint(1,100)/100,
               'manufacturerId' : self.manufacturerId,
               'createdDate' : '2000-01-01',
               'updatedDate' : '2000-02-01',
               'lastsoldDate' : '2000-03-01',
               'numSold' : 1,
               'numReturned' : 1,
               'published' : bool(random.randint(0,1)),
               'categorized' : bool(random.randint(0,1)),
               'brandId' : self.brandId,
               'availability' : 'asdf',
               'categories' : []}
        
    def tearDown(self):
        pass


    def testInsertProductsNoSupplier(self):
        productList = [self._genTestProduct() for _ in range(10)]
        self.assertEqual(0, SupplierModel.insertProducts(self.supplierId, productList))

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()