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

def createProduct(request):
    if request.method != "POST":
        resp = {"errCode": 1}
    else:
        data = json.loads(request.raw_post_data)
        productInfo = data['product_info']
        rtn = ProductModel.create(productInfo)
        resp = {"errCode": rtn}
    return HttpResponse(content=json.dumps(resp), content_type='application/json')

def getProduct(request):
    if request.method != "GET":
        resp = {"errCode": 1}
    else:
        data = json.loads(request.raw_post_data)
        productID = data['product_id']
        rtn = ProductModel.get(productID)
        if rtn:
            resp = {"errCode": 0,"product_info": rtn}
        else:
            resp = {"errCode": -1}
    return HttpResponse(content=json.dumps(resp), content_type='application/json')

def updateProduct(request):
    if request.method != "POST":
        resp = {"errCode": 1}
    else:
        data = json.loads(request.raw_post_data)
        productID = data['product_id']
        productInfo = data['product_info']
        rtn = ProductModel.update(productID, productInfo)
        resp = {"errCode": rtn}
    return HttpResponse(content=json.dumps(resp), content_type='application/json')

def deleteProduct(request):
    if request.method != "POST":
        resp = {"errCode": 1}
    else:
        data = json.loads(request.raw_post_data)
        productID = data['product_id']
        rtn = ProductModel.delete(productID)
        resp = {"errCode": rtn}
    return HttpResponse(content=json.dumps(resp), content_type='application/json')
#TODO
def copyProduct(request):
    if request.method != "POST":
        resp = {"errCode": 1}
    else:
        data = json.loads(request.raw_post_data)
        productID = data['product_id']
        rtn = ProductModel.copy(productID)
        resp = {"errCode": rtn}
    return HttpResponse(content=json.dumps(resp), content_type='application/json')