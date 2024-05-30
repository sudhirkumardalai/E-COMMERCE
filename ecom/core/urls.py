from django.urls import path
from .views import *
from . import views

urlpatterns = [
    path('', index, name='index'),
    path('orderlist/', orderlist, name='orderlist'),
    path('add_product/', add_product, name='add_product'),
    path('product_desc/<int:pk>/', product_desc, name='product_desc'),
    path('add_to_cart/<int:pk>/', add_to_cart, name='add_to_cart'),
    path('add_item/<int:pk>/', add_item, name='add_item'),
    path('remove_item/<int:pk>/', remove_item, name='remove_item'),
    path('checkout_page',checkout_page,name="checkout_page"),
    path('payment',views.payment,name="payment"),
    path('handlerequest',views.handlerequest,name="handlerequest"),
    path('render_pdf_view',views.render_pdf_view,name="render_pdf_view"),
]


