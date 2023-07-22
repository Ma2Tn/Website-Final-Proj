from datetime import date
from django.http import HttpResponse
from django.contrib import messages
from .filters import OrderFilter
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login, logout

from django.shortcuts import render

from django.shortcuts import render, redirect

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from appstore.decorators import unauthenticated_user
from .decorators import unauthenticated_user, allowed_users, admin_only

from .models import *

from .forms import OrderForm, CreateUserForm, CustomerForm





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

@unauthenticated_user
def registerPage(request):

	form = CreateUserForm()
	if request.method == 'POST':
		form = CreateUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			username = form.cleaned_data.get('username')

			group = Group.objects.get(name='customer')
			user.groups.add(group)

			messages.success(request, 'Account was created for ' + username)

			return redirect('login')
		

	context = {'form':form}
	return render(request, 'appstore/Registers.html', context)

@unauthenticated_user
def loginPage(request):

	if request.method == 'POST':
		username = request.POST.get('username')
		password =request.POST.get('password')

		user = authenticate(request, username=username, password=password)

		if user is not None:
			login(request, user)
			return redirect('home')
		else:
			messages.info(request, 'Username OR password is incorrect')

	context = {}
	return render(request, 'appstore/Logins.html', context)

def logoutUser(request):
	logout(request)
	return redirect('login')

@login_required(login_url='login')
@admin_only
def home(request):
	orders = Order.objects.all()
	customers = Customer.objects.all()

	total_customers = customers.count()

	total_orders = orders.count()
	delivered = orders.filter(status='Delivered').count()
	pending = orders.filter(status='Pending').count()

	context = {'orders':orders, 'customers':customers,
	'total_orders':total_orders,'delivered':delivered,
	'pending':pending }

	return render(request, 'appstore/Dashboards.html', context)

def userPage(request):
	context = {}
	return render(request, 'appstore/Users.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def products(request):
	products = Product.objects.all()

	return render(request, 'appstore/products.html', {'products':products})

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def customer(request, pk_test):
	customer = Customer.objects.get(id=pk_test)

	orders = customer.order_set.all()
	order_count = orders.count()

	myFilter = OrderFilter(request.GET, queryset=orders)
	orders = myFilter.qs 

	context = {'customer':customer, 'orders':orders, 'order_count':order_count,
	'myFilter':myFilter}
	return render(request, 'appstore/Customers.html',context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['customer']) 
def accountSettings(request):
    customer = request.user.customer
    form = CustomerForm(instance=customer)
    
    if request.method == 'POST':
      form = CustomerForm(request.POST, request.Files, instance=customer)
      if form.is_valid():
          form.save()
      
        
    context = {'form':form}
    return render(request, 'appstore/Account_Settings.html', context)

def get_date(product):
  return product['date']


def product_detail(request, slug):
  identified_product = next(product for product in all_products if product['slug'] == slug)
  return render(request, "appstore/product_detail.html", {
    "product": identified_product
  })


  

  
            
            
  
