# Create your views here.

from django.template.loader import get_template
from django.template import Context
from ecommerce.models import EcommerceModel
from ecommerce.ProductModels import ProductModel, CategoryModel
from ecommerce.SupplierModels import SupplierModel
from django.http import HttpResponse
from django.utils import simplejson as json
from django.views.decorators.csrf import csrf_exempt

def home(request):
    t = get_template('client.html')
    c = Context({})
    html = t.render(c)
    return HttpResponse(html)

def createSupplier(request):
    if request.method != "POST":
        resp = {"errCode": -1}
    else:
        supplierInfo = json.loads(request.raw_post_data)
        rtn = SupplierModel.create(supplierInfo)
        if rtn == -1:
            resp = {"errCode": rtn}
        else:
            resp = {"supplier_id": rtn, "errCode": 0}
    return HttpResponse(content=json.dumps(resp), content_type='application/json')    

def getSupplier(request):
   if request.method != "GET":
        resp = {"errCode": -1}
    else:
        data = json.loads(request.raw_post_data)
        supplierId = data['supplier_id']
        rtn = SupplierModel.get(supplierId)
        if rtn:
            resp = {"supplier_info": rtn, "errCode": 0}
        else:
            resp = {"errCode": -1}
    return HttpResponse(content=json.dumps(resp), content_type='application/json') 

def updateSuppler(request):
    if request.method != "POST":
        resp = {"errCode": -1}
    else:
        data = json.loads(request.raw_post_data)
        supplierId = data['supplier_id']
        supplierInfo = data['supplier_info']
        rtn = SupplierModel.update(supplierInfo, supplierId)
        resp = {"errCode": rtn}
    return HttpResponse(content=json.dumps(resp), content_type='application/json')        

def deleteSupplier(request):
    if request.method != "POST":
        resp = {"errCode": -1}
    else:
        data = json.loads(request.raw_post_data)
        supplierId = data['supplier_id']
        rtn = SupplierModel.delete(supplierId)
        resp = {"errCode": rtn}
    return HttpResponse(content=json.dumps(resp), content_type='application/json')     

def insertProducts(request):
    if request.method != "POST":
        resp = {"errCode": -1}
    else:
        data = json.loads(request.raw_post_data)
        supplierId = data['supplier_id']
        products = date['products']
        rtn = SupplierModel.insertProducts(supplierId, products)
        resp = {"errCode": rtn}
    return HttpResponse(content=json.dumps(resp), content_type='application/json')  

def addCategory(request):
    if request.method != "POST":
        resp = {"errCode": -1}
    else:
        categoryInfo = json.loads(request.raw_post_data)
        rtn = CategoryModel.add(categoryInfo)
        if rtn == -1:
            resp = {"errCode": rtn}
        else:
            resp = {"category_id": rtn, "errCode": 0}
    return HttpResponse(content=json.dumps(resp), content_type='application/json')    

def getCategory(request):
   if request.method != "GET":
        resp = {"errCode": -1}
    else:
        data = json.loads(request.raw_post_data)
        categoryId = data['category_id']
        rtn = CategoryModel.get(categoryId)
        if rtn:
            resp = {"category_info": rtn, "errCode": 0}
        else:
            resp = {"errCode": -1}
    return HttpResponse(content=json.dumps(resp), content_type='application/json') 

def updateCategory(request):
    if request.method != "POST":
        resp = {"errCode": -1}
    else:
        data = json.loads(request.raw_post_data)
        categoryId = data['category_id']
        categoryInfo = data['category_info']
        rtn = CategoryModel.update(categoryId, categoryInfo)
        resp = {"errCode": rtn}
    return HttpResponse(content=json.dumps(resp), content_type='application/json')      

def deleteCategory(request)
    if request.method != "POST":
        resp = {"errCode": -1}
    else:
        data = json.loads(request.raw_post_data)
        categoryId = data['category_id']
        rtn = CategoryModel.delete(categoryId)
        resp = {"errCode": rtn}
    return HttpResponse(content=json.dumps(resp), content_type='application/json')   

def getCategoryProducts(request):
   if request.method != "GET":
        resp = {"errCode": -1}
    else:
        data = json.loads(request.raw_post_data)
        categoryId = data['category_id']
        rtn = CategoryModel.getCategoryProducts(categoryId)
        if rtn:
            resp = {"products": rtn, "errCode": 0}
        else:
            resp = {"errCode": -1}
    return HttpResponse(content=json.dumps(resp), content_type='application/json')

def addProductsToCategory(request):
    if request.method != "POST":
        resp = {"errCode": -1}
    else:
        data = json.loads(request.raw_post_data)
        categoryId = data['category_id']
        products = data['products']
        rtn = CategoryModel.addProductsToCategory(categoryId, products)
        resp = {"errCode": rtn}
    return HttpResponse(content=json.dumps(resp), content_type='application/json')   

def delProductsFromCategory(request)
    if request.method != "POST":
        resp = {"errCode": -1}
    else:
        data = json.loads(request.raw_post_data)
        categoryId = data['category_id']
        products = data['products']
        rtn = CategoryModel.deleteProductsFromCategory(categoryId, products)
        resp = {"errCode": rtn}
    return HttpResponse(content=json.dumps(resp), content_type='application/json')  

def createProduct(request):
    if request.method != "POST":
        resp = {"errCode": -1}
    else:
        data = json.loads(request.raw_post_data)
        productInfo = data['product_info']
        rtn = ProductModel.create(productInfo)
        if rtn == -1:
            resp = {"errCode": rtn}
        else:
            resp = {"product_id": rtn, "errCode": 0}
    return HttpResponse(content=json.dumps(resp), content_type='application/json')

def getProduct(request):
    if request.method != "GET":
        resp = {"errCode": -1} 
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
        resp = {"errCode": -1}
    else:
        data = json.loads(request.raw_post_data)
        productID = data['product_id']
        productInfo = data['product_info']
        rtn = ProductModel.update(productID, productInfo)
        resp = {"errCode": rtn}
    return HttpResponse(content=json.dumps(resp), content_type='application/json')

def deleteProduct(request):
    if request.method != "POST":
        resp = {"errCode": -1}
    else:
        data = json.loads(request.raw_post_data)
        productID = data['product_id']
        rtn = ProductModel.delete(productID)
        resp = {"errCode": rtn}
    return HttpResponse(content=json.dumps(resp), content_type='application/json')

def copyProduct(request):
    if request.method != "GET":
        resp = {"errCode": -1}
    else:
        data = json.loads(request.raw_post_data)
        productID = data['product_id']
        rtn = ProductModel.copy(productID)
        if rtn:
            resp = {"errCode": 0,"product_info": rtn}
        else:
            resp = {"errCode": -1}
    return HttpResponse(content=json.dumps(resp), content_type='application/json')
