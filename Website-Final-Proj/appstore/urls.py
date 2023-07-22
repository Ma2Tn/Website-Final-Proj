from django.urls import path
from appstore import views

urlpatterns = [


    path('',views.home),
    path('products/',views.products),
    path('index/',views.index),
    path('featured/',views.featured),
    path("products/<slug:slug>", views.product_detail,
         name="product-detail-page")  
]

    