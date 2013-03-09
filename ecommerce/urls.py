from django.conf.urls import patterns, include, url
from ecommerce.views import *
from ecommerce import settings

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',

    # supplier handlers
    (r'^suppliers/create_supplier$', createSupplier),
    (r'^suppliers/get_supplier$', getSupplier),
    (r'^suppliers/update_supplier$', updateSupplier),
    (r'^suppliers/delete_supplier$', deleteSupplier),
    (r'^suppliers/insert_products$', insertProducts),
    
    # category handlers
    (r'^category/get_category$', getCategory),
    (r'^category/category_products$', getCategoryProducts),
    (r'^category/add_category$', addCategory);
    (r'^category/update_category$', updateCategory),
    (r'^category/delete_category$', deleteCategory),
    (r'^category/add_products$', addProductsToCategory),
    (r'^category/del_products$', delProductsFromCategory),
    
    # product handlers
    (r'^product/update_product$', updateProduct),
    (r'^product/create_product$', createProduct),
    (r'^product/get_product$', getProduct),
    (r'^product/copy_product$', copyProduct),
    (r'^product/delete_product$', deleteProduct),
    
    # site handler
    (r'^$', home),
    
    # static
    (r'^(?P<path>.*(js|css|bmp|jpg|gif|png|ico|html))$', 'django.views.static.serve', {'document_root':settings.PROJECT_DIR + '/media/'}),
    
    # Examples:
    # url(r'^$', 'ecommerce.views.home', name='home'),
    # url(r'^ecommerce/', include('ecommerce.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)