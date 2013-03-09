# Create your views here.

from django.template.loader import get_template
from django.template import Context
from ecommerce.models import EcommerceModel
from ecommerce.ProductModels import ProductModel, CategoryModel
from ecommerce.SupplierModels import SupplierModel
from django.http import HttpResponse
from django.utils import simplejson as json
from django.views.decorators.csrf import csrf_exempt

def home(request)

def createSupplier(request)

def getSupplier(request)

def updateSuppler(request)

def deleteSupplier(request)

def insertProducts(request)

def addCategory(request)

def getCategory(request)

def updateCategory(request)

def deleteCategory(request)

def getCategoryProducts(request)

def addProductsToCategory(request)

def delProductsFromCategory(request)

def createProduct(request)

def getProduct(request)

def updateProduct(request)

def deleteProduct(request)

def copyProduct(request)
