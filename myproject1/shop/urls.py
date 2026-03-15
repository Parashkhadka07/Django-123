from django.urls import path
from . import views

urlpatterns=[
    path('',views.home,name='shop-home'),
    path('about/',views.about,name="shop-about"),
    path('products/',views.products,name='shop-products')
]