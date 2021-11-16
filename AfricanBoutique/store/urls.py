from django.urls import path
from .import views

urlpatterns = [
    # Homepage url
    path('', views.home, name ='home'),
    # Aboutpage url
    path('product/', views.productPage, name ='product'),
]