from django.db import models
from django.core.validators import MinLengthValidator
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    caption = models.CharField(max_length=20)
    
class Customer(models.Model):
    first_name = models.CharField(max_length=100, null = True)
    last_name = models.CharField(max_length=100, null = True)
    email_address = models.EmailField(max_length=100, null = True)
    profile_pic = models.ImageField(default = "Charles_Chua_selfie.jpg", null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    
    
    @property
    def orders(self):
            order_count = self.order_set.all().count()
            return str(order_count)
    
class Tag(models.Model):
        name = models.CharField(max_length=200, null=True)   

class Product(models.Model):
    CATEGORY = (
			('Indoor', 'Indoor'),
			('Out Door', 'Out Door'),
			) 
    
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, db_index=True)
    image_name = models.CharField(max_length=100)
    date = models.DateField(auto_now=True)
    description = models.TextField(validators=[MinLengthValidator(10)])
    categories = models.ManyToManyField(Category)
    price = models.FloatField(null=True)
    tags = models.ManyToManyField(Tag)


    

    
class Order(models.Model):
    STATUS = (
        ('Pending', 'Pending'),
        ('Out for delivery', 'Out for delivery'),
        ('Delivered', 'Delivered')
    )
    
    customer = models.ForeignKey(Customer, null=True, on_delete = models.SET_NULL)
    product = models.ForeignKey(Product, null=True, on_delete= models.SET_NULL)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    status = models.CharField(max_length=200, null=True, choices=STATUS)
    note = models.CharField(max_length=1000, null=True, choices=STATUS)
    
    
    def __str__(self):
        return self.product.name
    


        