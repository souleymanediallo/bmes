from django.urls import path
from . import views

""" 
Definition of urls for catalogueapp
"""

urlpatterns = [
    path('', views.catalogue, name="catalogue"),
    path('<category_slug>/<brand_slug>/', views.catalogue, name="catalogue"),
    path('products/<product_slug>/', views.product_detail, name="product_detail"),
]