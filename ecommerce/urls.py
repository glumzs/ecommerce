from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
                       #supplier handlers
                       url(r'^suppliers/create_supplier$', 'ecommerce.views.createSupplier'),
                       url(r'^suppliers/get_supplier$', 'ecommerce.views.getSupplier'),
                       url(r'^suppliers/update_supplier$', 'ecommerce.views.updateSupplier'),
                       url(r'^suppliers/delete_supplier$', 'ecommerce.views.deleteSupplier'),
                       url(r'^suppliers/insert_products$', 'ecommerce.views.insertProducts'),
                       #category handlers
                       url(r'^category/get_category$', 'ecommerce.views.getCategory'),
                       url(r'^category/category_products$', 'ecommerce.views.getCategoryProducts'),
                       url(r'^category/add_category$', 'ecommerce.views.addCategory');
                       url(r'^category/update_category$', 'ecommerce.views.updateCategory'),
                       url(r'^category/delete_category$', 'ecommerce.views.deleteCategory'),
                       url(r'^category/add_products$', 'ecommerce.views.addProductsToCategory'),
                       url(r'^category/del_products$', 'ecommerce.views.delProductsFromCategory'),
                       #product handlers
                       url(r'^product/update_product$', 'ecommerce.views.updateProduct'),
                       url(r'^product/create_product$', 'ecommerce.views.createProduct'),
                       url(r'^product/get_product$', 'ecommerce.views.getProduct'),
                       url(r'^product/copy_product$', 'ecommerce.views.copyProduct'),
                       url(r'^product/delete_product$', 'ecommerce.views.deleteProduct'),
                       #site handler
                       url(r'^$', 'ecommerce.views.home'),
    # Examples:
    # url(r'^$', 'ecommerce.views.home', name='home'),
    # url(r'^ecommerce/', include('ecommerce.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
