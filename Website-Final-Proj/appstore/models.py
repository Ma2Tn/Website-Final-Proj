from django.db import models
from django.core.validators import MinLengthValidator

# Create your models here.
class Category(models.Model):
    caption = models.CharField(max_length=20)
    
class Customer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email_address = models.EmailField()

class Product(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, db_index=True)
    image_name = models.CharField(max_length=100)
    date = models.DateField(auto_now=True)
    description = models.TextField(validators=[MinLengthValidator(10)])
    categories = models.ManyToManyField(Category)