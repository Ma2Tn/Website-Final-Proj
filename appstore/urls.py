from django.urls import path
from . import views


urlpatterns = [
    path('register/', views.registerPage, name="register"),
	path('login/', views.loginPage, name="login"),  
    path('logout/', views.logoutUser, name="logout"),  
	
    path("", views.starting_page, name="starting-page"),
    path('user/', views.userPage, name ="user-page"),
    path("products", views.products, name="products-page"),
    path("products/<slug:slug>", views.product_detail,
         name="product-detail-page")  # /products/my-first-product
   
    
]