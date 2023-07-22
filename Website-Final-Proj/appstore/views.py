from django.shortcuts import render

from django.http import HttpResponse

from datetime import date
from django.http import HttpResponse
from django.contrib import messages

from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login , logout

from django.shortcuts import render

from django.shortcuts import render, redirect

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group






# Create your views here.

all_products = [
  {
    "slug": "jeans-for-sale",
    "title": "Jeans",
    "image": "notebook 1.jpg",
    "price": 1000,
    "description": "Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis aperiam est praesentium, quos iste consequuntur omnis exercitationem quam velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.",
    "availability": True,
    "date": date(2023, 6, 21),
  },
  {
    "slug": "eyewear",
    "title": "Eyewear",
    "image": "eraser 1.jpg",
    "price": 2000,
    "description": "Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis aperiam est praesentium, quos iste consequuntur omnis exercitationem quam velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.",
    "availability": True,
    "date": date(2023, 6, 10),
  },
  {
    "slug": "shirt",
    "title": "Shirt",
    "image": "stapler 1.jpg",
    "price": 500,
    "description": "Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis aperiam est praesentium, quos iste consequuntur omnis exercitationem quam velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.",
    "availability": True,
    "date": date(2023, 6, 22),
  },
  {
    "slug": "shop_img",
    "title": "Shop",
    "image": "whiteboard 1.jpg",
    "price": 500,
    "description": "Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis aperiam est praesentium, quos iste consequuntur omnis exercitationem quam velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.",
    "availability": False,
    "date": date(2023, 6, 2),
  },
  
   {
    "slug": "shop_img",
    "title": "Shop",
    "image": "ballpen 1.jpg",
    "price": 500,
    "description": "Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis aperiam est praesentium, quos iste consequuntur omnis exercitationem quam velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.",
    "availability": False,
    "date": date(2023, 6, 2),
  },
   
    {
    "slug": "shop_img",
    "title": "Shop",
    "image": "calc 1.jpg",
    "price": 500,
    "description": "Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis aperiam est praesentium, quos iste consequuntur omnis exercitationem quam velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.",
    "availability": False,
    "date": date(2023, 6, 2),
  },
]

def get_date(product):
  return product['date']


@login_required(login_url = 'login')
def starting_page(request): 
  sorted_products = sorted(all_products, key=get_date)
  latest_products = sorted_products[-3:]
  return render(request, "store/index.html", {
    "products": latest_products
  })


  

def product_detail(request, slug):
  identified_product = next(product for product in all_products if product['slug'] == slug)
  return render(request, "store/product_detail.html", {
    "product": identified_product
  })
 






  

  

def home(request):
    return render(request, 'appstore/dashboard.html')

def products(request):
    return render(request, 'appstore/products.html')

def index(request):
    return render(request, 'appstore/index.html')

def featured(request):
    return render(request, 'appstore/featured.html')

def product_detail(request):
  pass
