from django.urls import path
from . import views

urlpatterns = [
    # Homepage url
    path('', views.home, name ='home'),
    path('category/<slug:category_slug>', views.home, name='products_by_category'),
    # Aboutpage url
    path('category/<slug:category_slug>/<slug:product_slug>', views.productPage, name ='product_details'),
    # Create cart url
    # cart
    path('cart/add/<int:product_id>', views.add_cart, name='add_cart'),
    path('cart', views.cart_detail, name ='cart'),
    # remove item
    path('cart/remove/<int:product_id>', views.cart_remove, name='cart_remove'),
    # Delete item/cart
    path('cart/remove_product/<int:product_id>', views.cart_remove_product, name='cart_remove_product'),
    
    
]